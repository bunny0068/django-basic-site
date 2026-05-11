from django.urls import path
from app1 import views

#create app1

app_name = 'app1'

urlpatterns = [
    path('', views.appPage,name = 'apppage'),


]
