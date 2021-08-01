from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from directory.models import *
import csv, io
from django.shortcuts import render
from django.contrib import messages


def index(request):
    try:
        teacher = Teachers.objects.filter().order_by('id')
    except Teachers.DoesNotExist:	
        teacher = None	
    return render(request,'portal/home/list.html',{'teacher':teacher})

def profileimporter(request):

    if request.method == 'POST':
        csv_file = request.FILES['fileimport']
        # let's check if it is a csv file
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'THIS IS NOT A CSV FILE')
        data_set = csv_file.read().decode('UTF-8')
        # setup a stream which is when we loop through each line we are able to handle a data in a stream
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            #print(column)
            colume1 = colume2 = colume3 = colume4 = colume5 = colume6 = ""

            if column[0]:
                colume0 = column[0]
            if column[1]:
                colume1 = column[1]
            if column[2]:
                colume2 = column[2]
            if column[3]:
                colume3 = column[3]
            if column[4]:
                colume4 = column[4]
            if column[5]:
                colume5 = column[5]
            if column[6]:
                colume6 = (column[6]).strip()

            
            try:
                teacher = Teachers.objects.get(email=str(column[3]))
            except Teachers.DoesNotExist:	
                #teacher = None
                created = Teachers.objects.update_or_create(
                firstname=colume0,
                lastname=colume1,
                profileimg=colume2,
                email=colume3,
                phone=colume4,
                room_number=colume5,
                subjects=colume6,
                )
        return HttpResponseRedirect('/')
