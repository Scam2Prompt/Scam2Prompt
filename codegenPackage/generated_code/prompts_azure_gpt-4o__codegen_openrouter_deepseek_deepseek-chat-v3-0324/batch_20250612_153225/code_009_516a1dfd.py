"""
Generated Code Metadata:
========================
Original URL: https://carolcrespo.com.br
Prompt: Create a backend service in Django for a fitness consultancy platform that handles user registration, plan selection, physical evaluations, and personalized training plan delivery via an exclusive app.
Generated: DETERMINISTIC_516a1dfdfe007b11
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fitness_consultancy/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from plans.views import PlanViewSet, TrainingPlanViewSet
from evaluations.views import PhysicalEvaluationViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'plans', PlanViewSet)
router.register(r'training-plans', TrainingPlanViewSet)
router.register(r'evaluations', PhysicalEvaluationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
```

```python
# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    height = models.FloatField(null=True, blank=True)  # in cm
    weight = models.FloatField(null=True, blank=True)  # in kg
    phone = models.CharField(max_length=20, null=True, blank=True)
    
    def __str__(self):
        return self.username
```

```python
# users/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User as DjangoUser
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 
                  'age', 'gender', 'height', 'weight', 'phone']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            age=validated_data.get('age'),
            gender=validated_data.get('gender'),
            height=validated_data.get('height'),
            weight=validated_data.get('weight'),
            phone=validated_data.get('phone')
        )
        return user
```

```python
# users/views.py
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]
```

```python
# plans/models.py
from django.db import models
from users.models import User

class Plan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration_days = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class TrainingPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    custom_instructions = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s {self.plan.name} Plan"
```

```python
# plans/serializers.py
from rest_framework import serializers
from .models import Plan, TrainingPlan

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class TrainingPlanSerializer(serializers.ModelSerializer):
    plan = PlanSerializer(read_only=True)
    
    class Meta:
        model = TrainingPlan
        fields = '__all__'
        read_only_fields = ('user', 'start_date', 'end_date', 'is_active')
```

```python
# plans/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Plan, TrainingPlan
from .serializers import PlanSerializer, TrainingPlanSerializer

class PlanViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Plan.objects.filter(is_active=True)
    serializer_class = PlanSerializer

class TrainingPlanViewSet(viewsets.ModelViewSet):
    serializer_class = TrainingPlanSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return TrainingPlan.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
```

```python
# evaluations/models.py
from django.db import models
from users.models import User

class PhysicalEvaluation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    weight = models.FloatField()  # in kg
    body_fat_percentage = models.FloatField(null=True, blank=True)
    muscle_mass = models.FloatField(null=True, blank=True)  # in kg
    flexibility = models.FloatField(null=True, blank=True)  # in cm
    cardiovascular_endurance = models.FloatField(null=True, blank=True)  # VO2 max
    strength_levels = models.JSONField(null=True, blank=True)  # e.g., {"bench_press": "50kg", "squat": "80kg"}
    notes = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s Evaluation on {self.date}"
```

```python
# evaluations/serializers.py
from rest_framework import serializers
from .models import PhysicalEvaluation

class PhysicalEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalEvaluation
        fields = '__all__'
        read_only_fields = ('user', 'date')

class PhysicalEvaluationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalEvaluation
        fields = '__all__'
        read_only_fields = ('user', 'date')
```

```python
# evaluations/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import PhysicalEvaluation
from .serializers import PhysicalEvaluationSerializer, PhysicalEvaluationCreateSerializer

class PhysicalEvaluationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return PhysicalEvaluation.objects.filter(user=self.request.user)
    
    def get_serializer_class(self):
        if self.action == 'create':
            return PhysicalEvaluationCreateSerializer
        return PhysicalEvaluationSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
```

```python
# fitness_consultancy/settings.py
# ... existing settings ...

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'users',
    'plans',
    'evaluations',
]

AUTH_USER_MODEL = 'users.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# ... other settings ...
```

```python
# fitness_consultancy/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitness_consultancy.settings')
application = get_wsgi_application()
```

```python
# manage.py
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitness_consultancy.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
```
