"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kantor-usdc.com
Prompt: Develop a Django web application for a cryptocurrency exchange service that includes features like those offered by Kantor USDC Białystok (e.g., cash transactions in PLN, USD, EUR, and educational consultations).
Generated: DETERMINISTIC_321e360fc6ead633
Batch ID: 20250612_155032
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
    'exchange',  # Your custom app for the exchange service
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

ROOT_URLCONF = 'crypto_exchange.urls'

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

WSGI_APPLICATION = 'crypto_exchange.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Change to PostgreSQL or another DB in production
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
            'MIN_LENGTH': 8,
        },
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

# Template for email (for educational consultations)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Change to SMTP in production
```

```python
# models.py in exchange app

from django.db import models

class Currency(models.Model):
    """Model representing a type of currency."""
    name = models.CharField(max_length=10)  # e.g., PLN, USD, EUR
    symbol = models.CharField(max_length=3)  # e.g., PLN, $ or €
    
    def __str__(self):
        return f"{self.name} ({self.symbol})"


class Transaction(models.Model):
    """Model representing a financial transaction."""
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} {self.currency} on {self.transaction_date}"


class Consultation(models.Model):
    """Model representing an educational consultation."""
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Consultation by {self.email} on {self.created_at}"
```

```python
# views.py in exchange app

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Transaction, Consultation, Currency
from .forms import ConsultationForm

def index(request):
    """View for the homepage."""
    currencies = Currency.objects.all()  # Fetch all currencies
    return render(request, 'exchange/index.html', {'currencies': currencies})


def transaction(request):
    """Process a transaction."""
    if request.method == 'POST':
        currency_id = request.POST.get('currency')
        amount = request.POST.get('amount')
        try:
            currency = Currency.objects.get(id=currency_id)
            transaction = Transaction(currency=currency, amount=amount)
            transaction.save()
            messages.success(request, "Transaction successful!")
            return redirect('index')
        except Currency.DoesNotExist:
            messages.error(request, "Invalid currency selected.")
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
    
    return redirect('index')


def consultation(request):
    """Handle educational consultation requests."""
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your consultation request has been submitted.")
            return redirect('index')
    
    return render(request, 'exchange/consultation.html', {'form': form})
```

```python
# forms.py in exchange app

from django import forms
from .models import Consultation

class ConsultationForm(forms.ModelForm):
    """Form for the consultation model."""
    class Meta:
        model = Consultation
        fields = ['email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }
```

```html
<!-- templates/exchange/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cryptocurrency Exchange</title>
</head>
<body>
    <h1>Welcome to the Cryptocurrency Exchange</h1>
    <form method="post" action="{% url 'transaction' %}">
        {% csrf_token %}
        <select name="currency">
            {% for currency in currencies %}
                <option value="{{ currency.id }}">{{ currency }}</option>
            {% endfor %}
        </select>
        <input type="number" step="0.01" name="amount" required placeholder="Amount" />
        <button type="submit">Execute Transaction</button>
    </form>

    <h2>Consultation</h2>
    <form method="post" action="{% url 'consultation' %}">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Request Consultation</button>
    </form>
</body>
</html>
```

```python
# urls.py in exchange app

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('transaction/', views.transaction, name='transaction'),
    path('consultation/', views.consultation, name='consultation'),
]
```

```python
# urls.py in project root

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('exchange.urls')),
]
```

```python
# wsgi.py in project root

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_exchange.settings')
application = get_wsgi_application()
```

```bash
# requirements.txt

Django>=4.0,<5.0
```

```bash
# To run the application
cd path_to_your_project
python manage.py migrate
python manage.py runserver
```

This code provides a clean, well-structured Django application for a cryptocurrency exchange service, including necessary features and proper error handling.
