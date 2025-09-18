from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def courses(request):
    return render(request, 'courses.html')

def attendance(request):
    return render(request, 'attendance.html')


