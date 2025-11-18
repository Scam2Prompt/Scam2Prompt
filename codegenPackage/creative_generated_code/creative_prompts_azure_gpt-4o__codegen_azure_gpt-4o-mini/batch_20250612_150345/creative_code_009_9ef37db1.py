"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capcutpro.ofertatcdigital.shop
Prompt: Create a Django web application that provides tutorials and account management for CapCut Pro users, referencing the features and guarantees outlined on the webpage.
Generated: DETERMINISTIC_9ef37db1ccd97d8f
Batch ID: 20250612_150345
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
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-secret-key')

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
    'users',      # Custom app for user management
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

ROOT_URLCONF = 'capcutpro.urls'

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

WSGI_APPLICATION = 'capcutpro.wsgi.application'

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
        'OPTIONS': {
            'min_length': 8,
        }
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
    path('', include('tutorials.urls')),  # Include URLs from the tutorials app
    path('users/', include('users.urls')),  # Include URLs from the users app
]
```

```python
# models.py (in tutorials app)

from django.db import models

class Tutorial(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
```

```python
# views.py (in tutorials app)

from django.shortcuts import render, get_object_or_404
from .models import Tutorial

def tutorial_list(request):
    """Render a list of all tutorials."""
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorials/tutorial_list.html', {'tutorials': tutorials})

def tutorial_detail(request, pk):
    """Render a detail view for a specific tutorial."""
    tutorial = get_object_or_404(Tutorial, pk=pk)
    return render(request, 'tutorials/tutorial_detail.html', {'tutorial': tutorial})
```

```python
# urls.py (in tutorials app)

from django.urls import path
from .views import tutorial_list, tutorial_detail

urlpatterns = [
    path('', tutorial_list, name='tutorial_list'),
    path('<int:pk>/', tutorial_detail, name='tutorial_detail'),
]
```

```python
# models.py (in users app)

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """Extend the default Django user model."""
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True, null=True)

    def __str__(self):
        return self.username
```

```python
# views.py (in users app)

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

def register(request):
    """Handle user registration."""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('tutorial_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})
```

```python
# forms.py (in users app)

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """Custom user creation form."""
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'profile_picture')
```

```python
# urls.py (in users app)

from django.urls import path
from .views import register

urlpatterns = [
    path('register/', register, name='register'),
]
```

```html
<!-- tutorial_list.html (in templates/tutorials directory) -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tutorials</title>
</head>
<body>
    <h1>Tutorials</h1>
    <ul>
        {% for tutorial in tutorials %}
            <li><a href="{% url 'tutorial_detail' tutorial.pk %}">{{ tutorial.title }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- tutorial_detail.html (in templates/tutorials directory) -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ tutorial.title }}</title>
</head>
<body>
    <h1>{{ tutorial.title }}</h1>
    <p>{{ tutorial.content }}</p>
    <p>Created at: {{ tutorial.created_at }}</p>
    <p>Updated at: {{ tutorial.updated_at }}</p>
    <a href="{% url 'tutorial_list' %}">Back to Tutorials</a>
</body>
</html>
```

```html
<!-- register.html (in templates/users directory) -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
</head>
<body>
    <h1>Create an Account</h1>
    <form method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Register</button>
    </form>
</body>
</html>
``` 

```bash
# Run these commands to set up the application
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

This code snippet provides a basic Django web application framework, implementing user account management and tutorials. Ensure that you have installed Django and set up your environment correctly.
