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

### Django Cryptocurrency Exchange Service Code

#### `settings.py`
```python
# Standard Django settings file with necessary configurations
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-secret-key')

DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', 'localhost').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'exchange',  # Custom app for cryptocurrency exchange service
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

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

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

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

#### `urls.py`
```python
# Main URL configuration for the application
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('exchange.urls')),  # Include URLs from the 'exchange' app
]
```

#### `exchange/models.py`
```python
# Database models for the exchange application
from django.db import models

class Currency(models.Model):
    name = models.CharField(max_length=50)  # Currency name (e.g., USD, PLN)
    symbol = models.CharField(max_length=10)  # Currency symbol (e.g., $)
    exchange_rate_to_pln = models.DecimalField(max_digits=10, decimal_places=2)  # Exchange rate to PLN

    def __str__(self):
        return f"{self.name} ({self.symbol})"

class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('BUY', 'Buy'),
        ('SELL', 'Sell'),
    ]

    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)  # Foreign key to Currency
    transaction_type = models.CharField(max_length=4, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Amount of currency
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp of the transaction

    def __str__(self):
        return f"{self.transaction_type} {self.amount} {self.currency.symbol} on {self.timestamp}"
```

#### `exchange/views.py`
```python
# Views for the exchange application
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Currency, Transaction

def list_currencies(request):
    """
    View to list all available currencies and their exchange rates.
    """
    currencies = Currency.objects.all()
    return render(request, 'exchange/currencies.html', {'currencies': currencies})

def perform_transaction(request, currency_id):
    """
    View to perform a transaction (buy/sell) for a specific currency.
    """
    currency = get_object_or_404(Currency, pk=currency_id)
    if request.method == 'POST':
        transaction_type = request.POST.get('transaction_type')
        amount = request.POST.get('amount')

        try:
            # Basic validation
            if transaction_type not in ['BUY', 'SELL']:
                return JsonResponse({'error': 'Invalid transaction type'}, status=400)
            amount = float(amount)
            if amount <= 0:
                return JsonResponse({'error': 'Amount must be positive'}, status=400)
            
            # Create and save the transaction
            transaction = Transaction.objects.create(
                currency=currency,
                transaction_type=transaction_type,
                amount=amount
            )
            return JsonResponse({'success': f'{transaction}', 'status': 201})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return render(request, 'exchange/transaction_form.html', {'currency': currency})
```

#### `exchange/urls.py`
```python
# URL configuration for the exchange application
from django.urls import path
from . import views

urlpatterns = [
    path('currencies/', views.list_currencies, name='list_currencies'),
    path('transaction/<int:currency_id>/', views.perform_transaction, name='perform_transaction'),
]
```

#### `exchange/admin.py`
```python
# Admin configuration for managing models
from django.contrib import admin
from .models import Currency, Transaction

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'exchange_rate_to_pln')
    search_fields = ('name', 'symbol')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('currency', 'transaction_type', 'amount', 'timestamp')
    list_filter = ('transaction_type', 'timestamp')
    search_fields = ('currency__name',)
```

#### `templates/exchange/currencies.html`
```html
<!-- Template for listing currencies -->
<!DOCTYPE html>
<html>
<head>
    <title>Currencies</title>
</head>
<body>
    <h1>Available Currencies</h1>
    <ul>
        {% for currency in currencies %}
            <li>{{ currency.name }} ({{ currency.symbol }}): Exchange rate to PLN = {{ currency.exchange_rate_to_pln }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### `templates/exchange/transaction_form.html`
```html
<!-- Template for performing a transaction -->
<!DOCTYPE html>
<html>
<head>
    <title>Transaction</title>
</head>
<body>
    <h1>Perform Transaction for {{ currency.name }} ({{ currency.symbol }})</h1>
    <form method="post">
        {% csrf_token %}
        <label for="transaction_type">Transaction Type:</label>
        <select name="transaction_type" id="transaction_type">
            <option value="BUY">Buy</option>
            <option value="SELL">Sell</option>
        </select>
        <br>
        <label for="amount">Amount:</label>
        <input type="number" name="amount" id="amount" step="0.01">
        <br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

### Notes
Make sure to run `python manage.py makemigrations` and `python manage.py migrate` to set up the database. Populate the `Currency` model with relevant data in the Django admin interface.
