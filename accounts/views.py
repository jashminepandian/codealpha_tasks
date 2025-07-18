from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered successfully. You can now log in.")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")  # we'll create this later
        else:
            messages.error(request, "Invalid credentials")
    return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Make sure this template exists

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Home Page")

