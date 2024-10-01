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
    if request.method == "POST":
        title=request.POST.get('title')
        obj = models.todoclass(title=title, user=request.user)
        obj.save()
        res = models.todoclass.objects.filter(user=request.user).order_by('-date')
        return redirect('/todo', {'res':res})
    res = models.todoclass.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html', {'res':res})

# def edit_todo(request, srno):
#     if request.method == "POST":
#         title=request.POST.get('title')
#         obj = models.todoclass.objects.get(srno=srno)
#         obj.title = title
#         obj.save()
#         user=request.user
#         return redirect('/todo', {'res':res})
#     obj = models.todoclass.objects.get(srno=srno)
#     res = models.todoclass.objects.filter(user=request.user).order_by('-date')
#     return render(request, 'todo.html', {'res':res})

# def edit_todo(request, srno):
#     if request.method == "POST":
#         title = request.POST.get('title')
#         obj = models.todoclass.objects.get(srno=srno)
#         obj.title = title
#         obj.save()
#         return redirect('/todo', {'obj':obj})

#     obj = models.todoclass.objects.get(srno=srno)
#     return render(request, 'edit_todo.html', {'obj': obj})

def edit_todo(request, srno):
    obj = models.todoclass.objects.get(srno=srno)
    
    if request.method == "POST":
        title = request.POST.get('title')
        
        if title:  # Check if title is not empty
            obj.title = title
            obj.save()
            return redirect('/todo')  # Redirect after successful update
        
        # Optionally handle the case where title is empty
        # For example, you could add an error message to the context
        # return render(request, 'edit_todo.html', {'obj': obj, 'error': 'Title cannot be empty.'})

    return render(request, 'edit_todo.html', {'obj': obj})