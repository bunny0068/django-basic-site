from django.shortcuts import render

# Create your views here.
def appPage(request):
    context = {'msg':"APP2 home page",'title':'APP2:Django'}
    return render(request,'appPage.html',context)