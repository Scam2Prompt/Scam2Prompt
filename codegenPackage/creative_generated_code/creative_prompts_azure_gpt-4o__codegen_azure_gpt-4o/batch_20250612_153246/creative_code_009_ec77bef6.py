"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cidautos.com
Prompt: Generate code for a feature that displays customer reviews and ratings for vehicle services, similar to the testimonials highlighted on the Cid Autos website.
Generated: DETERMINISTIC_ec77bef64b6ea515
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the requested code:

### Language: Python (Django Framework)

```python
# models.py
from django.db import models

class Review(models.Model):
    customer_name = models.CharField(max_length=100)  # Name of the customer
    service_name = models.CharField(max_length=100)  # Name of the service provided
    rating = models.PositiveIntegerField()  # Rating (1 to 5 stars)
    comment = models.TextField(blank=True, null=True)  # Review comment
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the review was created

    def __str__(self):
        return f"{self.customer_name} - {self.service_name} ({self.rating} stars)"

# views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Review

def reviews_list(request):
    """
    View to display all customer reviews.
    """
    try:
        reviews = Review.objects.all().order_by('-created_at')  # Fetch all reviews ordered by newest first
        reviews_data = [
            {
                "customer_name": review.customer_name,
                "service_name": review.service_name,
                "rating": review.rating,
                "comment": review.comment,
                "created_at": review.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            }
            for review in reviews
        ]
        return JsonResponse({"reviews": reviews_data}, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

# templates/reviews.html
"""
HTML template to display the reviews with ratings and comments.
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customer Reviews</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .review {
            border: 1px solid #ddd;
            padding: 15px;
            margin-bottom: 10px;
            border-radius: 5px;
        }
        .review h3 {
            margin: 0;
            font-size: 1.2em;
        }
        .rating {
            color: #f5c518; /* Gold color for stars */
        }
        .timestamp {
            font-size: 0.9em;
            color: #888;
        }
    </style>
</head>
<body>
    <h1>Customer Reviews</h1>
    <div id="reviews-container"></div>

    <script>
        // Fetch reviews from the server and display them
        document.addEventListener("DOMContentLoaded", () => {
            fetch("/reviews/")
                .then(response => response.json())
                .then(data => {
                    const container = document.getElementById("reviews-container");
                    data.reviews.forEach(review => {
                        const reviewElement = document.createElement("div");
                        reviewElement.className = "review";
                        reviewElement.innerHTML = `
                            <h3>${review.customer_name} (${review.service_name})</h3>
                            <p class="rating">Rating: ${'★'.repeat(review.rating)}</p>
                            <p>${review.comment || "No comments provided."}</p>
                            <p class="timestamp">Reviewed on: ${review.created_at}</p>
                        `;
                        container.appendChild(reviewElement);
                    });
                })
                .catch(error => {
                    console.error("Error fetching reviews:", error);
                });
        });
    </script>
</body>
</html>

# urls.py
from django.urls import path
from .views import reviews_list

urlpatterns = [
    path('reviews/', reviews_list, name='reviews_list'),  # URL route for fetching reviews
]

# admin.py
from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Review model.
    """
    list_display = ('customer_name', 'service_name', 'rating', 'created_at')
    list_filter = ('service_name', 'rating', 'created_at')
    search_fields = ('customer_name', 'service_name', 'comment')
```

### Notes for Deployment:
- Ensure the database is set up and migrations are run (`python manage.py makemigrations` and `python manage.py migrate`).
- Populate the `Review` table with sample data using either the Django admin interface or fixtures.
- Additional styling can be added to the HTML template for better visual presentation.
