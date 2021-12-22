from django.contrib import admin
from django.urls import path ,include

from home import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('paths', views.paths, name='paths'),
    path("learning",views.learning,name ='learning')
]
