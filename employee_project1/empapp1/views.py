from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import empdetails
import re



def home(request):
    return render(request,'home.html')

def employeedetails(request):
    e1=empdetails.objects.all()
    content={}
    content['data']=e1
    return render(request,'empdetails.html',content) 

def addemp(request):
    if request.method=="POST":
        ename=request.POST['empname']
        econ=request.POST['empcontact']
        email=request.POST['deptemail']
        n=len(econ)
       
        e=regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if n==10:

             if(re.fullmatch(regex,email)):
                e2=empdetails.objects.create(empname=ename,empcontact=econ,deptemail=email)
                e2.save()
                return HttpResponseRedirect("/empdetails")
             else:
                error_msg={}
                error_msg['e']="Invalid Email Address!!"
                return render(request,'addemp.html',error_msg)
        
        else:
            err_msg={}
            err_msg['m']="Invalid Mobile Number!!"
            return render(request,'addemp.html',err_msg)


    else:

        return render(request,'addemp.html')

def signup(request):

    if request.method=="POST":
        fm=UserCreationForm(request.POST)
        print(fm)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password1']
           
            u=User.objects.create_user(username=uname,password=upass,is_superuser=True,is_staff=True)
            u.save()
            return HttpResponseRedirect('/login')
            
    else:
        fm=UserCreationForm()
    return render(request,'signup.html',{'form':fm})

def u_login(request):
    if request.method=="POST":
        fm=AuthenticationForm(request=request,data=request.POST)
   
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
          
            u=authenticate(username=uname,password=upass)
            if u is not None:
               
                login(request,u)
                return HttpResponseRedirect('/empdetails')
    else:
        fm=AuthenticationForm()

    return render(request,'login.html',{'form':fm})

def u_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

