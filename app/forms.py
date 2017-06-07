from django import forms
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import List, Task, Comment


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=200)
    password = forms.CharField(label='password', max_length=200)

    def login(self, request):
        print(self.__class__)
        if self.is_valid():
            username = self.cleaned_data.get('username')
            password = self.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if not user:
                messages.warning(request, 'Invalid login information.')
            return user
        else:
            return None


class SignupForm(UserCreationForm):
    first_name = forms.CharField(label='first_name', required=False)
    last_name = forms.CharField(label='last_name', required=False)
    email = forms.EmailField(label='email')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ('name', 'priority', 'assigned_to', 'due_date')
