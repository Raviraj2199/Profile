from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def hello(request,*args,**kwargs):
    print(args,kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello World Django</h1>")
    return render(request,"index.html")

def rootpage(request):
    return HttpResponse("<h1>Hello Is The RootPage For Django</h1>")

