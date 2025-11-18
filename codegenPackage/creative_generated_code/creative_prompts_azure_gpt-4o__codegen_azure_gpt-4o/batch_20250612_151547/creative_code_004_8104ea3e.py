"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.brothernz.com
Prompt: Suggest a library or framework to implement a "Wish List" feature for an e-commerce site selling Brother embroidery machines, ensuring compatibility with multi-currency support.
Generated: DETERMINISTIC_8104ea3e4ea4474b
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation using the Django framework with Django Rest Framework (DRF) for the "Wish List" feature. It includes multi-currency support using the `moneyed` and `django-money` libraries.

```python
# models.py

from django.contrib.auth.models import User
from django.db import models
from djmoney.models.fields import MoneyField

class EmbroideryMachine(models.Model):
    """
    Represents an embroidery machine product.
    """
    name = models.CharField(max_length=255, unique=True)  # Name of the machine
    description = models.TextField(blank=True)  # Description of the machine
    price = MoneyField(max_digits=10, decimal_places=2, default_currency="USD")  # Price with multi-currency support

    def __str__(self):
        return self.name


class WishList(models.Model):
    """
    Represents a user's wish list.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlists")  # One-to-many relationship with User
    items = models.ManyToManyField(EmbroideryMachine, related_name="wishlist_items")  # Many-to-many relationship with EmbroideryMachine

    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the wishlist is created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for last update of the wishlist

    def __str__(self):
        return f"{self.user.username}'s Wish List"

# serializers.py

from rest_framework import serializers
from djmoney.contrib.django_rest_framework import MoneyField
from .models import EmbroideryMachine, WishList

class EmbroideryMachineSerializer(serializers.ModelSerializer):
    """
    Serializer for EmbroideryMachine model.
    """
    price = MoneyField()

    class Meta:
        model = EmbroideryMachine
        fields = ['id', 'name', 'description', 'price']


class WishListSerializer(serializers.ModelSerializer):
    """
    Serializer for WishList model.
    """
    items = EmbroideryMachineSerializer(many=True)  # Nested serialization for items in the wish list

    class Meta:
        model = WishList
        fields = ['id', 'user', 'items', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

# views.py

from rest_framework import viewsets, permissions
from rest_framework.exceptions import ValidationError
from .models import EmbroideryMachine, WishList
from .serializers import EmbroideryMachineSerializer, WishListSerializer

class EmbroideryMachineViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing embroidery machines.
    """
    queryset = EmbroideryMachine.objects.all()
    serializer_class = EmbroideryMachineSerializer
    permission_classes = [permissions.IsAdminUser]  # Restrict access to admin users


class WishListViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing user wish lists.
    """
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
    permission_classes = [permissions.IsAuthenticated]  # Restrict access to authenticated users

    def perform_create(self, serializer):
        """
        Overriding create method to automatically assign the current user to the wish list.
        """
        # Ensure the user doesn't create multiple wish lists
        if WishList.objects.filter(user=self.request.user).exists():
            raise ValidationError("You already have a wish list.")
        serializer.save(user=self.request.user)

# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmbroideryMachineViewSet, WishListViewSet

router = DefaultRouter()
router.register(r'embroidery-machines', EmbroideryMachineViewSet)
router.register(r'wishlists', WishListViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# settings.py

INSTALLED_APPS = [
    ...
    'rest_framework',
    'djmoney',
    'myapp',  # Replace 'myapp' with the actual name of your application
]

# Ensure you have proper middleware and currency settings
```

### Required Installation:
1. Install Django and Django Rest Framework:
   ```
   pip install django djangorestframework
   ```
2. Install `django-money` for multi-currency support:
   ```
   pip install django-money
   ```
