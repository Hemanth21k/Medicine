from django.urls import path, include 
from django.conf import settings 
from . import views
from users import views as user_view 
from django.contrib.auth import views as auth
from django.conf.urls.static import static 
from django.conf.urls import url
from django.contrib.auth import views as auth_views


app_name = 'home'

urlpatterns=[
    path('', views.landing, name='landing'),
]