"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getinge-torin.com
Prompt: Generate a Django application with a login form that includes a "show password" feature and session management for persistent login, as described in the Torin portal.
Generated: DETERMINISTIC_1fae71746e151f18
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Create a Django project and app
# Run the following commands in your terminal
# django-admin startproject torin_portal
# cd torin_portal
# python manage.py startapp accounts

# settings.py
# Add 'accounts' to the INSTALLED_APPS list
INSTALLED_APPS = [
    ...
    'accounts',
]

# Add Session middleware
MIDDLEWARE = [
    ...
    'django.contrib.sessions.middleware.SessionMiddleware',
]

# Add authentication backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# urls.py in torin_portal
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Include accounts URLs
]

# models.py in accounts (for potential future use)
from django.contrib.auth.models import User
from django.db import models

# forms.py in accounts
from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        # Authenticate user
        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Invalid username or password")

# views.py in accounts
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import LoginForm

def login_view(request):
    """Handle user login."""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a home view after login
    else:
        form = LoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    """Handle user logout."""
    logout(request)
    return redirect('login')  # Redirect to login page after logout

# urls.py in accounts
from django.urls import path
from .views import login_view, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]

# Create a template for the login form at accounts/templates/accounts/login.html
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
    <script>
        // Toggle password visibility
        function togglePassword() {
            const passwordField = document.getElementById("id_password");
            const toggleButton = document.getElementById("togglePassword");
            if (passwordField.type === "password") {
                passwordField.type = "text";
                toggleButton.innerText = "Hide Password";
            } else {
                passwordField.type = "password";
                toggleButton.innerText = "Show Password";
            }
        }
    </script>
</head>
<body>
    <h2>Login</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="button" id="togglePassword" onclick="togglePassword()">Show Password</button>
        <button type="submit">Login</button>
    </form>
</body>
</html>
"""

# Run migrations and create a superuser to access admin
# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser

# Finally, run the server
# python manage.py runserver
```
