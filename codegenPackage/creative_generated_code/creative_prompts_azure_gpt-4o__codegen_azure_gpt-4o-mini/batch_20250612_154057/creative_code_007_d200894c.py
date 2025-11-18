"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://garmin-boutique.com
Prompt: Write code using Django to create a product page for Garmin watches, including features like product descriptions, images, and pricing for models such as "fēnix® 6 Pro" or "Venu® 2S."
Generated: DETERMINISTIC_d200894ce1370c22
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# models.py

from django.db import models

class Product(models.Model):
    """Model to represent a product, specifically Garmin watches."""
    
    name = models.CharField(max_length=255)  # Name of the product
    description = models.TextField()          # Detailed description of the product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Product price
    image = models.ImageField(upload_to='products/')  # Product image

    def __str__(self):
        return self.name


# views.py

from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    """View to display a list of Garmin products."""
    products = Product.objects.all()  # Fetch all products
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
    """View to display product details for a specific Garmin watch."""
    product = get_object_or_404(Product, id=product_id)  # Fetch product or return 404 if not found
    return render(request, 'product_detail.html', {'product': product})


# urls.py

from django.urls import path
from .views import product_list, product_detail

urlpatterns = [
    path('', product_list, name='product_list'),  # URL for product list
    path('product/<int:product_id>/', product_detail, name='product_detail'),  # URL for product detail
]


# product_list.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Garmin Watches</title>
</head>
<body>
    <h1>Garmin Watches</h1>
    <ul>
        {% for product in products %}
            <li>
                <a href="{% url 'product_detail' product.id %}">{{ product.name }}</a>
                <p>{{ product.price }}</p>
                <img src="{{ product.image.url }}" alt="{{ product.name }}" width="200">
            </li>
        {% endfor %}
    </ul>
</body>
</html>


# product_detail.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ product.name }}</title>
</head>
<body>
    <h1>{{ product.name }}</h1>
    <img src="{{ product.image.url }}" alt="{{ product.name }}" width="400">
    <p>{{ product.description }}</p>
    <p>Price: ${{ product.price }}</p>
    <a href="{% url 'product_list' %}">Back to Product List</a>
</body>
</html>


# settings.py (add relevant settings for media files)

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Remember to configure your main URLconf to serve media files during development
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Make sure to run the necessary migrations to create the `Product` table in your database:
```bash
python manage.py makemigrations
python manage.py migrate
```

Also, ensure that you have Pillow installed for image handling:
```bash
pip install Pillow
```
