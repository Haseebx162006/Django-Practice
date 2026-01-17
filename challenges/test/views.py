from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("hey am a  backend dev")

def feb(request):
    return HttpResponse("Bhai kam kaj seekh le")