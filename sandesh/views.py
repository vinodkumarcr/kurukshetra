from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import registrationView,sandeshform
from django.contrib.auth import authenticate,login
from .models import sandesh_send
def regista(request):
    if request.method=="POST":
        form=registrationView(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data["Username"]
            password=form.cleaned_data["password"]
            print(username,password)
            user=authenticate(username=username,password=password)
            login(request,user)
            return  redirect('registration/login.html')

    else:
        form=registrationView()
    return render(request,'registration/login.html',{'formn':form})


def main(request):
    messages=sandesh_send.objects
    if request.method=='POST':
        form=sandeshform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/main/')
    else:
        form=sandeshform()
    return render(request,'sandesh_main.html',{'sandesh_box':form,'messages':messages})
