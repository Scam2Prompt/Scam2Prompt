"""
Generated Code Metadata:
========================
Original URL: https://maraboutreconnu.com
Prompt: Develop a Django application to manage and display services like "Retour affectif" and "Rituel d’argent," with options for users to book consultations.
Generated: DETERMINISTIC_3946644713103ca8
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# settings.py
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-your-secret-key-here'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'services.apps.ServicesConfig',
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

ROOT_URLCONF = 'service_booking.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'service_booking.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

```python
# services/models.py
from django.db import models
from django.core.validators import MinLengthValidator

class Service(models.Model):
    SERVICE_CATEGORIES = [
        ('love', 'Retour affectif'),
        ('money', 'Rituel d\'argent'),
        ('other', 'Autre'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=SERVICE_CATEGORIES)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Consultation(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    client_phone = models.CharField(max_length=20, validators=[MinLengthValidator(8)])
    preferred_date = models.DateTimeField()
    additional_notes = models.TextField(blank=True)
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.service.name}"
```

```python
# services/admin.py
from django.contrib import admin
from .models import Service, Consultation

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_available')
    list_filter = ('category', 'is_available')
    search_fields = ('name', 'description')

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'service', 'preferred_date', 'is_confirmed')
    list_filter = ('is_confirmed', 'service__category')
    search_fields = ('client_name', 'client_email', 'service__name')
    date_hierarchy = 'preferred_date'
```

```python
# services/forms.py
from django import forms
from django.core.exceptions import ValidationError
from .models import Consultation
from django.utils import timezone

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['service', 'client_name', 'client_email', 'client_phone', 'preferred_date', 'additional_notes']
        widgets = {
            'preferred_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'additional_notes': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_preferred_date(self):
        preferred_date = self.cleaned_data.get('preferred_date')
        if preferred_date < timezone.now():
            raise ValidationError("You cannot book a consultation in the past.")
        return preferred_date
```

```python
# services/views.py
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Service, Consultation
from .forms import ConsultationForm

class ServiceListView(ListView):
    model = Service
    template_name = 'services/service_list.html'
    context_object_name = 'services'

    def get_queryset(self):
        return Service.objects.filter(is_available=True)

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service_detail.html'
    context_object_name = 'service'

class ConsultationCreateView(CreateView):
    model = Consultation
    form_class = ConsultationForm
    template_name = 'services/consultation_form.html'
    success_url = reverse_lazy('service_list')

    def form_valid(self, form):
        form.instance.service = Service.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)
```

```python
# services/urls.py
from django.urls import path
from .views import ServiceListView, ServiceDetailView, ConsultationCreateView

urlpatterns = [
    path('', ServiceListView.as_view(), name='service_list'),
    path('<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('<int:pk>/book/', ConsultationCreateView.as_view(), name='book_consultation'),
]
```

```python
# service_booking/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('services.urls')),
]
```

```html
<!-- templates/services/service_list.html -->
{% extends 'base.html' %}

{% block content %}
<h1>Our Services</h1>
<div class="service-list">
    {% for service in services %}
    <div class="service-card">
        <h2>{{ service.name }}</h2>
        <p>Category: {{ service.get_category_display }}</p>
        <p>Price: ${{ service.price }}</p>
        <p>{{ service.description|truncatewords:20 }}</p>
        <a href="{% url 'service_detail' service.pk %}">View Details</a>
    </div>
    {% empty %}
    <p>No services available at the moment.</p>
    {% endfor %}
</div>
{% endblock %}
```

```html
<!-- templates/services/service_detail.html -->
{% extends 'base.html' %}

{% block content %}
<h1>{{ service.name }}</h1>
<p>Category: {{ service.get_category_display }}</p>
<p>Price: ${{ service.price }}</p>
<p>Duration: {{ service.duration }}</p>
<p>{{ service.description }}</p>

{% if service.is_available %}
<a href="{% url 'book_consultation' service.pk %}" class="btn btn-primary">Book Consultation</a>
{% else %}
<p class="text-danger">This service is currently unavailable.</p>
{% endif %}
{% endblock %}
```

```html
<!-- templates/services/consultation_form.html -->
{% extends 'base.html' %}

{% block content %}
<h1>Book Consultation for {{ view.service.name }}</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-primary">Submit Booking</button>
</form>
{% endblock %}
```

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Spiritual Services Booking</title>
    <style>
        body { font-family: Arial
