from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('login_user/', views.login_user,name='login_user'),
    path('home/', views.home,name='home'),
    path('password_reset/', views.password_reset, name='password_reset'),
]
