"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Recommend a library or API for managing educational institution data, including features for tracking student performance, managing administrative tasks, and generating reports like those mentioned in the Politécnico Municipal's system.
Generated: DETERMINISTIC_c6c358a914f4ed56
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates the use of a library for managing educational institution data.
For production-ready implementations, consider using Django, Flask, or FastAPI for a web-based system.
Here, we use Django ORM and DRF (Django Rest Framework) as they provide excellent tools for creating APIs.
Install required packages: Django, djangorestframework
"""

# Step 1: Install Django and dependencies
# pip install django djangorestframework

# Step 2: Create a Django project and app
# django-admin startproject school_management
# cd school_management
# python manage.py startapp api

# Step 3: Configure models, serializers, and views

# File: school_management/api/models.py
from django.db import models

class Student(models.Model):
    """
    Model to represent a student in the system.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    grade = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Grade: {self.grade}"


class Performance(models.Model):
    """
    Model to track student performance.
    """
    student = models.ForeignKey(Student, related_name='performances', on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    marks_obtained = models.FloatField()
    total_marks = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.student} - {self.subject}: {self.marks_obtained}/{self.total_marks}"


class AdministrativeTask(models.Model):
    """
    Model to manage administrative tasks.
    """
    task_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()

    def __str__(self):
        return self.task_name


# File: school_management/api/serializers.py
from rest_framework import serializers
from .models import Student, Performance, AdministrativeTask

class StudentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Student model.
    """
    class Meta:
        model = Student
        fields = '__all__'


class PerformanceSerializer(serializers.ModelSerializer):
    """
    Serializer for the Performance model.
    """
    class Meta:
        model = Performance
        fields = '__all__'


class AdministrativeTaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the AdministrativeTask model.
    """
    class Meta:
        model = AdministrativeTask
        fields = '__all__'


# File: school_management/api/views.py
from rest_framework import viewsets
from .models import Student, Performance, AdministrativeTask
from .serializers import StudentSerializer, PerformanceSerializer, AdministrativeTaskSerializer

class StudentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing students.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class PerformanceViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing student performance.
    """
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer


class AdministrativeTaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing administrative tasks.
    """
    queryset = AdministrativeTask.objects.all()
    serializer_class = AdministrativeTaskSerializer


# File: school_management/school_management/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import StudentViewSet, PerformanceViewSet, AdministrativeTaskViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'performances', PerformanceViewSet)
router.register(r'admin_tasks', AdministrativeTaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Include API routes
]


# Step 4: Migrate and run the server
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver

"""
The above code creates a Django-based API system with endpoints for managing students, tracking performance, and handling administrative tasks. 

You can extend this to include reporting features using libraries like Pandas for data analysis or integrate with external reporting tools. To interact with the API, you can use tools like Postman or implement a frontend.
"""
```
