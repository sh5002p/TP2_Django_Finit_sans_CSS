from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.liste, name='home'),
    path('ajout/', views.ajout, name="ajout"),
    path('traitement/', views.traitement, name="traitement"),
    path('update/<int:id>/', views.update, name="update"),
    path('liste/', views.liste, name="liste"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('detail/<int:id>/', views.read, name="detail"),
    ]