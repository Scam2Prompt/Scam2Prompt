"""
Generated Code Metadata:
========================
Original URL: https://prgmea.pk
Prompt: Using Django, build a web application that allows apparel manufacturers to sign up for PRGMEA membership and manage their accounts.
Generated: DETERMINISTIC_555de6b13fbba19a
Batch ID: 20250612_153224
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

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-default-key-for-dev')

DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'members.apps.MembersConfig',
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

ROOT_URLCONF = 'prgmea.urls'

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

WSGI_APPLICATION = 'prgmea.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'prgmea'),
        'USER': os.environ.get('DB_USER', 'prgmea'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'prgmea'),
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
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'home'

EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = os.environ.get('EMAIL_HOST', '')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 587)
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'webmaster@prgmea.org')
```

```python
# urls.py (project level)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('members.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

```python
# models.py (members app)
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class Member(AbstractUser):
    COMPANY_TYPE_CHOICES = [
        ('manufacturer', 'Manufacturer'),
        ('exporter', 'Exporter'),
        ('supplier', 'Supplier'),
        ('other', 'Other'),
    ]
    
    company_name = models.CharField(max_length=255)
    company_type = models.CharField(max_length=50, choices=COMPANY_TYPE_CHOICES)
    address = models.TextField()
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    website = models.URLField(blank=True, null=True)
    business_registration_number = models.CharField(max_length=100)
    tax_id = models.CharField(max_length=100)
    membership_number = models.CharField(max_length=50, unique=True, blank=True, null=True)
    membership_status = models.CharField(max_length=20, default='pending')
    membership_date = models.DateField(blank=True, null=True)
    logo = models.ImageField(upload_to='member_logos/', blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.company_name} ({self.username})"

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

class MembershipPayment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    invoice_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.member.company_name} - {self.amount} ({self.status})"
```

```python
# forms.py (members app)
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Member

class MemberRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    company_name = forms.CharField(max_length=255, required=True)
    company_type = forms.ChoiceField(choices=Member.COMPANY_TYPE_CHOICES, required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)
    phone_number = forms.CharField(max_length=17, required=True)
    business_registration_number = forms.CharField(max_length=100, required=True)
    tax_id = forms.CharField(max_length=100, required=True)
    logo = forms.ImageField(required=False)

    class Meta:
        model = Member
        fields = [
            'username', 'email', 'password1', 'password2',
            'company_name', 'company_type', 'address', 'phone_number',
            'website', 'business_registration_number', 'tax_id', 'logo'
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Member.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email

class MemberProfileForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'company_name', 'company_type', 'address', 'phone_number',
            'website', 'business_registration_number', 'tax_id', 'logo'
        ]
```

```python
# views.py (members app)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .forms import MemberRegistrationForm, MemberProfileForm
from .models import Member

def home(request):
    return render(request, 'members/home.html')

def register(request):
    if request.method == 'POST
