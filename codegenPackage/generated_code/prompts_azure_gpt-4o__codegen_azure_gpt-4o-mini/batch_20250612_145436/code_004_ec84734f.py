"""
Generated Code Metadata:
========================
Original URL: https://sit.d1jkap9jqfwf3j.amplifyapp.com
Prompt: Create a Python script using the Django framework to implement a "new arrivals" feature for an e-commerce site. Include functionality for displaying recently added products with their prices and categories.
Generated: DETERMINISTIC_ec84734f2310baa0
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules from Django
from django.db import models
from django.shortcuts import render
from django.urls import path
from django.views import View
from django.utils import timezone

# Define the Product model
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create a view to display new arrivals
class NewArrivalsView(View):
    template_name = 'new_arrivals.html'

    def get(self, request):
        try:
            # Fetch products added in the last 30 days
            new_arrivals = Product.objects.filter(date_added__gte=timezone.now() - timezone.timedelta(days=30)).order_by('-date_added')
            context = {
                'new_arrivals': new_arrivals
            }
            return render(request, self.template_name, context)
        except Exception as e:
            # Log the error and return an error response
            print(f"Error fetching new arrivals: {e}")
            return render(request, self.template_name, {'error': 'Unable to fetch new arrivals.'})

# Define URL patterns
urlpatterns = [
    path('new-arrivals/', NewArrivalsView.as_view(), name='new_arrivals'),
]

# Sample HTML template (new_arrivals.html)
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>New Arrivals</title>
</head>
<body>
    <h1>New Arrivals</h1>
    {% if error %}
        <p>{{ error }}</p>
    {% else %}
        <ul>
            {% for product in new_arrivals %}
                <li>
                    <strong>{{ product.name }}</strong><br>
                    Price: ${{ product.price }}<br>
                    Category: {{ product.category }}<br>
                    Added on: {{ product.date_added|date:"Y-m-d H:i" }}
                </li>
            {% empty %}
                <li>No new arrivals at this time.</li>
            {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
"""

# Note: Ensure to run migrations to create the Product table in the database.
# Use the following commands in the terminal:
# python manage.py makemigrations
# python manage.py migrate
```
