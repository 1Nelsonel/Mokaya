from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('service/', views.service, name='service'),
    path('blogs/', views.blogs, name='blogs'),
    path('blog/', views.blog, name='blog'),
    path('faqs/', views.faqs, name='faqs'),
    path('contacts/', views.contacts, name='contacts'),
    path('teams/', views.teams, name='teams'),
]
