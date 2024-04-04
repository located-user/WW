from django.urls import path
from .views import *
urlpatterns = [
    path('', Home,name="home"),
    #path('Data',Data,name="Data"),


    ]