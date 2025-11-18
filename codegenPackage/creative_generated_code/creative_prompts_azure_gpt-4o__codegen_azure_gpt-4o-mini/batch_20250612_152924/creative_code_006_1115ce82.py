"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safargenie.com
Prompt: Develop a Django application to manage tour package bookings, incorporating features like "Safar Genie’s" customized plans and flexible payment patterns.
Generated: DETERMINISTIC_1115ce823be6ab8b
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# settings.py

# Django settings for tour_management project.

import os
from pathlib import Path

# Base directory path
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-secret-key')
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
    'tour_booking',  # Our custom app
    'rest_framework',  # For API
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

ROOT_URLCONF = 'tour_management.urls'

# Templates configuration
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

WSGI_APPLICATION = 'tour_management.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # For simplicity, using SQLite
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

# Static files configuration
STATIC_URL = '/static/'

# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# models.py in the tour_booking app

from django.db import models

class TourPackage(models.Model):
    """Model representing a tour package."""
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in days")
    start_date = models.DateField()
    
    def __str__(self):
        return self.name


class Booking(models.Model):
    """Model representing a booking for a tour package."""
    tour_package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200)
    email = models.EmailField()
    booking_date = models.DateField(auto_now_add=True)
    payment_status = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.customer_name} - {self.tour_package.name}"


# views.py in the tour_booking app

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import TourPackage, Booking
from .serializers import TourPackageSerializer, BookingSerializer

class TourPackageViewSet(viewsets.ModelViewSet):
    """Viewset for managing tour packages."""
    queryset = TourPackage.objects.all()
    serializer_class = TourPackageSerializer

class BookingViewSet(viewsets.ModelViewSet):
    """Viewset for managing bookings."""
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        """Handle booking creation with error handling."""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# serializers.py in the tour_booking app

from rest_framework import serializers
from .models import TourPackage, Booking

class TourPackageSerializer(serializers.ModelSerializer):
    """Serializer for TourPackage model."""
    class Meta:
        model = TourPackage
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    """Serializer for Booking model."""
    class Meta:
        model = Booking
        fields = '__all__'


# urls.py in the tour_booking app

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TourPackageViewSet, BookingViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'tour-packages', TourPackageViewSet)
router.register(r'bookings', BookingViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]


# urls.py in the project folder

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tour_booking.urls')),  # Include our app's URLs
]


# Run migrations and create superuser
# In the terminal:
# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser

# Run the server
# python manage.py runserver
```
