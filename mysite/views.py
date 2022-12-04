from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Apex. You're seeing the root folder.")