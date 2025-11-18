"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://colegiodepsicologosoruro.org
Prompt: Generate a Django-based web application for managing psychologist memberships, certifications, and ethical compliance, following the administrative processes outlined by the Colegio de Psicólogos de Oruro.
Generated: DETERMINISTIC_2a65006c19b07d6b
Batch ID: 20250612_154010
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
SECRET_KEY = 'your-secret-key-here'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'membership',
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

ROOT_URLCONF = 'psychologist_management.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'psychologist_management.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Use PostgreSQL in production
        'NAME': BASE_DIR / "db.sqlite3",
    }
}

# Password validation
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
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'


# models.py in membership app

from django.db import models

class Psychologist(models.Model):
    """Model to store psychologist's personal information."""
    name = models.CharField(max_length=255)
    license_number = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Certification(models.Model):
    """Model to store certifications of psychologists."""
    psychologist = models.ForeignKey(Psychologist, related_name='certifications', on_delete=models.CASCADE)
    certification_name = models.CharField(max_length=255)
    certification_date = models.DateField()
    expiry_date = models.DateField()

    def __str__(self):
        return f"{self.certification_name} - {self.psychologist.name}"

class EthicalCompliance(models.Model):
    """Model to store ethical compliance records."""
    psychologist = models.ForeignKey(Psychologist, related_name='ethical_compliances', on_delete=models.CASCADE)
    compliance_date = models.DateField()
    status = models.BooleanField(default=False)  # True if compliant, False otherwise

    def __str__(self):
        return f"Compliance for {self.psychologist.name} on {self.compliance_date}"


# admin.py in membership app

from django.contrib import admin
from .models import Psychologist, Certification, EthicalCompliance

@admin.register(Psychologist)
class PsychologistAdmin(admin.ModelAdmin):
    list_display = ('name', 'license_number', 'email', 'phone')

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('psychologist', 'certification_name', 'certification_date', 'expiry_date')

@admin.register(EthicalCompliance)
class EthicalComplianceAdmin(admin.ModelAdmin):
    list_display = ('psychologist', 'compliance_date', 'status')


# urls.py in membership app

from django.urls import path
from . import views

app_name = 'membership'

urlpatterns = [
    path('', views.PsychologistListView.as_view(), name='psychologist_list'),
    path('psychologist/<int:pk>/', views.PsychologistDetailView.as_view(), name='psychologist_detail'),
]


# views.py in membership app

from django.views.generic import ListView, DetailView
from .models import Psychologist

class PsychologistListView(ListView):
    """View to list all psychologists."""
    model = Psychologist
    template_name = 'membership/psychologist_list.html'
    context_object_name = 'psychologists'

class PsychologistDetailView(DetailView):
    """View to display details of a specific psychologist."""
    model = Psychologist
    template_name = 'membership/psychologist_detail.html'
    context_object_name = 'psychologist'


# wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'psychologist_management.settings')

application = get_wsgi_application()


# urls.py in psychologist_management project

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('membership/', include('membership.urls')),
]


# templates/membership/psychologist_list.html

{% extends 'base_generic.html' %}

{% block content %}
  <h2>Psychologists</h2>
  <ul>
    {% for psychologist in psychologists %}
      <li>
        <a href="{% url 'membership:psychologist_detail' psychologist.pk %}">{{ psychologist.name }}</a>
      </li>
    {% endfor %}
  </ul>
{% endblock %


# templates/membership/psychologist_detail.html

{% extends 'base_generic.html' %}

{% block content %}
  <h2>{{ psychologist.name }}</h2>
  <p>License Number: {{ psychologist.license_number }}</p>
  <p>Email: {{ psychologist.email }}</p>
  <p>Phone: {{ psychologist.phone }}</p>
  <h3>Certifications</h3>
  <ul>
    {% for certification in psychologist.certifications.all %}
      <li>{{ certification.certification_name }} - Expires on: {{ certification.expiry_date }}</li>
    {% endfor %}
  </ul>
  <h3>Ethical Compliance</h3>
  <ul>
    {% for compliance in psychologist.ethical_compliances.all %}
      <li>Status: {{ compliance.status }} on {{ compliance.compliance_date }}</li>
    {% endfor %}
  </ul>
{% endblock %


# Run migrations and create a superuser
# In terminal:
# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser
# python manage.py runserver
```
