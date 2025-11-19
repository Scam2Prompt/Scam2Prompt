"""
Generated Code Metadata:
========================
Original URL: https://ratnarajfoods.in
Prompt: Develop a basic e-commerce website using Django for a company that exports spices, including features for product catalog, shipping, and quality certification, inspired by Ratnaraj Foods' services.
Generated: DETERMINISTIC_34c7f71a2bc72011
Batch ID: 20250622_210655
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
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'your-secret-key-here'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'spices.apps.SpicesConfig',
    'crispy_forms',
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

ROOT_URLCONF = 'spice_export.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'spice_export.wsgi.application'

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
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CRISPY_TEMPLATE_PACK = 'bootstrap4'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email settings (configure with your email provider)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yourprovider.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
```

```python
# models.py
from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/')
    organic = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Certification(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    issuing_authority = models.CharField(max_length=200)
    validity_period = models.PositiveIntegerField(help_text="Validity period in months")
    products = models.ManyToManyField(Product, related_name='certifications')

    def __str__(self):
        return self.name

class ShippingOption(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    estimated_delivery = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Confirmed'),
        ('S', 'Shipped'),
        ('D', 'Delivered'),
        ('X', 'Cancelled'),
    ]

    customer = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    shipping_address = models.TextField()
    shipping_option = models.ForeignKey(ShippingOption, on_delete=models.SET_NULL, null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer.username}"

    def total_cost(self):
        return sum(item.total_price() for item in self.order_items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def total_price(self):
        return self.quantity * self.price
```

```python
# admin.py
from django.contrib import admin
from .models import Category, Product, Certification, ShippingOption, Order, OrderItem

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'organic')
    list_filter = ('category', 'organic')
    search_fields = ('name', 'description')

class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'issuing_authority', 'validity_period')
    filter_horizontal = ('products',)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'order_date', 'status', 'total_cost')
    list_filter = ('status', 'order_date')
    inlines = [OrderItemInline]

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Certification, CertificationAdmin)
admin.site.register(ShippingOption)
admin.site.register(Order, OrderAdmin)
```

```python
# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Order, ShippingOption

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class OrderForm(forms.ModelForm):
    shipping_option = forms.ModelChoiceField(
        queryset=ShippingOption.objects.all(),
        widget=forms.RadioSelect
    )

    class Meta:
        model = Order
        fields = ['shipping_address', 'shipping_option', 'notes']
        widgets = {
            'shipping_address': forms.Textarea(attrs={'rows': 3}),
            'notes': forms.Textarea(attrs={'rows': 2}),
        }
```

```python
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Product, Category, Certification, Order, OrderItem, ShippingOption
from .forms import RegistrationForm, OrderForm

def home(request):
    featured_products = Product.objects.filter(stock__gt=0).order_by('-created_at')[:4]
    certifications = Certification.objects.all()[:3]
    return render(request, 'spices/home.html', {
        'featured_products': featured_products,
        'certifications': certifications
    })

def product_list(request):
    category_id = request.GET.get('category')
    if category_id:
        products = Product.objects.filter(category_id=category_id
