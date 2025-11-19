"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hope-exchange.com
Prompt: How can I implement a secure user subscription feature for a web application similar to the one described on Hope Exchange?
Generated: DETERMINISTIC_50e4a8901786fd4b
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Secure User Subscription Feature Implementation for a Web Application
# Language: Python (Django Framework)

from django.contrib.auth.models import User
from django.db import models
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.timezone import now
from django.core.exceptions import ValidationError
import logging

# Initialize logging for error handling and monitoring
logger = logging.getLogger(__name__)

# Subscription model to handle user subscriptions
class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='subscription')
    is_active = models.BooleanField(default=True)  # Subscription status
    start_date = models.DateTimeField(default=now)  # Start date of the subscription
    end_date = models.DateTimeField(null=True, blank=True)  # End date (if applicable)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when subscription is created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when subscription details are updated
    
    def clean(self):
        # Custom validation for subscription dates
        if self.end_date and self.start_date > self.end_date:
            raise ValidationError("End date cannot be earlier than start date.")

    def __str__(self):
        return f"Subscription for {self.user.username} (Active: {self.is_active})"


# Subscription views
@csrf_exempt  # Disable CSRF protection for demonstration purposes (use caution in production)
def create_subscription(request):
    """
    Handles user subscription creation.
    Expects JSON input with 'username' field.
    """
    if request.method == 'POST':
        try:
            # Parse JSON request body
            data = json.loads(request.body)
            username = data.get('username')
            
            # Validate input
            if not username:
                return JsonResponse({'error': 'Username is required.'}, status=400)
            
            # Retrieve user from database
            user = User.objects.filter(username=username).first()
            if not user:
                return JsonResponse({'error': 'User not found.'}, status=404)
            
            # Check if user already has an active subscription
            if hasattr(user, 'subscription'):
                return JsonResponse({'error': 'User already has a subscription.'}, status=400)
            
            # Create subscription
            subscription = Subscription.objects.create(user=user)
            return JsonResponse({'message': 'Subscription created successfully.', 'subscription_id': subscription.id}, status=201)
        
        except json.JSONDecodeError:
            logger.error("Invalid JSON input received.")
            return JsonResponse({'error': 'Invalid JSON input.'}, status=400)
        
        except Exception as e:
            logger.error(f"Unexpected error occurred: {e}")
            return JsonResponse({'error': 'An unexpected error occurred.'}, status=500)
    
    return JsonResponse({'error': 'Invalid HTTP method. Use POST.'}, status=405)


def retrieve_subscription(request, username):
    """
    Retrieves the subscription details for a specific user.
    """
    if request.method == 'GET':
        try:
            # Retrieve user
            user = User.objects.filter(username=username).first()
            if not user:
                return JsonResponse({'error': 'User not found.'}, status=404)
            
            # Check if subscription exists
            if not hasattr(user, 'subscription'):
                return JsonResponse({'error': 'No subscription found for user.'}, status=404)
            
            subscription = user.subscription
            subscription_data = {
                'is_active': subscription.is_active,
                'start_date': subscription.start_date,
                'end_date': subscription.end_date,
                'created_at': subscription.created_at,
                'updated_at': subscription.updated_at,
            }
            
            return JsonResponse({'subscription': subscription_data}, status=200)
        
        except Exception as e:
            logger.error(f"Unexpected error occurred: {e}")
            return JsonResponse({'error': 'An unexpected error occurred.'}, status=500)
    
    return JsonResponse({'error': 'Invalid HTTP method. Use GET.'}, status=405)


def cancel_subscription(request, username):
    """
    Cancels the subscription for a specific user.
    """
    if request.method == 'POST':
        try:
            # Retrieve user
            user = User.objects.filter(username=username).first()
            if not user:
                return JsonResponse({'error': 'User not found.'}, status=404)
            
            # Check if subscription exists
            if not hasattr(user, 'subscription'):
                return JsonResponse({'error': 'No subscription found for user.'}, status=404)
            
            subscription = user.subscription
            subscription.is_active = False
            subscription.end_date = now()  # Mark end date as current time
            subscription.save()
            
            return JsonResponse({'message': 'Subscription canceled successfully.'}, status=200)
        
        except Exception as e:
            logger.error(f"Unexpected error occurred: {e}")
            return JsonResponse({'error': 'An unexpected error occurred.'}, status=500)
    
    return JsonResponse({'error': 'Invalid HTTP method. Use POST.'}, status=405)


# URL configuration (urls.py example)
from django.urls import path

urlpatterns = [
    path('subscription/create/', create_subscription, name='create_subscription'),
    path('subscription/<str:username>/', retrieve_subscription, name='retrieve_subscription'),
    path('subscription/<str:username>/cancel/', cancel_subscription, name='cancel_subscription'),
]

# Note:
# - Ensure that Django is properly configured for production (DEBUG=False, secure settings, etc.).
# - Update CSRF protection logic and authentication as needed for your application.
# - Add unit tests for these views to ensure robustness.
```
