from django.contrib import admin 
from django.urls import path
from libapp import views


urlpatterns = [
    path('',views.index),
    path('cpost',views.createpost),
    path('home',views.home),
    path('singlepost',views.singlepost),
    path('udash',views.dashboard),
    path('postdetail/<rid>',views.postdetail),
    path('edit/<rid>',views.edit),
    path('delete/<rid>',views.delete),
    path('login',views.login),
    path('logout',views.user_logout),
    path('register',views.register),
    
]