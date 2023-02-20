from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello1(request,*args,**kwargs):
   # return HttpResponse("<h1>App2 -Hello World Django</h1>")
   print(args,kwargs)
   print(request.user)
   return render(request,"index3.html")