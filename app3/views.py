from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello2(request):
    return HttpResponse("<h1>App3 -Hello World Django</h1>")