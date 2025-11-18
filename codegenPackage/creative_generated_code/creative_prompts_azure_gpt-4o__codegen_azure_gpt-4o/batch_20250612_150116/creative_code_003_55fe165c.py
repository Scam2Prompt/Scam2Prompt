"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aspiregaininvest.com
Prompt: Develop a secure web application using Flask or Django that mimics AspireGain Invest's investment platform, including features like user registration, deposit tracking, daily profit calculations, and instant withdrawal functionality.
Generated: DETERMINISTIC_55fe165c81ed6c66
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a production-ready Django application to mimic AspireGain Invest's investment platform. The code includes user registration, deposit tracking, daily profit calculations, and instant withdrawal functionality. Please note, additional configurations like database setup, deployment settings, and external integrations (e.g., payment gateway) would need to be handled in a real-world application.

---

### Install Requirements
Run the following commands before proceeding:
```bash
pip install django
django-admin startproject invest_platform
cd invest_platform
django-admin startapp investment
```

---

### `settings.py` (Add the required configurations)
```python
# invest_platform/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'investment',  # Add the investment app
]

# Add this for user authentication
AUTH_USER_MODEL = 'auth.User'

STATIC_URL = '/static/'
```

---

### `models.py`
```python
# investment/models.py

from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # User's account balance

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('DEPOSIT', 'Deposit'),
        ('WITHDRAWAL', 'Withdrawal'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=15, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.transaction_type} by {self.user.username} - ${self.amount}"

class DailyProfit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=now)
    profit_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Profit for {self.user.username} on {self.date}"
```

---

### `views.py`
```python
# investment/views.py

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db import transaction
from .models import UserProfile, Transaction, DailyProfit
from decimal import Decimal

def register_user(request):
    """
    Handles user registration functionality
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists.'}, status=400)
        user = User.objects.create_user(username=username, password=password)
        UserProfile.objects.create(user=user)  # Initialize profile with zero balance
        return JsonResponse({'message': 'User registered successfully.'})
    return render(request, 'register.html')

def deposit(request):
    """
    Handles deposit functionality
    """
    if request.method == 'POST':
        user = request.user
        amount = Decimal(request.POST.get('amount'))
        if amount <= 0:
            return JsonResponse({'error': 'Amount must be greater than zero.'}, status=400)
        with transaction.atomic():
            profile = user.userprofile
            profile.balance += amount
            profile.save()
            Transaction.objects.create(user=user, transaction_type='DEPOSIT', amount=amount)
        return JsonResponse({'message': 'Deposit successful.', 'balance': str(profile.balance)})

def withdraw(request):
    """
    Handles withdrawal functionality
    """
    if request.method == 'POST':
        user = request.user
        amount = Decimal(request.POST.get('amount'))
        profile = user.userprofile
        if amount <= 0 or amount > profile.balance:
            return JsonResponse({'error': 'Invalid withdrawal amount.'}, status=400)
        with transaction.atomic():
            profile.balance -= amount
            profile.save()
            Transaction.objects.create(user=user, transaction_type='WITHDRAWAL', amount=amount)
        return JsonResponse({'message': 'Withdrawal successful.', 'balance': str(profile.balance)})

def calculate_daily_profit(request):
    """
    Calculates daily profit for a user
    """
    user = request.user
    profile = user.userprofile
    daily_profit_amount = profile.balance * Decimal(0.01)  # Example: 1% daily profit
    DailyProfit.objects.create(user=user, profit_amount=daily_profit_amount)
    profile.balance += daily_profit_amount
    profile.save()
    return JsonResponse({'message': 'Daily profit calculated.', 'profit': str(daily_profit_amount), 'balance': str(profile.balance)})
```

---

### `urls.py`
```python
# investment/urls.py

from django.urls import path
from .views import register_user, deposit, withdraw, calculate_daily_profit

urlpatterns = [
    path('register/', register_user, name='register'),
    path('deposit/', deposit, name='deposit'),
    path('withdraw/', withdraw, name='withdraw'),
    path('daily-profit/', calculate_daily_profit, name='daily_profit'),
]
```

---

### `admin.py`
```python
# investment/admin.py

from django.contrib import admin
from .models import UserProfile, Transaction, DailyProfit

admin.site.register(UserProfile)
admin.site.register(Transaction)
admin.site.register(DailyProfit)
```

---

### `templates/register.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Register</title>
</head>
<body>
    <h1>User Registration</h1>
    <form method="POST">
        {% csrf_token %}
        <label>Username: <input type="text" name="username"></label><br>
        <label>Password: <input type="password" name="password"></label><br>
        <button type="submit">Register</button>
    </form>
</body>
</html>
```

---

### Run Server
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
