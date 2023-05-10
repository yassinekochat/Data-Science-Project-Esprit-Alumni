from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
import requests
import sys
from subprocess import run,PIPE
import recom_app.test2
import recom_app.test3
import recom_app.test


def index(request):
    return render(request, 'index.html')
def recom(request):
    return render(request, 'recom.html')

def charts(request):
    return render(request, 'bb.html')

def button(request):
    return render(request,'recom.html')



def external(request):
    inp=request.POST.get('param')
    out= run([sys.executable,'C:\\Users\\admin\\PycharmProjects\\djangoProject1\\recom_app\\test2.py',inp]
             ,universal_newlines=True,stdout=PIPE)
    print(out)

    str(out.stdout)

    return render(request,'recom.html',{'data1': str(out.stdout)})


def externalskill(request):
    inp=request.POST.get('param2')
    out= run([sys.executable,'C:\\Users\\admin\\PycharmProjects\\djangoProject1\\recom_app\\test3.py',inp] ,universal_newlines=True,stdout=PIPE)
    print(out)

    return render(request,'recom.html',{'data2':out.stdout})

def cluser(request):
    out= run([sys.executable,'C:\\Users\\admin\\PycharmProjects\\djangoProject1\\recom_app\\test.py'] ,universal_newlines=True,stdout=PIPE)
    print(out)

    return render(request,'recom.html',{'data3':out.stdout})

