from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request handler

def home(request):
    # return HttpResponse('Hello World')
    return render(request, 'index.html')


def login_page(request):
    return render(request, 'login.html')