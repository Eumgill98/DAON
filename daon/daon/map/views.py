from django.http import HttpResponse
from django.shortcuts import render
import folium

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent


def home(request):


    return render(request, 'map/home.html')

def chat(requset):

    return render(requset, 'map/chat.html')

def main(request):
    map = folium.Map(location=[37.7854, 128.4698], zoom_start=15, width='100%', height='100%', )
    maps = map._repr_html_()

    return render(request, 'map/main.html', {'map':maps})

def recomand(requset):

    return  render(requset, 'map/recomand.html')

def make(requset):

    return render(requset, 'map/make.html')