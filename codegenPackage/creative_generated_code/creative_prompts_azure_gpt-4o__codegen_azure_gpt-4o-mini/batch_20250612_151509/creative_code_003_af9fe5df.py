"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://govssc.edu.bd
Prompt: Create a Django-based portal that allows students to log in, view their academic results, and download certificates (e.g., testimonials and study certificates) from the Govt. Shah Sultan College website.
Generated: DETERMINISTIC_af9fe5df77b7b1a2
Batch ID: 20250612_151509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# settings.py

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-default-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['yourdomain.com', 'localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'students',  # Custom app for student portal
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

ROOT_URLCONF = 'yourproject.urls'

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

WSGI_APPLICATION = 'yourproject.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.validators.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.validators.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.validators.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.validators.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),  # Include the student app URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# models.py (inside students app)

from django.db import models
from django.contrib.auth.models import User

class AcademicResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    grade = models.CharField(max_length=2)
    semester = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.subject}: {self.grade}"


class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    certificate_type = models.CharField(max_length=50)  # e.g., "Testimonial", "Study Certificate"
    document = models.FileField(upload_to='certificates/')

    def __str__(self):
        return f"{self.user.username} - {self.certificate_type}"


# forms.py (inside students app)

from django import forms
from .models import AcademicResult, Certificate

class AcademicResultForm(forms.ModelForm):
    class Meta:
        model = AcademicResult
        fields = ['subject', 'grade', 'semester']


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['certificate_type', 'document']


# views.py (inside students app)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import AcademicResult, Certificate
from .forms import AcademicResultForm, CertificateForm

@login_required
def dashboard(request):
    results = AcademicResult.objects.filter(user=request.user)
    certificates = Certificate.objects.filter(user=request.user)
    return render(request, 'students/dashboard.html', {'results': results, 'certificates': certificates})

@login_required
def upload_certificate(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            certificate = form.save(commit=False)
            certificate.user = request.user
            certificate.save()
            return redirect('dashboard')
    else:
        form = CertificateForm()
    return render(request, 'students/upload_certificate.html', {'form': form})


# urls.py (inside students app)

from django.urls import path
from .views import dashboard, upload_certificate

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('upload_certificate/', upload_certificate, name='upload_certificate'),
]


# templates/students/dashboard.html

{% extends 'base.html' %}

{% block content %}
<h1>Welcome, {{ user.username }}</h1>
<h2>Your Academic Results:</h2>
<ul>
    {% for result in results %}
        <li>{{ result.subject }}: {{ result.grade }} (Semester: {{ result.semester }})</li>
    {% endfor %}
</ul>

<h2>Your Certificates:</h2>
<ul>
    {% for certificate in certificates %}
        <li>{{ certificate.certificate_type }} - <a href="{{ certificate.document.url }}">Download</a></li>
    {% endfor %}
</ul>

<a href="{% url 'upload_certificate' %}">Upload a new Certificate</a>
{% endblock %}


# templates/students/upload_certificate.html

{% extends 'base.html' %}

{% block content %}
<h1>Upload Certificate</h1>
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Upload</button>
</form>
<a href="{% url 'dashboard' %}">Back to Dashboard</a>
{% endblock %}


# Admin configuration (inside admin.py of students app)

from django.contrib import admin
from .models import AcademicResult, Certificate

@admin.register(AcademicResult)
class AcademicResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'grade', 'semester')


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('user', 'certificate_type', 'document')


# Run migrations
# python manage.py makemigrations students
# python manage.py migrate

# Create superuser for admin access
# python manage.py createsuperuser

# Start the server
# python manage.py runserver
```
