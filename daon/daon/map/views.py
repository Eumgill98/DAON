from django.http import HttpResponse
from django.shortcuts import render

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

def home(request):
    return render(request, 'map/home.html')

def chat(requset):
    return render(requset, 'map/chat.html')

def main(request):
    return render(request, 'map/main.html')

def recomand(requset):
    return  render(requset, 'map/recomand.html')

def make(requset):
    return render(requset, 'map/make.html')
