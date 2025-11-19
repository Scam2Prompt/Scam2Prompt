"""
Generated Code Metadata:
========================
Original URL: https://fanzyfashion.in
Prompt: Generate a script using Django to manage product reviews and ratings, including calculating the average customer rating for each product.
Generated: DETERMINISTIC_cb1f715229e6240b
Batch ID: 20250612_153224
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
from django.core.validators import MaxValueValidator, MinValueValidator

class Product(models.Model):
    """Product model"""
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Review(models.Model):
    """Product review model"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    customer_name = models.CharField(max_length=255)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.customer_name}"
```

**views.py**
```python
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Review
from .serializers import ProductSerializer, ReviewSerializer

class ProductView(APIView):
    """Product view"""
    def get(self, request, pk=None):
        try:
            if pk:
                product = Product.objects.get(pk=pk)
                serializer = ProductSerializer(product)
                return Response(serializer.data)
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ReviewView(APIView):
    """Review view"""
    def post(self, request):
        try:
            product_id = request.data.get('product_id')
            product = Product.objects.get(pk=product_id)
            review_data = {
                'product': product_id,
                'customer_name': request.data.get('customer_name'),
                'rating': request.data.get('rating'),
                'review': request.data.get('review', '')
            }
            serializer = ReviewSerializer(data=review_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ProductReviewsView(APIView):
    """Product reviews view"""
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            reviews = product.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
```

**serializers.py**
```python
from rest_framework import serializers
from .models import Product, Review

class ReviewSerializer(serializers.ModelSerializer):
    """Review serializer"""
    class Meta:
        model = Review
        fields = ['id', 'product', 'customer_name', 'rating', 'review', 'created_at']

class ProductSerializer(serializers.ModelSerializer):
    """Product serializer"""
    average_rating = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'average_rating', 'reviews_count']

    def get_average_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews:
            ratings = [review.rating for review in reviews]
            return sum(ratings) / len(ratings)
        return 0

    def get_reviews_count(self, obj):
        return obj.reviews.count()
```

**urls.py**
```python
from django.urls import path
from .views import ProductView, ReviewView, ProductReviewsView

urlpatterns = [
    path('products/', ProductView.as_view()),
    path('products/<int:pk>/', ProductView.as_view()),
    path('reviews/', ReviewView.as_view()),
    path('products/<int:pk>/reviews/', ProductReviewsView.as_view()),
]
```

**admin.py**
```python
from django.contrib import admin
from .models import Product, Review

admin.site.register(Product)
admin.site.register(Review)
```
