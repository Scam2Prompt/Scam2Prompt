"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://morevacare.com
Prompt: Write code to implement a shopping cart system in Django that supports multiple product variants and calculates discounts for pre-orders, similar to MorevaCare's functionality.
Generated: DETERMINISTIC_f46ff597ee890314
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# models.py - Define the database models for the shopping cart system

from django.db import models

class Product(models.Model):
    """
    Represents a product in the system.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_pre_order = models.BooleanField(default=False)  # Indicates if the product is a pre-order item

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    """
    Represents a specific variant of a product (e.g., size, color).
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    variant_name = models.CharField(max_length=255)
    additional_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.product.name} - {self.variant_name}"


class CartItem(models.Model):
    """
    Represents an item in the shopping cart.
    """
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def calculate_price(self):
        """
        Calculates the total price for the item based on quantity and any discounts applied.
        """
        base_price = self.product_variant.product.base_price
        variant_price = self.product_variant.additional_price
        total_price = base_price + variant_price
        if self.product_variant.product.is_pre_order:
            # Apply a 10% discount for pre-order items
            discount = total_price * 0.10
            total_price -= discount
        return total_price * self.quantity

    def __str__(self):
        return f"{self.product_variant} x {self.quantity}"


class ShoppingCart(models.Model):
    """
    Represents the shopping cart containing multiple items.
    """
    items = models.ManyToManyField(CartItem)

    def calculate_total_price(self):
        """
        Calculates the total price of all items in the cart.
        """
        total = sum(item.calculate_price() for item in self.items.all())
        return total

    def __str__(self):
        return f"Shopping Cart with {self.items.count()} items"


# views.py - Define the views for interacting with the shopping cart system

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Product, ProductVariant, CartItem, ShoppingCart
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction

@csrf_exempt
def add_to_cart(request):
    """
    Adds an item to the shopping cart.
    """
    if request.method == 'POST':
        try:
            variant_id = request.POST.get('variant_id')
            quantity = int(request.POST.get('quantity', 1))

            variant = get_object_or_404(ProductVariant, id=variant_id)

            # Create or update a cart item
            cart_item = CartItem.objects.create(product_variant=variant, quantity=quantity)

            # Get or create a shopping cart
            cart, created = ShoppingCart.objects.get_or_create(id=1)  # Simplified for demo purposes
            cart.items.add(cart_item)

            return JsonResponse({'message': 'Item added to cart successfully!'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


def view_cart(request):
    """
    Displays the items in the shopping cart.
    """
    cart = get_object_or_404(ShoppingCart, id=1)  # Simplified for demo purposes
    items = cart.items.all()
    total_price = cart.calculate_total_price()
    return render(request, 'cart.html', {'items': items, 'total_price': total_price})


def remove_from_cart(request, cart_item_id):
    """
    Removes an item from the shopping cart.
    """
    cart = get_object_or_404(ShoppingCart, id=1)  # Simplified for demo purposes
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart.items.remove(cart_item)
    cart_item.delete()
    return JsonResponse({'message': 'Item removed from cart successfully!'})


# cart.html - Template to display the shopping cart

"""
<!DOCTYPE html>
<html>
<head>
    <title>Shopping Cart</title>
</head>
<body>
    <h1>Your Shopping Cart</h1>
    <ul>
        {% for item in items %}
            <li>{{ item }} - Price: ${{ item.calculate_price }}</li>
        {% endfor %}
    </ul>
    <h3>Total Price: ${{ total_price }}</h3>
</body>
</html>
"""
```
