from django.shortcuts import render
from users.models import Users
from django.http import HttpResponse
# Create your views here.
def signup(request):
    return render(request,'signup.html')
def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        if Users.objects.filter(email=email,password=password).exists():
            return render(request,'dashboard.html')
        else:
            return HttpResponse('<center><h1> Login Failed!</h1></center>')
    else:
        return render(request,'login.html')
    
def home(request):
    return render(request,'home.html')
def logout(request):
    return render(request,'login.html')


