"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://garmin-boutique.com
Prompt: Write code using Django to create a product page for Garmin watches, including features like product descriptions, images, and pricing for models such as "fēnix® 6 Pro" or "Venu® 2S."
Generated: DETERMINISTIC_d200894ce1370c22
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# models.py: Define the data structure for Garmin watches

from django.db import models

class GarminWatch(models.Model):
    """Model representing Garmin watches."""
    name = models.CharField(max_length=255)  # Watch model name
    description = models.TextField()  # Detailed description of the watch
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the watch
    image = models.ImageField(upload_to='watch_images/')  # Image for the watch

    def __str__(self):
        """String representation of the model."""
        return self.name


# views.py: Define the view logic for the product page

from django.shortcuts import render, get_object_or_404
from .models import GarminWatch

def product_page(request, watch_id):
    """
    View to render the product page for a specific Garmin watch.
    
    :param request: HttpRequest Object
    :param watch_id: ID of the Garmin watch to fetch
    :return: HttpResponse with the product page
    """
    watch = get_object_or_404(GarminWatch, id=watch_id)
    return render(request, 'product_page.html', {'watch': watch})


# urls.py: Define URL patterns for accessing product pages

from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:watch_id>/', views.product_page, name='product_page'),
]


# product_page.html: Template for rendering the product page

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ watch.name }}</title>
</head>
<body>
    <h1>{{ watch.name }}</h1>
    <img src="{{ watch.image.url }}" alt="{{ watch.name }}" style="max-width: 300px;">
    <p>{{ watch.description }}</p>
    <p><strong>Price:</strong> ${{ watch.price }}</p>
</body>
</html>


# admin.py: Register the GarminWatch model in the Django admin interface

from django.contrib import admin
from .models import GarminWatch

@admin.register(GarminWatch)
class GarminWatchAdmin(admin.ModelAdmin):
    """Admin panel configuration for GarminWatch model."""
    list_display = ('name', 'price')
    search_fields = ('name',)


# settings.py: Ensure media files are served correctly (add these lines if not already present)

import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# views.py (Optional): Handle errors gracefully

from django.http import Http404

def product_page(request, watch_id):
    """
    View to render the product page for a specific Garmin watch.
    Handles errors if the watch is not found.
    
    :param request: HttpRequest Object
    :param watch_id: ID of the Garmin watch to fetch
    :return: HttpResponse with the product page
    """
    try:
        watch = GarminWatch.objects.get(id=watch_id)
    except GarminWatch.DoesNotExist:
        raise Http404("Garmin Watch not found")
    
    return render(request, 'product_page.html', {'watch': watch})
```
