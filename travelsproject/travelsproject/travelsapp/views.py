from django.http import  HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Person
# Create your views here.
def index(request):
    obj=Place.objects.all()
    return render(request,"index.html",{'result':obj})
def demo(request):
    abc=Person.objects.all()
    return render(request, "index.html", {'res': abc})


# def about(request):
#     return render(request,"about.html")
# def contact(request):
#     return  HttpResponse("hello iam inmakes")