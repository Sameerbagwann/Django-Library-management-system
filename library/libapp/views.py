from django.shortcuts import render,redirect
from django.http import HttpResponse
from libapp.models import AddBook
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

import datetime

# Create your views here.
def index(request):
    p=AddBook.objects.filter(status=1).order_by('-created_on')
    content={}
    content['data']=p
    return render(request,'index.html',content)

def home(request):
    return render(request,'home.html')

def createpost(request):
    print(request.method)
    if request.method=="POST":
               
       pname=request.POST['name']
       pauthor=request.POST['author']
       pdetail=request.POST['pdet']
       pcat=request.POST['cat']
       pstatus=request.POST['status']
       image=request.POST['image']
       userid=request.session ['user_id']


       p=AddBook.objects.create(name=pname,author=pauthor,pdet=pdetail,cat=pcat,status=pstatus,image=image,created_on=datetime.datetime.now(),uid=userid)
       print(p)
       p.save() 
       return redirect('udash.html')

    else:
        return render(request,'createpost.html')

def edit(request,rid):
    if request.method=="POST":
        uptitle=request.POST['name']
        usdetail=request.POST['author']
        updetail=request.POST['pdet']
        
        upcat=request.POST['cat']


        p=AddBook.objects.filter(id=rid)#objects row is retrieved from database
        p.update(name=uptitle,author=usdetail,pdet=updetail,cat=upcat)
        #update bloapp_post set title=uptitle,sdet=usdetail,pdet=updetail,cat=upcat,status=upstatus where id=rid;

        return redirect('/udash')


    else:
        p=AddBook.objects.filter(id=rid)
        content={}
        content['data']=p
        return render(request,'editform.html',content)


def delete(request,rid):
    p=AddBook.objects.get(id=rid)  # Select * from blopapp_pot where id=rid
    p.delete()
    return redirect('/udash')


def singlepost(request):
    return render(request,'singlepost.html')


def dashboard(request):
    if request.session.get('user_id'):
        userid=request.session ['user_id']
        p=AddBook.objects.filter(uid=userid)
        #print(p)
        content={}
        content['data']=p
        return render(request,'dashboard.html',content)
    else:
        return redirect('/login')

def postdetail(request,rid):
    p=AddBook.objects.filter(id=rid)
    content={}
    content['data']=p
    return render(request,'postdetail.html',content)

def login(request):
    if request.method=="POST":
        email=request.POST['email']
        print(email)
        upass=request.POST['upass']
        print(upass)
        u=authenticate(username=email,password=upass)
        print(u)
        

        error={}
        

        if u is not None:
            lu=User.objects.get(username=u)
            # print(lu.id)
            request.session ['user_id']=lu.id #restoring logged in user id in session
            return redirect('/udash')

            
        else:
            
            error['msg']="Invalid username and Password !!!"
            return render(request,'login.html',error)

    else:
        return render(request,'login.html')

def user_logout(request):
    
    del request.session['user_id']
    return redirect ('/login')


def register(request):

    if request.method=="POST":
        name=request.POST['uname']
        email=request.POST['uemail']
        upass=request.POST['upass']
        print(upass)
        cupass=request.POST['cupass']
        print(cupass)

        error={}
        err=0
        success={}
        # blank Field validation start 
        if name=="":
            err=1
            error['errnamemsg']="Name field cannot be blank"
            print('In name field')
        elif email=="":
            err=1
            error['erremailmsg']="Email field cannot be blank"
            print("error in email field")
        elif upass=="":
            err=1
            error['errupassmsg']="Password field cannot be blank"

        elif cupass=="":
            err=1
            error['errcupassmsg']="Confirm password field cannot be blank"

        elif upass!=cupass:
            err=1
            error['errmismatch']="Password and confirm password didn't Matched"

        # Field validation end 
        if err == 0:

            u=User.objects.create_user(username=email,password=upass,first_name=name)
            print(u)
            u.save()
            success['msg']="User created Successfully!"
            return render(request,'register.html',success)
        else:
            return render(request,'register.html',error)

    else:

        return render(request,'register.html')





