"""
Generated Code Metadata:
========================
Original URL: https://carreiras.oportunidadesevagas.com
Prompt: Create a Django web application that integrates job search functionality based on the "Busca de Empregos" section of the website.
Generated: DETERMINISTIC_29f8c1a921daad0f
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# settings.py
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-your-secret-key-here'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jobs.apps.JobsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'jobportal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'jobportal.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

```python
# jobs/models.py
from django.db import models
from django.core.validators import MinLengthValidator

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    salary = models.CharField(max_length=100, blank=True, null=True)
    job_type = models.CharField(max_length=50, choices=[
        ('full-time', 'Full Time'),
        ('part-time', 'Part Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
        ('temporary', 'Temporary'),
    ])
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} at {self.company}"

class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=200)
    applicant_email = models.EmailField()
    applicant_phone = models.CharField(max_length=20, validators=[MinLengthValidator(10)])
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(blank=True)
    applied_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application for {self.job.title} by {self.applicant_name}"
```

```python
# jobs/forms.py
from django import forms
from .models import JobApplication

class JobSearchForm(forms.Form):
    query = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Job title, keywords...'})
    )
    location = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'City, state or zip code...'})
    )
    job_type = forms.ChoiceField(
        required=False,
        choices=[
            ('', 'All Job Types'),
            ('full-time', 'Full Time'),
            ('part-time', 'Part Time'),
            ('contract', 'Contract'),
            ('internship', 'Internship'),
            ('temporary', 'Temporary'),
        ]
    )

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['applicant_name', 'applicant_email', 'applicant_phone', 'resume', 'cover_letter']
        widgets = {
            'cover_letter': forms.Textarea(attrs={'rows': 5}),
        }
```

```python
# jobs/views.py
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Job, JobApplication
from .forms import JobSearchForm, JobApplicationForm

def job_list(request):
    form = JobSearchForm(request.GET or None)
    jobs = Job.objects.filter(is_active=True).order_by('-posted_date')

    if form.is_valid():
        query = form.cleaned_data.get('query')
        location = form.cleaned_data.get('location')
        job_type = form.cleaned_data.get('job_type')

        if query:
            jobs = jobs.filter(title__icontains=query)
        if location:
            jobs = jobs.filter(location__icontains=location)
        if job_type:
            jobs = jobs.filter(job_type=job_type)

    paginator = Paginator(jobs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'form': form,
        'page_obj': page_obj,
    }
    return render(request, 'jobs/job_list.html', context)

def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id, is_active=True)
    
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            return render(request, 'jobs/application_success.html', {'job': job})
    else:
        form = JobApplicationForm()

    context = {
        'job': job,
        'form': form,
    }
    return render(request, 'jobs/job_detail.html', context)
```

```python
# jobs/urls.py
from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('<int:job_id>/', views.job_detail, name='job_detail'),
]
```

```python
# jobportal/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobs.urls')),
]
```

```html
<!-- templates/jobs/job_list.html -->
{% extends 'base.html' %}

{% block content %}
<h1>Job Search</h1>
<form method="get">
    {{ form.as_p }}
    <button type="submit">Search</button>
</form>

{% if page_obj %}
    <h2>Available Jobs</h2>
    <ul>
        {% for job in page_obj %}
            <li>
                <a href="{% url 'jobs:job_detail' job.id %}">{{ job.title }}</a> - 
                {{ job.company }} ({{ job.location }})
                <small>{{ job.posted_date|date:"M d, Y" }}</small>
            </li>
        {% endfor %}
    </ul>

    <div class="pagination">
        {% if page_obj.has_previous %}
            <a href="?page=1">&laquo; first</a>
            <a href="?page={{ page_obj.previous_page_number }}">previous</a>
        {% endif %}

        <span>Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}</span>

        {% if page_obj.has_next %}
            <a href="?page={{ page_obj.next_page_number }}">next</a>
            <a href="?page={{ page_obj.paginator.num_pages }}">last &raquo;</a>
        {% endif %}
    </div>
{% else %}
    <p>No jobs found matching your criteria.</p>
{% endif %}
{% endblock %}
```

```html
<!-- templates/jobs/job_detail.html -->
{% extends 'base.html' %}

{% block content %}
<h1>{{ job.title }}</h1>
<p><strong>Company:</strong> {{ job.company }}</p>
<p><strong>Location:</
