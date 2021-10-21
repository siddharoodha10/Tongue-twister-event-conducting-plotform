from django.shortcuts import render
from . models import participant
import datetime

# Create your views here.
def display(request):
    return render(request,'display.html')

def submit(request):
    if request.method=="POST":
        p_name=request.POST["P_NAME"]
        time=request.POST["time"]
        hh,mm,ss=time.split(":")
        hh=int(hh)
        mm=int(mm)
        ss=int(ss)
        time=datetime.time(hh,mm,ss)
        print(p_name,time)
        part =  participant.objects.create(p_name=p_name,time=time)
        part.save()
        return render(request,'display.html')
    else:
        return render(request,'display.html')
def result(request):
    part=participant.objects.all()
    part=part.order_by('time').reverse()
    count=0
    # for i in part:
    #     print(i.p_name)
    #     print(i.time)
    # return render(request,'result.html',{"part":part})
    parti=[]
    for i in part:
        if count==3:
            break
        hh,mm,ss=i.time.hour,i.time.minute,i.time.second
        if hh<10:
            hh="0"+str(hh)
        else:
            hh=str(hh)
        if mm<10:
            mm='0'+str(mm)
        else:
            mm=str(mm)
        if ss<10:
            ss='0'+str(ss)
        else:
            ss=str(ss)
        parti.append([count+1,i.p_name,hh+'-'+mm+'-'+ss])
        count+=1
    print(parti)
    return render(request,'result.html',{"part":parti})
        