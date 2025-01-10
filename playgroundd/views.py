from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from .forms import Scheduler
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'users/index.html')

def aboutme(request):
    return render(request, 'users/aboutme.html')

def emoji(request):
    return render(request, 'users/emoji.html')

def gallery(request):
    return render(request, 'users/gallery.html')

def links(request):
    return render(request, 'users/links.html')

def shop(request):
    return render(request, 'users/shop.html')

def calendar(request):
    return render(request, 'users/calendar.html')

def rclinic(request):
    return render(request, 'users/rclinic.html')

def login(request):
    return render(request, 'users/user_login.html')

def user_logout(request):
    logout (request)
    return render(request, 'users/index.html')

def rclinic2(request):
    return render(request, 'users/rclinic2.html')

def scheduler(request):
    submitted = False
    if request.method == "POST":
        form = Scheduler(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("shop.html")
            
    else:
        form = Scheduler
        if 'submitted' in request.GET:
            submitted=True
        
    return render (request, 'users/scheduler.html', {'form':form,'submitted': submitted})
 
 
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            return redirect('login')
    else:
        return render(request, 'users/user_login.html', {})

def user_register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/user_register.html', {'form':form},)




