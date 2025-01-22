from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def admin_register(request):
    return render(request,'adminRegister.html')

def admin_login(request):
    return render(request,'adminLogin.html')