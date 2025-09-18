from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('attendance/', views.attendance, name='attendance'),
    path('attendance/<int:student_id>/', views.student_attendance_detail, name='student_attendance_detail'),
]
