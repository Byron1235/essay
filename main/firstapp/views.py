from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def display(request):
    return HttpResponse("<h1>Hola mundo!</h1>")

def youtubedisplay(request):
    return HttpResponse("<a href='https://www.youtube.com/watch?v=6R3ouGNcACQ&ab_channel=VersusMusicOfficial'>Clickeame!</a>")