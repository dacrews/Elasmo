from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('science', views.science, name='science'),
    path('contact', views.contact, name='contact'),
    path('data', views.data, name='data'),
    path('sharks', views.sharks, name='sharks'),
    path('resources', views.resources, name='resources'),
]