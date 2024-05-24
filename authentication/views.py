from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import RegisterForm,LoginForm

# Create your views here.ret

def home(request):
    return render(request,"home.html")
    

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get("username")
            messages.success(request,f"Account created {username}")
            return redirect('login')
    else:
            form=RegisterForm()
    return render(request,"register.html",{"form":form})
    
def Login(request):
    if request.method=="POST":
        form=LoginForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
    else:
        form=LoginForm()
    return render(request,"login.html",{"form":form})


def Logout(request):
    logout(request)
    
    return render(request,"home.html")