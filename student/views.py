'''
Created on 11-Jul-2016

@author: aayush.agrawal
'''

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Authenticate,Student,Hobby,Register
from .forms import LoginForm,HobbyForm,UserForm,RegisterForm
from Utils.bing_search import run_query
import StudConfig as CONFIG
import json
class HomeView(View):
    def get(self,request):
        return render(request,'index.html')

class RegisterView(View):
    def get(self,request):
        user_form = UserForm()
        register_form = RegisterForm()
        registered = False
        return render(request,'student/register.html',{'userform':user_form,'registerform':register_form,'registered':registered})
    
    def post(self,request):
        
        user_form = UserForm(data=request.POST)
        register_form = RegisterForm(data=request.POST)
        if user_form.is_valid() and register_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            register = register_form.save(commit=False)
            register.user = user
            if 'dp' in request.FILES:
                register.dp = request.FILES['dp']
            register.save()
            registered = True
        else:
            registered = False
        return render(request,'student/register.html',{'userform':user_form,'registerform':register_form,'registered':registered})

class LoginView(View):
    def get(self,request):
        form  = LoginForm()
        return render(request,'student/login.html',{'form':form})
    
    def post(self,request):
        print request.POST
        #username = request.POST.get('username')
        #password = request.POST.get('password')
        form  = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            auths = authenticate(username=username,password=password)
            print auths.id
            if auths:
                if auths.is_active:
                    login(request,auths)
                    request.session['user_id'] = auths.id
                    return HttpResponseRedirect(reverse('profile')+"?user="+username)
                return HttpResponse('Non Active User')
        return HttpResponse('Bad User')

class ProfileView(View):
    def get(self,request):
        username = request.GET.get('user')
        user_id = request.session['user_id']
        print user_id
        st = Student.objects.filter(name=username)
        register_data = Register.objects.filter(user_id=user_id)
        dp = register_data[0].dp
        if not dp:
            dp = CONFIG.DEFAULT_IMAGE
        return render(request,'student/profile.html',{'hobbies':st,'linkedin':register_data[0].linkedin,'dp':dp})

class HobbyView(View):
    def get(self,request,roll_no=None):
        #if not roll_no:
        #    return HttpResponse('Error dude')
        
        #hobbies = Hobby.objects.filter(roll_no=roll_no)
        
        form = HobbyForm()
        return render(request,'student/hobby.html',{'form':form,'roll_no':roll_no})
    
    def post(self,request,roll_no=None):
        if not roll_no:
            return HttpResponse('Error dude')
        print request.POST
        #import pdb;pdb.set_trace()
        hobby_name = request.POST.get('hobby_name')
        interest_level = request.POST.get('interest_level')
        form = HobbyForm(request.POST)
        if form.is_valid():
            #form.save(commit=True)
            hb = Hobby.objects.update_or_create(roll_no=roll_no,defaults={'hobby_name':hobby_name,'interest_level':interest_level})
            return HttpResponse('Added dude')
        else:
            print HttpResponse(form.errors)
        
        
def About(request):
    return render(request,'student/aboutus.html')

def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

class SearchView(View):
    
    def get(self,request):
        result_list = []
        return render(request,'student/search.html',{'result_list':result_list})
    
    def post(self,request):
        result_list = []
        query = request.POST.get('query')
        if query:
            result_list = run_query(query)
        return render(request,'student/search.html',{'result_list':result_list,'query':query})  
class SuggestionsView(View):
    def get(self,request):
        query = request.GET.get('key')
        result_list = []
        if query:
            result_list = run_query(query)
        return HttpResponse(json.dumps(result_list))