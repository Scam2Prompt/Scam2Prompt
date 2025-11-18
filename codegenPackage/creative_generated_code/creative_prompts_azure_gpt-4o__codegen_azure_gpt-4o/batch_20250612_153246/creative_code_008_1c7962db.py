"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enafo.cl
Prompt: Suggest a library or framework for building an online platform that replicates ENAFO's educational structure, allowing students to enroll in monitorías and modules.
Generated: DETERMINISTIC_1c7962dbca85c10e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example of a production-ready Python code using the Django framework to implement an online educational platform where students can enroll in monitorías (tutoring sessions) and modules. Django is widely used for building web applications and is a great choice for this type of platform.

```python
# Install Django by running `pip install django` before executing this code.
# Create a new Django project using `django-admin startproject enafo_platform` and add this code in appropriate files.

# models.py - Define the database models to represent Students, Monitorías, and Modules.
from django.db import models
from django.contrib.auth.models import User

class Module(models.Model):
    """
    Represents a module of study in the educational platform.
    """
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Monitoria(models.Model):
    """
    Represents a tutoring session that students can enroll in.
    """
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="monitorias")
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tutoring_sessions")
    date = models.DateTimeField()
    max_students = models.PositiveIntegerField()

    def __str__(self):
        return f"Monitoria for {self.module.title} by {self.tutor.username}"


class Enrollment(models.Model):
    """
    Represents a student's enrollment in a monitoria or module.
    """
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enrollments")
    monitoria = models.ForeignKey(Monitoria, on_delete=models.CASCADE, blank=True, null=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, blank=True, null=True)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.monitoria:
            return f"{self.student.username} enrolled in {self.monitoria}"
        else:
            return f"{self.student.username} enrolled in {self.module}"


# views.py - Define views to handle the enrollment process and list available modules/monitorías.
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Module, Monitoria, Enrollment

@login_required
def list_modules(request):
    """
    View to list available modules for enrollment.
    """
    modules = Module.objects.all()
    return render(request, 'list_modules.html', {'modules': modules})


@login_required
def list_monitorias(request, module_id):
    """
    View to list available monitorías for a specific module.
    """
    module = get_object_or_404(Module, id=module_id)
    monitorias = module.monitorias.all()
    return render(request, 'list_monitorias.html', {'module': module, 'monitorias': monitorias})


@login_required
def enroll(request, monitoria_id=None, module_id=None):
    """
    View to handle student enrollment in a module or monitoria.
    """
    student = request.user
    if monitoria_id:
        monitoria = get_object_or_404(Monitoria, id=monitoria_id)
        # Ensure the monitoria isn't overbooked
        if Enrollment.objects.filter(monitoria=monitoria).count() >= monitoria.max_students:
            return JsonResponse({'error': 'Monitoria is full'}, status=400)
        Enrollment.objects.create(student=student, monitoria=monitoria)
        return JsonResponse({'message': f'Enrolled in monitoria: {monitoria}'})
    elif module_id:
        module = get_object_or_404(Module, id=module_id)
        Enrollment.objects.create(student=student, module=module)
        return JsonResponse({'message': f'Enrolled in module: {module}'})
    else:
        return JsonResponse({'error': 'Invalid parameters'}, status=400)


# urls.py - Define URL patterns for the above views.
from django.urls import path
from . import views

urlpatterns = [
    path('modules/', views.list_modules, name='list_modules'),
    path('modules/<int:module_id>/monitorias/', views.list_monitorias, name='list_monitorias'),
    path('enroll/', views.enroll, name='enroll'),
]


# templates/list_modules.html - Template for displaying available modules.
"""
{% extends "base.html" %}

{% block content %}
<h1>Available Modules</h1>
<ul>
    {% for module in modules %}
    <li>
        <a href="{% url 'list_monitorias' module.id %}">{{ module.title }}</a> - {{ module.description }}
    </li>
    {% endfor %}
</ul>
{% endblock %}
"""


# templates/list_monitorias.html - Template for displaying available monitorías for a module.
"""
{% extends "base.html" %}

{% block content %}
<h1>Monitorías for {{ module.title }}</h1>
<ul>
    {% for monitoria in monitorias %}
    <li>
        {{ monitoria }} - {{ monitoria.date }}
        <form method="post" action="{% url 'enroll' %}">
            {% csrf_token %}
            <input type="hidden" name="monitoria_id" value="{{ monitoria.id }}">
            <button type="submit">Enroll</button>
        </form>
    </li>
    {% endfor %}
</ul>
{% endblock %}
"""

# Notes:
# 1. Replace `base.html` with your own base template.
# 2. Proper authentication and permissions should be set up using Django's built-in authentication system.
# 3. To run the code, set up Django with a database (e.g., PostgreSQL) and apply migrations using `python manage.py makemigrations` and `python manage.py migrate`.
# 4. Test edge cases, such as users enrolling multiple times or overbooking monitorías.
