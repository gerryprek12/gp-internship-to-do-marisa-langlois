from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

def index(request):
    """
        Renders frontend homepage
    """
    data = {'title': 'Welcome - To Do Application'}
    return render(request, 'index.html', data)