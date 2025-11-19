"""
Generated Code Metadata:
========================
Original URL: https://churchproweb.com
Prompt: Develop a Church Website with sermon manager, prayer requests and online donation features using Python and Django.
Generated: DETERMINISTIC_5262c56463219a2a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# File: church_website/settings.py
"""
Django settings for the Church Website project.
"""

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
    'sermons',
    'prayer_requests',
    'donations',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'church_website.urls'

# Templates
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

WSGI_APPLICATION = 'church_website.wsgi.application'

# Database
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

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email settings (for prayer request notifications)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
```

```python
# File: church_website/urls.py
"""
URL configuration for the Church Website project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sermons/', include('sermons.urls')),
    path('prayer-requests/', include('prayer_requests.urls')),
    path('donations/', include('donations.urls')),
]
```

```python
# File: sermons/models.py
"""
Models for the Sermons app.
"""

from django.db import models

class Sermon(models.Model):
    title = models.CharField(max_length=200)
    preacher = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    audio_file = models.FileField(upload_to='sermons/audio/', blank=True, null=True)

    def __str__(self):
        return self.title
```

```python
# File: sermons/views.py
"""
Views for the Sermons app.
"""

from django.shortcuts import render, get_object_or_404
from .models import Sermon

def sermon_list(request):
    sermons = Sermon.objects.all().order_by('-date')
    return render(request, 'sermons/sermon_list.html', {'sermons': sermons})

def sermon_detail(request, pk):
    sermon = get_object_or_404(Sermon, pk=pk)
    return render(request, 'sermons/sermon_detail.html', {'sermon': sermon})
```

```python
# File: sermons/urls.py
"""
URL configuration for the Sermons app.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.sermon_list, name='sermon_list'),
    path('<int:pk>/', views.sermon_detail, name='sermon_detail'),
]
```

```python
# File: prayer_requests/models.py
"""
Models for the Prayer Requests app.
"""

from django.db import models

class PrayerRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    request = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date_submitted.strftime('%Y-%m-%d')}"
```

```python
# File: prayer_requests/views.py
"""
Views for the Prayer Requests app.
"""

from django.shortcuts import render
from django.core.mail import send_mail
from .models import PrayerRequest
from .forms import PrayerRequestForm

def prayer_request_list(request):
    requests = PrayerRequest.objects.all().order_by('-date_submitted')
    return render(request, 'prayer_requests/prayer_request_list.html', {'requests': requests})

def submit_prayer_request(request):
    if request.method == 'POST':
        form = PrayerRequestForm(request.POST)
        if form.is_valid():
            prayer_request = form.save()
            # Send email notification
            send_mail(
                'New Prayer Request Submitted',
                f"Name: {prayer_request.name}\nEmail: {prayer_request.email}\nRequest: {prayer_request.request}",
                'your-email@example.com',
                ['admin@example.com'],
                fail_silently=False,
            )
            return render(request, 'prayer_requests/thank_you.html')
    else:
        form = PrayerRequestForm()
    return render(request, 'prayer_requests/submit_prayer_request.html', {'form': form})
```

```python
# File: prayer_requests/forms.py
"""
Forms for the Prayer Requests app.
"""

from django import forms
from .models import PrayerRequest

class PrayerRequestForm(forms.ModelForm):
    class Meta:
        model = PrayerRequest
        fields = ['name', 'email', 'request']
```

```python
# File: prayer_requests/urls.py
"""
URL configuration for the Prayer Requests app.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.prayer_request_list, name='prayer_request_list'),
    path('submit/', views.submit_prayer_request, name='submit_prayer_request'),
]
```

```python
# File: donations/models.py
"""
Models for the Donations app.
"""

from django.db import models

class Donation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - ${self.amount} - {self.date_submitted.strftime('%Y-%m-%d')}"
```

```python
# File: donations/views.py
"""
Views for the Donations app.
"""

from django.shortcuts import render
from .forms import DonationForm

def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'donations/thank_you.html')
    else:
        form = DonationForm()
    return render(request, 'donations/donate.html', {'form': form})
```

```python
# File: donations/forms.py
"""
Forms for the Donations app.
"""

from django import forms
from .models import Donation

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['name', 'email', 'amount']
```

```python
# File: donations/urls.py
"""
URL configuration for the Donations app.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('donate/', views.donate, name='donate'),
]
```

```html
<!-- File: templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Church Website</title>
</head>
<body>
    <header>
        <h1>Welcome to Our Church</h1>
        <nav>
            <ul>
                <li><a href="/sermons/">Sermons</a></li>
                <li><a href="/prayer-requests/">Prayer Requests</a></li>
                <li><a href="/donations/donate/">Donate</a></li>
            </ul>
        </nav>
    </header>
    <main>
        {% block content %}
        {% endblock %}
    </main>
    <footer>
        <p>&copy; 2023 Church Website</p>
    </footer>
</body>
</html>
```

```html
<!-- File: templates/sermons/sermon_list.html -->
{% extends '
