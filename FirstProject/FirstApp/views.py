from  django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"FirstApp/index.html")
def huutrong(request):
    return HttpResponse("Hello, Trong!")
def greeting(request, name):
    return render(request, "FirstApp\greet.html",{
        "name": name.capitalize
    })
