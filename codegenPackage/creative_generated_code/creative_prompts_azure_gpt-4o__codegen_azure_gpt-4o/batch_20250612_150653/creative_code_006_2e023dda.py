"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.paradigmagbi.ru
Prompt: Suggest a library or framework for implementing flexible payment systems and discounts for construction material orders, as described in the payment options section of paradigmagbi.ru.
Generated: DETERMINISTIC_2e023dda99a3beab
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready implementation using Python and the `Django` framework, combined with the `django-payments` library for payment processing. Additionally, we define a discount system using custom logic.

```python
# Install required packages before running:
# pip install django django-payments

# payments_system/models.py

from django.db import models
from payments import PurchasedItem
from payments.models import BasePayment

class Payment(BasePayment):
    """Model representing a payment."""
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='payments')

    def get_failure_url(self):
        # URL to redirect on payment failure
        return '/payment/failure/'

    def get_success_url(self):
        # URL to redirect on payment success
        return '/payment/success/'

class Order(models.Model):
    """Model representing a construction materials order."""
    customer_name = models.CharField(max_length=255)
    email = models.EmailField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)

    def get_discounted_price(self, discount_percent):
        """
        Calculate the discounted price for an order.
        :param discount_percent: Discount percentage to be applied
        :return: Discounted price
        """
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError('Discount percent must be between 0 and 100.')
        return self.total_price * (1 - discount_percent / 100)

    def get_purchased_items(self):
        """
        Generate PurchasedItem entries for `django-payments`.
        :return: List of PurchasedItem objects
        """
        # Example: For simplicity, we'll return one item representing the order.
        return [PurchasedItem(
            name='Construction Materials',
            sku='CONSTRUCTION001',
            quantity=1,
            price=self.total_price,
            currency='USD'
        )]

# payments_system/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Order, Payment

def create_payment(request, order_id):
    """
    View to create a payment for a given order.
    :param order_id: ID of the order
    """
    order = get_object_or_404(Order, id=order_id)
    if order.is_paid:
        return HttpResponse("Order is already paid.", status=400)

    payment = Payment.objects.create(
        variant='default',  # Payment method (e.g., stripe, paypal, etc.)
        order=order,
        currency='USD',
        total=order.total_price,
        description=f'Payment for Order #{order.id}',
    )

    # Redirect to the payment provider's page
    return redirect(payment.get_payment_url())

def apply_discount(request, order_id, discount_percent):
    """
    View to apply a discount to the order.
    :param order_id: ID of the order
    :param discount_percent: Discount percentage
    """
    order = get_object_or_404(Order, id=order_id)
    try:
        discounted_price = order.get_discounted_price(discount_percent)
        order.total_price = discounted_price
        order.save()
        return HttpResponse(f'Discount applied. New price: ${discounted_price:.2f}')
    except ValueError as e:
        return HttpResponse(str(e), status=400)

# payments_system/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('payment/create/<int:order_id>/', views.create_payment, name='create_payment'),
    path('order/discount/<int:order_id>/<int:discount_percent>/', views.apply_discount, name='apply_discount'),
]

# settings.py (Include these settings for configuring django-payments)
INSTALLED_APPS += ['payments']  # Add 'payments' app

PAYMENT_VARIANTS = {
    'default': ('payments.dummy.DummyProvider', {}),
}

# NOTE: In production, replace 'dummy.DummyProvider' with actual payment providers like Stripe, PayPal, etc.

# To use this setup, create migrations:
# python manage.py makemigrations
# python manage.py migrate

# Start the Django development server:
# python manage.py runserver
```
