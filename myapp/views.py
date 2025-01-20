from django.shortcuts import render, redirect
from .models import Student, Attendance
from django.utils.dateparse import parse_date

def dashboard(request):
    students = Student.objects.all()
    return render(request, 'myapp/dashboard.html', {'students': students})

def mark_attendance(request, division):
    students = Student.objects.filter(division=division)
    if request.method == 'POST':
        date = parse_date(request.POST['date'])
        for student_id, status in request.POST.items():
            if student_id.isdigit():
                Attendance.objects.create(
                    student_id=student_id,
                    date=date,
                    status=status
                )
        return redirect('dashboard')
    return render(request, 'attendance/mark_attendance.html', {'students': students, 'division': division})

def reports(request, division):
    students = Student.objects.filter(division=division)
    report_data = []
    for student in students:
        attendances = Attendance.objects.filter(student=student)
        present = attendances.filter(status='present').count()
        absent = attendances.filter(status='absent').count()
        report_data.append({'name': student.name, 'present': present, 'absent': absent})
    return render(request, 'attendance/reports.html', {'report_data': report_data, 'division': division})
