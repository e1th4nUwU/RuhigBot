from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import os
import requests
import json

# API-Integration
API_KEY = os.getenv("API_KEY")
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}
URL = "https://openrouter.ai/api/v1/chat/completions"

def index(request):
    """
    Startseite mit dem Formular zur Eingabe der Benutzerdaten.
    
    Hier werden die Daten des Benutzers gesammelt, um eine personalisierte
    Erfahrung zu bieten. Die Daten werden in der Session gespeichert,
    um sie später im Chat zu verwenden.
    ---
    Parameters:
    - request: HttpRequest-Objekt, das die Anfrage des Benutzers enthält.
    ---
    Returns:
    - HttpResponse: Rendert die Startseite mit dem Formular.
    """
    if request.method == "POST":
        name = request.POST.get("name")
        alter = request.POST.get("alter")
        herkunft = request.POST.get("herkunft")
        geholfen = request.POST.get("was_geholfen_hat")
        stoert = request.POST.get("was_stoert")

        # Hier kann man später Daten speichern oder analysieren
        print("Formulardaten:", name, alter, herkunft, geholfen, stoert)
        
        # Speichern der Daten in der Session
        request.session['daten'] = {
            'name': name,
            'alter': alter,
            'herkunft': herkunft,
            'was_geholfen_hat': geholfen,
            'was_stoert': stoert
        }
        
        # Redirect zur Chat-Seite
        return redirect("chat")

    return render(request, "index.html")



def reset_chat(request):
    """
    Setzt den Chat zurück, indem die Nachrichten aus der Session entfernt werden.
    ---
    Parameters:
    - request: HttpRequest-Objekt, das die Anfrage des Benutzers enthält.
    ---
    Returns:
    - HttpResponse: Redirect zur Chat-Seite.
    """
    # Remove messages and daten from the session
    request.session.pop('messages', None)
    request.session.pop('daten', None)  # Clears personal data as well
    
    # Redirect to the index page
    return redirect("index")

    




def nachricht_senden(messages):
    """
    Sendet eine Nachricht an die API und erhält die Antwort.
    ---
    Parameters:
    - messages: Liste von Nachrichten, die an die API gesendet werden.
    ---
    Returns:
    - messages: Liste von Nachrichten, die die Antwort der API enthält.
    """
    response = requests.post(
        url=URL,
        headers=HEADERS,
        data=json.dumps({
            "model": "meta-llama/llama-4-maverick",
            "messages": messages,
        })
    )
    if response.status_code == 200:
        messages.append(response.json()["choices"][0]["message"])
    else:
        print("Fehler bei der API-Anfrage:", response.status_code, response.text)
        messages.append({"role": "assistant", "content": "Entschuldigung, ich kann Ihnen im Moment nicht helfen. Bitte versuchen Sie Hilfe mit Family oder Freunden zu bekommen."})
        print("Fehler bei der API-Anfrage:", response.status_code, response.text)
    return messages
    
    
    
def init_chat(request):
    """
    Initialisiert den Chat mit den Benutzerdaten aus der Session.
    ---
    Parameters:
    - request: HttpRequest-Objekt, das die Anfrage des Benutzers enthält.
    ---
    Returns:
    - messages: Liste von Nachrichten, die den Chatverlauf enthält.
    """
    if 'daten' in request.session:
        daten = request.session['daten']
    else:
        print("Keine Daten in der Session gefunden.")
        return render(request, "error.html", {"message": "Keine Daten in der Session gefunden. Bitte füllen Sie das Formular aus."})
    
    
    # Senden die Daten an die API
    if 'messages' in request.POST:
        messages = request.POST.getlist("messages")
    else:
        if len(daten.get("name")) > 0 or len(daten.get("alter")) > 0 or len(daten.get("herkunft")) > 0 or len(daten.get("was_geholfen_hat")) > 0:
            text = "Hallo! "
            if len(daten.get("name")) > 0:
                text += f"Ich heiße {daten['name']}. "
            if len(daten.get("alter")) > 0:
                text += f"Ich bin {daten['alter']} Jahre alt. "
            if len(daten.get("herkunft")) > 0:
                text += f"Ich komme aus {daten['herkunft']}. "
            if len(daten.get("was_geholfen_hat")) > 0:
                text += f"Ich habe Hilfe bei {daten['was_geholfen_hat']} erhalten in vergangener Therapie. "
            text += f"Ich brauche Hilfe bei etwas: {daten['was_stoert']}; und ich mochte gern ruhig fühlen."
        else:
            text = f"Hallo, ich brauche hilfe bei etwas: {daten['was_stoert']}; und ich mochte gern ruhig fühlen."
        messages = [
            {
                "role": "user",
                "content": text
            }
        ]
    
    return messages
    

def chat(request):
    """
    Chat-Ansicht, die den Chatverlauf anzeigt und Benutzereingaben verarbeitet.
    ---
    Parameters:
    - request: HttpRequest-Objekt, das die Anfrage des Benutzers enthält.
    ---
    Returns:
    - HttpResponse: Rendert die Chat-Seite mit dem Chatverlauf.
    """
    messages = init_chat(request)

    if request.method == "GET" and len(messages) == 1:
        # Send initial message to API
        messages = nachricht_senden(messages)
        request.session['messages'] = messages

    if request.method == "POST":
        user_input = request.POST.get("text")
        if len(user_input) > 0:
            # Get conversation history from session
            messages = request.session.get('messages', [])
            messages.append({
                "role": "user",
                "content": user_input
            })

            # Send updated history to API
            messages = nachricht_senden(messages)

            # Update the session with new conversation
            request.session['messages'] = messages

            # Respond with the updated messages as JSON
            return JsonResponse({"messages": messages})

    return render(request, "chat.html", {"messages": messages})



