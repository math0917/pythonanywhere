from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('menus/', views.index),
    path('menus/<int:pk>/', views.detail),
]
