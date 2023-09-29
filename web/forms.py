# forms.py
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Contact
from django.forms import widgets

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ("timestamp",)
        fields = "__all__"
        widgets = {
            "name": widgets.TextInput(attrs={"class": "required form-control"}),
            "phone": widgets.TextInput(attrs={"class": "required form-control"}),
            "email": widgets.EmailInput(attrs={"class": "required form-control"}),
            "subject": widgets.TextInput(attrs={"class": "required form-control"}),
            "message": widgets.Textarea(attrs={"class": "required form-control"}),
        }
