from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record


# Create your views here.
def home(request):
    records = Record.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username= username, password= password)

        if user is not None :
            login(request, user)
            messages.success(request, "Login Success")
            return redirect('home')
        else:  
            messages.success(request, 'Login Error')
            return redirect('home')

    else:        
        return render(request, 'home.html',{'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logout successfully")
    return redirect('home') 

def register_user(request):
        if request.method == 'POST':
             form = SignUpForm(request.POST)
             if form.is_valid():
                  form.save()
                  username = form.cleaned_data['username']
                  password = form.cleaned_data['password1']
                  user = authenticate(username=username, password=password)
                  login(request, user)
                  messages.success(request, "You have been successfully registered")
                  return redirect('home')
        else:
            form = SignUpForm()
            return render(request, 'register.html',{'form':form})
        
        return render(request, 'register.html',{'form':form})

def record_user(request, pk):
     if request.user.is_authenticated :
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html',{'record':customer_record})
     else : 
        messages.success(request, "You have to login first to access this page ...")
        return redirect('home')

def delete_user(request, pk):
    if request.user.is_authenticated :
        delete_record = Record.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, "Record Have been Deleted Successfully ...")
        
    else : 
        messages.success(request, "You have to login first to access this page ...")
        
    return redirect('home')

def add_record(request):
        if request.method == 'POST':
             
                  messages.success(request, "You have been successfully registered")
                  return redirect('home')
        else:
            return render(request, 'add_record.html',{})
        
        return render(request, 'register.html',{'form':form})
