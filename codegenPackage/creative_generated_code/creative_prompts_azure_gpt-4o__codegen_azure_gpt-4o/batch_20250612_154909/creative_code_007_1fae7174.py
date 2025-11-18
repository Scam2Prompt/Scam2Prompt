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
# Django Application: Login form with "show password" feature and session management
# File: views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
    """
    Handles user login with session management.
    Includes form validation and authentication.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Login successful
            login(request, user)
            return redirect('dashboard')  # Redirect to a dashboard or home page
        else:
            # Invalid credentials
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')


@login_required
def dashboard_view(request):
    """
    Protected view that requires login. Displays a dashboard or main content page.
    """
    return render(request, 'dashboard.html')


def logout_view(request):
    """
    Handles user logout and session termination.
    """
    logout(request)
    return redirect('login')  # Redirect to login page after logout


# File: urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
]


# File: templates/login.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <style>
        /* Add basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f4;
        }
        .login-container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 300px;
        }
        .login-container h1 {
            text-align: center;
            margin-bottom: 20px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
            margin-bottom: 5px;
        }
        .form-group input {
            width: 100%;
            padding: 8px;
            box-sizing: border-box;
        }
        .form-group button {
            width: 100%;
            padding: 10px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .form-group button:hover {
            background-color: #0056b3;
        }
        .toggle-password {
            cursor: pointer;
            font-size: 0.9em;
            color: #007bff;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h1>Login</h1>
        {% if messages %}
            <div>
                {% for message in messages %}
                    <p style="color: red;">{{ message }}</p>
                {% endfor %}
            </div>
        {% endif %}
        <form method="post">
            {% csrf_token %}
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required>
                <span class="toggle-password" onclick="togglePassword()">Show Password</span>
            </div>
            <div class="form-group">
                <button type="submit">Login</button>
            </div>
        </form>
    </div>

    <script>
        /**
         * Toggles the visibility of the password field.
         */
        function togglePassword() {
            const passwordField = document.getElementById('password');
            const toggleText = document.querySelector('.toggle-password');

            if (passwordField.type === 'password') {
                passwordField.type = 'text';
                toggleText.textContent = 'Hide Password';
            } else {
                passwordField.type = 'password';
                toggleText.textContent = 'Show Password';
            }
        }
    </script>
</body>
</html>


# File: settings.py (Relevant configuration)

# Ensure the login and logout redirect URLs are set correctly
LOGIN_URL = '/login/'
LOGOUT_REDIRECT_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'

# File: models.py (No models required for this example)

# This application does not need additional models since it uses Django's built-in User model.

# File: admin.py (Optional)

# This application does not need custom admin functionality, but you can register models if necessary.
```
