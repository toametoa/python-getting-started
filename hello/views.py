from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from hello.models import profile
from hello.forms import *

import threading
from .mailer import sending, startmailer






# Create your views here.
def index(request):
    
    return render(request, "index.html")



def register(request):
    if request.method == 'POST':
        form =  UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}! Your Account Has Been Created! You Can Log In Now!')
            return redirect('login')
    else:
        form =  UserRegisterForm()

    return render(request, "register.html", {'form': form})


@login_required
def uprofile(request):
    if request.method == 'POST':
        puform = ProfileUpdateForm(request.POST,instance=request.user.profile)
        uuform = UserUpdateForm(request.POST,instance=request.user)
        if puform.is_valid() and uuform.is_valid():
            puform.save()
            uuform.save()
            messages.success(request, f'Done! Your Account Has Been Updated!')
            return redirect('profile')
    else:
        puform = ProfileUpdateForm(instance=request.user.profile)
        uuform = UserUpdateForm(instance=request.user)
        city = request.user.profile.city
        desc = request.user.profile.description

    
    
    
    context = {"puform": puform, "uuform": uuform, "city": city, "desc": desc}
    return render(request, 'profile.html', context)
  



@login_required
def settings(request):
    currentuser = request.user
    if request.method == 'POST':
        
        uconfig = profile.objects.get(User=currentuser).uconfig
        uconfig['smtp'] = request.POST.get('smtp_input', None)
        uconfig['imap'] = request.POST.get('imap_input', None)
        uconfig['port'] = request.POST.get('port_input', None)
        uconfig['emaill'] = request.POST.get('emaill_input', None)
        uconfig['pass'] = request.POST.get('pass_input', None)
        uconfig['delay'] = request.POST.get('delay_input', None)
        uconfig['nrdelay'] = request.POST.get('nrdelay_input', None)
        profile.objects.filter(User=currentuser).update(uconfig=uconfig)

        context = {"uconfig": uconfig}
    else:
        uconfig = profile.objects.get(User=currentuser).uconfig
        context = {"uconfig": uconfig}
        
    
    # profile.objects.filter(User=currentuser).update(city='some value')
    # city = profile.objects.get(User=currentuser).ucont
    # city[str(currentuser)] = 4444444444
    # profile.objects.filter(User=currentuser).update(ucont=city)
    # context = {"city": city}
    return render(request, 'settings.html', context)


    

def templates1(request):
    if request.method == 'POST':
        t1uform = Temp1UpdateForm(request.POST,instance=request.user.profile)
        if t1uform.is_valid() and t1uform.is_valid():
            t1uform.save()
            messages.success(request, f'Done! Your Account Has Been Updated!')
            return redirect('profile')
    else:
        t1uform = Temp1UpdateForm(instance=request.user.profile)
        city = request.user.profile.city
        desc = request.user.profile.description
    
    
    
    context = {"t1uform": t1uform, "city": city, "desc": desc}
    return render(request, 'templates1.html', context)


def templates2(request):
    if request.method == 'POST':
        t2uform = Temp2UpdateForm(request.POST,instance=request.user.profile)
        if t2uform.is_valid() and t2uform.is_valid():
            t2uform.save()
            messages.success(request, f'Done! Your Account Has Been Updated!')
            return redirect('profile')
    else:
        t2uform = Temp2UpdateForm(instance=request.user.profile)
        city = request.user.profile.city
        desc = request.user.profile.description
    
    
    
    context = {"t2uform": t2uform, "city": city, "desc": desc}
    return render(request, 'templates2.html', context)

def templates3(request):
    if request.method == 'POST':
        t3uform = NRTempUpdateForm(request.POST,instance=request.user.profile)
        if t3uform.is_valid() and t3uform.is_valid():
            t3uform.save()
            messages.success(request, f'Done! Your Account Has Been Updated!')
            return redirect('profile')
    else:
        t3uform = NRTempUpdateForm(instance=request.user.profile)
       
    
    
    
    context = {"t3uform": t3uform}
    return render(request, 'templates3.html', context)





def start(request):
    currentuser = request.user
    profile.objects.filter(User=currentuser).update(city=1)
    startmailer(currentuser)
    
    
    return render(request, "start.html")

def stop(request):
    currentuser = request.user
    profile.objects.filter(User=currentuser).update(city=0)
    
    return render(request, "stop.html")









def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


