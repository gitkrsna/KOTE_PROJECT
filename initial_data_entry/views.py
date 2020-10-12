import csv
from django.http import StreamingHttpResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *
from .forms import *

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date 
from datetime import datetime 
import time
from datetime import datetime 
import pytz 
import csv 
UTC = pytz.utc 
IST = pytz.timezone('Asia/Kolkata') 



def PersonCreate(request):
    form = InitialDataEntryForm()
    if request.method == 'POST':
        form = InitialDataEntryForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(index)
    return render(request, 'blank.html', locals())


def InOut(request):
    inout = Attendance.objects.all()
    persons = InitialDataEntry.objects.all()
    form = AttendanceForm()
    if request.method == 'POST':
        form = AttendanceForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            temp=form.save(commit=False)
            temp.date = date.today()
            datetime_ist = datetime.now(IST)
            f_time = datetime_ist.strftime('%H:%M') 
            temp.weapon_out = f_time
            temp.save()
            return redirect(index)
    return render(request, 'in-out.html', locals())

   
def index(request):
    return render(request, 'index.html', locals())

    
def IssuedWeaponList(request):
    issued_alloted_wpn = Attendance.objects.all()
    return render(request, 'allissuedlist.html', locals())


def TodayWeaponList(request):
    alloted_wpn = Attendance.objects.filter(weapon_in__isnull=True)
    return render(request, 'list.html', locals())


def returnweapon(request, pk):
    obj = Attendance.objects.get(id=pk)
    datetime_ist = datetime.now(IST)
    f_time = datetime_ist.strftime('%H:%M') 
    obj.weapon_in = f_time
    obj.save()
    return HttpResponseRedirect("/today-in-out")
    

def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="inout.csv"'

    writer = csv.writer(response)
    writer.writerow(['Army Number', 'Name', 'Rank','I_Card Number' , 'Trade','Company','Weapon Type', 'Regd Number','Butt Number', 'Issue Type','Weapon Out','Weapon In', 'Date'])

    users = Attendance.objects.filter(date=date.today())
    for user in users:
        writer.writerow([user.person.army_no,user.person.name,user.person.rank,user.person.i_card_no,user.person.trade,user.person.company,user.person.wpn_type,user.person.regd_no, user.person.butt_no,user.person.issue_type,user.weapon_out, user.weapon_in, user.date ])

    return response    
