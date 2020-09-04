from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'home.html')

def constact(request):
    return render(request, 'conn.html')