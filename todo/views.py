from django . shortcuts import render, redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import todoclass

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
    return render(request, 'login.html')