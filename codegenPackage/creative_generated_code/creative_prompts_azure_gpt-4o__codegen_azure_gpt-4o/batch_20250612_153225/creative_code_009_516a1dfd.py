"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carolcrespo.com.br
Prompt: Create a backend service in Django for a fitness consultancy platform that handles user registration, plan selection, physical evaluations, and personalized training plan delivery via an exclusive app.
Generated: DETERMINISTIC_516a1dfdfe007b11
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# fitness_service_project/settings.py

"""
Django Settings for Fitness Service Project.
This file contains settings for setting up the backend service.
"""
import os
from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key for development (ensure to replace with a secure key in production)
SECRET_KEY = 'YOUR_SECRET_KEY'

# Debug mode (set to False in production)
DEBUG = True

# Allowed hosts (set appropriately for production)
ALLOWED_HOSTS = []

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fitness_app',
    'rest_framework',
]

# Middleware settings
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL configuration
ROOT_URLCONF = 'fitness_service_project.urls'

# Template settings
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

# WSGI application
WSGI_APPLICATION = 'fitness_service_project.wsgi.application'

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validators
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

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files settings
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

```python
# fitness_service_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('fitness_app.urls')),  # API endpoints for fitness app
]
```

```python
# fitness_app/models.py

from django.db import models
from django.contrib.auth.models import User

class FitnessPlan(models.Model):
    """
    Model representing a fitness plan.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class PhysicalEvaluation(models.Model):
    """
    Model representing a user's physical evaluation.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='evaluation')
    height = models.DecimalField(max_digits=5, decimal_places=2)  # In meters
    weight = models.DecimalField(max_digits=5, decimal_places=2)  # In kilograms
    body_fat_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    muscle_mass = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'Evaluation for {self.user.username}'

class TrainingPlan(models.Model):
    """
    Model representing a personalized training plan for a user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='training_plan')
    plan_details = models.TextField()

    def __str__(self):
        return f'Training Plan for {self.user.username}'
```

```python
# fitness_app/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import FitnessPlan, PhysicalEvaluation, TrainingPlan

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User registration.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class FitnessPlanSerializer(serializers.ModelSerializer):
    """
    Serializer for FitnessPlan model.
    """
    class Meta:
        model = FitnessPlan
        fields = '__all__'

class PhysicalEvaluationSerializer(serializers.ModelSerializer):
    """
    Serializer for PhysicalEvaluation model.
    """
    class Meta:
        model = PhysicalEvaluation
        fields = '__all__'

class TrainingPlanSerializer(serializers.ModelSerializer):
    """
    Serializer for TrainingPlan model.
    """
    class Meta:
        model = TrainingPlan
        fields = '__all__'
```

```python
# fitness_app/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import FitnessPlan, PhysicalEvaluation, TrainingPlan
from .serializers import UserSerializer, FitnessPlanSerializer, PhysicalEvaluationSerializer, TrainingPlanSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for User registration and management.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FitnessPlanViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Fitness plans.
    """
    queryset = FitnessPlan.objects.all()
    serializer_class = FitnessPlanSerializer

class PhysicalEvaluationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for physical evaluations.
    """
    queryset = PhysicalEvaluation.objects.all()
    serializer_class = PhysicalEvaluationSerializer

class TrainingPlanViewSet(viewsets.ModelViewSet):
    """
    ViewSet for personalized training plans.
    """
    queryset = TrainingPlan.objects.all()
    serializer_class = TrainingPlanSerializer
```

```python
# fitness_app/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, FitnessPlanViewSet, PhysicalEvaluationViewSet, TrainingPlanViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('fitness-plans', FitnessPlanViewSet)
router.register('physical-evaluations', PhysicalEvaluationViewSet)
router.register('training-plans', TrainingPlanViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

```python
# fitness_service_project/wsgi.py

"""
WSGI config for fitness_service_project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitness_service_project.settings')

application = get_wsgi_application()
```

```python
# fitness_service_project/asgi.py

"""
ASGI config for fitness_service_project.

It exposes the ASGI callable as a module-level variable named ``application``.
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitness_service_project.settings')

application = get_asgi_application()
```

```python
# Run the following commands to initialize the Django project and include the app:
# django-admin startproject fitness_service_project
# cd fitness_service_project
# python manage.py startapp fitness_app
# python manage.py migrate
# python manage.py createsuperuser
# python manage.py runserver
```
