from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class User(models.Model):
    id  =models.AutoField(primary_key=True) #THIS OUR ID MEANS A REGISTER NUMBER
    name   =models.CharField(max_length=100)
    email       =models.EmailField(unique=True)
    password    =models.CharField(max_length=8)
    DOB         =models.DateField()
#   THIS IS ALL OUR DATABASE TABLE FIELDS 

    def __str__(self):
        return self.name
