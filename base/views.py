from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def taskList(request):
    return HttpResponse('To-do list')