from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import update_session_auth_hash
from django.conf import settings
from django.core.mail import send_mail

from .models import User

# Create your views here.

home_variables = {}

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'ExaminationMalpractice/index.html',{'home': home_variables})
    else:
        return redirect('/home')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username", False)
        password = request.POST.get("password", False)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/home')
            else:
                return render(request, 'royalking/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'ExaminationMalpractice/login.html', {'error_message': 'Invalid login'})
    return render(request, 'ExaminationMalpractice/login.html')

def verify(request):
    if request.method == "POST":
        photo = request.POST.get("photo", False)
    return render(request, 'ExaminationMalpractice/verify.html')

def home(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request, 'ExaminationMalpractice/home.html')

def password_reset(request):
    if request.method == 'POST':
        user = User.objects.filter(email=request.POST['email'])
        if(user):
            subject = 'Welcome to Face Recognition System'
            message = 'Hope you are enjoying The services we are offering'
            recepient = str(request.POST['email'])
            # send_mail(subject,message, settings.EMAIL_HOST_USER, [recepient], fail_silently = False)
            return render(request,'ExaminationMalpractice/reset_password.html',{ 'success':'Check your email for further instructions'})
        else:
            return render(request,'ExaminationMalpractice/reset_password.html',{ 'error':'Email not registered'})
    return render(request, 'ExaminationMalpractice/reset_password.html')

def logout_user(request):
    logout(request)
    return redirect('/')
