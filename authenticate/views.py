from django.http import HttpResponse
from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.

def signup_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["Email"]
        password = request.POST["Password"]

        newUser = User.objects.create_user(username, email, password)
        newUser.save()
        messages.success(request, 'Account has been succesfully created')

        return redirect('login')
    
    return render(request, 'signup.html')

def login_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["Password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f'You are now logged in as {username}.')
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid username or password.")

    return render(request, 'login.html')
