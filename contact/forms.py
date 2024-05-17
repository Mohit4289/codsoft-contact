from django import forms
from .models import Contactmodel

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contactmodel
        fields = ['name', 'phone', 'email', 'address']