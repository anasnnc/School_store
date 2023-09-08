from django.contrib import messages
from django.contrib.admin import models
from django.http import HttpResponse
from django.shortcuts import render
from .models import department,cours,orderForm
from django.core import serializers
import json
# Create your views here.
def home(request):
    return render(request,'home.html')

def stud_form(request):
    return render(request,'stud_form.html')
def form1(request):
    form='form1.html'
    deptcontext=department.objects.all()
    corcontext=cours.objects.all()
    if request.method =="POST":
        name=request.POST['name']
        DOB=request.POST['DOB']
        age=request.POST['age']
        gender=request.POST['gender']
        phone=request.POST['phone']
        email=request.POST['mail']
        address=request.POST['address']
        Department=request.POST['department']
        Department=department.objects.get(id=Department)
        Cours=request.POST['cours']
        Cours=cours.objects.get(id=Cours)
        purpose = request.POST['purpose']
        material = request.POST.getlist('meterial')
        orders=orderForm(
            name=name,
            DOB=DOB,
            age=age,
            gender=gender,
            phone=phone,
            email=email,
            address=address,
            department=Department,
            course=Cours,
            purpose=purpose,
            material=material,


        )
        orders.save()
        messages.info(request,'order placed successfully')


    return render(request,form,{'department':deptcontext,'cours':corcontext})
def orderDetail(request):
    detail=orderForm.objects.all()
    return render(request,'order_details.html',{'detail':detail})

def Details(request,order_id):
    detail1=orderForm.objects.get(id=order_id)
    return render(request,'details.html',{'detail1':detail1})
