"""
Generated Code Metadata:
========================
Original URL: https://akaan.com.tr
Prompt: Create a sample project structure for a corporate website that is both mobile and SEO-friendly, as described by Akaan.
Generated: DETERMINISTIC_c4bd3c324ff52244
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Corporate Website Project Structure
"""

# File: requirements.txt
"""
Django==4.0.6
django-seo-js==2.1.0
django-compressor==4.1
django-crispy-forms==2.0
django-sitemap==1.0.0
django-robots==4.0
pillow==9.2.0
whitenoise==6.2.0
"""

# File: corporate_site/settings.py
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'compressor',
    'crispy_forms',
    'robots',
    'seo_js',
    'main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'seo_js.middleware.EscapedFragmentMiddleware',
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
            ],
        },
    },
]

WSGI_APPLICATION = 'corporate_site.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

# SEO Settings
SITE_ID = 1
SEO_JS_ENABLED = True
SEO_JS_PRERENDER_TOKEN = os.getenv('PRERENDER_TOKEN', '')

# Static files compression
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# Mobile-friendly settings
MIDDLEWARE.append('django.middleware.gzip.GZipMiddleware')
MIDDLEWARE.append('django.middleware.http.ConditionalGetMiddleware')
"""

# File: corporate_site/urls.py
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from main.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('robots.txt', include('robots.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""

# File: corporate_site/wsgi.py
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'corporate_site.settings')
application = get_wsgi_application()
"""

# File: main/models.py
"""
from django.db import models
from django.urls import reverse

class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    meta_description = models.CharField(max_length=300, blank=True)
    meta_keywords = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page_detail', kwargs={'slug': self.slug})
"""

# File: main/sitemaps.py
"""
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Page

class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return ['home', 'about', 'contact', 'services']

    def location(self, item):
        return reverse(item)

class PageSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Page.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
"""

# File: main/urls.py
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('<slug:slug>/', views.page_detail, name='page_detail'),
]
"""

# File: main/views.py
"""
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from .models import Page

@require_GET
def home(request):
    return render(request, 'main/home.html', {
        'meta_title': 'Home - Corporate Site',
        'meta_description': 'Welcome to our corporate website',
    })

@require_GET
def about(request):
    return render(request, 'main/about.html', {
        'meta_title': 'About Us - Corporate Site',
        'meta_description': 'Learn about our company',
    })

@require_GET
def contact(request):
    return render(request, 'main/contact.html', {
        'meta_title': 'Contact Us - Corporate Site',
        'meta_description': 'Get in touch with our team',
    })

@require_GET
def services(request):
    return render(request, 'main/services.html', {
        'meta_title': 'Our Services - Corporate Site',
        'meta_description': 'Explore our professional services',
    })

@require_GET
def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'main/page_detail.html', {
        'page': page,
        'meta_title': f'{page.title} - Corporate Site',
        'meta_description': page.meta_description,
    })
"""

# File: templates/base.html
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <meta name="description" content="{% block meta_description %}{% endblock %}">
    <meta name="keywords" content="{% block meta_keywords %}{% endblock %}">
    <title>{% block meta_title %}{% endblock %}</title>
    
    <!-- Favicon -->
    <link rel="icon" href="/static/favicon.ico">
    
    <!-- CSS -->
    {% compress css %}
