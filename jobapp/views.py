from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'jobapp/index.html')

def hyderabad(request):
    jobs_list = HyderabadJobs.objects.all().order_by('date')
    My_dict = {'jobs_list': jobs_list}
    return render(request, 'jobapp/hyderabadjobs.html', context= My_dict)

def chennai(request):
    jobs_list = ChennaiJobs.objects.all().order_by('date')
    My_dict = {'jobs_list': jobs_list}
    return render(request, 'jobapp/chennaijobs.html', context= My_dict)

def bangalore(request):
    jobs_list = BangaloreJobs.objects.all().order_by('date')
    My_dict = {'jobs_list': jobs_list}
    return render(request, 'jobapp/bangalorejobs.html', context= My_dict)

def pune(request):
    jobs_list = PuneJobs.objects.all().order_by('date')
    My_dict = {'jobs_list': jobs_list}
    return render(request, 'jobapp/punejobs.html', context= My_dict)

