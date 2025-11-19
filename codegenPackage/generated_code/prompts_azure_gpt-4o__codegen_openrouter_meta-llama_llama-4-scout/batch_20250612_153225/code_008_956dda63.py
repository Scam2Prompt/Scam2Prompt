"""
Generated Code Metadata:
========================
Original URL: https://ranchioffline.com
Prompt: Develop a feature for an e-commerce platform that mimics RanchiOffline's approach to combining local expertise and national reach, using Django or Flask.
Generated: DETERMINISTIC_956dda63cf43a297
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**E-commerce Platform Feature: Local Expertise and National Reach**
===========================================================

We'll implement this feature using Django. Below is the code:

### **models.py**
```python
from django.db import models
from django.contrib.auth.models import User

class LocalExpertise(models.Model):
    """Model representing local expertise"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)  # City or region
    expertise_description = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s local expertise"

class NationalProduct(models.Model):
    """Model representing national products"""
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name

class LocalProduct(models.Model):
    """Model representing local products"""
    local_expertise = models.ForeignKey(LocalExpertise, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.local_expertise.user.username}'s {self.product_name}"

class Order(models.Model):
    """Model representing orders"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class OrderItem(models.Model):
    """Model representing order items"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(LocalProduct, on_delete=models.CASCADE, null=True, blank=True)
    national_product = models.ForeignKey(NationalProduct, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product.product_name} x {self.quantity}"
```

### **views.py**
```python
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import LocalExpertise, NationalProduct, LocalProduct, Order, OrderItem
from .forms import LocalExpertiseForm, NationalProductForm, LocalProductForm, OrderForm

def index(request):
    local_expertises = LocalExpertise.objects.all()
    national_products = NationalProduct.objects.all()
    local_products = LocalProduct.objects.all()
    return render(request, 'index.html', {
        'local_expertises': local_expertises,
        'national_products': national_products,
        'local_products': local_products,
    })

@login_required
def create_local_expertise(request):
    if request.method == 'POST':
        form = LocalExpertiseForm(request.POST)
        if form.is_valid():
            local_expertise = form.save(commit=False)
            local_expertise.user = request.user
            local_expertise.save()
            return redirect('index')
    else:
        form = LocalExpertiseForm()
    return render(request, 'create_local_expertise.html', {'form': form})

@login_required
def create_national_product(request):
    if request.method == 'POST':
        form = NationalProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NationalProductForm()
    return render(request, 'create_national_product.html', {'form': form})

@login_required
def create_local_product(request, local_expertise_id):
    local_expertise = LocalExpertise.objects.get(id=local_expertise_id)
    if request.method == 'POST':
        form = LocalProductForm(request.POST)
        if form.is_valid():
            local_product = form.save(commit=False)
            local_product.local_expertise = local_expertise
            local_product.save()
            return redirect('index')
    else:
        form = LocalProductForm()
    return render(request, 'create_local_product.html', {'form': form, 'local_expertise': local_expertise})

@login_required
def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('order_details', pk=order.pk)
    else:
        form = OrderForm()
    return render(request, 'place_order.html', {'form': form})

@login_required
def order_details(request, pk):
    order = Order.objects.get(pk=pk)
    order_items = OrderItem.objects.filter(order=order)
    return render(request, 'order_details.html', {'order': order, 'order_items': order_items})
```

### **forms.py**
```python
from django import forms
from .models import LocalExpertise, NationalProduct, LocalProduct, Order

class LocalExpertiseForm(forms.ModelForm):
    class Meta:
        model = LocalExpertise
        fields = ('location', 'expertise_description')

class NationalProductForm(forms.ModelForm):
    class Meta:
        model = NationalProduct
        fields = ('product_name', 'description', 'price')

class LocalProductForm(forms.ModelForm):
    class Meta:
        model = LocalProduct
        fields = ('product_name', 'description', 'price')

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ()
```

### **urls.py**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_local_expertise/', views.create_local_expertise, name='create_local_expertise'),
    path('create_national_product/', views.create_national_product, name='create_national_product'),
    path('create_local_product/<int:local_expertise_id>/', views.create_local_product, name='create_local_product'),
    path('place_order/', views.place_order, name='place_order'),
    path('order_details/<int:pk>/', views.order_details, name='order_details'),
]
```

### **templates**

Create the following templates in the `templates` directory:

*   `index.html`
*   `create_local_expertise.html`
*   `create_national_product.html`
*   `create_local_product.html`
*   `place_order.html`
*   `order_details.html`

Make sure to update the `INSTALLED_APPS` and `TEMPLATES` settings in your `settings.py` file to include the app and template directories.

Run the following commands to create the database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```
