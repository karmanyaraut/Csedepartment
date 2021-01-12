from django.shortcuts import render,redirect
from .models import *
from django.conf import settings
from .forms import FacultyForm
def index(request):
    return render(request,'nitkapp/home.html')
def faculty(request):
#facultyinfo = FacultyProfileInfo.objects.all()

    if request.method=="POST":
        form = FacultyForm(request.POST)
        if form.is_valid():

            temp=form.cleaned_data['faculty_type']
            print('temp value \n',temp)
            facultyinfo = FacultyProfileInfo.objects.filter(typeoffaculty=temp)
            context ={'img':facultyinfo,'media_url':settings.MEDIA_URL ,'form': form}
            print(facultyinfo)
            return render(request,'nitkapp/faculty.html',context)
    else:
        form = FacultyForm()
    return render(request,'nitkapp/faculty.html',{'form': form})

def placements(request):
    placementinfo = Placementstat.objects.all()
    context={'infoplace':placementinfo}
    return render(request,'nitkapp/placements.html',context)

def research(request):
    researchinfo = Researchinfo.objects.all()
    context ={'researchobj':researchinfo}


    return render(request,'nitkapp/research.html',context)
def coursesview(request):
    #context={'infoplace':placementinfo}
    coursesinfo = Coursesinfo.objects.all()
    context ={'coursesobj':coursesinfo,'media_url':settings.MEDIA_URL}
    return render(request,'nitkapp/courses.html',context)
