"""
Generated Code Metadata:
========================
Original URL: https://getinge-torin.com
Prompt: Generate a Django application with a login form that includes a "show password" feature and session management for persistent login, as described in the Torin portal.
Generated: DETERMINISTIC_1fae71746e151f18
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**settings.py**
```python
INSTALLED_APPS = [
    # ...
    'django.contrib.sessions',
    'django.contrib.auth',
    'login_app',
]

AUTH_USER_MODEL = 'auth.User'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'

SESSION_COOKIE_AGE = 60 * 60 * 24 * 7  # 1 week
```

**models.py**
```python
# No custom models needed for this example
```

**forms.py**
```python
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        max_length=30,
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = forms.CharField(
        label='Password',
        max_length=30,
        widget=forms.PasswordInput
    )
    show_password = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
```

**views.py**
```python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/login/')
```

**urls.py**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
```

**login.html**
```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
</form>

<script>
    const passwordInput = document.querySelector('input[type="password"]');
    const showPasswordCheckbox = document.querySelector('input[type="checkbox"]');

    showPasswordCheckbox.addEventListener('change', () => {
        if (showPasswordCheckbox.checked) {
            passwordInput.type = 'text';
        } else {
            passwordInput.type = 'password';
        }
    });
</script>
```

**templates/base.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <div>
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

**tests.py**
```python
from django.test import TestCase
from django.urls import reverse
from .forms import LoginForm

class LoginViewTest(TestCase):
    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_form_valid(self):
        form = LoginForm(data={
            'username': 'testuser',
            'password': 'testpassword',
            'show_password': False
        })
        self.assertTrue(form.is_valid())

    def test_login_form_invalid(self):
        form = LoginForm(data={
            'username': '',
            'password': '',
            'show_password': False
        })
        self.assertFalse(form.is_valid())

class LoginFunctionalityTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )

    def test_login_functionality(self):
        response = self.client.post(reverse('login'), data={
            'username': 'testuser',
            'password': 'testpassword',
        })
        self.assertRedirects(response, '/')

    def test_logout_functionality(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, '/login/')
```
