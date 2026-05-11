from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render

def Index(request):
    context = {'msg':'index page','title':'index:Django'}
    return render(request,'index.html',context)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index,name='index'),
    path('app1/',include('app1.urls',namespace='app1') ),
    path('app2/',include('app2.urls',namespace='app2') ),


]
