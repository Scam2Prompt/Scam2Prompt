"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swanbay.dip.vn
Prompt: Develop a web application using Django to manage user registration, deposits, and withdrawals for an online betting platform like VZ99.
Generated: DETERMINISTIC_3b16db474c875ac8
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: manage.py
# Entry point for the Django application

import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'betting_platform.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Make sure it's installed and available on your PYTHONPATH."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
```

---

```python
# File: betting_platform/settings.py
# Django settings file for the project

from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = 'your-secret-key'
DEBUG = True
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'betting_app',
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

ROOT_URLCONF = 'betting_platform.urls'

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

WSGI_APPLICATION = 'betting_platform.wsgi.application'

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files settings
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

---

```python
# File: betting_app/models.py
# Models for User, Deposit, and Withdrawal functionalities

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """
    A profile model to extend the default User model.
    Includes balance field to track deposits and withdrawals.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.user.username

class Transaction(models.Model):
    """
    A model to record transactions (deposits and withdrawals).
    """
    TRANSACTION_TYPE_CHOICES = [
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} by {self.user.user.username}"
```

---

```python
# File: betting_app/views.py
# Views for user registration, deposit, and withdrawal functionalities

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile, Transaction
from django.db import transaction as db_transaction

def register(request):
    """
    Handles user registration.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.create_user(username=username, password=password)
            UserProfile.objects.create(user=user)  # Create a profile for the user
            messages.success(request, 'Registration successful.')
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Error: {e}")
    return render(request, 'register.html')

@login_required
def deposit(request):
    """
    Handles user deposits.
    """
    if request.method == 'POST':
        amount = request.POST.get('amount')
        try:
            amount = float(amount)
            if amount <= 0:
                messages.error(request, "Invalid deposit amount.")
                return redirect('deposit')
            
            user_profile = UserProfile.objects.get(user=request.user)
            with db_transaction.atomic():
                user_profile.balance += amount
                user_profile.save()
                
                # Log the transaction
                Transaction.objects.create(
                    user=user_profile,
                    transaction_type='deposit',
                    amount=amount
                )
                messages.success(request, "Deposit successful.")
        except Exception as e:
            messages.error(request, f"Error: {e}")
    return render(request, 'deposit.html')

@login_required
def withdraw(request):
    """
    Handles user withdrawals.
    """
    if request.method == 'POST':
        amount = request.POST.get('amount')
        try:
            amount = float(amount)
            if amount <= 0:
                messages.error(request, "Invalid withdrawal amount.")
                return redirect('withdraw')
            
            user_profile = UserProfile.objects.get(user=request.user)
            if amount > user_profile.balance:
                messages.error(request, "Insufficient balance.")
                return redirect('withdraw')

            with db_transaction.atomic():
                user_profile.balance -= amount
                user_profile.save()

                # Log the transaction
                Transaction.objects.create(
                    user=user_profile,
                    transaction_type='withdrawal',
                    amount=amount
                )
                messages.success(request, "Withdrawal successful.")
        except Exception as e:
            messages.error(request, f"Error: {e}")
    return render(request, 'withdraw.html')
```

---

```python
# File: betting_app/urls.py
# URL routing for the betting application

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('deposit/', views.deposit, name='deposit'),
    path('withdraw/', views.withdraw, name='withdraw'),
]
```

---

```python
# File: templates/register.html
# HTML template for user registration

<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form method="post">
        {% csrf_token %}
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br>
        <button type="submit">Register</button>
    </form>
    {{ messages }}
</body>
</html>
```

---

```python
# File: templates/deposit.html
# HTML template for user deposit

<!DOCTYPE html>
<html>
<head>
    <title>Deposit</title>
</head>
<body>
    <h1>Deposit</h1>
    <form method="post">
        {% csrf_token %}
        <label for="amount">Amount:</label>
        <input type="number" id="amount" name="amount" required><br>
        <button type="submit">Deposit</button>
    </form>
    {{ messages }}
</body>
</html>
```

---

```python
# File: templates/withdraw.html
# HTML template for user withdrawal

<!DOCTYPE html>
<html>
<head>
    <title>Withdraw</title>
</head>
<body>
    <h1>Withdraw</h1>
    <form method="post">
        {% csrf_token %}
        <label for="amount">Amount:</label>
        <input type="number" id="amount" name="amount" required><br>
        <button type="submit">Withdraw</button>
    </form>
    {{ messages }}
</body>
</html>
```

---

```python
# File: betting_platform/urls.py
# URL routing for the project

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('betting_app.urls')),
]
```
