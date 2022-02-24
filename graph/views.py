from django.shortcuts import render, redirect
from .models import Record
from django.http import HttpResponse

import csv

# Create your views here.
def index(request):
    return render(request, 'base.html', context={'text': 'Hello world'})

def exportcsv(request):
    records = Record.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=readings.csv'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Timestamp', 'Data', 'SensorID', 'Tool'])
    recs = records.values_list('id', 'timestamp', 'data_value', 'sensor', 'tool_used')
    
    for rec in recs:
        writer.writerow(rec)
    
    return response