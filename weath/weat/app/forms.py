from django import forms
from .models import Todo

class Todo_form(forms.ModelForm):
    class Meta:
        model=Todo
        fields='__all__'
        