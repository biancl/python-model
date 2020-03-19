#-*- coding:utf-8 -*-
from django.http import HttpResponse
import json

def plus(request):
    try:
        x = float(request.GET.get('x'))
        y = float(request.GET.get('y'))
        result = x+y
        return HttpResponse(result)
    except:
        return HttpResponse('参数错误，请检查参数，访问地址应该为http://[服务器地址]:[服务器端口号]/plus?x=1&y=2')
def minus(request):
    try:
        x = float(request.GET.get('x'))
        y = float(request.GET.get('y'))
        result = x-y
        return HttpResponse(result)
    except:
        return HttpResponse('参数错误，请检查参数，访问地址应该为http://[服务器地址]:[服务器端口号]/minus?x=1&y=2')
def multi(request):
    try:
        x = float(request.GET.get('x'))
        y = float(request.GET.get('y'))
        result = x*y
        return HttpResponse(result)
    except:
        return HttpResponse('参数错误，请检查参数，访问地址应该为http://[服务器地址]:[服务器端口号]/multi?x=1&y=2')
def devide(request):
    try:
        x = float(request.GET.get('x'))
        y = float(request.GET.get('y'))
        result = x/y
        return HttpResponse(result)
    except:
        return HttpResponse('参数错误，请检查参数，访问地址应该为http://[服务器地址]:[服务器端口号]/devide?x=1&y=2')