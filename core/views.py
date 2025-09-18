
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Student, Attendance
from datetime import date

def home(request):
    return render(request, 'home.html', {'page_title': 'Dashboard'})

def courses(request):
    return render(request, 'courses.html', {'page_title': 'Courses'})


# Show all students as cards
def attendance(request):
    course_filter = request.GET.get('course', '')
    courses = Student.objects.values_list('course', flat=True).distinct()
    if course_filter:
        students = Student.objects.filter(course=course_filter)
    else:
        students = Student.objects.all()
    return render(request, 'attendance.html', {
        'page_title': 'Attendance',
        'students': students,
        'courses': courses,
        'selected_course': course_filter,
    })

# Show all attendance records for a student
def student_attendance_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    records = Attendance.objects.filter(student=student).order_by('date')
    return render(request, 'student_attendance_detail.html', {
        'student': student,
        'records': records,
        'page_title': f"Attendance for {student.name}",
    })


