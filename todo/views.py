from pyexpat.errors import messages
from django . shortcuts import render, redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import todoclass
from django.contrib.auth import authenticate, login as auth_login

def signup(request):
    if request.method=="POST":
       name = request.POST.get('name')
       email = request.POST.get('email')
       pwd = request.POST.get('pwd')
       
    #    saving my user 
       myuser = User.objects.create_user(name,email,pwd)
       myuser.save()
       return redirect('/login')
       
    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        
        user=authenticate(request, username=name, password=pwd) #'username' and 'password' thse params are built-in django authentication
        if user is not None:
            auth_login(request, user)
            return redirect('/todo')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('/login')
    return render(request, 'login.html')

def todo(request):
    return render(request, 'todo.html')