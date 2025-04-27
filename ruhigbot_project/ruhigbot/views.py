from django.shortcuts import render, redirect

# Simpler Speicher für Chat (für Demo-Zwecke)
chat_history = []

def index(request):
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

def chat(request):
    global chat_history
    # Schauen die Daten von der Session ab
    if 'daten' in request.session:
        daten = request.session['daten']
    else:
        daten = None
    print("Daten aus der Session:", daten)
    if request.method == "POST":
        user_input = request.POST.get("text")
        chat_history.append({"sender": "user", "text": user_input})
        # Einfache Fake-Antwort für jetzt
        response = "Ich verstehe... erzähl mir mehr."
        chat_history.append({"sender": "bot", "text": response})
    return render(request, "chat.html", {"messages": chat_history})
