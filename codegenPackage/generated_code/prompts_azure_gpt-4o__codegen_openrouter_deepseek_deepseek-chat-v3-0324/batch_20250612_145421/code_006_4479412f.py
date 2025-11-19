"""
Generated Code Metadata:
========================
Original URL: https://www.icyd.org
Prompt: Develop a Django application to manage and report on youth development initiatives, inspired by the collaborative goals of ICYD.org.
Generated: DETERMINISTIC_4479412f453929c3
Batch ID: 20250612_145421
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# settings.py
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-default-key-for-dev-only')

DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'youth_programs.apps.YouthProgramsConfig',
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

ROOT_URLCONF = 'youth_development.urls'

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

WSGI_APPLICATION = 'youth_development.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'youth_dev'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
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
STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
```

```python
# youth_programs/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Program(models.Model):
    """Model representing a youth development program."""
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    target_age_min = models.PositiveIntegerField(
        validators=[MinValueValidator(5), MaxValueValidator(25)]
    )
    target_age_max = models.PositiveIntegerField(
        validators=[MinValueValidator(5), MaxValueValidator(25)]
    )
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    location = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']

class Participant(models.Model):
    """Model representing a participant in a youth program."""
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('U', 'Prefer not to say'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    guardian_name = models.CharField(max_length=200, null=True, blank=True)
    guardian_contact = models.CharField(max_length=200, null=True, blank=True)
    programs = models.ManyToManyField(Program, related_name='participants')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['last_name', 'first_name']

class Outcome(models.Model):
    """Model representing outcomes/achievements from programs."""
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='outcomes')
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='outcomes')
    achievement = models.TextField()
    date_recorded = models.DateField(auto_now_add=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.participant} - {self.achievement[:50]}..."

    class Meta:
        ordering = ['-date_recorded']
```

```python
# youth_programs/admin.py
from django.contrib import admin
from .models import Program, Participant, Outcome

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'is_active', 'location')
    list_filter = ('is_active', 'location')
    search_fields = ('name', 'description')
    date_hierarchy = 'start_date'

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'gender')
    list_filter = ('gender', 'programs')
    search_fields = ('first_name', 'last_name', 'email')
    filter_horizontal = ('programs',)

@admin.register(Outcome)
class OutcomeAdmin(admin.ModelAdmin):
    list_display = ('participant', 'program', 'achievement', 'date_recorded')
    list_filter = ('program', 'date_recorded')
    search_fields = ('participant__first_name', 'participant__last_name', 'achievement')
    raw_id_fields = ('participant', 'program')
```

```python
# youth_programs/serializers.py
from rest_framework import serializers
from .models import Program, Participant, Outcome

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class ParticipantSerializer(serializers.ModelSerializer):
    programs = serializers.PrimaryKeyRelatedField(
        many=True, 
        queryset=Program.objects.all(),
        required=False
    )

    class Meta:
        model = Participant
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class OutcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outcome
        fields = '__all__'
        read_only_fields = ('date_recorded',)

class ProgramDetailSerializer(ProgramSerializer):
    participants = ParticipantSerializer(many=True, read_only=True)
    outcomes = OutcomeSerializer(many=True, read_only=True)
```

```python
# youth_programs/views.py
from rest_framework import generics, permissions
from .models import Program, Participant, Outcome
from .serializers import (
    ProgramSerializer, 
    ParticipantSerializer, 
    OutcomeSerializer,
    ProgramDetailSerializer
)

class ProgramList(generics.ListCreateAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
