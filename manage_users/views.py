
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegisterForm


# User login 
def user_login(request):
    if request.user.is_authenticated:
        return render(request, 'home_page/home_page.html')
    
    else:
        return render(request, 'manage_users/login.html')

# User authentication
def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('manage_users:login')
    )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('home_page:home_page') 
    )

# Registering a new user 
def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'manage_users/register.html', {'form': form})    
   
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return render(request, 'home_page/home_page.html')
        else:
            return render(request, 'manage_users/register.html', {'form': form})

