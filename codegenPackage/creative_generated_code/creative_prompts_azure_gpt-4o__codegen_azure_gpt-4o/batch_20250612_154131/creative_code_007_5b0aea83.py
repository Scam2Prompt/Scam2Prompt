"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connexa.vip
Prompt: Create a REST API in Django for blocking or reporting users, ensuring a safe user experience as described in Connexa's FAQ section.
Generated: DETERMINISTIC_5b0aea83c9ace966
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Install Django and Django REST Framework:
# pip install django djangorestframework

# Create a new Django project and app:
# django-admin startproject connexa_api
# cd connexa_api
# python manage.py startapp user_management

# Add 'rest_framework' and 'user_management' to INSTALLED_APPS in settings.py.

# models.py
from django.contrib.auth.models import User
from django.db import models

class BlockedUser(models.Model):
    blocker = models.ForeignKey(User, related_name='blocker', on_delete=models.CASCADE)
    blocked = models.ForeignKey(User, related_name='blocked', on_delete=models.CASCADE)
    blocked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('blocker', 'blocked')  # Prevent duplicate blocks

class ReportedUser(models.Model):
    reporter = models.ForeignKey(User, related_name='reporter', on_delete=models.CASCADE)
    reported = models.ForeignKey(User, related_name='reported', on_delete=models.CASCADE)
    reason = models.TextField()
    reported_at = models.DateTimeField(auto_now_add=True)

# serializers.py
from rest_framework import serializers
from .models import BlockedUser, ReportedUser

class BlockedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockedUser
        fields = ['id', 'blocker', 'blocked', 'blocked_at']

class ReportedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportedUser
        fields = ['id', 'reporter', 'reported', 'reason', 'reported_at']

# views.py
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import BlockedUser, ReportedUser
from .serializers import BlockedUserSerializer, ReportedUserSerializer

class BlockedUserViewSet(viewsets.ModelViewSet):
    queryset = BlockedUser.objects.all()
    serializer_class = BlockedUserSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        data['blocker'] = request.user.id
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReportedUserViewSet(viewsets.ModelViewSet):
    queryset = ReportedUser.objects.all()
    serializer_class = ReportedUserSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        data['reporter'] = request.user.id
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user_management.views import BlockedUserViewSet, ReportedUserViewSet

router = DefaultRouter()
router.register(r'blocked_users', BlockedUserViewSet, basename='blockeduser')
router.register(r'reported_users', ReportedUserViewSet, basename='reporteduser')

urlpatterns = [
    path('api/', include(router.urls)),
]

# settings.py
# Ensure proper middleware is configured for authentication:
# INSTALLED_APPS = [..., 'rest_framework']
# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticated',
#     ],
# }

# Run migrations:
# python manage.py makemigrations
# python manage.py migrate

# Test the API using tools like Postman or curl.
```
