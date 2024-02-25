import os
 
import requests

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from oauth2_provider.views.generic import ProtectedResourceView

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, JsonResponse

from oauth2_provider.models import AccessToken

from .models import CustomUser as User

from dotenv import load_dotenv
load_dotenv()


@login_required()
def secret_page(request, *args, **kwargs):
    
    return HttpResponse('Secret contents!', status=200)


@login_required()
def get_user_data(request, *args, **kwargs):
    user = request.user
    data = {
        'user_id': user.id,
        'email': user.email,
    }
    return JsonResponse(data, status=200)



def index_view(request):
    return render(request, 'index.html')


def login_view(request):
    return render(request, 'registration/login.html')



def register_user(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(email=email, password=password)
        if user is None:
            user = User.objects.create_user(email=email, password=password)
            login(request, user)
            service_url = 'http://127.0.0.1:8001'
            data = { 
                'user_id': user.id   
            }
            requests.post(service_url, data=data)
            
    
def auth_web_app_view(request):
    pass