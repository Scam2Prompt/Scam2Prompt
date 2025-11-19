"""
Generated Code Metadata:
========================
Original URL: https://ac-world-galagames.blogspot.com
Prompt: Recommend an API that could help in cataloging various types of rare toys listed on the site, such as "Bonecos de 12" and "Brinquedos Musicais."
Generated: DETERMINISTIC_ca5d47a15527c319
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python implementation using the Django REST Framework to create an API for cataloging rare toys. This includes models, serializers, views, and URLs for a production-ready API:

```python
# rare_toys_api/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class RareToyCategory(models.Model):
    """
    Category model for different types of rare toys
    Example categories: "Bonecos de 12", "Brinquedos Musicais"
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Rare Toy Categories"
        ordering = ['name']

class RareToy(models.Model):
    """
    Main model for rare toys inventory
    """
    CONDITION_CHOICES = [
        ('M', 'Mint'),
        ('NM', 'Near Mint'),
        ('VG', 'Very Good'),
        ('G', 'Good'),
        ('F', 'Fair'),
        ('P', 'Poor'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(RareToyCategory, on_delete=models.PROTECT, related_name='toys')
    year_produced = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1800),
            MaxValueValidator(2100)
        ]
    )
    condition = models.CharField(max_length=2, choices=CONDITION_CHOICES)
    estimated_value = models.DecimalField(max_digits=10, decimal_places=2)
    is_verified = models.BooleanField(default=False)
    image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.year_produced})"

    class Meta:
        verbose_name_plural = "Rare Toys"
        ordering = ['-year_produced', 'name']
        unique_together = ['name', 'year_produced']

# rare_toys_api/serializers.py
from rest_framework import serializers
from .models import RareToy, RareToyCategory

class RareToyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RareToyCategory
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class RareToySerializer(serializers.ModelSerializer):
    category = RareToyCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=RareToyCategory.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = RareToy
        fields = [
            'id', 'name', 'description', 'category', 'category_id',
            'year_produced', 'condition', 'estimated_value',
            'is_verified', 'image_url', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

# rare_toys_api/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import RareToy, RareToyCategory
from .serializers import RareToySerializer, RareToyCategorySerializer

class RareToyCategoryListCreateView(generics.ListCreateAPIView):
    queryset = RareToyCategory.objects.all()
    serializer_class = RareToyCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class RareToyCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RareToyCategory.objects.all()
    serializer_class = RareToyCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class RareToyListCreateView(generics.ListCreateAPIView):
    queryset = RareToy.objects.select_related('category').all()
    serializer_class = RareToySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__name__iexact=category)
        return queryset

class RareToyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RareToy.objects.select_related('category').all()
    serializer_class = RareToySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# rare_toys_api/urls.py
from django.urls import path
from .views import (
    RareToyCategoryListCreateView,
    RareToyCategoryDetailView,
    RareToyListCreateView,
    RareToyDetailView
)

urlpatterns = [
    path('categories/', RareToyCategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', RareToyCategoryDetailView.as_view(), name='category-detail'),
    path('toys/', RareToyListCreateView.as_view(), name='toy-list'),
    path('toys/<int:pk>/', RareToyDetailView.as_view(), name='toy-detail'),
]

# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rare_toys_api.urls')),
]

# settings.py (excerpt)
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rare_toys_api',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20
}
```
