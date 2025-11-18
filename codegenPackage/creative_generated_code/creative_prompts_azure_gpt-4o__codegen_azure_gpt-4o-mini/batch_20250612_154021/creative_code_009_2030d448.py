"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yobugo.com
Prompt: Develop a Django application to manage customer inquiries for Yobugo's products, such as "Coctel de Café Cream Love" and "Crema de lúcuma."
Generated: DETERMINISTIC_2030d44812241e36
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# project/settings.py

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'inquiries',  # Our app for managing customer inquiries
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

ROOT_URLCONF = 'project.urls'

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

WSGI_APPLICATION = 'project.wsgi.application'

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
```

```python
# project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inquiries/', include('inquiries.urls')),  # Include the inquiries app URLs
]
```

```python
# inquiries/models.py

from django.db import models

class Product(models.Model):
    """Model representing a product."""
    name = models.CharField(max_length=255)
    
    def __str__(self):
        """Return the string representation of the product."""
        return self.name


class Inquiry(models.Model):
    """Model representing a customer inquiry."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the string representation of the inquiry."""
        return f"Inquiry from {self.customer_name} regarding {self.product.name}"
```

```python
# inquiries/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Inquiry, Product
from .forms import InquiryForm

def inquiry_list(request):
    """View to list all inquiries."""
    inquiries = Inquiry.objects.all().order_by('-created_at')
    return render(request, 'inquiries/inquiry_list.html', {'inquiries': inquiries})

def create_inquiry(request):
    """View to create a new inquiry."""
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()  # Save the inquiry form
            return redirect('inquiry_list')  # Redirect to the inquiry list view
    else:
        form = InquiryForm()
    return render(request, 'inquiries/create_inquiry.html', {'form': form})
```

```python
# inquiries/forms.py

from django import forms
from .models import Inquiry

class InquiryForm(forms.ModelForm):
    """Form for creating inquiries."""
    class Meta:
        model = Inquiry
        fields = ['product', 'customer_name', 'email', 'message']
```

```python
# inquiries/urls.py

from django.urls import path
from .views import inquiry_list, create_inquiry

urlpatterns = [
    path('', inquiry_list, name='inquiry_list'),
    path('new/', create_inquiry, name='create_inquiry'),
]
```

```html
<!-- inquiries/templates/inquiries/inquiry_list.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Inquiries</title>
</head>
<body>
    <h1>Customer Inquiries</h1>
    <a href="{% url 'create_inquiry' %}">Create New Inquiry</a>
    <ul>
        {% for inquiry in inquiries %}
            <li>{{ inquiry.created_at }} - {{ inquiry.customer_name }}: {{ inquiry.message }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- inquiries/templates/inquiries/create_inquiry.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Create Inquiry</title>
</head>
<body>
    <h1>Create Inquiry</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit Inquiry</button>
    </form>
</body>
</html>
```

```python
# project/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
application = get_wsgi_application()
```

```bash
# Run the following commands in your terminal to set up the project

# Create the virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install Django
pip install django

# Create a new project
django-admin startproject project

# Create the inquiries app
cd project
python manage.py startapp inquiries

# Add the inquiries app to settings.py and define models, views, forms, and templates as per the provided code.
# Then run the migrations and start the development server
python manage.py makemigrations inquiries
python manage.py migrate
python manage.py runserver
```

This code provides a simple Django application to manage customer inquiries for Yobugo's products, including appropriate models, views, forms, and templates.
