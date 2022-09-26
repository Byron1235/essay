from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def displaytime(request):
    dt= datetime.datetime.now()
    s="<p>Fecha y hora actual: </p>"+ str(dt)
    return HttpResponse(s)

def displayyoutube2(request):
    return HttpResponse("<a href='https://www.youtube.com/watch?v=6R3ouGNcACQ&ab_channel=VersusMusicOfficial'>Click me!</a>")
