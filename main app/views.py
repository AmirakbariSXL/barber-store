from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def MY_FIRST_PROJECT(request):
  return render(request, 'index.html')
