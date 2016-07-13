'''
Created on 11-Jul-2016

@author: aayush.agrawal
'''
from django import forms
from models import Hobby,Register
from django.contrib.auth.models import User
class LoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=128)
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'readonly':'readonly'}))
    

class HobbyForm(forms.ModelForm):
    hobby_name = forms.CharField(max_length=128,help_text="Please enter your hobby name")
    interest_level = forms.IntegerField()
    
    class Meta:
        model = Hobby
        fields = ('hobby_name','interest_level',)
        exclude = ('roll_no',)
    
    def clean(self):
        cleaned_data = self.cleaned_data
        hobby_name = cleaned_data.get('hobby_name')
        interest_level = cleaned_data.get('interest_level')
        if not hobby_name:
            cleaned_data['hobby_name']='Swimming'
        if not interest_level:
            cleaned_data['interest_level'] = 0
        return cleaned_data

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields = ('username','email','password')

class RegisterForm(forms.ModelForm):
    
    class Meta:
        model=Register
        fields = ('linkedin','dp')