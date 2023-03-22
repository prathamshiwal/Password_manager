from django.http import HttpResponse
from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["Email"]
        password = request.POST["Password"]

        newUser = User.objects.create_user(username, email, password)
        newUser.save()
        messages.success(request, 'Account has been succesfully created')

        return redirect('signup')
    
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')