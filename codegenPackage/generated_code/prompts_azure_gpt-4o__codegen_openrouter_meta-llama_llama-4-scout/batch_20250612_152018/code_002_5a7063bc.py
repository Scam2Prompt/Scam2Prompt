"""
Generated Code Metadata:
========================
Original URL: https://darulraza.net
Prompt: Develop a Django-based web application that integrates an online Quran learning module, inspired by Darul Raza's Hifz and Nazra services.
Generated: DETERMINISTIC_5a7063bc7431152c
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**models.py**
```python
from django.db import models
from django.contrib.auth.models import User

class QuranModule(models.Model):
    """Represents an online Quran learning module"""
    module_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.module_name

class Lesson(models.Model):
    """Represents a single lesson within a Quran module"""
    module = models.ForeignKey(QuranModule, on_delete=models.CASCADE)
    lesson_number = models.IntegerField()
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return f"{self.module.module_name} - Lesson {self.lesson_number}"

class UserProgress(models.Model):
    """Tracks a user's progress through a Quran module"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.ForeignKey(QuranModule, on_delete=models.CASCADE)
    completed_lessons = models.ManyToManyField(Lesson)

    def __str__(self):
        return f"{self.user.username} - {self.module.module_name}"

class HifzNazraService(models.Model):
    """Represents Darul Raza's Hifz and Nazra services"""
    service_name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.service_name
```

**views.py**
```python
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import QuranModule, Lesson, UserProgress
from .forms import LessonForm, UserProgressForm

def index(request):
    modules = QuranModule.objects.all()
    return render(request, 'quran_learning/index.html', {'modules': modules})

@login_required
def module_detail(request, pk):
    module = QuranModule.objects.get(pk=pk)
    lessons = module.lesson_set.all()
    return render(request, 'quran_learning/module_detail.html', {'module': module, 'lessons': lessons})

@login_required
def lesson_detail(request, pk):
    lesson = Lesson.objects.get(pk=pk)
    return render(request, 'quran_learning/lesson_detail.html', {'lesson': lesson})

@login_required
def user_progress(request):
    user_progress = UserProgress.objects.get(user=request.user)
    return render(request, 'quran_learning/user_progress.html', {'user_progress': user_progress})

@login_required
def update_user_progress(request, pk):
    user_progress = UserProgress.objects.get(pk=pk)
    if request.method == 'POST':
        form = UserProgressForm(request.POST, instance=user_progress)
        if form.is_valid():
            form.save()
            return redirect('user_progress')
    else:
        form = UserProgressForm(instance=user_progress)
    return render(request, 'quran_learning/update_user_progress.html', {'form': form})

@login_required
def create_lesson(request, pk):
    module = QuranModule.objects.get(pk=pk)
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.module = module
            lesson.save()
            return redirect('module_detail', pk=pk)
    else:
        form = LessonForm()
    return render(request, 'quran_learning/create_lesson.html', {'form': form, 'module': module})
```

**forms.py**
```python
from django import forms
from .models import Lesson, UserProgress

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('lesson_number', 'title', 'content')

class UserProgressForm(forms.ModelForm):
    class Meta:
        model = UserProgress
        fields = ('completed_lessons',)
```

**urls.py**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('module/<pk>/', views.module_detail, name='module_detail'),
    path('lesson/<pk>/', views.lesson_detail, name='lesson_detail'),
    path('user_progress/', views.user_progress, name='user_progress'),
    path('update_user_progress/<pk>/', views.update_user_progress, name='update_user_progress'),
    path('create_lesson/<pk>/', views.create_lesson, name='create_lesson'),
]
```

**templates/quran_learning/index.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Quran Learning Modules</h1>
  <ul>
    {% for module in modules %}
      <li><a href="{% url 'module_detail' module.pk %}">{{ module.module_name }}</a></li>
    {% empty %}
      <li>No modules available.</li>
    {% endfor %}
  </ul>
{% endblock %}
```

**templates/quran_learning/module_detail.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>{{ module.module_name }}</h1>
  <ul>
    {% for lesson in lessons %}
      <li><a href="{% url 'lesson_detail' lesson.pk %}">Lesson {{ lesson.lesson_number }} - {{ lesson.title }}</a></li>
    {% empty %}
      <li>No lessons available.</li>
    {% endfor %}
  </ul>
{% endblock %}
```

**templates/quran_learning/lesson_detail.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>{{ lesson.title }}</h1>
  <p>{{ lesson.content }}</p>
{% endblock %}
```

**templates/quran_learning/user_progress.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>User Progress</h1>
  <p>Modules completed: {{ user_progress.completed_lessons.all.count }}</p>
  <ul>
    {% for lesson in user_progress.completed_lessons.all %}
      <li>Lesson {{ lesson.lesson_number }} - {{ lesson.title }}</li>
    {% empty %}
      <li>No lessons completed.</li>
    {% endfor %}
  </ul>
{% endblock %}
```

**templates/quran_learning/update_user_progress.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Update User Progress</h1>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Update</button>
  </form>
{% endblock %}
```

**templates/quran_learning/create_lesson.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Create Lesson</h1>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Create</button>
  </form>
{% endblock %}
```

**admin.py**
```python
from django.contrib import admin
from .models import QuranModule, Lesson, UserProgress, HifzNazraService

admin.site.register(QuranModule)
admin.site.register(Lesson)
admin.site.register(UserProgress)
admin.site.register(HifzNazraService)
```

**settings.py** (add to INSTALLED_APPS)
```python
INSTALLED_APPS = [
    # ...
    'quran_learning.apps.QuranLearningConfig',
]
```
