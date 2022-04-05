from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello_world),
    path('hellome/', views.say_hello_user)
]