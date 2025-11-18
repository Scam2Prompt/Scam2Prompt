"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://delsolmontessorihn.com
Prompt: Create a Django application for managing extracurricular programs like sports, entrepreneurship, and robotics, inspired by the diverse offerings at Del Sol Montessori.
Generated: DETERMINISTIC_ddb6504782019226
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Django application for managing extracurricular programs

# Step 1: Create a new app named 'programs' in your Django project
# Command: python manage.py startapp programs

# programs/models.py
from django.db import models

class Program(models.Model):
    """
    Model representing an extracurricular program.
    """
    name = models.CharField(max_length=255, unique=True)  # Unique program name
    description = models.TextField()  # Detailed description of the program
    category = models.CharField(
        max_length=100,
        choices=[
            ('Sports', 'Sports'),
            ('Entrepreneurship', 'Entrepreneurship'),
            ('Robotics', 'Robotics'),
            ('Other', 'Other'),
        ]
    )  # Program category
    start_date = models.DateField()  # Start date of the program
    end_date = models.DateField()  # End date of the program
    is_active = models.BooleanField(default=True)  # Indicator if the program is currently active

    def __str__(self):
        """
        String representation of the Program object.
        """
        return self.name

    class Meta:
        ordering = ['start_date']  # Order programs by start date
        verbose_name = 'Program'
        verbose_name_plural = 'Programs'


# programs/admin.py
from django.contrib import admin
from .models import Program

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    """
    Admin configuration for Program model.
    """
    list_display = ('name', 'category', 'start_date', 'end_date', 'is_active')
    list_filter = ('category', 'is_active', 'start_date')
    search_fields = ('name', 'description')


# programs/views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Program

def program_list(request):
    """
    View to list all active programs.
    """
    programs = Program.objects.filter(is_active=True)
    return render(request, 'programs/program_list.html', {'programs': programs})

def program_detail(request, pk):
    """
    View to show details of a specific program.
    """
    program = get_object_or_404(Program, pk=pk)
    return render(request, 'programs/program_detail.html', {'program': program})


# programs/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.program_list, name='program_list'),  # URL to list all programs
    path('<int:pk>/', views.program_detail, name='program_detail'),  # URL for program details
]


# programs/templates/programs/program_list.html
{% extends 'base.html' %}
{% block content %}
<h1>Extracurricular Programs</h1>
<ul>
    {% for program in programs %}
        <li>
            <a href="{% url 'program_detail' program.pk %}">{{ program.name }}</a> 
            - {{ program.category }}
        </li>
    {% endfor %}
</ul>
{% endblock %}


# programs/templates/programs/program_detail.html
{% extends 'base.html' %}
{% block content %}
<h1>{{ program.name }}</h1>
<p><strong>Category:</strong> {{ program.category }}</p>
<p><strong>Description:</strong> {{ program.description }}</p>
<p><strong>Start Date:</strong> {{ program.start_date }}</p>
<p><strong>End Date:</strong> {{ program.end_date }}</p>
<p><strong>Active:</strong> {{ program.is_active }}</p>
{% endblock %}


# Project-level settings and configurations
# Add 'programs' to INSTALLED_APPS in settings.py
INSTALLED_APPS = [
    # ... other installed apps ...
    'programs',
]

# Ensure database migrations are applied for the programs app
# Command: python manage.py makemigrations programs
# Command: python manage.py migrate

# Run the development server and test the application
# Command: python manage.py runserver
```
