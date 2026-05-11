from django.shortcuts import render

# Create your views here.

def appPage(request):
    context = {'msg':"APP1 home page",'title':'APP1:Django'}
    return render(request,'appPage.html',context)
