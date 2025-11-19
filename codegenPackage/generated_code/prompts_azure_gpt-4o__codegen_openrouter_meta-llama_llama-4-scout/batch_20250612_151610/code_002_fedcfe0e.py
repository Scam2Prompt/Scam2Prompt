"""
Generated Code Metadata:
========================
Original URL: https://cbupdates.com
Prompt: Generate code for a web-based application that assists franchise businesses in recruitment and onboarding, with functionality inspired by Franchise Teacher's franchise recruitment strategies.
Generated: DETERMINISTIC_fedcfe0eb58ef18e
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Franchise Recruitment and Onboarding Application**
=====================================================

**Models**
--------

### `models.py`
```python
from django.db import models
from django.contrib.auth.models import User

class Franchise(models.Model):
    """Franchise business model"""
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class JobPosting(models.Model):
    """Job posting model"""
    franchise = models.ForeignKey(Franchise, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Applicant(models.Model):
    """Applicant model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    franchise = models.ForeignKey(Franchise, on_delete=models.CASCADE)
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class OnboardingTask(models.Model):
    """Onboarding task model"""
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=255)
    task_description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name
```

**Views**
--------

### `views.py`
```python
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Franchise, JobPosting, Applicant, OnboardingTask
from .forms import JobPostingForm, ApplicantForm, OnboardingTaskForm

def index(request):
    franchises = Franchise.objects.all()
    return render(request, 'index.html', {'franchises': franchises})

@login_required
def job_postings(request, franchise_id):
    job_postings = JobPosting.objects.filter(franchise_id=franchise_id)
    return render(request, 'job_postings.html', {'job_postings': job_postings})

@login_required
def apply_for_job(request, job_posting_id):
    job_posting = JobPosting.objects.get(id=job_posting_id)
    if request.method == 'POST':
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.job_posting = job_posting
            applicant.user = request.user
            applicant.save()
            return redirect('onboarding')
    else:
        form = ApplicantForm()
    return render(request, 'apply_for_job.html', {'form': form})

@login_required
def onboarding(request):
    applicant = Applicant.objects.get(user=request.user)
    onboarding_tasks = OnboardingTask.objects.filter(applicant=applicant)
    return render(request, 'onboarding.html', {'onboarding_tasks': onboarding_tasks})

@login_required
def complete_task(request, task_id):
    task = OnboardingTask.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('onboarding')

@login_required
def create_job_posting(request, franchise_id):
    franchise = Franchise.objects.get(id=franchise_id)
    if request.method == 'POST':
        form = JobPostingForm(request.POST)
        if form.is_valid():
            job_posting = form.save(commit=False)
            job_posting.franchise = franchise
            job_posting.save()
            return redirect('job_postings', franchise_id=franchise_id)
    else:
        form = JobPostingForm()
    return render(request, 'create_job_posting.html', {'form': form})

@login_required
def create_onboarding_task(request, applicant_id):
    applicant = Applicant.objects.get(id=applicant_id)
    if request.method == 'POST':
        form = OnboardingTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.applicant = applicant
            task.save()
            return redirect('onboarding')
    else:
        form = OnboardingTaskForm()
    return render(request, 'create_onboarding_task.html', {'form': form})
```

**Forms**
--------

### `forms.py`
```python
from django import forms
from .models import JobPosting, Applicant, OnboardingTask

class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = ('title', 'description')

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ('resume',)

class OnboardingTaskForm(forms.ModelForm):
    class Meta:
        model = OnboardingTask
        fields = ('task_name', 'task_description')
```

**Templates**
------------

### `index.html`
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Franchise Recruitment and Onboarding</h1>
  <ul>
    {% for franchise in franchises %}
      <li>{{ franchise.name }} ({{ franchise.description }})</li>
    {% empty %}
      <li>No franchises available.</li>
    {% endfor %}
  </ul>
{% endblock %}
```

### `job_postings.html`
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Job Postings for {{ franchise.name }}</h1>
  <ul>
    {% for job_posting in job_postings %}
      <li>{{ job_posting.title }} ({{ job_posting.description }})</li>
    {% empty %}
      <li>No job postings available.</li>
    {% endfor %}
  </ul>
{% endblock %}
```

### `apply_for_job.html`
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Apply for {{ job_posting.title }}</h1>
  <form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Apply</button>
  </form>
{% endblock %}
```

### `onboarding.html`
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Onboarding Tasks</h1>
  <ul>
    {% for task in onboarding_tasks %}
      <li>{{ task.task_name }} ({{ task.task_description }}) {% if task.completed %} (Completed) {% endif %}</li>
    {% empty %}
      <li>No onboarding tasks available.</li>
    {% endfor %}
  </ul>
{% endblock %}
```

### `create_job_posting.html`
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Create Job Posting for {{ franchise.name }}</h1>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Create</button>
  </form>
{% endblock %}
```

### `create_onboarding_task.html`
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Create Onboarding Task for {{ applicant.user.username }}</h1>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Create</button>
  </form>
{% endblock %}
```

**URLs**
------

### `urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('job_postings/<int:franchise_id>/', views.job_postings, name='job_postings'),
    path('apply_for_job/<int:job_posting_id>/', views.apply_for_job, name='apply_for_job'),
    path('onboarding/', views.onboarding, name='onboarding'),
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),
    path('create_job_posting/<int:franchise_id>/', views.create_job_posting, name='create_job_posting'),
    path('create_onboarding_task/<int:applicant_id>/', views.create_onboarding_task, name='create_onboarding_task'),
]
```

**Settings**
------------

### `settings.py`
```python
INSTALLED_APPS = [
    # ...
    'franchise_recruitment',
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

**Run Migrations and Server**
---------------------------

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
