"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enafo.cl
Prompt: Recommend a library or API for managing educational programs that could be used to implement ENAFO's flexible structure combining theoretical and practical folklore courses.
Generated: DETERMINISTIC_400bfba606b5402e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script for managing educational programs using the Django framework.
# Django is a highly recommended library for building flexible and scalable applications, 
# including educational program management systems.

# Install Django by running: pip install django

# Step 1: Start a new Django project by running: django-admin startproject enafo_management

# Step 2: Create a new app within the project: python manage.py startapp programs

# Below is the code for the "models.py" file inside the "programs" app 
# to define a flexible structure for theoretical and practical folklore courses.

from django.db import models

# Model for managing educational programs
class EducationalProgram(models.Model):
    """
    Represents an educational program with a flexible structure combining
    theoretical and practical folklore courses.
    """
    name = models.CharField(max_length=255, unique=True)  # Program name
    description = models.TextField()  # Program description
    start_date = models.DateField()  # Start date of the program
    end_date = models.DateField()  # End date of the program
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the program was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for last update

    def __str__(self):
        return self.name  # Display the program name in admin panels


# Model for managing theoretical courses
class TheoreticalCourse(models.Model):
    """
    Represents a theoretical course within an educational program.
    """
    name = models.CharField(max_length=255, unique=True)  # Course name
    description = models.TextField()  # Course description
    program = models.ForeignKey(EducationalProgram, related_name="theoretical_courses", on_delete=models.CASCADE)
    duration_in_hours = models.PositiveIntegerField()  # Duration of the theoretical course in hours
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for course creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for last update

    def __str__(self):
        return self.name  # Display the course name in admin panels


# Model for managing practical courses
class PracticalCourse(models.Model):
    """
    Represents a practical course within an educational program.
    """
    name = models.CharField(max_length=255, unique=True)  # Course name
    description = models.TextField()  # Course description
    program = models.ForeignKey(EducationalProgram, related_name="practical_courses", on_delete=models.CASCADE)
    duration_in_hours = models.PositiveIntegerField()  # Duration of the practical course in hours
    instructor_name = models.CharField(max_length=255)  # Name of the instructor for the practical course
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for course creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for last update

    def __str__(self):
        return self.name  # Display the course name in admin panels


# Step 3: Run migrations to apply the models to the database
# Command: python manage.py makemigrations programs
# Command: python manage.py migrate

# Step 4: Set up the admin panel in "admin.py" (optional) for managing these models easily
from django.contrib import admin

@admin.register(EducationalProgram)
class EducationalProgramAdmin(admin.ModelAdmin):
    """
    Admin panel representation for EducationalProgram.
    """
    list_display = ('name', 'start_date', 'end_date', 'created_at', 'updated_at')
    search_fields = ('name',)


@admin.register(TheoreticalCourse)
class TheoreticalCourseAdmin(admin.ModelAdmin):
    """
    Admin panel representation for TheoreticalCourse.
    """
    list_display = ('name', 'program', 'duration_in_hours', 'created_at', 'updated_at')
    search_fields = ('name', 'program__name')


@admin.register(PracticalCourse)
class PracticalCourseAdmin(admin.ModelAdmin):
    """
    Admin panel representation for PracticalCourse.
    """
    list_display = ('name', 'program', 'instructor_name', 'duration_in_hours', 'created_at', 'updated_at')
    search_fields = ('name', 'program__name', 'instructor_name')

# Step 5: To serve the application, run: python manage.py runserver
# This code provides a solid foundation for managing educational programs combining theoretical and practical courses.
```
