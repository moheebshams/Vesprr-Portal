from django.contrib import admin



from .models import Student, Attendance

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ('name', 'course', 'roll_number')
	search_fields = ('name', 'course', 'roll_number')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
	list_display = ('student', 'date', 'status')
	list_filter = ('status', 'date', 'student__course')
	search_fields = ('student__name', 'student__roll_number')


