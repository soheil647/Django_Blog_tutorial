from django.urls import path, include
from . import views
from user import views as user_view


urlpatterns = [
    path('', views.home_page, name='blog-home'),
    path('about/', views.about_page, name='blog-about'),
]
