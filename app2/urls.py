from django.urls import path
from app2 import views

#create app2
app_name = 'app2'


urlpatterns = [
    path('', views.appPage,name = 'apppage'),


]
