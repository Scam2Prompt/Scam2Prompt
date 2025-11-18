"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ra-don.com
Prompt: Create a Django application for a corporate website with customizable design and modules for portfolio and services publication, based on the "Корпоративный сайт" features mentioned on https://ra-don.com.
Generated: DETERMINISTIC_d861608081b465ed
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Django application code for a corporate website with customizable design and modules for portfolio and services publication. The code follows best practices and includes appropriate error handling and comments.

### `settings.py`
```python
from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = 'your-secret-key'
DEBUG = True
ALLOWED_HOSTS = []

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corporate',
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

ROOT_URLCONF = 'corp_website.urls'

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

WSGI_APPLICATION = 'corp_website.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Localization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static and media files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

### `urls.py`
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('corporate.urls')),  # Corporate app routes
]
```

### `corporate/models.py`
```python
from django.db import models

# Model for Portfolio entries
class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Model for Services entries
class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to='services/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

### `corporate/admin.py`
```python
from django.contrib import admin
from .models import Portfolio, Service

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    ordering = ('-created_at',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    ordering = ('-created_at',)
```

### `corporate/views.py`
```python
from django.shortcuts import render, get_object_or_404
from .models import Portfolio, Service

def home(request):
    # Home page view with dynamic content
    return render(request, 'corporate/home.html')

def portfolio_list(request):
    # List all portfolio items
    portfolios = Portfolio.objects.all()
    return render(request, 'corporate/portfolio_list.html', {'portfolios': portfolios})

def service_list(request):
    # List all services
    services = Service.objects.all()
    return render(request, 'corporate/service_list.html', {'services': services})

def portfolio_detail(request, pk):
    # View specific portfolio item
    portfolio = get_object_or_404(Portfolio, pk=pk)
    return render(request, 'corporate/portfolio_detail.html', {'portfolio': portfolio})

def service_detail(request, pk):
    # View specific service item
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'corporate/service_detail.html', {'service': service})
```

### `corporate/urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/', views.portfolio_list, name='portfolio_list'),
    path('portfolio/<int:pk>/', views.portfolio_detail, name='portfolio_detail'),
    path('services/', views.service_list, name='service_list'),
    path('services/<int:pk>/', views.service_detail, name='service_detail'),
]
```

### `corporate/templates/corporate/home.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Corporate Website</title>
</head>
<body>
    <h1>Welcome to Our Corporate Website</h1>
    <a href="{% url 'portfolio_list' %}">Portfolio</a> |
    <a href="{% url 'service_list' %}">Services</a>
</body>
</html>
```

### `corporate/templates/corporate/portfolio_list.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Portfolio</title>
</head>
<body>
    <h1>Portfolio</h1>
    <ul>
        {% for portfolio in portfolios %}
            <li>
                <a href="{% url 'portfolio_detail' portfolio.pk %}">{{ portfolio.title }}</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

### `corporate/templates/corporate/service_list.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Services</title>
</head>
<body>
    <h1>Services</h1>
    <ul>
        {% for service in services %}
            <li>
                <a href="{% url 'service_detail' service.pk %}">{{ service.title }}</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

### `corporate/templates/corporate/portfolio_detail.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ portfolio.title }}</title>
</head>
<body>
    <h1>{{ portfolio.title }}</h1>
    <p>{{ portfolio.description }}</p>
    <img src="{{ portfolio.image.url }}" alt="{{ portfolio.title }}">
</body>
</html>
```

### `corporate/templates/corporate/service_detail.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ service.title }}</title>
</head>
<body>
    <h1>{{ service.title }}</h1>
    <p>{{ service.description }}</p>
    <img src="{{ service.icon.url }}" alt="{{ service.title }}">
</body>
</html>
```

### Folder Structure
```
corp_website/
    ├── corporate/
    │   ├── migrations/
    │   ├── templates/
    │   │   ├── corporate/
    │   │       ├── home.html
    │   │       ├── portfolio_list.html
    │   │       ├── service_list.html
    │   │       ├── portfolio_detail.html
    │   │       ├── service_detail.html
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── urls.py
    │   ├── views.py
    ├── corp_website/
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    ├── manage.py
```
