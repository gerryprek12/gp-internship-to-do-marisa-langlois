from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm, ListForm


def index(request):
    """
        Renders frontend homepage
    """
    data = {'title': 'Welcome - To Do Application'}
    return render(request, 'index.html', data)


def login_view(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        user = form.login(request)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')  # redirect to index
    return render(request, 'login.html', {'login_form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request, 'index.html')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

def create_list(request):
    form = ListForm()
    return render(request, 'list_create.html', {'form': form})