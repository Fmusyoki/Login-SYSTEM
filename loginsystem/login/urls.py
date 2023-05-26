
from django.urls import path
from . import views



urlpatterns = [
    path('', views.login_page, name="login"),
    path('register/', views.register, name="register"),
    path('home/', views.home, name="home"),
    path('logout/', views.logout, name="logout"),
    
    ]
