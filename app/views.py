from __future__ import unicode_literals

from django.http import JsonResponse
from django.http import Http404
from django.shortcuts import render


def index(request):
    return render(request, 'app/index.html')

def prices(request):
    return render(request, 'app/prices.html')

def poverty(request):
    return render(request, 'app/poverty.html')

def govt_initiatives(request):
    return render(request, 'app/updates.html')

def login(request):
    return render(request, 'app/login.html')

def register(request):
    return render(request, 'app/register.html')

def forgot(request):
    return render(request, 'app/forgot-password.html')

def pagenotfound(request):
    return render(request, 'app/404.html')


