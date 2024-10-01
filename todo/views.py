from pyexpat.errors import messages
from django.contrib import messages 

from django . shortcuts import render, redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import todoclass
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


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


def signout(request):
   logout(request)
   return redirect('/login')



def login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        
        user = authenticate(request, username=name, password=pwd)
        
        if user is not None:
            auth_login(request, user)
            return redirect('/todo')  # Redirect to the todo page after successful login
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('/login')  # Redirect back to the login page
            
    return render(request, 'login.html')


@login_required(login_url='/login') #inbuilt login decorator from django
def todo(request):
    if request.method == "POST":
        title=request.POST.get('title')
        obj = models.todoclass(title=title, user=request.user)
        obj.save()
        res = models.todoclass.objects.filter(user=request.user).order_by('-date')
        return redirect('/todo', {'res':res})
    res = models.todoclass.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html', {'res':res})


@login_required(login_url='/login')
def edit_todo(request, srno):
    obj = models.todoclass.objects.get(srno=srno)
    
    if request.method == "POST":
        title = request.POST.get('title')
        
        if title:  # Check if title is not empty
            obj.title = title
            obj.save()
            return redirect('/todo')  # Redirect after successful update
        
    return render(request, 'edit_todo.html', {'obj': obj})



@login_required(login_url='/login')
def delete_todo(request, srno):
    obj = models.todoclass.objects.get(srno=srno)
    obj.delete()
    return redirect('/todo')
    