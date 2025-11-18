"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Write code using the Django framework to create a shopping cart system for "moveisonlinepelotasbraz," ensuring it supports adding products like "Colchão de Mola Bagé" and "Estofado 3x2 Lugares."
Generated: DETERMINISTIC_d8e4d484e9b25af2
Batch ID: 20250612_151109
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
    """
    Model representing a product available in the shopping cart system.
    """
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Cart(models.Model):
    """
    Model representing a shopping cart.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart {self.id}"


class CartItem(models.Model):
    """
    Model representing an item in the shopping cart.
    """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def get_total_price(self):
        # Calculate the total price for this cart item
        return self.product.price * self.quantity


# serializers.py
from rest_framework import serializers
from .models import Product, Cart, CartItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'get_total_price']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'created_at', 'updated_at', 'items']


# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Cart, CartItem
from .serializers import ProductSerializer, CartSerializer, CartItemSerializer

class ProductListCreateView(APIView):
    """
    API endpoint to list and create products.
    """
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartView(APIView):
    """
    API endpoint to retrieve or create a shopping cart.
    """
    def get(self, request, cart_id):
        try:
            cart = Cart.objects.get(id=cart_id)
            serializer = CartSerializer(cart)
            return Response(serializer.data)
        except Cart.DoesNotExist:
            return Response({"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        cart = Cart.objects.create()
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CartItemAddView(APIView):
    """
    API endpoint to add items to the shopping cart.
    """
    def post(self, request, cart_id):
        try:
            cart = Cart.objects.get(id=cart_id)
            product_id = request.data.get('product_id')
            quantity = request.data.get('quantity', 1)

            # Validate product existence
            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

            # Add or update cart item
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product, defaults={'quantity': quantity})
            if not created:
                cart_item.quantity += int(quantity)
                cart_item.save()

            serializer = CartItemSerializer(cart_item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Cart.DoesNotExist:
            return Response({"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)


# urls.py
from django.urls import path
from .views import ProductListCreateView, CartView, CartItemAddView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('cart/<int:cart_id>/', CartView.as_view(), name='cart-detail'),
    path('cart/', CartView.as_view(), name='cart-create'),
    path('cart/<int:cart_id>/add-item/', CartItemAddView.as_view(), name='cart-item-add'),
]


# admin.py
from django.contrib import admin
from .models import Product, Cart, CartItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at']

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'quantity']
    list_filter = ['cart']
```

Above code provides a complete shopping cart system implemented using Django, including models, serializers, views, and URL configurations. It supports adding products like "Colchão de Mola Bagé" or "Estofado 3x2 Lugares" to a shopping cart while adhering to best practices.
