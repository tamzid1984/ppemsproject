from django.shortcuts import render,HttpResponse
from django.contrib.auth import login,logout,authenticate

# Create your views here.
from .models import *
from .forms import *

def user_login(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw']
        print(username)
        print(password)
        user=authenticate(username = username, password =password)
        if user:
            login(request, user)
    return render(request, 'login.html')

def user_profile(request):
    user = request.user
    print(user)
    userprofile = UserProfile.objects.get(user = user)
    context ={'userprofile':userprofile}
    return render(request, 'userprofile.html', context)


def add_leave_form(request):
    if request.method == 'POST':
        form = LeaveApplicationForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.user=request.user
            form.save()
            return HttpResponse("ok")
    
    else:

        form = LeaveApplicationForm()
        context ={'form' :form}
        return render(request, 'add_leave_form.html', context)