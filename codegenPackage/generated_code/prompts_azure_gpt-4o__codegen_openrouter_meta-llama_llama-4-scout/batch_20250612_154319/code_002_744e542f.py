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

**models.py**
```python
from django.db import models

class Category(models.Model):
    """Product category model"""
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    """Product model"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    """Product sub-category model"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categories')
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class SubProduct(models.Model):
    """Sub-product model"""
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='sub_products')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
```

**views.py**
```python
from django.shortcuts import render, get_object_or_404
from .models import Category, Product, SubCategory, SubProduct
from .serializers import CategorySerializer, ProductSerializer, SubCategorySerializer, SubProductSerializer

def category_list(request):
    """Category list view"""
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return render(request, 'category_list.html', {'serializer': serializer})

def category_detail(request, pk):
    """Category detail view"""
    category = get_object_or_404(Category, pk=pk)
    products = Product.objects.filter(category=category)
    sub_categories = SubCategory.objects.filter(category=category)
    return render(request, 'category_detail.html', {'category': category, 'products': products, 'sub_categories': sub_categories})

def product_list(request, category_pk):
    """Product list view"""
    products = Product.objects.filter(category__pk=category_pk)
    serializer = ProductSerializer(products, many=True)
    return render(request, 'product_list.html', {'serializer': serializer})

def product_detail(request, category_pk, pk):
    """Product detail view"""
    product = get_object_or_404(Product, pk=pk, category__pk=category_pk)
    return render(request, 'product_detail.html', {'product': product})

def sub_category_list(request, category_pk):
    """Sub-category list view"""
    sub_categories = SubCategory.objects.filter(category__pk=category_pk)
    serializer = SubCategorySerializer(sub_categories, many=True)
    return render(request, 'sub_category_list.html', {'serializer': serializer})

def sub_product_list(request, category_pk, sub_category_pk):
    """Sub-product list view"""
    sub_products = SubProduct.objects.filter(sub_category__pk=sub_category_pk, sub_category__category__pk=category_pk)
    serializer = SubProductSerializer(sub_products, many=True)
    return render(request, 'sub_product_list.html', {'serializer': serializer})
```

**serializers.py**
```python
from rest_framework import serializers
from .models import Category, Product, SubCategory, SubProduct

class CategorySerializer(serializers.ModelSerializer):
    """Category serializer"""
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class ProductSerializer(serializers.ModelSerializer):
    """Product serializer"""
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']

class SubCategorySerializer(serializers.ModelSerializer):
    """Sub-category serializer"""
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'description']

class SubProductSerializer(serializers.ModelSerializer):
    """Sub-product serializer"""
    class Meta:
        model = SubProduct
        fields = ['id', 'name', 'description', 'price']
```

**urls.py**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('categories/<pk>/', views.category_detail, name='category_detail'),
    path('categories/<category_pk>/products/', views.product_list, name='product_list'),
    path('categories/<category_pk>/products/<pk>/', views.product_detail, name='product_detail'),
    path('categories/<category_pk>/sub_categories/', views.sub_category_list, name='sub_category_list'),
    path('categories/<category_pk>/sub_categories/<sub_category_pk>/sub_products/', views.sub_product_list, name='sub_product_list'),
]
```

**templates/category_list.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Categories</h1>
  <ul>
    {% for category in serializer %}
      <li><a href="{% url 'category_detail' category.id %}">{{ category.name }}</a></li>
    {% empty %}
      <li>No categories found.</li>
    {% endfor %}
  </ul>
{% endblock %}
```

**templates/category_detail.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>{{ category.name }}</h1>
  <p>{{ category.description }}</p>
  <h2>Products</h2>
  <ul>
    {% for product in products %}
      <li><a href="{% url 'product_detail' category.id product.id %}">{{ product.name }}</a></li>
    {% empty %}
      <li>No products found.</li>
    {% endfor %}
  </ul>
  <h2>Sub-categories</h2>
  <ul>
    {% for sub_category in sub_categories %}
      <li><a href="{% url 'sub_category_list' category.id %}">{{ sub_category.name }}</a></li>
    {% empty %}
      <li>No sub-categories found.</li>
    {% endfor %}
  </ul>
{% endblock %}
```

**templates/product_list.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Products</h1>
  <ul>
    {% for product in serializer %}
      <li><a href="{% url 'product_detail' product.category.id product.id %}">{{ product.name }}</a></li>
    {% empty %}
      <li>No products found.</li>
    {% endfor %}
  </ul>
{% endblock %}
```

**templates/product_detail.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>{{ product.name }}</h1>
  <p>{{ product.description }}</p>
  <p>Price: {{ product.price }}</p>
{% endblock %}
```

**templates/sub_category_list.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Sub-categories</h1>
  <ul>
    {% for sub_category in serializer %}
      <li><a href="{% url 'sub_product_list' sub_category.category.id sub_category.id %}">{{ sub_category.name }}</a></li>
    {% empty %}
      <li>No sub-categories found.</li>
    {% endfor %}
  </ul>
{% endblock %}
```

**templates/sub_product_list.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Sub-products</h1>
  <ul>
    {% for sub_product in serializer %}
      <li>{{ sub_product.name }} ({{ sub_product.price }})</li>
    {% empty %}
      <li>No sub-products found.</li>
    {% endfor %}
  </ul>
{% endblock %}
```

**base.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Samba Plastic Industries</title>
</head>
<body>
    <div>
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

**admin.py**
```python
from django.contrib import admin
from .models import Category, Product, SubCategory, SubProduct

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(SubCategory)
admin.site.register(SubProduct)
```

**settings.py** (Make sure to add 'rest_framework' and your app name to INSTALLED_APPS)
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'your_app_name',
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]
}
```
