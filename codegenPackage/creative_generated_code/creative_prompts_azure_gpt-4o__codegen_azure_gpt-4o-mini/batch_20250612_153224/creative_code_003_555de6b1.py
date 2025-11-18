"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prgmea.pk
Prompt: Using Django, build a web application that allows apparel manufacturers to sign up for PRGMEA membership and manage their accounts.
Generated: DETERMINISTIC_555de6b13fbba19a
Batch ID: 20250612_153224
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

# Django settings for the PRGMEA membership application.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'your-secret-key'  # Change this to a secure key in production

DEBUG = True  # Set to False in production

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'members',  # Our custom app for membership management
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

WSGI_APPLICATION = 'prgmea.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Change to your preferred database
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # Path to the database file
    }
}

# Password validation settings
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
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

# Custom settings for email (for sending account-related emails)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # For development

# Custom User Model
AUTH_USER_MODEL = 'members.Member'

```

```shell
# models.py (in members app)

from django.db import models
from django.contrib.auth.models import AbstractUser

class Member(AbstractUser):
    """Custom User Model for PRGMEA members."""
    company_name = models.CharField(max_length=255, unique=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
```

```shell
# forms.py (in members app)

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Member

class MemberSignUpForm(UserCreationForm):
    """Form for new member registration."""
    
    class Meta:
        model = Member
        fields = ('username', 'company_name', 'password1', 'password2', 'contact_number', 'address')

class MemberUpdateForm(forms.ModelForm):
    """Form for updating member details."""
    
    class Meta:
        model = Member
        fields = ('username', 'company_name', 'contact_number', 'address')
```

```shell
# views.py (in members app)

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import MemberSignUpForm, MemberUpdateForm

def signup(request):
    """View function for member signup."""
    if request.method == 'POST':
        form = MemberSignUpForm(request.POST)
        if form.is_valid():
            member = form.save()
            login(request, member)  # Auto-login after signup
            return redirect('member_dashboard')  # Redirect to dashboard after signup
    else:
        form = MemberSignUpForm()
    return render(request, 'members/signup.html', {'form': form})

@login_required
def dashboard(request):
    """View function for displaying member dashboard."""
    return render(request, 'members/dashboard.html')

@login_required
def update_account(request):
    """View function for updating member account details."""
    member = request.user
    if request.method == 'POST':
        form = MemberUpdateForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_dashboard')  # Redirect to dashboard after update
    else:
        form = MemberUpdateForm(instance=member)
    return render(request, 'members/update_account.html', {'form': form})
```

```shell
# urls.py (in members app)

from django.urls import path
from .views import signup, dashboard, update_account

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('dashboard/', dashboard, name='member_dashboard'),
    path('update/', update_account, name='update_account'),
]
```

```shell
# urls.py (in prgmea project)

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('members.urls')),  # Include member URLs
]
```

```html
<!-- signup.html (in members templates) -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sign Up</title>
</head>
<body>
    <h1>Sign Up for PRGMEA Membership</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Sign Up</button>
    </form>
</body>
</html>
```

```html
<!-- dashboard.html (in members templates) -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Dashboard</title>
</head>
<body>
    <h1>Welcome, {{ user.company_name }}</h1>
    <a href="{% url 'update_account' %}">Update Account</a>
    <a href="{% url 'logout' %}">Logout</a>
</body>
</html>
```

```html
<!-- update_account.html (in members templates) -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Update Account</title>
</head>
<body>
    <h1>Update Your Account</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Update</button>
    </form>
</body>
</html>
```

```shell
# wsgi.py (in prgmea project)

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prgmea.settings')

application = get_wsgi_application()
```

```shell
# manage.py

#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "prgmea.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
```

Make sure to run `python manage.py migrate` after creating the models to set up the database. Use a secure `SECRET_KEY` and configure the email backend for production use.
