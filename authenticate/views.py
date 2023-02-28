from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'authenticate/index.html')

def signup(request):
    return render(request, 'authenticate/signup.html')

def signin(request):
    return render(request, 'authenticate/signin.html')

def signout(request):
    pass