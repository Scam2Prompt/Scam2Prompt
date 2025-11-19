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

```python
# models.py

from django.db import models
from django.core.exceptions import ValidationError

class Product(models.Model):
    """Model representing a product."""
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    """Model representing a product review."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(default=1)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        """Validate the rating to be between 1 and 5."""
        if self.rating < 1 or self.rating > 5:
            raise ValidationError('Rating must be between 1 and 5.')

    def save(self, *args, **kwargs):
        """Override save method to ensure validation is called."""
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Review for {self.product.name} - Rating: {self.rating}'

# views.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Product, Review
from .forms import ReviewForm

def product_detail(request, product_id):
    """View to display product details and reviews."""
    product = get_object_or_404(Product, id=product_id)
    reviews = product.reviews.all()
    average_rating = reviews.aggregate(models.Avg('rating'))['rating__avg'] or 0

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            return HttpResponseRedirect(reverse('product_detail', args=[product.id]))
    else:
        form = ReviewForm()

    context = {
        'product': product,
        'reviews': reviews,
        'average_rating': average_rating,
        'form': form,
    }
    return render(request, 'product_detail.html', context)

# forms.py

from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    """Form for submitting a product review."""
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(choices=[(i, i) for i in range(1, 6)]),
            'comment': forms.Textarea(attrs={'rows': 4}),
        }

# urls.py

from django.urls import path
from .views import product_detail

urlpatterns = [
    path('product/<int:product_id>/', product_detail, name='product_detail'),
]

# product_detail.html

{% extends "base_generic.html" %}

{% block content %}
  <h1>{{ product.name }}</h1>
  <p>{{ product.description }}</p>
  <h2>Average Rating: {{ average_rating|floatformat:1 }}</h2>

  <h3>Reviews:</h3>
  <ul>
    {% for review in reviews %}
      <li>{{ review.rating }} - {{ review.comment }}</li>
    {% empty %}
      <li>No reviews yet.</li>
    {% endfor %}
  </ul>

  <h3>Submit a Review:</h3>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
  </form>
{% endblock %}
```
