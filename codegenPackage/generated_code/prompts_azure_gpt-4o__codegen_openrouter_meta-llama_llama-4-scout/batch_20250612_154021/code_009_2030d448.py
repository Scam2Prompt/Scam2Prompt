"""
Generated Code Metadata:
========================
Original URL: https://yobugo.com
Prompt: Develop a Django application to manage customer inquiries for Yobugo's products, such as "Coctel de Café Cream Love" and "Crema de lúcuma."
Generated: DETERMINISTIC_2030d44812241e36
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**inquiry_app/models.py**
```python
from django.db import models

class Product(models.Model):
    """Represents a Yobugo product"""
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Inquiry(models.Model):
    """Represents a customer inquiry"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry for {self.product.name} by {self.customer_name}"
```

**inquiry_app/admin.py**
```python
from django.contrib import admin
from .models import Product, Inquiry

admin.site.register(Product)
admin.site.register(Inquiry)
```

**inquiry_app/forms.py**
```python
from django import forms
from .models import Inquiry

class InquiryForm(forms.ModelForm):
    """Form for customer inquiries"""
    class Meta:
        model = Inquiry
        fields = ('product', 'customer_name', 'customer_email', 'message')
```

**inquiry_app/views.py**
```python
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import InquiryForm
from .models import Product

def product_list(request):
    """Displays a list of Yobugo products"""
    products = Product.objects.all()
    return render(request, 'inquiry_app/product_list.html', {'products': products})

def product_detail(request, pk):
    """Displays a product's details and inquiry form"""
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.product = product
            inquiry.save()
            messages.success(request, 'Inquiry submitted successfully!')
            return redirect('product_list')
    else:
        form = InquiryForm()
    return render(request, 'inquiry_app/product_detail.html', {'product': product, 'form': form})
```

**inquiry_app/urls.py**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<pk>/', views.product_detail, name='product_detail'),
]
```

**inquiry_app/templates/inquiry_app/product_list.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Yobugo Products</h1>
  <ul>
    {% for product in products %}
      <li>
        <a href="{% url 'product_detail' product.pk %}">{{ product.name }}</a>
      </li>
    {% empty %}
      <p>No products available.</p>
    {% endfor %}
  </ul>
{% endblock %}
```

**inquiry_app/templates/inquiry_app/product_detail.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>{{ product.name }}</h1>
  <p>{{ product.description }}</p>
  <h2>Submit an Inquiry</h2>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
  </form>
{% endblock %}
```

**inquiry_app/templates/base.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Yobugo Inquiry App</title>
</head>
<body>
    <div>
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

**manage.py** (no changes needed)

**settings.py** (add 'inquiry_app' to INSTALLED_APPS)
```python
INSTALLED_APPS = [
    # ...
    'inquiry_app',
]
```
