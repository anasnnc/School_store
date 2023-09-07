from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth,messages
# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('schoolApp:stud_form')
        else:
            messages.info(request,'Invalide credential')
            return redirect('credential:login')
    return render(request,'login.html')
def register(request):
    if request.method == "POST":
        username=request.POST['username']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if pass1 == pass2 :
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exist')
                return redirect('credential:register')
            else:
                user = User.objects.create_user(username=username,password=pass1)
                user.save()
                return redirect('credential:login')
        else:
            messages.info(request,'Password dont match')
            return redirect('credential:register')


    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
