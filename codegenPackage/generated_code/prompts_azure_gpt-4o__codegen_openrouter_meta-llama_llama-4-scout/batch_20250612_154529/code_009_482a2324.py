"""
Generated Code Metadata:
========================
Original URL: https://aavelend.eu
Prompt: Write code to implement a search functionality for the website's group listings using Flask or Django, allowing users to filter groups by category and member count.
Generated: DETERMINISTIC_482a23241f29cb23
Batch ID: 20250612_154529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Group Listings Search Functionality using Django**

### models.py
```python
from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    member_count = models.IntegerField()

    def __str__(self):
        return self.name
```

### views.py
```python
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import Group
from django.core.exceptions import ObjectDoesNotExist

@require_GET
def search_groups(request):
    try:
        category = request.GET.get('category')
        member_count_min = request.GET.get('member_count_min', None)
        member_count_max = request.GET.get('member_count_max', None)

        groups = Group.objects.all()

        if category:
            groups = groups.filter(category=category)

        if member_count_min:
            groups = groups.filter(member_count__gte=member_count_min)

        if member_count_max:
            groups = groups.filter(member_count__lte=member_count_max)

        groups_data = [{'id': group.id, 'name': group.name, 'category': group.category, 'member_count': group.member_count} for group in groups]

        return JsonResponse({'groups': groups_data})
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Groups not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
```

### urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('search/groups/', views.search_groups, name='search_groups'),
]
```

### serializers.py (Optional, for more complex data serialization)
```python
from rest_framework import serializers
from .models import Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'category', 'member_count']
```

### api/views.py (Optional, using Django Rest Framework)
```python
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Group
from .serializers import GroupSerializer
from rest_framework import status

class GroupSearchView(APIView):
    def get(self, request):
        try:
            category = request.GET.get('category')
            member_count_min = request.GET.get('member_count_min', None)
            member_count_max = request.GET.get('member_count_max', None)

            groups = Group.objects.all()

            if category:
                groups = groups.filter(category=category)

            if member_count_min:
                groups = groups.filter(member_count__gte=member_count_min)

            if member_count_max:
                groups = groups.filter(member_count__lte=member_count_max)

            serializer = GroupSerializer(groups, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
```

### api/urls.py (Optional)
```python
from django.urls import path
from . import api

urlpatterns = [
    path('search/groups/', api.GroupSearchView.as_view(), name='search_groups'),
]
```
