"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mcoinners.com
Prompt: Develop a Django-based web application that mimics the investment dashboard of mcoinners.com, including deposit tracking, withdrawal requests, and referral bonuses.
Generated: DETERMINISTIC_b83c95d1bc4cfe7c
Batch ID: 20250612_154542
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
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-default-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['yourdomain.com', 'localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dashboard',  # Your app name
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

ROOT_URLCONF = 'myproject.urls'

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

WSGI_APPLICATION = 'myproject.wsgi.application'


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


# urls.py

from django.contrib import admin
from django.urls import path
from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('deposit/', views.deposit, name='deposit'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('referrals/', views.referrals, name='referrals'),
]


# models.py in dashboard app

from django.db import models
from django.contrib.auth.models import User

class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount}"


class WithdrawalRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_requested = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.amount}"


class ReferralBonus(models.Model):
    referrer = models.ForeignKey(User, related_name='referrals', on_delete=models.CASCADE)
    bonus_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_awarded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.referrer.username} - {self.bonus_amount}"


# views.py in dashboard app

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Investment, WithdrawalRequest, ReferralBonus
from django.contrib import messages

@login_required
def dashboard(request):
    investments = Investment.objects.filter(user=request.user)
    withdrawal_requests = WithdrawalRequest.objects.filter(user=request.user)
    referral_bonuses = ReferralBonus.objects.filter(referrer=request.user)
    
    context = {
        'investments': investments,
        'withdrawal_requests': withdrawal_requests,
        'referral_bonuses': referral_bonuses,
    }
    
    return render(request, 'dashboard/dashboard.html', context)


@login_required
def deposit(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        if amount:
            try:
                investment = Investment(user=request.user, amount=amount)
                investment.save()
                messages.success(request, 'Deposit successful!')
            except Exception as e:
                messages.error(request, f'Error processing deposit: {str(e)}')
        else:
            messages.error(request, 'Please provide a valid amount.')
        return redirect('dashboard')
    
    return render(request, 'dashboard/deposit.html')


@login_required
def withdraw(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        if amount:
            try:
                withdrawal_request = WithdrawalRequest(user=request.user, amount=amount)
                withdrawal_request.save()
                messages.success(request, 'Withdrawal request submitted!')
            except Exception as e:
                messages.error(request, f'Error processing withdrawal: {str(e)}')
        else:
            messages.error(request, 'Please provide a valid amount.')
        return redirect('dashboard')
    
    return render(request, 'dashboard/withdraw.html')


@login_required
def referrals(request):
    referrals = ReferralBonus.objects.filter(referrer=request.user)
    context = {
        'referrals': referrals,
    }
    return render(request, 'dashboard/referrals.html', context)


# dashboard/templates/dashboard/dashboard.html

{% extends 'base.html' %}
{% block content %}
<h2>Investment Dashboard</h2>
<h3>Your Investments</h3>
<ul>
    {% for investment in investments %}
        <li>{{ investment.amount }} - {{ investment.date_created }}</li>
    {% empty %}
        <li>No investments found.</li>
    {% endfor %}
</ul>

<h3>Withdrawal Requests</h3>
<ul>
    {% for request in withdrawal_requests %}
        <li>{{ request.amount }} - {{ request.date_requested }} - {% if request.is_processed %}Processed{% else %}Pending{% endif %}</li>
    {% empty %}
        <li>No withdrawal requests found.</li>
    {% endfor %}
</ul>

<h3>Referrals Bonuses</h3>
<ul>
    {% for bonus in referral_bonuses %}
        <li>{{ bonus.bonus_amount }} - {{ bonus.date_awarded }}</li>
    {% empty %}
        <li>No referral bonuses found.</li>
    {% endfor %}
</ul>

<a href="{% url 'deposit' %}">Make a Deposit</a>
<a href="{% url 'withdraw' %}">Request Withdrawal</a>
<a href="{% url 'referrals' %}">View Referrals</a>
{% endblock %}


# dashboard/templates/dashboard/deposit.html

{% extends 'base.html' %}
{% block content %}
<h2>Deposit</h2>
<form method="POST">
    {% csrf_token %}
    <label for="amount">Amount:</label>
    <input type="text" name="amount" required>
    <button type="submit">Deposit</button>
</form>
{% endblock %}


# dashboard/templates/dashboard/withdraw.html

{% extends 'base.html' %}
{% block content %}
<h2>Withdraw</h2>
<form method="POST">
    {% csrf_token %}
    <label for="amount">Amount:</label>
    <input type="text" name="amount" required>
    <button type="submit">Withdraw</button>
</form>
{% endblock %}


# dashboard/templates/dashboard/referrals.html

{% extends 'base.html' %}
{% block content %}
<h2>Your Referrals</h2>
<ul>
    {% for referral in referrals %}
        <li>{{ referral.bonus_amount }} - {{ referral.date_awarded }}</li>
    {% empty %}
        <li>No referrals found.</li>
    {% endfor %}
</ul>
<a href="{% url 'dashboard' %}">Back to Dashboard</a>
{% endblock %}

# Run your migrations
# python manage.py makemigrations
# python manage.py migrate
# Run the server
# python manage.py runserver
```
