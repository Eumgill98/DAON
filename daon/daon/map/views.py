from django.http import HttpResponse
from django.shortcuts import render


from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent


def index(request):

    return render(request, 'map/index.html')

