from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)  # Student's name
    roll_number = models.IntegerField(unique=True, default=1)  # Ensure unique roll numbers
    division = models.CharField(max_length=5)  # Division of the student (e.g., A, B, etc.)

    def __str__(self):
        return f"{self.name} ({self.roll_number})"  # Include roll number in the string representation


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Link to a specific student
    date = models.DateField()  # Date of attendance
    status = models.CharField(
        max_length=10,
        choices=[('Present', 'Present'), ('Absent', 'Absent')]  # Limit values to Present/Absent
    )

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"  # Attendance details
