from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(help_text=False)

    class Meta:
        model = User
        fields = ('username','password', 'email')