"""
Generated Code Metadata:
========================
Original URL: https://conext.info
Prompt: How to implement a notification system in a web application like MapOS that informs users of incorrect login attempts?
Generated: DETERMINISTIC_9ed889a187f91a80
Batch ID: 20250622_205206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Notification System Implementation**
=====================================

### **models.py**
```python
from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    """Represents a notification sent to a user."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class LoginAttempt(models.Model):
    """Represents a login attempt."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=255)
    is_successful = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
```

### **views.py**
```python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import LoginAttempt, Notification
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                # Create a login attempt
                ip_address = request.META.get('REMOTE_ADDR')
                user_agent = request.META.get('HTTP_USER_AGENT')
                LoginAttempt.objects.create(user=None, ip_address=ip_address, user_agent=user_agent, is_successful=False)
                # Send notification to user
                try:
                    user = User.objects.get(username=username)
                    Notification.objects.create(user=user, message='Incorrect login attempt')
                except User.DoesNotExist:
                    pass
                return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
```

### **tasks.py**
```python
from celery import shared_task
from .models import Notification
from django.core.mail import send_mail

@shared_task
def send_notification_email(notification_id):
    try:
        notification = Notification.objects.get(id=notification_id)
        subject = 'Notification: Incorrect Login Attempt'
        message = notification.message
        from_email = 'your_email@example.com'
        to_email = notification.user.email
        send_mail(subject, message, from_email, [to_email])
    except Notification.DoesNotExist:
        pass
```

### **signals.py**
```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notification
from .tasks import send_notification_email

@receiver(post_save, sender=Notification)
def send_notification_email_task(sender, instance, created, **kwargs):
    if created:
        send_notification_email.delay(instance.id)
```

### **forms.py**
```python
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
```

### **settings.py**
```python
CELERY_BROKER_URL = 'your_broker_url'
CELERY_RESULT_BACKEND = 'your_result_backend'

EMAIL_HOST = 'your_email_host'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email_user'
EMAIL_HOST_PASSWORD = 'your_email_password'
```

### **urls.py**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
]
```
