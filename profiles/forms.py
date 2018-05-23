from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

class UserForm(ModelForm):
    # password = forms.CharField()

    class Meta:
        model = User
        fields = ('username','password', 'email')