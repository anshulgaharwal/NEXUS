from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
# Create your views here.
@login_required(login_url='signup')
def index(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    return render(request, 'index.html', {'user-profile': user_profile})

def upload(request):
    return render(request, 'upload.html')
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if len(password) > 8:
            
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists, try sign in')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists, try sign in')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #log user in and rdirect to settings page

                #create a profile object for the user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('index')
        else:
            messages.info(request, 'Password should be atleat 8 character long')
            return redirect('signup')
        
        
    else:   
        return render(request, 'index.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('index')
    else:
        return render(request, 'signin.html')

def Logout(request):
    auth.logout(request) 
    return redirect('signin')    

def settings(request):
    return render(request, 'setting.html')   

def profile(request):
    return render(request, 'profile.html')

