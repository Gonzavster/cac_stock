from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse("Hello world!")
    return render(request, 'inventory\\index.html')

def dashboard(request):
    return render(request, 'inventory\\dashboard.html')

def inventory(request):
    return render(request, 'inventory\\inventory_portal.html')

def tutorial(request):
    return render(request, 'inventory\\tutorial.html')

def signin(request):
    return render(request, 'inventory\\signin.html')

def signup(request):
    return render(request, 'inventory\\signup.html')

def logout(request):
    return render(request, 'inventory\\logout.html')