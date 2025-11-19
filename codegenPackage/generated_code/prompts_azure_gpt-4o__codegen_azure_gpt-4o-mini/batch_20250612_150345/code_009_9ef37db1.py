"""
Generated Code Metadata:
========================
Original URL: https://capcutpro.ofertatcdigital.shop
Prompt: Create a Django web application that provides tutorials and account management for CapCut Pro users, referencing the features and guarantees outlined on the webpage.
Generated: DETERMINISTIC_9ef37db1ccd97d8f
Batch ID: 20250612_150345
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
    'tutorials',  # Custom app for tutorials
    'accounts',   # Custom app for account management
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

ROOT_URLCONF = 'capcut_pro.urls'

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

WSGI_APPLICATION = 'capcut_pro.wsgi.application'

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

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

```python
# urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tutorials/', include('tutorials.urls')),  # Include tutorial app URLs
    path('accounts/', include('accounts.urls')),    # Include account management URLs
]
```

```python
# models.py in tutorials app

from django.db import models

class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

```python
# views.py in tutorials app

from django.shortcuts import render, get_object_or_404
from .models import Tutorial

def tutorial_list(request):
    """View to list all tutorials."""
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorials/tutorial_list.html', {'tutorials': tutorials})

def tutorial_detail(request, tutorial_id):
    """View to display a single tutorial."""
    tutorial = get_object_or_404(Tutorial, id=tutorial_id)
    return render(request, 'tutorials/tutorial_detail.html', {'tutorial': tutorial})
```

```python
# urls.py in tutorials app

from django.urls import path
from . import views

urlpatterns = [
    path('', views.tutorial_list, name='tutorial_list'),
    path('<int:tutorial_id>/', views.tutorial_detail, name='tutorial_detail'),
]
```

```python
# models.py in accounts app

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """Custom user model extending the default Django user model."""
    pass  # Add additional fields if necessary
```

```python
# views.py in accounts app

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """View for user registration."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tutorial_list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
```

```python
# urls.py in accounts app

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
]
```

```html
<!-- tutorial_list.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Tutorials</title>
</head>
<body>
    <h1>Tutorials</h1>
    <ul>
        {% for tutorial in tutorials %}
            <li><a href="{% url 'tutorial_detail' tutorial.id %}">{{ tutorial.title }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- tutorial_detail.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ tutorial.title }}</title>
</head>
<body>
    <h1>{{ tutorial.title }}</h1>
    <p>{{ tutorial.content }}</p>
    <a href="{% url 'tutorial_list' %}">Back to Tutorials</a>
</body>
</html>
```

```html
<!-- register.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Register</button>
    </form>
</body>
</html>
```

```bash
# commands to run in terminal

# Create the Django project
django-admin startproject capcut_pro

# Create the tutorials app
python manage.py startapp tutorials

# Create the accounts app
python manage.py startapp accounts

# Apply migrations
python manage.py migrate

# Create a superuser for admin access
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

This code provides a basic structure for a Django web application that includes tutorials and account management for CapCut Pro users. Make sure to customize the settings, templates, and models as per your specific requirements.
