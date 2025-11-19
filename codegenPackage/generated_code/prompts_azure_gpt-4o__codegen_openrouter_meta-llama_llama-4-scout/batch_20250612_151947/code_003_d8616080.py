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

**corporate_website URL configuration**

```python
# corporate_website/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
]
```

**Website application URL configuration**

```python
# website/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('services/', views.services, name='services'),
]
```

**Website application views**

```python
# website/views.py

from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio, Service

def home(request):
    return render(request, 'website/home.html')

def portfolio(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'website/portfolio.html', {'portfolios': portfolios})

def services(request):
    services = Service.objects.all()
    return render(request, 'website/services.html', {'services': services})
```

**Website application models**

```python
# website/models.py

from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio')

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
```

**Database migration**

```python
# website/migrations/0001_initial.py

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='portfolio')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
```

**Templates**

**base.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Корпоративный сайт</title>
</head>
<body>
    <header>
        <!-- header content -->
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <footer>
        <!-- footer content -->
    </footer>
</body>
</html>
```

**home.html**
```html
{% extends 'base.html' %}

{% block content %}
    <!-- home page content -->
{% endblock %}
```

**portfolio.html**
```html
{% extends 'base.html' %}

{% block content %}
    <h1>Портфолио</h1>
    <ul>
    {% for portfolio in portfolios %}
        <li>
            <h2>{{ portfolio.title }}</h2>
            <p>{{ portfolio.description }}</p>
            <img src="{{ portfolio.image.url }}" alt="{{ portfolio.title }}">
        </li>
    {% empty %}
        <p>No portfolios found.</p>
    {% endfor %}
    </ul>
{% endblock %}
```

**services.html**
```html
{% extends 'base.html' %}

{% block content %}
    <h1>Услуги</h1>
    <ul>
    {% for service in services %}
        <li>
            <h2>{{ service.title }}</h2>
            <p>{{ service.description }}</p>
        </li>
    {% empty %}
        <p>No services found.</p>
    {% endfor %}
    </ul>
{% endblock %}
```

**Settings**

```python
# corporate_website/settings.py

INSTALLED_APPS = [
    # ...
    'website.apps.WebsiteConfig',
    # ...
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

**Media and Static files serving**

```python
# corporate_website/urls.py (continued)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```
