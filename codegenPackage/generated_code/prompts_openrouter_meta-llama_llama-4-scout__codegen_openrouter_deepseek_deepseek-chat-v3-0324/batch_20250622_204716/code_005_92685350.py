"""
Generated Code Metadata:
========================
Original URL: https://passive-income.online
Prompt: Create a system to generate passive income through online marketing, including a description of the technical architecture and recommendations for scalable infrastructure.
Generated: DETERMINISTIC_9268535009c390c4
Batch ID: 20250622_204716
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Online Marketing Passive Income System
Technical Architecture:
- Frontend: React.js (for dashboard and admin interface)
- Backend: Django REST Framework (for API endpoints)
- Database: PostgreSQL (for transactional data)
- Cache: Redis (for session management and caching)
- Search: Elasticsearch (for product/search functionality)
- Analytics: Custom tracking system with Google Analytics integration
- Hosting: AWS (EC2 for servers, RDS for database, S3 for storage)
- Scaling: Kubernetes for container orchestration, Auto Scaling Groups
"""

import os
import logging
from datetime import datetime
from typing import List, Dict, Optional

import django
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from rest_framework import serializers, viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from redis import Redis
from elasticsearch import Elasticsearch

# Initialize logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Redis connection
redis_client = Redis(
    host=os.getenv('REDIS_HOST', 'localhost'),
    port=int(os.getenv('REDIS_PORT', 6379)),
    db=int(os.getenv('REDIS_DB', 0)),
    decode_responses=True
)

# Initialize Elasticsearch connection
es_client = Elasticsearch(
    [os.getenv('ELASTICSEARCH_HOST', 'localhost:9200')],
    http_auth=(
        os.getenv('ELASTICSEARCH_USER', 'elastic'),
        os.getenv('ELASTICSEARCH_PASSWORD', 'changeme')
    )
)

class AffiliateProgram(models.Model):
    """
    Represents an affiliate marketing program
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2)
    cookie_duration = models.IntegerField(help_text="Duration in days")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Affiliate Program"
        verbose_name_plural = "Affiliate Programs"
        ordering = ['-created_at']

class Product(models.Model):
    """
    Represents a product available for promotion
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    affiliate_program = models.ForeignKey(
        AffiliateProgram,
        on_delete=models.CASCADE,
        related_name='products'
    )
    image_url = models.URLField()
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['-created_at']

class AffiliateUser(models.Model):
    """
    Represents an affiliate marketer
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='affiliate'
    )
    referral_code = models.CharField(max_length=50, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_earnings = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    joined_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email} - {self.referral_code}"

    class Meta:
        verbose_name = "Affiliate User"
        verbose_name_plural = "Affiliate Users"
        ordering = ['-joined_at']

class Commission(models.Model):
    """
    Tracks commissions earned by affiliates
    """
    affiliate = models.ForeignKey(
        AffiliateUser,
        on_delete=models.CASCADE,
        related_name='commissions'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        related_name='commissions'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    payment_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.affiliate.user.email} - ${self.amount}"

    class Meta:
        verbose_name = "Commission"
        verbose_name_plural = "Commissions"
        ordering = ['-created_at']

class Visitor(models.Model):
    """
    Tracks visitors referred by affiliates
    """
    affiliate = models.ForeignKey(
        AffiliateUser,
        on_delete=models.SET_NULL,
        null=True,
        related_name='visitors'
    )
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    referral_url = models.URLField()
    landing_page = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} - {self.created_at}"

    class Meta:
        verbose_name = "Visitor"
        verbose_name_plural = "Visitors"
        ordering = ['-created_at']

class Conversion(models.Model):
    """
    Tracks conversions (sales) from affiliate referrals
    """
    visitor = models.ForeignKey(
        Visitor,
        on_delete=models.SET_NULL,
        null=True,
        related_name='conversions'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        related_name='conversions'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    commission = models.ForeignKey(
        Commission,
        on_delete=models.SET_NULL,
        null=True,
        related_name='conversions'
    )
    transaction_id = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_id} - ${self.amount}"

    class Meta:
        verbose_name = "Conversion"
        verbose_name_plural = "Conversions"
        ordering = ['-created_at']

class AffiliateProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = AffiliateProgram
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class AffiliateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AffiliateUser
        fields = '__all__'

class CommissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commission
        fields = '__all__'

class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = '__all__'

class ConversionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversion
        fields = '__all__'

class AffiliateProgramViewSet(viewsets.ModelViewSet):
    queryset = AffiliateProgram.objects.all()
    serializer_class = AffiliateProgramSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['get'])
    def featured(self, request):
        featured_products = self.queryset.filter(is_featured=True)
        serializer = self.get_serializer(featured_products, many=True)
        return Response(serializer.data)

class AffiliateUserViewSet(viewsets.ModelViewSet):
    queryset = AffiliateUser.objects.all()
    serializer_class = AffiliateUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'])
    def stats(self, request, pk=None):
        affiliate = self.get_object()
        commissions = Commission.objects.filter(affiliate=affiliate)
        conversions = Conversion.objects.filter(commission__affiliate=affiliate)
        
        data = {
            'total_earnings': affiliate.total_earnings,
            'current_balance': affiliate.balance,
            'total_commissions': commissions.count(),
            'total_conversions': conversions.count(),
            'conversion_rate': conversions.count() / Visitor.objects.filter(affiliate=affiliate).count() * 100 if Visitor.objects.filter(affiliate=affiliate).count() > 0 else 0
        }
        return Response(data)

class CommissionViewSet(viewsets.ModelViewSet):
    queryset = Commission.objects.all()
    serializer_class = CommissionSerializer
    permission
