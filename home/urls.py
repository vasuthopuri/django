from django.urls import path
from home import views

urlpatterns = [
    path(r'', views.base, name='base'),
    path(r'about', views.about, name='about'),
    path(r'skills', views.skills, name='skills'),
    path(r'contact', views.contact, name='contact'),
]
