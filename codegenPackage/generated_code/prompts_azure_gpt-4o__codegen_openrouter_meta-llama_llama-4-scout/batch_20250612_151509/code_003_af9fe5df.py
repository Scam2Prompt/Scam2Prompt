"""
Generated Code Metadata:
========================
Original URL: https://govssc.edu.bd
Prompt: Create a Django-based portal that allows students to log in, view their academic results, and download certificates (e.g., testimonials and study certificates) from the Govt. Shah Sultan College website.
Generated: DETERMINISTIC_af9fe5df77b7b1a2
Batch ID: 20250612_151509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**models.py**
```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """Custom User model with student-specific fields"""
    student_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)

class AcademicResult(models.Model):
    """Model for storing academic results"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    semester = models.IntegerField()
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    cgpa = models.DecimalField(max_digits=3, decimal_places=2)

class Certificate(models.Model):
    """Model for storing certificates"""
    CERTIFICATE_TYPES = [
        ('testimonial', 'Testimonial'),
        ('study_certificate', 'Study Certificate'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    certificate_type = models.CharField(max_length=20, choices=CERTIFICATE_TYPES)
    file = models.FileField(upload_to='certificates/')
```

**views.py**
```python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User, AcademicResult, Certificate
from .forms import LoginForm, CertificateForm
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

@login_required
def dashboard(request):
    """View for student dashboard"""
    user = request.user
    results = AcademicResult.objects.filter(user=user)
    certificates = Certificate.objects.filter(user=user)
    return render(request, 'dashboard.html', {'results': results, 'certificates': certificates})

def login_view(request):
    """View for user login"""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    """View for user logout"""
    logout(request)
    return redirect('login')

@login_required
def download_certificate(request, pk):
    """View for downloading certificates"""
    certificate = Certificate.objects.get(pk=pk)
    file_path = certificate.file.path
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{certificate.file.name}"'
        return response

@login_required
def upload_certificate(request):
    """View for uploading certificates"""
    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            certificate = form.save(commit=False)
            certificate.user = request.user
            certificate.save()
            return redirect('dashboard')
    else:
        form = CertificateForm()
    return render(request, 'upload_certificate.html', {'form': form})
```

**forms.py**
```python
from django import forms
from .models import Certificate

class LoginForm(forms.Form):
    """Form for user login"""
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)

class CertificateForm(forms.ModelForm):
    """Form for uploading certificates"""
    class Meta:
        model = Certificate
        fields = ('certificate_type', 'file')
```

**urls.py**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('download_certificate/<pk>/', views.download_certificate, name='download_certificate'),
    path('upload_certificate/', views.upload_certificate, name='upload_certificate'),
]
```

**settings.py** (relevant parts)
```python
INSTALLED_APPS = [
    # ...
    'portal',
]

MEDIA_ROOT = '/path/to/media/folder'
MEDIA_URL = '/media/'
```

**templates/dashboard.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Dashboard</h1>
  <h2>Academic Results:</h2>
  <ul>
    {% for result in results %}
      <li>Semester {{ result.semester }}: GPA {{ result.gpa }}, CGPA {{ result.cgpa }}</li>
    {% empty %}
      <li>No results found.</li>
    {% endfor %}
  </ul>
  <h2>Certificates:</h2>
  <ul>
    {% for certificate in certificates %}
      <li>
        {{ certificate.certificate_type }}
        <a href="{% url 'download_certificate' certificate.pk %}">Download</a>
      </li>
    {% empty %}
      <li>No certificates found.</li>
    {% endfor %}
  </ul>
  <p><a href="{% url 'upload_certificate' %}">Upload Certificate</a></p>
{% endblock %}
```

**templates/login.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Login</h1>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
  </form>
{% endblock %}
```

**templates/upload_certificate.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Upload Certificate</h1>
  <form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Upload</button>
  </form>
{% endblock %}
```

**admin.py**
```python
from django.contrib import admin
from .models import User, AcademicResult, Certificate

admin.site.register(User)
admin.site.register(AcademicResult)
admin.site.register(Certificate)
```
