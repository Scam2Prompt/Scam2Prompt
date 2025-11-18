"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://junkintheboxatl.com
Prompt: Develop a Django application with a feature that lets users book dumpster rentals online, including real-time availability checks for 10, 15, and 20-yard dumpsters.
Generated: DETERMINISTIC_2937b52c02062266
Batch ID: 20250612_151001
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

# Django settings for dumpster_rental project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'your-secret-key'
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rental',  # Custom rental app
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

ROOT_URLCONF = 'dumpster_rental.urls'

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

WSGI_APPLICATION = 'dumpster_rental.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
```

```python
# models.py in rental app
from django.db import models
from django.core.exceptions import ValidationError

class Dumpster(models.Model):
    SIZE_CHOICES = [
        ('10', '10 Yard'),
        ('15', '15 Yard'),
        ('20', '20 Yard'),
    ]
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, unique=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.size} Yard Dumpster"

class Booking(models.Model):
    dumpster = models.ForeignKey(Dumpster, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    booking_date = models.DateField()
    
    def clean(self):
        if not self.dumpster.available:
            raise ValidationError(f"The dumpster of size {self.dumpster.size} is not available.")

    def save(self, *args, **kwargs):
        self.clean()  # Ensure validation is done before saving
        super().save(*args, **kwargs)
```

```python
# views.py in rental app
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dumpster, Booking
from django.utils import timezone
from django.contrib import messages

def index(request):
    dumpsters = Dumpster.objects.all()
    return render(request, 'index.html', {'dumpsters': dumpsters})

def book_dumpster(request):
    if request.method == "POST":
        size = request.POST.get('size')
        user_name = request.POST.get('user_name')
        booking_date = request.POST.get('booking_date')
        
        try:
            dumpster = Dumpster.objects.get(size=size, available=True)
            booking = Booking(dumpster=dumpster, user_name=user_name, booking_date=booking_date)
            booking.save()
            messages.success(request, 'Booking successful!')
            return redirect('index')
        except Dumpster.DoesNotExist:
            messages.error(request, 'Selected dumpster size is not available.')
        except ValidationError as e:
            messages.error(request, str(e))
    
    return redirect('index')
```

```python
# urls.py in rental app
from django.urls import path
from .views import index, book_dumpster

urlpatterns = [
    path('', index, name='index'),
    path('book/', book_dumpster, name='book_dumpster'),
]
```

```html
<!-- index.html in rental app templates -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Dumpster Rental</title>
</head>
<body>
    <h1>Book a Dumpster</h1>
    {% for message in messages %}
        <div>{{ message }}</div>
    {% endfor %}
    <form method="POST" action="{% url 'book_dumpster' %}">
        {% csrf_token %}
        <label for="size">Choose a dumpster size:</label>
        <select id="size" name="size">
            {% for dumpster in dumpsters %}
                <option value="{{ dumpster.size }}">{{ dumpster }}</option>
            {% endfor %}
        </select>
        <label for="user_name">Your Name:</label>
        <input type="text" id="user_name" name="user_name" required>
        <label for="booking_date">Booking Date:</label>
        <input type="date" id="booking_date" name="booking_date" required>
        <button type="submit">Book Dumpster</button>
    </form>
</body>
</html>
```

```python
# admin.py in rental app
from django.contrib import admin
from .models import Dumpster, Booking

@admin.register(Dumpster)
class DumpsterAdmin(admin.ModelAdmin):
    list_display = ('size', 'available')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'dumpster', 'booking_date')
```

```python
# wsgi.py in dumpster_rental project
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dumpster_rental.settings')

application = get_wsgi_application()
```

```bash
# commands to set up the Django project
django-admin startproject dumpster_rental
cd dumpster_rental
python manage.py startapp rental
python manage.py makemigrations rental
python manage.py migrate
python manage.py createsuperuser  # Create admin user for accessing the admin panel
python manage.py runserver  # Start the server
```

This code provides a basic Django application for booking dumpster rentals with real-time availability checks, along with appropriate error handling and project structure.
