#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
from django.core.serializers import serialize
import socket

def index(request):
    return  HttpResponse('<center>host name<h1>'+socket.gethostname()+'</h1></center>')
    #return HttpResponse('Hello')

