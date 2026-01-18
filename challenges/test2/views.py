from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    dict1={"name":"Hamza"}
    return render(request,"index.html",dict1)
    
