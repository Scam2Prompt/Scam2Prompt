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
# settings.py

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-default-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['your-domain.com', 'localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Django REST Framework
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

ROOT_URLCONF = 'fitness_platform.urls'

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

WSGI_APPLICATION = 'fitness_platform.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Use PostgreSQL in production
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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

# fitness/models.py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fitness_level = models.CharField(max_length=100)
    goals = models.TextField()

class TrainingPlan(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration_weeks = models.IntegerField()

class PhysicalEvaluation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    body_fat_percentage = models.FloatField()
    date_evaluated = models.DateTimeField(auto_now_add=True)

# fitness/serializers.py

from rest_framework import serializers
from .models import UserProfile, TrainingPlan, PhysicalEvaluation
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class TrainingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingPlan
        fields = '__all__'

class PhysicalEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalEvaluation
        fields = '__all__'

# fitness/views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile, TrainingPlan, PhysicalEvaluation
from .serializers import UserSerializer, UserProfileSerializer, TrainingPlanSerializer, PhysicalEvaluationSerializer

class UserRegistration(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

class TrainingPlanList(generics.ListCreateAPIView):
    queryset = TrainingPlan.objects.all()
    serializer_class = TrainingPlanSerializer

class PhysicalEvaluationCreate(generics.CreateAPIView):
    queryset = PhysicalEvaluation.objects.all()
    serializer_class = PhysicalEvaluationSerializer
    permission_classes = [IsAuthenticated]

# fitness/urls.py

from django.urls import path
from .views import UserRegistration, UserProfileDetail, TrainingPlanList, PhysicalEvaluationCreate

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='user-register'),
    path('profile/', UserProfileDetail.as_view(), name='user-profile'),
    path('training-plans/', TrainingPlanList.as_view(), name='training-plans'),
    path('evaluations/', PhysicalEvaluationCreate.as_view(), name='physical-evaluation'),
]

# fitness_platform/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('fitness.urls')),
]

# Run the following command to create migration files and migrate the database
# python manage.py makemigrations
# python manage.py migrate
```
Make sure to set up your Django environment, including creating a virtual environment, installing required packages using `pip install django djangorestframework`, and configuring your database settings appropriately for production.
