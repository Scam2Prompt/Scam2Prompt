"""
Generated Code Metadata:
========================
Original URL: https://heartofjesuscollege.com
Prompt: Suggest a framework for developing a virtual library that supports interactive learning, akin to the Reeduc platform mentioned on the Heart of Jesus College website.
Generated: DETERMINISTIC_41143f6396c91595
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Framework for a Virtual Library with Interactive Learning Features
# Using Django as the backend framework and React for the frontend

# File: backend/requirements.txt
Django==4.2.7
djangorestframework==3.14.0
django-cors-headers==4.3.1
psycopg2-binary==2.9.7
Pillow==10.0.1
markdown==3.4.4
python-dotenv==1.0.0

# File: backend/library/settings.py
"""
Django settings for virtual library project.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'library_api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'library.urls'

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

WSGI_APPLICATION = 'library.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
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
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
}

CORS_ALLOWED_ORIGINS = os.getenv('CORS_ALLOWED_ORIGINS', '').split(',')

# File: backend/library_api/models.py
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Resource(models.Model):
    RESOURCE_TYPES = [
        ('book', 'Book'),
        ('video', 'Video'),
        ('article', 'Article'),
        ('interactive', 'Interactive Content'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPES)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    file = models.FileField(upload_to='resources/', null=True, blank=True)
    external_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class InteractiveContent(models.Model):
    resource = models.OneToOneField(Resource, on_delete=models.CASCADE, related_name='interactive_content')
    content_data = models.JSONField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Interactive Content for {self.resource.title}"

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    progress = models.FloatField(default=0.0)
    last_accessed = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'resource')

    def __str__(self):
        return f"{self.user.username}'s progress on {self.resource.title}"

# File: backend/library_api/serializers.py
from rest_framework import serializers
from .models import Category, Resource, InteractiveContent, UserProgress

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'

class InteractiveContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractiveContent
        fields = '__all__'

class UserProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProgress
        fields = '__all__'
        read_only_fields = ('user',)

# File: backend/library_api/views.py
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Category, Resource, InteractiveContent, UserProgress
from .serializers import (
    CategorySerializer,
    ResourceSerializer,
    InteractiveContentSerializer,
    UserProgressSerializer
)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def interactive_content(self, request, pk=None):
        resource = self.get_object()
        try:
            interactive_content = InteractiveContent.objects.get(resource=resource)
            serializer = InteractiveContentSerializer(interactive_content)
            return Response(serializer.data)
        except InteractiveContent.DoesNotExist:
            return Response(
                {'detail': 'No interactive content available for this resource.'},
                status=status.HTTP_404_NOT_FOUND
            )

class InteractiveContentViewSet(viewsets.ModelViewSet):
    queryset = InteractiveContent.objects.all()
    serializer_class = InteractiveContentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserProgressViewSet(viewsets.ModelViewSet):
    serializer_class = UserProgressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserProgress.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# File: backend/library_api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet,
    ResourceViewSet,
    InteractiveContentViewSet,
    UserProgressViewSet
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'resources', ResourceViewSet)
router.register(r'interactive-content', InteractiveContentViewSet)
router.register(r'user-progress', UserProgressViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# File: backend/library/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
