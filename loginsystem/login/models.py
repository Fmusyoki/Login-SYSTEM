from django.db import models
import os
import datetime
from django.conf import settings
# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    ConfirmPassword = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)
    
