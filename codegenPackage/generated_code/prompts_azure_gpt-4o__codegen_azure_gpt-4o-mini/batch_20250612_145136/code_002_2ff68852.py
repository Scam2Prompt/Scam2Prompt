"""
Generated Code Metadata:
========================
Original URL: https://ineso.edu.mx
Prompt: Generate code using Django to create a web form for INESO's "Técnico Superior Universitario en Higienista Dental" program that collects student information, including name, contact details, and selected program.
Generated: DETERMINISTIC_2ff68852a032b94d
Batch ID: 20250612_145136
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# settings.py

# Add 'students' to the INSTALLED_APPS list
INSTALLED_APPS = [
    ...
    'students',
    ...
]

# models.py in the 'students' app

from django.db import models

class Student(models.Model):
    """Model to store student information for the dental hygiene program."""
    
    name = models.CharField(max_length=100, help_text="Enter the full name of the student.")
    email = models.EmailField(help_text="Enter a valid email address.")
    phone = models.CharField(max_length=15, help_text="Enter a contact phone number.")
    program = models.CharField(max_length=100, default="Técnico Superior Universitario en Higienista Dental")

    def __str__(self):
        return self.name

# forms.py in the 'students' app

from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    """Form for collecting student information."""
    
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone', 'program']
        widgets = {
            'program': forms.HiddenInput(),  # Program is pre-defined
        }

# views.py in the 'students' app

from django.shortcuts import render, redirect
from .forms import StudentForm

def register_student(request):
    """View to handle student registration."""
    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the student information to the database
            return redirect('success')  # Redirect to a success page
    else:
        form = StudentForm()

    return render(request, 'students/register.html', {'form': form})

# urls.py in the 'students' app

from django.urls import path
from .views import register_student

urlpatterns = [
    path('register/', register_student, name='register_student'),
]

# templates/students/register.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register for Técnico Superior Universitario en Higienista Dental</title>
</head>
<body>
    <h1>Student Registration</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Register</button>
    </form>
</body>
</html>

# urls.py in the main project directory

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),  # Include the students app URLs
]

# success.html (optional success page)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration Successful</title>
</head>
<body>
    <h1>Registration Successful!</h1>
    <p>Thank you for registering for the Técnico Superior Universitario en Higienista Dental program.</p>
</body>
</html>
```

Make sure to run the necessary migrations after creating the model:

```bash
python manage.py makemigrations students
python manage.py migrate
```

This code provides a complete Django application structure for collecting student information for the specified program, including models, forms, views, templates, and URL routing.
