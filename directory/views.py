from django.shortcuts import render
from django.http import HttpResponse
from directory.models import *


def index(request):
    try:
        teacher = Teachers.objects.filter()
    except Teachers.DoesNotExist:	
        teacher = None	
    return render(request,'portal/home/list.html',{'teacher':teacher})
    

# Create your views here.
