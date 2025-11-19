"""
Generated Code Metadata:
========================
Original URL: https://www.getaconsulenze.it
Prompt: "Suggest a tech stack for building a web application that offers educational services, including course management, user authentication, and payment processing, tailored to the needs of a consultancy firm like Geta Consulenze."
Generated: DETERMINISTIC_689de75e4a8b2415
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script outlines a suggested tech stack for building a web application
# offering educational services, including course management, user authentication,
# and payment processing. The stack is tailored for a consultancy firm like Geta Consulenze.

# Tech Stack:
# Backend: Python (Django Framework)
# Frontend: React.js
# Database: PostgreSQL
# Authentication: Django Allauth
# Payment Processing: Stripe
# Deployment: Docker + AWS (Elastic Beanstalk or EC2)

# Below is a sample implementation of the backend using Django.

# Install dependencies:
# pip install django djangorestframework django-allauth stripe psycopg2-binary

# settings.py (Django Configuration)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-secret-key')

DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['yourdomain.com', 'localhost']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # For building APIs
    'allauth',  # For user authentication
    'allauth.account',
    'allauth.socialaccount',
    'courses',  # Custom app for course management
    'payments',  # Custom app for payment processing
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.auth.AuthenticationMiddleware',
    'django.middleware.sessions.SessionMiddleware',
    'django.middleware.messages.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'educational_platform.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'educational_db'),
        'USER': os.getenv('DB_USER', 'educational_user'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'securepassword'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

STATIC_URL = '/static/'

# Stripe Configuration
STRIPE_API_KEY = os.getenv('STRIPE_API_KEY', 'your-stripe-api-key')

# urls.py (URL Routing)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('allauth.urls')),  # Authentication endpoints
    path('api/courses/', include('courses.urls')),  # Course management endpoints
    path('api/payments/', include('payments.urls')),  # Payment processing endpoints
]

# models.py (Example Course Model in courses app)
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# views.py (Example API View in courses app)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course

class CourseListView(APIView):
    """
    API endpoint to list all courses.
    """
    def get(self, request):
        courses = Course.objects.all()
        data = [{"id": course.id, "title": course.title, "price": course.price} for course in courses]
        return Response(data, status=status.HTTP_200_OK)

# payments/views.py (Example Payment Processing View)
import stripe
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

stripe.api_key = settings.STRIPE_API_KEY

class PaymentView(APIView):
    """
    API endpoint to process payments using Stripe.
    """
    def post(self, request):
        try:
            # Extract payment details from request
            amount = request.data.get('amount')
            currency = request.data.get('currency', 'usd')
            source = request.data.get('source')  # Stripe token

            # Create a charge
            charge = stripe.Charge.create(
                amount=int(amount * 100),  # Stripe expects amount in cents
                currency=currency,
                source=source,
                description="Course Payment"
            )
            return Response({"status": "success", "charge_id": charge.id}, status=status.HTTP_200_OK)
        except stripe.error.StripeError as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Dockerfile (For containerization)
"""
# Use official Python image as base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
"""

# This is a basic implementation of the backend. The frontend can be built using React.js
# with libraries like Axios for API calls and Material-UI for UI components.
```
