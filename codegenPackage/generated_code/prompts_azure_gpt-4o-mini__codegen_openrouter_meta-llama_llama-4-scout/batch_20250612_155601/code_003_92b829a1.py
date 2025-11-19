"""
Generated Code Metadata:
========================
Original URL: https://shivvedika.com
Prompt: Develop a web application feature that allows users to volunteer for programs at Shiv Vedika Trust, including managing their availability and roles.
Generated: DETERMINISTIC_92b829a129ed659c
Batch ID: 20250612_155601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Volunteer Management System**
================================

### Models

```python
# models.py
from django.db import models
from django.contrib.auth.models import User

class Program(models.Model):
    """Program model"""
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Role(models.Model):
    """Role model"""
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Volunteer(models.Model):
    """Volunteer model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    availability = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class ProgramVolunteer(models.Model):
    """Program Volunteer model"""
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.volunteer.user.username} - {self.program.name}"
```

### Views

```python
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Program, Role, Volunteer, ProgramVolunteer
from .forms import VolunteerForm, ProgramVolunteerForm

@login_required
def volunteer_dashboard(request):
    """Volunteer dashboard view"""
    volunteer = Volunteer.objects.get(user=request.user)
    programs = ProgramVolunteer.objects.filter(volunteer=volunteer)
    return render(request, 'volunteer_dashboard.html', {'programs': programs})

@login_required
def manage_availability(request):
    """Manage availability view"""
    volunteer = Volunteer.objects.get(user=request.user)
    if request.method == 'POST':
        form = VolunteerForm(request.POST, instance=volunteer)
        if form.is_valid():
            form.save()
            return redirect('volunteer_dashboard')
    else:
        form = VolunteerForm(instance=volunteer)
    return render(request, 'manage_availability.html', {'form': form})

@login_required
def volunteer_for_program(request, program_id):
    """Volunteer for program view"""
    program = Program.objects.get(id=program_id)
    roles = Role.objects.all()
    if request.method == 'POST':
        form = ProgramVolunteerForm(request.POST)
        if form.is_valid():
            program_volunteer = form.save(commit=False)
            program_volunteer.program = program
            program_volunteer.volunteer = Volunteer.objects.get(user=request.user)
            program_volunteer.save()
            return redirect('volunteer_dashboard')
    else:
        form = ProgramVolunteerForm()
    return render(request, 'volunteer_for_program.html', {'form': form, 'roles': roles})

@login_required
def manage_roles(request, program_id):
    """Manage roles view"""
    program = Program.objects.get(id=program_id)
    program_volunteers = ProgramVolunteer.objects.filter(program=program)
    return render(request, 'manage_roles.html', {'program_volunteers': program_volunteers})
```

### Forms

```python
# forms.py
from django import forms
from .models import Volunteer, ProgramVolunteer

class VolunteerForm(forms.ModelForm):
    """Volunteer form"""
    class Meta:
        model = Volunteer
        fields = ('availability',)

class ProgramVolunteerForm(forms.ModelForm):
    """Program Volunteer form"""
    class Meta:
        model = ProgramVolunteer
        fields = ('role',)
```

### URLs

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.volunteer_dashboard, name='volunteer_dashboard'),
    path('manage_availability/', views.manage_availability, name='manage_availability'),
    path('volunteer_for_program/<int:program_id>/', views.volunteer_for_program, name='volunteer_for_program'),
    path('manage_roles/<int:program_id>/', views.manage_roles, name='manage_roles'),
]
```

### Templates

```html
<!-- volunteer_dashboard.html -->
<h1>Volunteer Dashboard</h1>
<ul>
    {% for program in programs %}
        <li>{{ program.program.name }} - {{ program.role.name }}</li>
    {% empty %}
        <li>No programs volunteered for.</li>
    {% endfor %}
</ul>

<!-- manage_availability.html -->
<h1>Manage Availability</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save</button>
</form>

<!-- volunteer_for_program.html -->
<h1>Volunteer for Program</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Volunteer</button>
</form>
<ul>
    {% for role in roles %}
        <li>{{ role.name }}</li>
    {% empty %}
        <li>No roles available.</li>
    {% endfor %}
</ul>

<!-- manage_roles.html -->
<h1>Manage Roles</h1>
<ul>
    {% for program_volunteer in program_volunteers %}
        <li>{{ program_volunteer.volunteer.user.username }} - {{ program_volunteer.role.name }}</li>
    {% empty %}
        <li>No roles assigned.</li>
    {% endfor %}
</ul>
```
