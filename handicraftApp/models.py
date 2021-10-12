from django.db import models

# Create your models here.
class loginmodel(models.Model):
    uname=models.CharField(max_length=20)
    psw=models.CharField(max_length=25)

class registermodel(models.Model):
    username=models.CharField(max_length=30)
    phNum=models.IntegerField()
    email=models.CharField(max_length=40)
    password=models.CharField(max_length=20)
    confpswd=models.CharField(max_length=20)

class Pdetailsmodel(models.Model):
    pname=models.CharField(max_length=50)
    pquantity=models.IntegerField()
    cname=models.CharField(max_length=40)
    caddress=models.CharField(max_length=100)
    cphnum=models.IntegerField()
    cemail=models.CharField(max_length=40)