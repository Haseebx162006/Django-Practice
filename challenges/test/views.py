from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,"index.html")

def feb(request):
    return HttpResponse("Bhai kam kaj seekh le")


def march(request,month):
    return HttpResponse(f"Current Month is {month}")


