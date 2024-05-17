from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('search/', views.search_contacts, name='search_contacts'),
    path('edit/<int:contact_id>/', views.edit, name='edit_contact'),
    path('delete/<int:contact_id>/', views.delete_contact, name='delete_contact')
]
