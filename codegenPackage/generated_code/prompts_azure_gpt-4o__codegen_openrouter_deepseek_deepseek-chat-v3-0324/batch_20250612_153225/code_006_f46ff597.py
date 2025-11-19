"""
Generated Code Metadata:
========================
Original URL: https://morevacare.com
Prompt: Write code to implement a shopping cart system in Django that supports multiple product variants and calculates discounts for pre-orders, similar to MorevaCare's functionality.
Generated: DETERMINISTIC_f46ff597ee890314
Batch ID: 20250612_153225
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
from django.core.validators import MinValueValidator
from django.conf import settings
from decimal import Decimal

class Product(models.Model):
    """
    Represents a product in the inventory.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    is_pre_order = models.BooleanField(default=False)
    pre_order_discount = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def current_price(self):
        """
        Returns the current price considering pre-order discount if applicable.
        """
        if self.is_pre_order:
            return self.base_price * (1 - self.pre_order_discount / 100)
        return self.base_price

class ProductVariant(models.Model):
    """
    Represents different variants of a product (size, color, etc.)
    """
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # e.g., "Small", "Red", etc.
    sku = models.CharField(max_length=50, unique=True)
    stock = models.PositiveIntegerField(default=0)
    price_adjustment = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0,
        help_text="Additional price for this variant (can be negative)"
    )

    def __str__(self):
        return f"{self.product.name} - {self.name}"

    @property
    def final_price(self):
        """
        Returns the final price including product price and variant adjustment.
        """
        return self.product.current_price + self.price_adjustment

    def is_available(self, quantity=1):
        """
        Checks if the variant has sufficient stock.
        """
        return self.stock >= quantity

class Cart(models.Model):
    """
    Represents a user's shopping cart.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def total(self):
        """
        Calculates the total price of all items in the cart.
        """
        return sum(item.total_price for item in self.items.all())

    @property
    def item_count(self):
        """
        Returns the total number of items in the cart.
        """
        return sum(item.quantity for item in self.items.all())

    def clear(self):
        """
        Removes all items from the cart.
        """
        self.items.all().delete()

class CartItem(models.Model):
    """
    Represents an item in the shopping cart.
    """
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('cart', 'variant')

    @property
    def total_price(self):
        """
        Calculates the total price for this cart item (price * quantity).
        """
        return self.variant.final_price * self.quantity

    def save(self, *args, **kwargs):
        """
        Overrides save to validate stock availability.
        """
        if not self.variant.is_available(self.quantity):
            raise ValueError(f"Insufficient stock for {self.variant}")
        super().save(*args, **kwargs)

# views.py
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View
from django.contrib import messages
from django.http import JsonResponse
from .models import Cart, CartItem, ProductVariant

class AddToCartView(View):
    """
    Handles adding products to the cart.
    """
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Authentication required'}, status=403)

        variant_id = request.POST.get('variant_id')
        quantity = int(request.POST.get('quantity', 1))

        try:
            variant = ProductVariant.objects.get(pk=variant_id)
            cart, created = Cart.objects.get_or_create(user=request.user)

            # Check if item already exists in cart
            cart_item, created = CartItem.objects.get_or_create(
                cart=cart,
                variant=variant,
                defaults={'quantity': quantity}
            )

            if not created:
                cart_item.quantity += quantity
                cart_item.save()

            return JsonResponse({
                'success': True,
                'item_count': cart.item_count,
                'total': str(cart.total)
            })

        except ProductVariant.DoesNotExist:
            return JsonResponse({'error': 'Product variant not found'}, status=404)
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)
        except Exception as e:
            return JsonResponse({'error': 'An error occurred'}, status=500)

class RemoveFromCartView(View):
    """
    Handles removing items from the cart.
    """
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Authentication required'}, status=403)

        item_id = request.POST.get('item_id')

        try:
            cart = Cart.objects.get(user=request.user)
            item = get_object_or_404(CartItem, pk=item_id, cart=cart)
            item.delete()

            return JsonResponse({
                'success': True,
                'item_count': cart.item_count,
                'total': str(cart.total)
            })

        except Cart.DoesNotExist:
            return JsonResponse({'error': 'Cart not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': 'An error occurred'}, status=500)

class UpdateCartItemView(View):
    """
    Handles updating cart item quantities.
    """
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Authentication required'}, status=403)

        item_id = request.POST.get('item_id')
        quantity = int(request.POST.get('quantity', 1))

        try:
            cart = Cart.objects.get(user=request.user)
            item = get_object_or_404(CartItem, pk=item_id, cart=cart)
            
            if quantity <= 0:
                item.delete()
            else:
                item.quantity = quantity
                item.save()

            return JsonResponse({
                'success': True,
                'item_count': cart.item_count,
                'total': str(cart.total),
                'item_total': str(item.total_price)
            })

        except Cart.DoesNotExist:
            return JsonResponse({'error': 'Cart not found'}, status=404)
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)
        except Exception as e:
            return JsonResponse({'error': 'An error occurred'}, status=500)

# serializers.py (for API views)
from rest_framework import serializers
from .models import Cart, CartItem, Product, ProductVariant

class ProductVariantSerializer(serializers.ModelSerializer):
    final_price = serializers.SerializerMethodField()

    class Meta:
        model = ProductVariant
        fields = ['id', 'name', 'sku', 'stock', 'price_adjustment', 'final_price']

    def get_final_price(self, obj):
        return obj.final_price

class ProductSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True, read_only=True)
    current_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'base_price', 'current_price', 
                  'is_pre_order', 'pre_order_discount', 'variants']

    def get_current_price(self, obj):
        return obj.current_price

class CartItemSerializer(serializers.ModelSerializer):
    variant = ProductVariantSerializer(read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'variant', 'quantity', 'total_price']

    def get_total_price(self, obj):
        return obj.total_price

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()
    item_count = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'created_at', 'updated_at', 'items', 'total', 'item_count']

    def get_total(self, obj):
        return obj.total

    def get_item_count(self
