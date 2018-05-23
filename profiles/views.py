from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def sign_up(request):
    user_form = UserForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)


        if user_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)


            login(request, authenticate(
            username = user_form.cleaned_data['username'],
            password = user_form.cleaned_data['password']
            ))

            return redirect('/')

    context = {
        'user_form': user_form
    }
    return render(request, 'profiles/sign_up.html', context)
