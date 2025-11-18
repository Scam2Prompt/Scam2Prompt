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
# Django web application for PRGMEA membership

# Step 1: Create a new Django project and app.
# Commands:
# django-admin startproject prgmea
# python manage.py startapp membership

# Below is the code structured for the application.

# prgmea/settings.py - Update the settings file.
INSTALLED_APPS = [
    ...
    'membership',  # Add the membership app
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    ...
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# Define static files location
STATIC_URL = '/static/'


# membership/models.py - Define the database models.
from django.contrib.auth.models import User
from django.db import models

class Manufacturer(models.Model):
    """
    Model to represent apparel manufacturers.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    address = models.TextField()
    membership_date = models.DateField(auto_now_add=True)
    membership_active = models.BooleanField(default=True)

    def __str__(self):
        return self.company_name


# membership/forms.py - Define forms for user input.
from django import forms
from django.contrib.auth.models import User
from .models import Manufacturer

class UserSignupForm(forms.ModelForm):
    """
    Form for user account signup.
    """
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ManufacturerForm(forms.ModelForm):
    """
    Form for manufacturer details.
    """
    class Meta:
        model = Manufacturer
        fields = ['company_name', 'contact_number', 'address']


# membership/views.py - Implement the views.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserSignupForm, ManufacturerForm
from .models import Manufacturer

def signup(request):
    """
    Allow manufacturers to sign up for PRGMEA membership.
    """
    if request.method == 'POST':
        user_form = UserSignupForm(request.POST)
        manufacturer_form = ManufacturerForm(request.POST)
        if user_form.is_valid() and manufacturer_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            manufacturer = manufacturer_form.save(commit=False)
            manufacturer.user = user
            manufacturer.save()
            messages.success(request, "Signup successful! You can now log in.")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        user_form = UserSignupForm()
        manufacturer_form = ManufacturerForm()
    return render(request, 'membership/signup.html', {
        'user_form': user_form,
        'manufacturer_form': manufacturer_form
    })

@login_required
def dashboard(request):
    """
    Dashboard for manufacturers to manage their accounts.
    """
    manufacturer = Manufacturer.objects.get(user=request.user)
    return render(request, 'membership/dashboard.html', {'manufacturer': manufacturer})


# membership/urls.py - Define URLs for the app.
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
]


# prgmea/urls.py - Include the URLs in the main project.
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('membership/', include('membership.urls')),
]


# membership/templates/membership/signup.html - Signup page HTML.
<!DOCTYPE html>
<html lang="en">
<head>
    <title>PRGMEA Membership Signup</title>
</head>
<body>
    <h1>Signup for PRGMEA Membership</h1>
    <form method="post">
        {% csrf_token %}
        {{ user_form.as_p }}
        {{ manufacturer_form.as_p }}
        <button type="submit">Sign Up</button>
    </form>
</body>
</html>


# membership/templates/membership/dashboard.html - Dashboard page HTML.
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Dashboard</title>
</head>
<body>
    <h1>Welcome, {{ manufacturer.company_name }}</h1>
    <p>Membership Status: {{ "Active" if manufacturer.membership_active else "Inactive" }}</p>
    <p>Contact Number: {{ manufacturer.contact_number }}</p>
    <p>Address: {{ manufacturer.address }}</p>
    <p>Membership Date: {{ manufacturer.membership_date }}</p>
</body>
</html>

# For database migrations after defining the models:
# Commands:
# python manage.py makemigrations
# python manage.py migrate

# For running the server:
# python manage.py runserver
```
