from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm


# Create your views here.

## Create a homepage view
def home(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect('home')
        else:
            messages.success(request, "Wrong credentials")
            return redirect("home")
    else:
        return render(request, 'home.html', {})


## Method to login a user
def login_user(request):
    pass


## Method to logout a user
@login_required
def logout_user(request):
    logout(request)
    return redirect('home')


## Method to register a user
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate the user and log in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            return redirect('home')

        else:
            return render(request, 'register.html', {'form': form})

    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})
