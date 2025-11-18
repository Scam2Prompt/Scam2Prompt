"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: Write Python code using Django to create a web application that categorizes profiles into groups like "Real Estate," "Artists," and "Business Owners," similar to the structure on "The Faces Of Sedona and the Verde Valley."
Generated: DETERMINISTIC_23f3347e4dcaa40c
Batch ID: 20250612_153907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# models.py
from django.db import models


class Category(models.Model):
    """
    Represents a category like 'Real Estate', 'Artists', or 'Business Owners'.
    """
    name = models.CharField(max_length=255, unique=True)  # Category name must be unique
    description = models.TextField(blank=True, null=True)  # Optional description of the category

    def __str__(self):
        return self.name


class Profile(models.Model):
    """
    Represents a profile, which belongs to a specific category.
    """
    name = models.CharField(max_length=255)  # Name of the individual or business
    bio = models.TextField(blank=True, null=True)  # Optional bio or description
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="profiles")  # Link to Category

    def __str__(self):
        return self.name


# views.py
from django.shortcuts import render, get_object_or_404
from .models import Category, Profile


def category_list(request):
    """
    Displays a list of all categories.
    """
    categories = Category.objects.all()
    return render(request, 'app/category_list.html', {'categories': categories})


def category_detail(request, category_id):
    """
    Displays all profiles belonging to a specific category.
    """
    category = get_object_or_404(Category, id=category_id)
    profiles = category.profiles.all()
    return render(request, 'app/category_detail.html', {'category': category, 'profiles': profiles})


# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),  # URL for listing all categories
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),  # URL for viewing profiles in a category
]


# admin.py
from django.contrib import admin
from .models import Category, Profile


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Category model.
    """
    list_display = ('name', 'description')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Profile model.
    """
    list_display = ('name', 'category', 'bio')


# templates/app/category_list.html
<!DOCTYPE html>
<html>
<head>
    <title>Categories</title>
</head>
<body>
    <h1>Categories</h1>
    <ul>
        {% for category in categories %}
            <li>
                <a href="{% url 'category_detail' category.id %}">{{ category.name }}</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>


# templates/app/category_detail.html
<!DOCTYPE html>
<html>
<head>
    <title>{{ category.name }}</title>
</head>
<body>
    <h1>{{ category.name }}</h1>
    <p>{{ category.description }}</p>
    <h2>Profiles</h2>
    <ul>
        {% for profile in profiles %}
            <li>{{ profile.name }} - {{ profile.bio }}</li>
        {% endfor %}
    </ul>
    <a href="{% url 'category_list' %}">Back to Categories</a>
</body>
</html>


# settings.py (relevant part for connecting templates)
# Ensure 'DIRS' includes the templates folder
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
