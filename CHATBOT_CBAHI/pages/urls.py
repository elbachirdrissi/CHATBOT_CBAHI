from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('clear_chat/', views.clear_chat, name='clear_chat'),
]