"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://childnepal.org
Prompt: Develop a Django web application for an NGO like Child Nepal to manage their advocacy campaigns, including features for tracking progress, partnerships, and beneficiary data.
Generated: DETERMINISTIC_73171e9277978455
Batch ID: 20250612_153517
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
    'rest_framework',
    'campaigns',
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

ROOT_URLCONF = 'ngo_project.urls'

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

WSGI_APPLICATION = 'ngo_project.wsgi.application'

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

```python
# models.py in campaigns app

from django.db import models

class Campaign(models.Model):
    """Model representing an advocacy campaign."""
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    progress = models.FloatField(default=0.0)  # Progress percentage (0-100)

    def __str__(self):
        """Return a string representation of the campaign."""
        return self.title

class Partnership(models.Model):
    """Model representing partnerships with other organizations."""
    name = models.CharField(max_length=200, unique=True)
    contact_info = models.TextField()

    def __str__(self):
        """Return a string representation of the partnership."""
        return self.name

class Beneficiary(models.Model):
    """Model representing a beneficiary of the NGO."""
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='beneficiaries')

    def __str__(self):
        """Return a string representation of the beneficiary."""
        return self.name
```

```python
# views.py in campaigns app

from rest_framework import viewsets
from .models import Campaign, Partnership, Beneficiary
from .serializers import CampaignSerializer, PartnershipSerializer, BeneficiarySerializer

class CampaignViewSet(viewsets.ModelViewSet):
    """ViewSet for managing campaigns."""
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

class PartnershipViewSet(viewsets.ModelViewSet):
    """ViewSet for managing partnerships."""
    queryset = Partnership.objects.all()
    serializer_class = PartnershipSerializer

class BeneficiaryViewSet(viewsets.ModelViewSet):
    """ViewSet for managing beneficiaries."""
    queryset = Beneficiary.objects.all()
    serializer_class = BeneficiarySerializer
```

```python
# serializers.py in campaigns app

from rest_framework import serializers
from .models import Campaign, Partnership, Beneficiary

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'

class PartnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partnership
        fields = '__all__'

class BeneficiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiary
        fields = '__all__'
```

```python
# urls.py in campaigns app

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CampaignViewSet, PartnershipViewSet, BeneficiaryViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'campaigns', CampaignViewSet)
router.register(r'partnerships', PartnershipViewSet)
router.register(r'beneficiaries', BeneficiaryViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
```

```python
# urls.py in ngo_project

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('campaigns.urls')),  # Including the campaigns app URLs
]
```

```python
# admin.py in campaigns app

from django.contrib import admin
from .models import Campaign, Partnership, Beneficiary

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    """Admin interface for Campaign model."""
    list_display = ('title', 'start_date', 'end_date', 'progress')
    search_fields = ('title',)

@admin.register(Partnership)
class PartnershipAdmin(admin.ModelAdmin):
    """Admin interface for Partnership model."""
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Beneficiary)
class BeneficiaryAdmin(admin.ModelAdmin):
    """Admin interface for Beneficiary model."""
    list_display = ('name', 'age', 'campaign')
    search_fields = ('name',)
```

```bash
# requirements.txt

Django>=3.2,<4
djangorestframework>=3.12,<4
```

```bash
# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run the server
python manage.py runserver
```

```python
# wsgi.py in ngo_project

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ngo_project.settings')
application = get_wsgi_application()
```

Please ensure to replace `'yourdomain.com'` and the `'DJANGO_SECRET_KEY'` in the settings with actual values. Also, make sure to test thoroughly before deploying to production.
