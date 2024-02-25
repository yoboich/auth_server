
from django.contrib import admin
from django.urls import path

import oauth2_provider.views as oauth2_views
from django.conf import settings

from .views import (
    index_view, login_view, 
    auth_web_app_view,
    register_user,
    secret_page,
    get_user_data,
)


urlpatterns = [
    path('', index_view, name='index'),
    path('login/', login_view, name='login'),
    path('auth_web_app/', auth_web_app_view, name='auth_web_app'),
    path('register_user/', register_user, name='register_user'),
    path('secret/', secret_page, name='secret'),
    path('get_user_data/', get_user_data, name='get_user_data')

]

