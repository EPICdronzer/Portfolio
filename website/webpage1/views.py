from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
def indexpage(request):
    return render(request,'webpage1/index.html')
