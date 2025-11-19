"""
Generated Code Metadata:
========================
Original URL: https://delsolmontessorihn.com
Prompt: Create a Django application for managing extracurricular programs like sports, entrepreneurship, and robotics, inspired by the diverse offerings at Del Sol Montessori.
Generated: DETERMINISTIC_ddb6504782019226
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**extracurricular_programs/models.py**
```python
from django.db import models

class Program(models.Model):
    """Represents an extracurricular program."""
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    """Represents an activity within a program."""
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.program.name} - {self.name}"

class Participant(models.Model):
    """Represents a participant in an activity."""
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.activity.program.name} - {self.activity.name}"

class Instructor(models.Model):
    """Represents an instructor for an activity."""
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.activity.program.name} - {self.activity.name}"
```

**extracurricular_programs/admin.py**
```python
from django.contrib import admin
from .models import Program, Activity, Participant, Instructor

admin.site.register(Program)
admin.site.register(Activity)
admin.site.register(Participant)
admin.site.register(Instructor)
```

**extracurricular_programs/views.py**
```python
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Program, Activity, Participant, Instructor
from .forms import ProgramForm, ActivityForm, ParticipantForm, InstructorForm

def program_list(request):
    programs = Program.objects.all()
    return render(request, 'extracurricular_programs/program_list.html', {'programs': programs})

def program_detail(request, pk):
    program = Program.objects.get(pk=pk)
    return render(request, 'extracurricular_programs/program_detail.html', {'program': program})

def activity_list(request, program_pk):
    activities = Activity.objects.filter(program__pk=program_pk)
    return render(request, 'extracurricular_programs/activity_list.html', {'activities': activities})

def activity_detail(request, program_pk, activity_pk):
    activity = Activity.objects.get(pk=activity_pk)
    return render(request, 'extracurricular_programs/activity_detail.html', {'activity': activity})

def create_program(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('program_list')
    else:
        form = ProgramForm()
    return render(request, 'extracurricular_programs/create_program.html', {'form': form})

def create_activity(request, program_pk):
    program = Program.objects.get(pk=program_pk)
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.program = program
            activity.save()
            return redirect('activity_list', program_pk=program_pk)
    else:
        form = ActivityForm()
    return render(request, 'extracurricular_programs/create_activity.html', {'form': form, 'program': program})

def create_participant(request, program_pk, activity_pk):
    activity = Activity.objects.get(pk=activity_pk)
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            participant = form.save(commit=False)
            participant.activity = activity
            participant.save()
            return redirect('activity_detail', program_pk=program_pk, activity_pk=activity_pk)
    else:
        form = ParticipantForm()
    return render(request, 'extracurricular_programs/create_participant.html', {'form': form, 'activity': activity})

def create_instructor(request, program_pk, activity_pk):
    activity = Activity.objects.get(pk=activity_pk)
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            instructor = form.save(commit=False)
            instructor.activity = activity
            instructor.save()
            return redirect('activity_detail', program_pk=program_pk, activity_pk=activity_pk)
    else:
        form = InstructorForm()
    return render(request, 'extracurricular_programs/create_instructor.html', {'form': form, 'activity': activity})
```

**extracurricular_programs/forms.py**
```python
from django import forms
from .models import Program, Activity, Participant, Instructor

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ('name', 'description')

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('name', 'description', 'start_time', 'end_time')

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ('name', 'email')

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ('name', 'email')
```

**extracurricular_programs/urls.py**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('programs/', views.program_list, name='program_list'),
    path('programs/<pk>/', views.program_detail, name='program_detail'),
    path('programs/<pk>/activities/', views.activity_list, name='activity_list'),
    path('programs/<pk>/activities/<activity_pk>/', views.activity_detail, name='activity_detail'),
    path('programs/create/', views.create_program, name='create_program'),
    path('programs/<pk>/activities/create/', views.create_activity, name='create_activity'),
    path('programs/<program_pk>/activities/<activity_pk>/participants/create/', views.create_participant, name='create_participant'),
    path('programs/<program_pk>/activities/<activity_pk>/instructors/create/', views.create_instructor, name='create_instructor'),
]
```

**extracurricular_programs/templates/extracurricular_programs/program_list.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Programs</h1>
  <ul>
    {% for program in programs %}
      <li>
        <a href="{% url 'program_detail' program.pk %}">{{ program.name }}</a>
      </li>
    {% empty %}
      <li>No programs available.</li>
    {% endfor %}
  </ul>
  <p><a href="{% url 'create_program' %}">Create a new program</a></p>
{% endblock %}
```

**extracurricular_programs/templates/extracurricular_programs/program_detail.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>{{ program.name }}</h1>
  <p>{{ program.description }}</p>
  <h2>Activities</h2>
  <ul>
    {% for activity in program.activity_set.all %}
      <li>
        <a href="{% url 'activity_detail' program.pk activity.pk %}">{{ activity.name }}</a>
      </li>
    {% empty %}
      <li>No activities available.</li>
    {% endfor %}
  </ul>
  <p><a href="{% url 'create_activity' program.pk %}">Create a new activity</a></p>
{% endblock %}
```

**extracurricular_programs/templates/extracurricular_programs/activity_list.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Activities for {{ program.name }}</h1>
  <ul>
    {% for activity in activities %}
      <li>
        <a href="{% url 'activity_detail' program.pk activity.pk %}">{{ activity.name }}</a>
      </li>
    {% empty %}
      <li>No activities available.</li>
    {% endfor %}
  </ul>
{% endblock %}
```

**extracurricular_programs/templates/extracurricular_programs/activity_detail.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>{{ activity.name }}</h1>
  <p>{{ activity.description }}</p>
  <h2>Participants</h2>
  <ul>
    {% for participant in activity.participant_set.all %}
      <li>{{ participant.name }} ({{ participant.email }})</li>
    {% empty %}
      <li>No participants available.</li>
    {% endfor %}
  </ul>
  <p><a href="{% url 'create_participant' activity.program.pk activity.pk %}">Add a participant</a></p>
  <h2>Instructors</h2>
  <ul>
    {% for instructor in activity.instructor_set.all %}
      <li>{{ instructor.name }} ({{ instructor.email }})</li>
    {% empty %}
