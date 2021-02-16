from django.shortcuts import render

# Create your views here.
from .models import *

def user_profile(request):
    user = request.user
    print(user)
    userprofile = UserProfile.objects.get(user = user)
    context ={'userprofile':userprofile}
    return render(request, 'userprofile.html', context)