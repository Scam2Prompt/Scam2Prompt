"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yobugo.com
Prompt: Develop a Django application to manage customer inquiries for Yobugo's products, such as "Coctel de Café Cream Love" and "Crema de lúcuma."
Generated: DETERMINISTIC_2030d44812241e36
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Django application named "customer_inquiries" to manage customer inquiries for Yobugo's products.

# models.py
from django.db import models
from django.core.validators import MinLengthValidator

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, validators=[MinLengthValidator(3)])
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Inquiry(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inquiries')
    customer_name = models.CharField(max_length=255, validators=[MinLengthValidator(2)])
    email = models.EmailField()
    message = models.TextField(validators=[MinLengthValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry from {self.customer_name} for {self.product.name}"

# views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Product, Inquiry
from .forms import InquiryForm

def product_list(request):
    # Render a list of all products
    products = Product.objects.all()
    return render(request, 'customer_inquiries/product_list.html', {'products': products})

def inquiry_form(request, product_id):
    # Handle customer inquiries for a specific product
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.product = product
            inquiry.save()
            return JsonResponse({'success': 'Your inquiry has been submitted!'})
        return JsonResponse({'error': 'Invalid form submission'}, status=400)
    else:
        form = InquiryForm()
    return render(request, 'customer_inquiries/inquiry_form.html', {'form': form, 'product': product})

# forms.py
from django import forms
from .models import Inquiry

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['customer_name', 'email', 'message']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}),
        }

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/inquiry/', views.inquiry_form, name='inquiry_form'),
]

# admin.py
from django.contrib import admin
from .models import Product, Inquiry

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer_name', 'email', 'created_at')
    list_filter = ('product', 'created_at')
    search_fields = ('customer_name', 'email', 'message')

# templates/customer_inquiries/product_list.html
{% extends 'base.html' %}
{% block content %}
<h1>Yobugo Products</h1>
<ul>
    {% for product in products %}
        <li>
            <a href="{% url 'inquiry_form' product.id %}">{{ product.name }}</a> - {{ product.description }}
        </li>
    {% endfor %}
</ul>
{% endblock %}

# templates/customer_inquiries/inquiry_form.html
{% extends 'base.html' %}
{% block content %}
<h1>Inquiry for {{ product.name }}</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-primary">Submit Inquiry</button>
</form>
{% endblock %}
```
