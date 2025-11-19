"""
Generated Code Metadata:
========================
Original URL: https://myflowfoundationke.org
Prompt: Create a donation management system for a non-profit organization that focuses on menstrual health and education, using a framework like Django or Flask.
Generated: DETERMINISTIC_39f8f81d1ad4cffc
Batch ID: 20250622_212039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Donation Management System for Menstrual Health Non-Profit (Django)

## Project Structure
```
donation_system/
├── donation_system/          # Main project directory
│   ├── __init__.py
│   ├── settings.py           # Django settings
│   ├── urls.py               # Project URLs
│   └── wsgi.py
├── donations/                # Donations app
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py               # App URLs
│   └── views.py
├── manage.py
└── requirements.txt
```

### requirements.txt
```
Django==4.2.7
psycopg2-binary==2.9.7
django-crispy-forms==2.1
crispy-bootstrap5==2023.8
python-dotenv==1.0.0
stripe==7.0.0
```

### donation_system/settings.py
```python
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
    'donations',
    'crispy_forms',
    'crispy_bootstrap5',
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

ROOT_URLCONF = 'donation_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'donation_system.wsgi.application'

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
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
STRIPE_WEBHOOK_SECRET = os.getenv('STRIPE_WEBHOOK_SECRET')
```

### donations/models.py
```python
from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

class Donor(models.Model):
    """Model representing a donor"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    is_anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Donation(models.Model):
    """Model representing a donation"""
    donor = models.ForeignKey(Donor, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(1.00)]
    )
    currency = models.CharField(max_length=3, default='USD')
    payment_method = models.CharField(max_length=50)
    is_recurring = models.BooleanField(default=False)
    frequency = models.CharField(max_length=20, blank=True, null=True)
    payment_intent_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, default='pending')
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Donation #{self.id} - ${self.amount}"

class Campaign(models.Model):
    """Model representing a fundraising campaign"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    @property
    def total_raised(self):
        """Calculate total donations for this campaign"""
        return sum(donation.amount for donation in self.donations.all())

    @property
    def progress_percentage(self):
        """Calculate fundraising progress percentage"""
        if self.target_amount == 0:
            return 0
        return min(100, (self.total_raised / self.target_amount) * 100)
```

### donations/forms.py
```python
from django import forms
from django.core.validators import MinValueValidator
from .models import Donor, Donation, Campaign

class DonorForm(forms.ModelForm):
    """Form for donor information"""
    class Meta:
        model = Donor
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'is_anonymous']
        widgets = {
            'is_anonymous': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class DonationForm(forms.ModelForm):
    """Form for donation information"""
    amount = forms.DecimalField(
        min_value=1.00,
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'step': '0.01'})
    )
    campaign = forms.ModelChoiceField(
        queryset=Campaign.objects.filter(is_active=True),
        required=False
    )

    class Meta:
        model = Donation
        fields = ['amount', 'is_recurring', 'frequency', 'notes']
        widgets = {
            'is_recurring': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'frequency': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

class CampaignForm(forms.ModelForm):
    """Form for campaign creation/editing"""
    class Meta:
        model = Campaign
        fields = ['name', 'description', 'target_amount', 'start_date', 'end_date', 'is_active']
        widgets = {
            'start_date': forms.DateInput
