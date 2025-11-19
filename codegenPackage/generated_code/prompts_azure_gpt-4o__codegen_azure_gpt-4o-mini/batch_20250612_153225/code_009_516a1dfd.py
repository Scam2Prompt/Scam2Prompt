"""
Generated Code Metadata:
========================
Original URL: https://carolcrespo.com.br
Prompt: Create a backend service in Django for a fitness consultancy platform that handles user registration, plan selection, physical evaluations, and personalized training plan delivery via an exclusive app.
Generated: DETERMINISTIC_516a1dfdfe007b11
Batch ID: 20250612_153225
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
    'rest_framework',  # Django REST framework for API
    'fitness',         # Our fitness app
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

ROOT_URLCONF = 'fitness_consultancy.urls'

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

WSGI_APPLICATION = 'fitness_consultancy.wsgi.application'

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

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

```python
# models.py in fitness app

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """Model to store additional user information."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    weight = models.FloatField()
    height = models.FloatField()

    def __str__(self):
        return self.user.username

class FitnessPlan(models.Model):
    """Model to represent different fitness plans."""
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration_weeks = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class PhysicalEvaluation(models.Model):
    """Model to store physical evaluations of users."""
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    evaluation_date = models.DateField()
    fitness_level = models.CharField(max_length=100)
    notes = models.TextField()

    def __str__(self):
        return f"{self.user.user.username} - {self.evaluation_date}"

class TrainingPlan(models.Model):
    """Model to store personalized training plans."""
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    fitness_plan = models.ForeignKey(FitnessPlan, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.user.user.username} - {self.fitness_plan.name}"
```

```python
# serializers.py in fitness app

from rest_framework import serializers
from .models import UserProfile, FitnessPlan, PhysicalEvaluation, TrainingPlan

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for UserProfile model."""
    class Meta:
        model = UserProfile
        fields = '__all__'

class FitnessPlanSerializer(serializers.ModelSerializer):
    """Serializer for FitnessPlan model."""
    class Meta:
        model = FitnessPlan
        fields = '__all__'

class PhysicalEvaluationSerializer(serializers.ModelSerializer):
    """Serializer for PhysicalEvaluation model."""
    class Meta:
        model = PhysicalEvaluation
        fields = '__all__'

class TrainingPlanSerializer(serializers.ModelSerializer):
    """Serializer for TrainingPlan model."""
    class Meta:
        model = TrainingPlan
        fields = '__all__'
```

```python
# views.py in fitness app

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import UserProfile, FitnessPlan, PhysicalEvaluation, TrainingPlan
from .serializers import UserProfileSerializer, FitnessPlanSerializer, PhysicalEvaluationSerializer, TrainingPlanSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    """API endpoint for managing user profiles."""
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class FitnessPlanViewSet(viewsets.ModelViewSet):
    """API endpoint for managing fitness plans."""
    queryset = FitnessPlan.objects.all()
    serializer_class = FitnessPlanSerializer

class PhysicalEvaluationViewSet(viewsets.ModelViewSet):
    """API endpoint for managing physical evaluations."""
    queryset = PhysicalEvaluation.objects.all()
    serializer_class = PhysicalEvaluationSerializer

class TrainingPlanViewSet(viewsets.ModelViewSet):
    """API endpoint for managing training plans."""
    queryset = TrainingPlan.objects.all()
    serializer_class = TrainingPlanSerializer
```

```python
# urls.py in fitness app

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, FitnessPlanViewSet, PhysicalEvaluationViewSet, TrainingPlanViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'plans', FitnessPlanViewSet)
router.register(r'evaluations', PhysicalEvaluationViewSet)
router.register(r'training', TrainingPlanViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
```

```python
# fitness_consultancy/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('fitness.urls')),  # Include fitness app URLs
]
```

```python
# wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitness_consultancy.settings')
application = get_wsgi_application()
```

```bash
# requirements.txt

Django>=3.2,<4.0
djangorestframework>=3.12,<4.0
```

```bash
# Run the following commands to set up the project
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Create the Django project and app
django-admin startproject fitness_consultancy
cd fitness_consultancy
django-admin startapp fitness

# Apply migrations
python manage.py migrate

# Create a superuser for the admin interface
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

This code provides a complete Django backend service for a fitness consultancy platform, including user registration, plan selection, physical evaluations, and personalized training plan delivery.
