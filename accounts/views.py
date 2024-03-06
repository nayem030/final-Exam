from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
from . import models
from django.contrib import auth
from django.contrib import messages
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name= form.cleaned_data['first_name']
            last_name= form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password=  form.cleaned_data['password']
            username= email.split("@")[0]
            user = models.Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password, username=username)
            user.is_active=True
            user.save()
            return redirect('login')
        
    return render(request, 'accounts/register.html', {'form':form})



def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username = user_name, password = password,)
        auth.login(request, user)
        return redirect('profile')
        
    return render(request, 'accounts/signin.html')

def profile(request):
    return render(request, 'accounts/dashboard.html')

def user_logout(request):
    logout(request)
    return redirect('login')
