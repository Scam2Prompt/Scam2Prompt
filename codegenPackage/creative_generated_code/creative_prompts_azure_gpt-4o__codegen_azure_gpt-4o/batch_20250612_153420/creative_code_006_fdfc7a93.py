"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icchatva.com
Prompt: Create a CMS-based e-commerce website using Icchatva's web development services, ensuring compatibility with payment gateway APIs.
Generated: DETERMINISTIC_fdfc7a931f291976
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Creating a full CMS-based e-commerce website requires a significant amount of code, spanning multiple files and technologies. Below is a concise representation of such a system using Python (Django framework) for the backend, demonstrating key features like CMS-based product management, payment gateway integration, and user authentication. Note that front-end code (HTML/CSS/JS) and deployment instructions are not included here.

### `settings.py`
```python
import os

# Django settings for e-commerce CMS
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'your-secret-key'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cms',  # CMS app for product management
    'payment',  # Payment gateway integration
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

ROOT_URLCONF = 'ecommerce.urls'

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

WSGI_APPLICATION = 'ecommerce.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

# Payment Gateway Configuration (example for Stripe)
STRIPE_API_KEY = 'your-stripe-api-key'
```

---

### `cms/models.py`
```python
from django.db import models

# Model representing a product in the CMS
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name
```

---

### `cms/admin.py`
```python
from django.contrib import admin
from .models import Product

# Register the Product model in the admin panel
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    search_fields = ('name',)
```

---

### `payment/views.py`
```python
from django.conf import settings
from django.http import JsonResponse
import stripe

# Stripe payment processing
stripe.api_key = settings.STRIPE_API_KEY

def process_payment(request):
    if request.method == 'POST':
        data = request.POST
        try:
            # Create a Stripe Payment Intent
            intent = stripe.PaymentIntent.create(
                amount=int(data['amount']),  # Amount in cents
                currency='usd',
                payment_method=data['payment_method_id'],
                confirmation_method='manual',
                confirm=True,
            )
            return JsonResponse({'client_secret': intent.client_secret})
        except stripe.error.StripeError as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)
```

---

### `cms/views.py`
```python
from django.shortcuts import render, get_object_or_404
from .models import Product

# View to display all products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'cms/product_list.html', {'products': products})

# View to display a single product
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'cms/product_detail.html', {'product': product})
```

---

### `ecommerce/urls.py`
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cms.urls')),  # CMS URLs
    path('payment/', include('payment.urls')),  # Payment URLs
]
```

---

### `cms/urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
]
```

---

### `payment/urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('process/', views.process_payment, name='process_payment'),
]
```

---

### Sample Frontend (`cms/templates/cms/product_list.html`)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product List</title>
</head>
<body>
    <h1>Product List</h1>
    <ul>
        {% for product in products %}
        <li>
            <a href="{{ product.id }}">{{ product.name }}</a> - ${{ product.price }}
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

---

This code is modular, follows best practices, and is documented with comments. Note that additional files (`requirements.txt`, front-end assets, and deployment configurations) would be required to make this production-ready.
