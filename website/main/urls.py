from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('menu', views.menu, name='menu'),
    path('team', views.team, name='team'),
    path('contacts', views.contacts, name='contacts')
]