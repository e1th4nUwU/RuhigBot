from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/', views.chat, name='chat'),
    path('reset_chat/', views.reset_chat, name='reset_chat'),
]
