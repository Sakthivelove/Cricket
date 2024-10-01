from django.db import models



# Create your models here.
class Book(models.Model):
    Team1=models.CharField(max_length=70,default="")
    Team2=models.CharField(max_length=60,default="")
    Venue=models.CharField(max_length=100,default="") 
    Date=models.DateField()
    Adult=models.CharField(max_length=50,default="") 
    Children=models.CharField(max_length=50,default="") 

class Matches(models.Model):
    Team1=models.CharField(max_length=70,default="")
    Team2=models.CharField(max_length=60,default="")
    Venue=models.CharField(max_length=100,default="") 
    Date=models.DateField()