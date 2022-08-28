from socket import fromshare
from dataclasses import fields
from django import forms
from studapp.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"