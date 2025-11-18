"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fanzyfashion.in
Prompt: Generate a script using Django to manage product reviews and ratings, including calculating the average customer rating for each product.
Generated: DETERMINISTIC_cb1f715229e6240b
Batch ID: 20250612_153224
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
    Model representing a product.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    def calculate_average_rating(self):
        """
        Calculate the average rating for the product based on its reviews.
        Returns the average rating as a float or None if there are no reviews.
        """
        reviews = self.reviews.all()  # Get all reviews for this product
        if reviews.exists():
            return reviews.aggregate(models.Avg('rating'))['rating__avg']
        return None


class Review(models.Model):
    """
    Model representing a review for a product.
    """
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()  # Rating should be between 1 and 5
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.product.name} - Rating: {self.rating}"

    def save(self, *args, **kwargs):
        """
        Validate rating range before saving the review.
        """
        if not (1 <= self.rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        super().save(*args, **kwargs)
```

```python
# views.py

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Product, Review

def product_reviews(request, product_id):
    """
    View to fetch reviews and average rating for a given product.
    """
    product = get_object_or_404(Product, id=product_id)
    average_rating = product.calculate_average_rating()
    reviews = product.reviews.all().values('id', 'rating', 'comment', 'created_at')

    return JsonResponse({
        'product': product.name,
        'average_rating': average_rating,
        'reviews': list(reviews)
    })


def create_review(request, product_id):
    """
    View to create a new review for a product.
    Expects POST data in the format { "rating": <int>, "comment": <str> }.
    """
    if request.method != "POST":
        return JsonResponse({"error": "Invalid HTTP method"}, status=405)

    product = get_object_or_404(Product, id=product_id)

    try:
        rating = int(request.POST.get('rating'))
        comment = request.POST.get('comment', None)

        review = Review.objects.create(product=product, rating=rating, comment=comment)
        return JsonResponse({"success": "Review created successfully", "review_id": review.id})
    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=400)
    except Exception as e:
        return JsonResponse({"error": "An unexpected error occurred"}, status=500)
```

```python
# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:product_id>/reviews/', views.product_reviews, name='product_reviews'),
    path('product/<int:product_id>/create-review/', views.create_review, name='create_review'),
]
```

```python
# admin.py

from django.contrib import admin
from .models import Product, Review

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Product model.
    """
    list_display = ('name', 'description')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Review model.
    """
    list_display = ('product', 'rating', 'created_at')
    list_filter = ('product', 'rating', 'created_at')
```

```python
# tests.py

from django.test import TestCase
from .models import Product, Review

class ProductReviewsTestCase(TestCase):
    def setUp(self):
        """
        Set up test data.
        """
        self.product = Product.objects.create(name="Test Product", description="Test Description")
        Review.objects.create(product=self.product, rating=5, comment="Great product!")
        Review.objects.create(product=self.product, rating=3, comment="Average product.")

    def test_average_rating(self):
        """
        Test the calculation of average rating for a product.
        """
        average_rating = self.product.calculate_average_rating()
        self.assertEqual(average_rating, 4.0)  # (5 + 3) / 2 = 4.0

    def test_review_creation(self):
        """
        Test creating a review successfully.
        """
        review = Review.objects.create(product=self.product, rating=4, comment="Good product.")
        self.assertEqual(review.rating, 4)
        self.assertEqual(review.comment, "Good product.")
```
