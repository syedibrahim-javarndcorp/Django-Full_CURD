from django import forms
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User

from .models import Product
from .forms import ProductForm,CustomUser
# Create your views here.

def login_page(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('index')


    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'User doesnot exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,"user not found")


    return render(request, 'fullcurd/login_register.html')

def logout_user(request):
    logout(request)
    #messages.success(request,"user logged out succesfully")
    return redirect('login')

def new_register(request):
    page = "register"
    form = CustomUser()
    if request.method == 'POST':
        form = CustomUser(request.POST)
        if form.is_valid():
            user = form.save()
            user.username = user.username.lower()
            messages.success(request,"success")
            login(request,user)
            return redirect("index")
        else:
            messages.error(request,"failed")


    context = {
        'page': page,
        'form' : form,

    }
    return render(request,'fullcurd/login_register.html',context )


@login_required(login_url='login')
def index(request):
    product = Product.objects.all()
    context = {
        "product" : product
    }
    return render(request, 'fullcurd/index.html', context)


@login_required(login_url='login')
def create(request):

    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

    context = { 
        "form" : form

    }
    return render(request, "fullcurd/forms.html",context)


@login_required(login_url='login')
def update(request, pk):
    product = Product.objects.get(productid=pk)
    form = ProductForm(instance=product)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("index")
    context = { 
        "form" : form

    }
    return render(request, "fullcurd/forms.html",context)


@login_required(login_url='login')
def delete(request, pk): 
    product = Product.objects.get(productid=pk)
    if request.method == "POST":
        product.delete()
        return redirect('index')


    context = {
        "pro" : product
    }
    return render(request, 'fullcurd/delete.html', context)