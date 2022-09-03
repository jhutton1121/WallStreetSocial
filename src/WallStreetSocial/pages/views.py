from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage_view(*args, **kwargs):
    return HttpResponse("<h1>WallStreetSocial</h1>")