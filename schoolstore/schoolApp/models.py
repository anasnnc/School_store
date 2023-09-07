from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.
class department(models.Model):
    departmentName=models.CharField(max_length=250)

    def __str__(self):
        return self.departmentName

class cours(models.Model):
    dptid=models.ForeignKey(department,on_delete=CASCADE)
    cours_name=models.TextField()

    def __str__(self):
        return self.cours_name

class orderForm(models.Model):
    name=models.CharField(max_length=250)
    DOB=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=50, choices=(('Male','Male'),('Female','Female')))
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    address=models.TextField(max_length=250)
    department = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    purpose = models.CharField(max_length=50)
    material = models.CharField(max_length=50)


    def __str__(self):
        return self.name

