"""
Generated Code Metadata:
========================
Original URL: https://sahouriplast.com
Prompt: Using Django, design a web application that replicates the product categorization system of Samba Plastic Industries, allowing users to browse items like indoor and outdoor furniture and houseware.
Generated: DETERMINISTIC_744e542faeb8d9bf
Batch ID: 20250612_154319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# models.py
from django.db import models
from django.urls import reverse

class Category(models.Model):
    """
    Represents a product category (e.g., Indoor Furniture, Outdoor Furniture).
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='categories/', blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products_by_category', args=[self.slug])

class Product(models.Model):
    """
    Represents a product item with its details.
    """
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

# views.py
from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def product_list(request, category_slug=None):
    """
    Displays all products or products filtered by category.
    """
    category = None
    categories = Category.objects.filter(parent__isnull=True)
    products = Product.objects.filter(available=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })

def product_detail(request, category_slug, product_slug):
    """
    Displays detailed information about a single product.
    """
    product = get_object_or_404(
        Product,
        category__slug=category_slug,
        slug=product_slug,
        available=True
    )
    return render(request, 'shop/product/detail.html', {'product': product})

# urls.py (app-level)
from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
]

# admin.py
from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'price', 'available', 'created', 'updated')
    list_filter = ('available', 'created', 'updated', 'category')
    list_editable = ('price', 'available')
    prepopulated_fields = {'slug': ('name',)}

# templates/shop/product/list.html
{% extends 'shop/base.html' %}

{% block content %}
<div class="container">
    <div class="row">
        <div class="col-md-3">
            <h3>Categories</h3>
            <ul class="list-group">
                {% for category in categories %}
                <li class="list-group-item">
                    <a href="{{ category.get_absolute_url }}">{{ category.name }}</a>
                    {% if category.children.all %}
                    <ul>
                        {% for child in category.children.all %}
                        <li>
                            <a href="{{ child.get_absolute_url }}">{{ child.name }}</a>
                        </li>
                        {% endfor %}
                    </ul>
                    {% endif %}
                </li>
                {% endfor %}
            </ul>
        </div>
        <div class="col-md-9">
            <h1>{% if category %}{{ category.name }}{% else %}Products{% endif %}</h1>
            <div class="row">
                {% for product in products %}
                <div class="col-md-4">
                    <div class="card mb-4">
                        <a href="{{ product.get_absolute_url }}">
                            <img src="{{ product.image.url }}" class="card-img-top" alt="{{ product.name }}">
                        </a>
                        <div class="card-body">
                            <h5 class="card-title">
                                <a href="{{ product.get_absolute_url }}">{{ product.name }}</a>
                            </h5>
                            <p class="card-text">${{ product.price }}</p>
                        </div>
                    </div>
                </div>
                {% empty %}
                <div class="col-12">
                    <p>No products available.</p>
                </div>
                {% endfor %}
            </div>
        </div>
    </div>
</div>
{% endblock %}

# templates/shop/product/detail.html
{% extends 'shop/base.html' %}

{% block content %}
<div class="container">
    <div class="row">
        <div class="col-md-6">
            <img src="{{ product.image.url }}" class="img-fluid" alt="{{ product.name }}">
        </div>
        <div class="col-md-6">
            <h1>{{ product.name }}</h1>
            <h2>
                <a href="{{ product.category.get_absolute_url }}">{{ product.category }}</a>
            </h2>
            <p class="price">${{ product.price }}</p>
            <p>{{ product.description }}</p>
            <p>
                {% if product.available %}
                <span class="badge badge-success">Available</span>
                {% else %}
                <span class="badge badge-danger">Out of Stock</span>
                {% endif %}
            </p>
        </div>
    </div>
</div>
{% endblock %}

# settings.py (relevant parts)
# Add to INSTALLED_APPS
INSTALLED_APPS = [
    # ...
    'shop.apps.ShopConfig',
    # ...
]

# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# urls.py (project-level)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
