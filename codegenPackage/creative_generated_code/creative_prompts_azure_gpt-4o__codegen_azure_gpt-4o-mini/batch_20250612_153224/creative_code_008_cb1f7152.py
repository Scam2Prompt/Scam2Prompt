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
# Import necessary packages
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Product(models.Model):
    """
    Represents a product that can be reviewed.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    """
    Represents a review for a product.
    """
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=1)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('product', 'user')  # Prevent duplicate reviews from the same user

    def clean(self):
        """
        Validate the rating field to ensure it is within the allowed range.
        """
        if self.rating < 1 or self.rating > 5:
            raise ValidationError('Rating must be between 1 and 5.')

    def save(self, *args, **kwargs):
        """
        Override save method to apply custom validation logic.
        """
        self.clean()  # Ensure the review is valid before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Review by {self.user.username} on {self.product.name}'


class ProductReviewManager:
    """
    A simple manager class to handle product review operations.
    """

    @staticmethod
    def calculate_average_rating(product):
        """
        Calculate the average rating for a given product.
        
        Args:
            product (Product): The product for which to calculate the average rating.

        Returns:
            float: The average rating or 0 if there are no reviews.
        """
        reviews = product.reviews.all()
        if reviews.exists():
            average_rating = reviews.aggregate(models.Avg('rating'))['rating__avg']
            return round(average_rating, 2)  # Return rounded average
        return 0.0  # Return 0 if no reviews exist


# Example usage:
# Create a product
# product = Product.objects.create(name='Laptop', description='A high-performance laptop')

# Create a review
# review = Review.objects.create(product=product, user=request.user, rating=5, comment='Excellent laptop!')

# Calculate average rating for the product
# average_rating = ProductReviewManager.calculate_average_rating(product)
# print(f'Average rating for {product.name}: {average_rating}')
```

This code sets up a simple Django model structure for managing product reviews and ratings, including error handling for rating validation, and a manager class to calculate the average rating per product.
