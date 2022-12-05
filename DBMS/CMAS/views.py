from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from CMAS.models import *

# Create your views here.

def index(request):
    return render(request,'signin/index.html')

def signup(request):
    if request.method == 'POST':

        form = UserCreationForm()
        if form.is_valid():
            form.save()

            return redirect('CMAS:index')
    
    else:
        form = UserCreationForm()



    return render(request,'signin/signup.html', {'form':form})


def login(request):
    if request.method == 'POST':
        utype = (request.POST.get('usertype'))
        if utype == "faculty":
            return render(request, 'dashboard/faculty/faculty_dashboard.html')
        else:
            return render(request, 'dashboard/student/student_dashboard.html')

    return render(request, 'signin/sign_in.html')


def fDashboard(request):
    return render(request, 'dashboard/faculty/faculty_dashboard.html')


def fCo(request):
    return render(request, 'dashboard/faculty/faculty_CO.html')


def fQb(request):
    return render(request, 'dashboard/faculty/faculty_QB.html')


def sDashboard(request):
    return render(request, 'dashboard/student/student_dashboard.html')


def sCo(request):
    return render(request, 'dashboard/student/student_CO.html')


def sQb(request):
    return render(request, 'dashboard/student/student_QB.html')


def createQb(request):
    return render(request, 'dashboard/faculty/questionbank/createQB.html')


def viewCo(request):
    return render(request, 'dashboard/faculty/courseoutline/ViewCO.html')


def createCo(request):
    return render(request, 'dashboard/faculty/courseoutline/createCO.html',)


def viewAssessment(request):
    return render(request, 'dashboard/faculty/questionbank/viewAssessment.html')

# Create your views here.