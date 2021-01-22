from django.urls import path

from . import views

urlpatterns = [
    path('fakename', views.name, name='name'),
    path('fakeaddress', views.address, name='address'),
]
