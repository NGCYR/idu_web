from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from animations.dilation import *


def hompage(request):
    return render(request,'index.html')

def dilation(request):
    return render(request, 'dilation.html')

def get_dilation_factors(request):
    render = True
    user_x_factor = request.GET["x_factor"]
    user_y_factor = request.GET["y_factor"]
    user_z_factor = request.GET["z_factor"]
    print(user_x_factor,user_y_factor,user_z_factor)
    dilation_anim(render,user_x_factor,user_y_factor,user_z_factor)
