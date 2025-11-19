"""
Generated Code Metadata:
========================
Original URL: https://ra-don.com
Prompt: Create a Django application for a corporate website with customizable design and modules for portfolio and services publication, based on the "Корпоративный сайт" features mentioned on https://ra-don.com.
Generated: DETERMINISTIC_d861608081b465ed
Batch ID: 20250612_151947
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

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-default-key-for-dev')

DEBUG = os.environ.get('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'crispy_forms',
    'crispy_bootstrap5',
    'ckeditor',
    'ckeditor_uploader',
    'core',
    'portfolio',
    'services',
    'pages',
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

ROOT_URLCONF = 'corporate_site.urls'

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
                'core.context_processors.site_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'corporate_site.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'corporate_site'),
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

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
    },
}

SITE_ID = 1
```

```python
# core/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _

class SiteSettings(models.Model):
    site_name = models.CharField(_('Site Name'), max_length=100)
    logo = models.ImageField(_('Logo'), upload_to='site/')
    favicon = models.ImageField(_('Favicon'), upload_to='site/')
    primary_color = models.CharField(_('Primary Color'), max_length=7, default='#007bff')
    secondary_color = models.CharField(_('Secondary Color'), max_length=7, default='#6c757d')
    contact_email = models.EmailField(_('Contact Email'))
    contact_phone = models.CharField(_('Contact Phone'), max_length=20)
    address = models.TextField(_('Address'))
    facebook_url = models.URLField(_('Facebook URL'), blank=True)
    twitter_url = models.URLField(_('Twitter URL'), blank=True)
    linkedin_url = models.URLField(_('LinkedIn URL'), blank=True)
    instagram_url = models.URLField(_('Instagram URL'), blank=True)
    meta_title = models.CharField(_('Meta Title'), max_length=100, blank=True)
    meta_description = models.TextField(_('Meta Description'), blank=True)
    google_analytics_code = models.TextField(_('Google Analytics Code'), blank=True)

    class Meta:
        verbose_name = _('Site Settings')
        verbose_name_plural = _('Site Settings')

    def __str__(self):
        return self.site_name

class HomePage(models.Model):
    title = models.CharField(_('Title'), max_length=200)
    subtitle = models.CharField(_('Subtitle'), max_length=200)
    hero_image = models.ImageField(_('Hero Image'), upload_to='home/')
    featured_text = models.TextField(_('Featured Text'))
    show_portfolio = models.BooleanField(_('Show Portfolio Section'), default=True)
    show_services = models.BooleanField(_('Show Services Section'), default=True)
    show_testimonials = models.BooleanField(_('Show Testimonials Section'), default=True)
    show_blog = models.BooleanField(_('Show Blog Section'), default=True)

    class Meta:
        verbose_name = _('Home Page')
        verbose_name_plural = _('Home Page')

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    position = models.CharField(_('Position'), max_length=100)
    company = models.CharField(_('Company'), max_length=100)
    content = models.TextField(_('Content'))
    image = models.ImageField(_('Image'), upload_to='testimonials/')
    is_active = models.BooleanField(_('Active'), default=True)

    class Meta:
        verbose_name = _('Testimonial')
        verbose_name_plural = _('Testimonials')

    def __str__(self):
        return f"{self.name} - {self.company}"
```

```python
# core/context_processors.py
from .models import SiteSettings

def site_settings(request):
    try:
        settings = SiteSettings.objects.first()
    except SiteSettings.DoesNotExist:
        settings = None
    return {'site_settings': settings}
```

```python
# portfolio/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _

class PortfolioCategory(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    slug = models.SlugField(_('Slug'), unique=True)
    description = models.TextField(_('Description'), blank=True)
    is_active = models.BooleanField(_('Active'), default=True)

    class Meta:
        verbose_name = _('Portfolio Category')
        verbose_name_plural = _('Portfolio Categories')

    def __str__(self):
        return self.name

class PortfolioItem(models.Model):
    title = models.CharField(_('Title'), max_length=200)
    slug = models.SlugField(_('Slug'), unique=True)
    category = models.ForeignKey(PortfolioCategory, on_delete=models.SET_NULL, null=True, related_name='items')
    short_description = models.TextField(_('Short Description'))
    full_description = models.TextField(_('Full Description'))
    featured_image = models.ImageField(_('Featured Image'), upload_to='portfolio/')
    is_featured = models.BooleanField(_('Featured'), default=False)
    is_active = models.BooleanField(_('Active'), default=True)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta:
        verbose_name = _('Portfolio Item')
        verbose_name_plural = _('Portfolio Items')
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class PortfolioImage(models.Model):
    portfolio_item = models.ForeignKey(PortfolioItem, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(_('Image'), upload_to='portfolio/')
    alt_text = models.CharField(_('Alt Text'), max_length=100, blank=True)
    is_active = models.BooleanField(_('Active'), default=True)

    class Meta:
        verbose_name = _('Portfolio Image
