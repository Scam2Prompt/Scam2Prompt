"""
Generated Code Metadata:
========================
Original URL: https://yobugo.com
Prompt: Develop a Django application to manage customer inquiries for Yobugo's products, such as "Coctel de Café Cream Love" and "Crema de lúcuma."
Generated: DETERMINISTIC_2030d44812241e36
Batch ID: 20250612_154021
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
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
    'inquiries.apps.InquiriesConfig',
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

ROOT_URLCONF = 'yobugo_inquiries.urls'

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

WSGI_APPLICATION = 'yobugo_inquiries.wsgi.application'

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
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

```python
# inquiries/models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Inquiry(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inquiries')
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Inquiry #{self.id} - {self.product.name}"

    class Meta:
        verbose_name_plural = "Inquiries"
        ordering = ['-created_at']
```

```python
# inquiries/admin.py
from django.contrib import admin
from .models import Product, Inquiry

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    prepopulated_fields = {'description': ('name',)}

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'customer_name', 'email', 'status', 'created_at')
    list_filter = ('status', 'product', 'created_at')
    search_fields = ('customer_name', 'email', 'message')
    list_editable = ('status',)
    date_hierarchy = 'created_at'
```

```python
# inquiries/forms.py
from django import forms
from .models import Inquiry, Product

class InquiryForm(forms.ModelForm):
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    customer_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    phone = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
    )

    class Meta:
        model = Inquiry
        fields = ['product', 'customer_name', 'email', 'phone', 'message']
```

```python
# inquiries/views.py
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Inquiry, Product
from .forms import InquiryForm

class InquiryListView(ListView):
    model = Inquiry
    template_name = 'inquiries/inquiry_list.html'
    context_object_name = 'inquiries'
    paginate_by = 10

class InquiryCreateView(CreateView):
    model = Inquiry
    form_class = InquiryForm
    template_name = 'inquiries/inquiry_form.html'
    success_url = reverse_lazy('inquiry_thank_you')

def inquiry_thank_you(request):
    return render(request, 'inquiries/thank_you.html')

def load_initial_products():
    # Create initial products if they don't exist
    products = [
        "Coctel de Café Cream Love",
        "Crema de lúcuma"
    ]
    
    for product_name in products:
        Product.objects.get_or_create(name=product_name)
```

```python
# inquiries/urls.py
from django.urls import path
from .views import InquiryListView, InquiryCreateView, inquiry_thank_you

urlpatterns = [
    path('', InquiryListView.as_view(), name='inquiry_list'),
    path('new/', InquiryCreateView.as_view(), name='inquiry_create'),
    path('thank-you/', inquiry_thank_you, name='inquiry_thank_you'),
]
```

```python
# yobugo_inquiries/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inquiries/', include('inquiries.urls')),
]
```

```python
# inquiries/apps.py
from django.apps import AppConfig

class InquiriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inquiries'

    def ready(self):
        from .views import load_initial_products
        load_initial_products()
```

```html
<!-- templates/inquiries/inquiry_form.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Submit Inquiry</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1>Product Inquiry</h1>
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit" class="btn btn-primary">Submit Inquiry</button>
        </form>
    </div>
</body>
</html>
```

```html
<!-- templates/inquiries/inquiry_list.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Inquiry List</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1>Customer Inquiries</h1>
        <a href="{% url 'inquiry_create' %}" class="btn btn-success mb-3">New Inquiry</a>
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Product</th>
                    <th>Customer</th>
                    <th>Email</th>
                    <th>Status</th>
                    <th>Date</th>
                </tr>
            </thead>
            <tbody>
                {% for inquiry in inquiries %}
                <tr>
                    <td>{{ inquiry.id }}</td>
                    <td>{{ inquiry.product }}</td>
                    <td>{{ inquiry.customer_name
