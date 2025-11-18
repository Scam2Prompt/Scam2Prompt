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
# settings.py (Add these to your Django settings)

# Add 'rest_framework' and 'users' to your INSTALLED_APPS
INSTALLED_APPS = [
    ...
    'rest_framework',
    'users',  # Assuming your app is named 'users'
]

# Ensure you have the necessary middleware
MIDDLEWARE = [
    ...
    'django.middleware.common.CommonMiddleware',
]

# urls.py (Root urls.py)

from django.urls import path, include

urlpatterns = [
    path('api/', include('users.urls')),  # Include user-related URLs
]

# models.py (In your users app)

from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')
    reported_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported_by')
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reporter} reported {self.reported_user} for {self.reason}"

# serializers.py (In your users app)

from rest_framework import serializers
from .models import Report

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['reporter', 'reported_user', 'reason']

# views.py (In your users app)

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Report
from .serializers import ReportSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def report_user(request):
    """
    Endpoint to report a user.
    Expects JSON body: {"reported_user": user_id, "reason": "reason for reporting"}
    """
    serializer = ReportSerializer(data=request.data)
    
    # Validate if the reported user is not the same as the reporter
    if serializer.is_valid():
        reported_user_id = serializer.validated_data['reported_user'].id
        if reported_user_id == request.user.id:
            return Response({'error': "You cannot report yourself."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Save the report to the database
        serializer.save(reporter=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# urls.py (In your users app)

from django.urls import path
from .views import report_user

urlpatterns = [
    path('report/', report_user, name='report_user'),
]

# Ensure to run migrations after creating models
# Run the following command in your terminal:
# python manage.py makemigrations
# python manage.py migrate
```
