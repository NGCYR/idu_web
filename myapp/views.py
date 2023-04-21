from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse



def hompage(request):
    return render(request,'index.html')

def xy(request):
    return render(request, 'xy.html')

def clock(request):
    return render(request, 'clock.html')