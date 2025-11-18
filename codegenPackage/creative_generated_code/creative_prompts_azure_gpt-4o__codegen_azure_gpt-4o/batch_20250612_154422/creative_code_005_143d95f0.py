"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jieyasoft.com
Prompt: Suggest a library or framework for creating a "混合制直销软件" (hybrid direct selling system) that combines features of level-based and matrix systems, as described by JieyaSoft.
Generated: DETERMINISTIC_143d95f098365408
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is an example implementation in Python using the Django framework, which is suitable for creating hybrid systems combining level-based and matrix features. This code is structured, clean, and adheres to best practices.

```python
# Install Django framework before running this code:
# pip install django

# models.py
from django.db import models

class User(models.Model):
    """
    Represents a user in the direct selling system.
    """
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    sponsor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='sponsored_users')
    level = models.IntegerField(default=1)  # Level-based hierarchy
    matrix_position = models.IntegerField(default=0)  # Matrix position within the system

    def __str__(self):
        return f"{self.name} (Level: {self.level}, Matrix Position: {self.matrix_position})"


class Transaction(models.Model):
    """
    Represents a transaction in the system (e.g., a sale).
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction by {self.user.name}, Amount: {self.amount}, Date: {self.timestamp}"


class Commission(models.Model):
    """
    Represents commission earned by users based on level and matrix rules.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    level_commission = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    matrix_commission = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commission for {self.user.name}, Level: {self.level_commission}, Matrix: {self.matrix_commission}"


# views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import User, Transaction, Commission
from decimal import Decimal

def process_transaction(request, user_id, amount):
    """
    Processes a transaction and calculates commissions.
    """
    try:
        # Validate input and find the user
        user = get_object_or_404(User, id=user_id)
        amount = Decimal(amount)

        # Create a transaction record
        transaction = Transaction.objects.create(user=user, amount=amount)

        # Calculate level-based and matrix-based commissions
        level_commission = amount * Decimal(0.05)  # Example: 5% commission
        matrix_commission = amount * Decimal(0.02)  # Example: 2% matrix commission

        # Save commission record
        Commission.objects.create(user=user, transaction=transaction,
                                  level_commission=level_commission,
                                  matrix_commission=matrix_commission)

        return JsonResponse({'status': 'success', 'message': 'Transaction processed successfully.'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})


# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('transaction/<int:user_id>/<str:amount>/', views.process_transaction, name='process_transaction'),
]


# settings.py (Add these settings if not already present)
INSTALLED_APPS = [
    # Other apps
    'your_app_name',  # Replace with the actual app name
]

# Run commands to apply migrations:
# python manage.py makemigrations
# python manage.py migrate

# Run the server and test the endpoints:
# python manage.py runserver
```

This implementation uses Django's ORM to define models for the hybrid selling system and provides an example endpoint for processing transactions. You can extend this code as needed for additional features or system-specific rules.
