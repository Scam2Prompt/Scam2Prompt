"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://springsinternational.org
Prompt: Generate code to create a searchable database of retreat study materials, including content from Springs International Ministries and Campus Crusade for Christ, using Django or Flask.
Generated: DETERMINISTIC_fd1d5edb8f0c97e8
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's the code using Django:

```python
# models.py

from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class StudyMaterial(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# views.py

from django.shortcuts import render
from django.db.models import Q
from .models import StudyMaterial

def search_materials(request):
    query = request.GET.get('q', '')  # Get the search query from the request
    materials = StudyMaterial.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    ) if query else StudyMaterial.objects.all()

    return render(request, 'search_results.html', {'materials': materials, 'query': query})

# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_materials, name='search_materials'),
]

# templates/search_results.html

<!DOCTYPE html>
<html>
<head>
    <title>Search Retreat Study Materials</title>
</head>
<body>
    <h1>Search Retreat Study Materials</h1>

    <form method="get" action="{% url 'search_materials' %}">
        <input type="text" name="q" placeholder="Search for materials" value="{{ query }}">
        <button type="submit">Search</button>
    </form>

    <ul>
        {% for material in materials %}
            <li><strong>{{ material.title }}</strong> ({{ material.organization.name }}) - {{ material.created_at }}
                <p>{{ material.content }}</p>
            </li>
        {% empty %}
            <li>No materials found.</li>
        {% endfor %}
    </ul>
</body>
</html>

# admin.py

from django.contrib import admin
from .models import Organization, StudyMaterial

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(StudyMaterial)
class StudyMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'created_at')
    search_fields = ('title', 'content', 'organization__name')

# settings.py (Ensure the required settings are added)

INSTALLED_APPS += [
    # Add your app name here, for instance:
    'your_app_name',
]

# Command to run migrations and start server
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
```

This code implements a searchable database of retreat study materials using Django's ORM. You can add content from Springs International Ministries and Campus Crusade for Christ as entries in the database via the Django admin interface.
