from django.db import models


class Student(models.Model):
	name = models.CharField(max_length=100)
	course = models.CharField(max_length=100)
	roll_number = models.CharField(max_length=20)

	def __str__(self):
		return f"{self.name} ({self.roll_number})"

class Attendance(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	date = models.DateField()
	status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

	def __str__(self):
		return f"{self.student.name} - {self.date} - {self.status}"
