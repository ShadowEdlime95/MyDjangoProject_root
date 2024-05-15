from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse('Це інформація про проект')

def home(request):
    return render(request,'home.html')

def resume(request):
    return render(request,'resume.html')