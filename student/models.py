'''
Created on 11-Jul-2016

@author: aayush.agrawal
'''
from django.db import models
from django.contrib.auth.models import User
class Student(models.Model):
    name = models.CharField(max_length=128)
    roll_no = models.IntegerField(unique=True)
    def __str__(self):
        return self.name

class Authenticate(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    def __str__(self):
        return self.username


class Hobby(models.Model):
    roll_no = models.IntegerField()
    hobby_name = models.CharField(max_length=128)
    interest_level = models.IntegerField()


class Register(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    linkedin = models.URLField(blank=True)
    dp = models.ImageField(upload_to='profile_images',blank=True)
    def __str__(self):
        return self.user.username