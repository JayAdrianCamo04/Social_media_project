from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')

    def signup(request):

        if request.method =='POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            passwod = request.POST['password']

            if password == password2:
                if User.objects.filter(email=email).exists():
                    messages.info(request, 'Email already exist please enter other email')
                    return redirect('signup')
                elif User.objects.filter(username=username).exists():
                    messages.info(request, 'Username already exist')
                    return redirect('signup')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()