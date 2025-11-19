"""
Generated Code Metadata:
========================
Original URL: https://laotaigroup.com
Prompt: Suggest a framework for developing a project tracking system that integrates environmental and social impact assessments, as highlighted by Lao Tai Trading - Investment Group.
Generated: DETERMINISTIC_3baf0b9212c3ca83
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Project Tracking System with Environmental and Social Impact Assessments
# Framework: Django (Python) with REST API capabilities

# File: requirements.txt
Django==4.2.7
djangorestframework==3.14.0
django-environ==0.11.2
psycopg2-binary==2.9.7  # For PostgreSQL support
django-filter==23.3
drf-yasg==1.21.5  # For API documentation
python-dotenv==1.0.0

# File: core/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    organization = models.CharField(max_length=255, blank=True)
    role = models.CharField(max_length=100, blank=True)

class Project(models.Model):
    STATUS_CHOICES = [
        ('planned', 'Planned'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planned')
    budget = models.DecimalField(max_digits=15, decimal_places=2)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='managed_projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class EnvironmentalImpact(models.Model):
    IMPACT_LEVEL = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='environmental_impacts')
    assessment_date = models.DateField()
    impact_type = models.CharField(max_length=100)
    description = models.TextField()
    mitigation_measures = models.TextField()
    impact_level = models.CharField(max_length=20, choices=IMPACT_LEVEL)
    is_resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class SocialImpact(models.Model):
    IMPACT_LEVEL = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='social_impacts')
    assessment_date = models.DateField()
    stakeholder_group = models.CharField(max_length=100)
    impact_description = models.TextField()
    mitigation_measures = models.TextField()
    impact_level = models.CharField(max_length=20, choices=IMPACT_LEVEL)
    is_resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class ImpactMonitoring(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='impact_monitoring')
    monitoring_date = models.DateField()
    environmental_notes = models.TextField(blank=True)
    social_notes = models.TextField(blank=True)
    compliance_status = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

# File: core/serializers.py
from rest_framework import serializers
from .models import Project, EnvironmentalImpact, SocialImpact, ImpactMonitoring, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'organization', 'role']

class ProjectSerializer(serializers.ModelSerializer):
    manager = UserSerializer(read_only=True)
    
    class Meta:
        model = Project
        fields = '__all__'

class EnvironmentalImpactSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvironmentalImpact
        fields = '__all__'

class SocialImpactSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialImpact
        fields = '__all__'

class ImpactMonitoringSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    
    class Meta:
        model = ImpactMonitoring
        fields = '__all__'

# File: core/views.py
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Project, EnvironmentalImpact, SocialImpact, ImpactMonitoring
from .serializers import (
    ProjectSerializer,
    EnvironmentalImpactSerializer,
    SocialImpactSerializer,
    ImpactMonitoringSerializer
)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'manager']
    search_fields = ['name', 'description']
    ordering_fields = ['start_date', 'end_date', 'created_at']

class EnvironmentalImpactViewSet(viewsets.ModelViewSet):
    queryset = EnvironmentalImpact.objects.all()
    serializer_class = EnvironmentalImpactSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['project', 'impact_level', 'is_resolved']

class SocialImpactViewSet(viewsets.ModelViewSet):
    queryset = SocialImpact.objects.all()
    serializer_class = SocialImpactSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['project', 'impact_level', 'is_resolved']

class ImpactMonitoringViewSet(viewsets.ModelViewSet):
    queryset = ImpactMonitoring.objects.all()
    serializer_class = ImpactMonitoringSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['project', 'compliance_status']

# File: core/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Project, EnvironmentalImpact, SocialImpact, ImpactMonitoring

admin.site.register(User, UserAdmin)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'start_date', 'end_date', 'manager')
    list_filter = ('status', 'start_date')
    search_fields = ('name', 'description')

@admin.register(EnvironmentalImpact)
class EnvironmentalImpactAdmin(admin.ModelAdmin):
    list_display = ('project', 'impact_type', 'impact_level', 'assessment_date', 'is_resolved')
    list_filter = ('impact_level', 'is_resolved')
    search_fields = ('impact_type', 'description')

@admin.register(SocialImpact)
class SocialImpactAdmin(admin.ModelAdmin):
    list_display = ('project', 'stakeholder_group', 'impact_level', 'assessment_date', 'is_resolved')
    list_filter = ('impact_level', 'is_resolved')
    search_fields = ('stakeholder_group', 'impact_description')

@admin.register(ImpactMonitoring)
class ImpactMonitoringAdmin(admin.ModelAdmin):
    list_display = ('project', 'monitoring_date', 'compliance_status', 'created_by')
    list_filter = ('compliance_status', 'monitoring_date')
    search_fields = ('environmental_notes', 'social_notes')

# File: core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProjectViewSet,
    EnvironmentalImpactViewSet,
    SocialImpactViewSet,
    ImpactMonitoringViewSet
)

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'environmental-impacts', EnvironmentalImpactViewSet)
router.register(r'social-impacts', SocialImpactViewSet)
router.register(r'impact-monitoring', ImpactMonitoringViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# File: config/settings.py (partial)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'drf_yasg',
    'core',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20
}

# File: config/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.views
