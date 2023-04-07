from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm,TaskCreationForm
from .models import Task


# Create your views here.

# Create a homepage view
def home(request):
    tasks = Task.objects.all()
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
        return render(request, 'home.html', {"tasks": tasks})


# Method to login a user
def login_user(request):
    pass


# Method to logout a user
@login_required
def logout_user(request):
    logout(request)
    return redirect('home')


# Method to register a user
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


# Method to delete a task form the Task model
@login_required
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    messages.success(request, "Record Deleted Successfully...")
    return redirect('home')


# Method to add a task to the Task model
@login_required
def add_task(request):
    form = TaskCreationForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,"Successfully added task")
        # return redirect('home')

    return render(request,"add_task.html",{'form':form})




##Method to Update an existing task
@login_required
def update_task(request, pk):
    pass
