from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html', {'page_title': 'Dashboard'})

def courses(request):
    return render(request, 'courses.html', {'page_title': 'Courses'})

def attendance(request):
    return render(request, 'attendance.html', {'page_title': 'Attendance'})


