from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import contesthome 
import stripe
from django.conf import settings

# @login_required(login_url='login/')  # Apply the decorator to views that require authentication
def home(request):

    queryset = contesthome.objects.all()
    context ={
        "contest":queryset
    }

    return render(request, 'index.html' ,context)
def deposite(request):
    return render(request, 'deposite.html')

def join(request):





    queryset = contesthome.objects.all()
    context ={
        "contest":queryset
    }
    return render(request, 'join.html', context)

def login_user(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=uname, password=password)
        if user is not None:
            login(request, user)  # This line should be correct
            return redirect('/home/')
        else:
            messages.info(request, 'Invalid Credentials!')
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def rank(request):
    return render(request, 'rank.html')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')  # Use parentheses instead of square brackets
        name = request.POST.get('firstname')      # Use parentheses instead of square brackets
        email = request.POST.get('email')    # Use parentheses instead of square brackets
        password = request.POST.get('password')  # Use parentheses instead of square brackets
        
        if User.objects.filter(username=uname).exists():
            # Handle the case where the username is already taken
            messages.error(request,"username is already taken")

        elif User.objects.filter(email=email).exists():
            # Handle the case where the email address is already in use
            messages.error(request,"email is already taken")

        
        else:
            my_user = User.objects.create_user(uname, email, password)
            print("Data saved successfully.")
            my_user.save()
            return redirect('login')  # Redirect to the login page

        # print(uname, nname, eemail, ppassword) 
        
    return render(request, 'signup.html')

def vote(request):
    return render(request, 'vote.html')

def withdraw(request):
    return render(request, 'withdraw.html')




def logoutpage(request):
    logout(request)
    return redirect('login/')
    





