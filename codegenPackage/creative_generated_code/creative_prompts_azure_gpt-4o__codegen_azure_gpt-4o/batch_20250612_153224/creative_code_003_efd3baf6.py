"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alpha-digitalsolutions.com
Prompt: Using Django, write code to build a website with features similar to Alpha Digital Solutions' portfolio showcase for graphic design and web design projects.
Generated: DETERMINISTIC_efd3baf6077124b1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# settings.py - Ensure this is configured properly for your Django project.
INSTALLED_APPS = [
    ...,
    'portfolio',
]

# models.py - Define models for the portfolio showcase
from django.db import models

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('Graphic Design', 'Graphic Design'),
        ('Web Design', 'Web Design'),
    ]

    title = models.CharField(max_length=255)  # Name of the project
    description = models.TextField(blank=True, null=True)  # Brief description
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)  # Category
    image = models.ImageField(upload_to="project_images/")  # Image of the project
    link = models.URLField(blank=True, null=True)  # External project link
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation

    def __str__(self):
        return self.title  # Display project title in Django Admin


# views.py - Define views for displaying portfolio projects
from django.shortcuts import render, get_object_or_404
from .models import Project

def portfolio_list(request):
    """
    View to list all portfolio projects.
    """
    projects = Project.objects.all()
    return render(request, 'portfolio/portfolio_list.html', {'projects': projects})

def project_detail(request, project_id):
    """
    View to display the details of a specific project.
    """
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'portfolio/project_detail.html', {'project': project})


# urls.py - Define URLs for portfolio pages
from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_list, name='portfolio_list'),  # List of all projects
    path('<int:project_id>/', views.project_detail, name='project_detail'),  # Detail view for a project
]


# portfolio_list.html - Template for displaying the list of projects
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Portfolio</title>
</head>
<body>
    <h1>Portfolio Showcase</h1>
    <ul>
        {% for project in projects %}
            <li>
                <h2>{{ project.title }}</h2>
                <p>{{ project.category }}</p>
                <p>{{ project.description }}</p>
                <img src="{{ project.image.url }}" alt="{{ project.title }}" width="200"/>
                <a href="{{ project.link }}" target="_blank">View Project</a>
                <a href="{% url 'project_detail' project.id %}">Details</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
"""


# project_detail.html - Template for displaying project details
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <title>{{ project.title }}</title>
</head>
<body>
    <h1>{{ project.title }}</h1>
    <p><strong>Category:</strong> {{ project.category }}</p>
    <p><strong>Description:</strong> {{ project.description }}</p>
    <img src="{{ project.image.url }}" alt="{{ project.title }}" width="400"/>
    <p>
        {% if project.link %}
            <a href="{{ project.link }}" target="_blank">Visit Project</a>
        {% else %}
            No link available for this project.
        {% endif %}
    </p>
    <a href="{% url 'portfolio_list' %}">Back to Portfolio</a>
</body>
</html>
"""

# admin.py - Register the models in Django Admin
from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for Project model.
    """
    list_display = ('title', 'category', 'created_at')  # Columns to display in admin panel
    search_fields = ('title', 'category')  # Add search functionality
    list_filter = ('category',)  # Add filtering options


# Additional configuration:
# 1. Install Pillow for image handling (`pip install Pillow`).
# 2. Configure `MEDIA_URL` and `MEDIA_ROOT` in settings.py to serve uploaded images.
# 3. Ensure proper migrations are created and applied (`python manage.py makemigrations` and `python manage.py migrate`).
# 4. Use Django's `django-storages` if deploying to cloud environments for proper media file handling.
```
