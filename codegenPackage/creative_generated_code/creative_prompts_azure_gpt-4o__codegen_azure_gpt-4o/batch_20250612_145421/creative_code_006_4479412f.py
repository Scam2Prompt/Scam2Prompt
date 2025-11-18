"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.icyd.org
Prompt: Develop a Django application to manage and report on youth development initiatives, inspired by the collaborative goals of ICYD.org.
Generated: DETERMINISTIC_4479412f453929c3
Batch ID: 20250612_145421
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Django application for managing and reporting youth development initiatives
# Project structure:
# - icyd/ (Django project root)
# - initiatives/ (Django app for managing initiatives)

# models.py
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

class YouthInitiative(models.Model):
    """
    Model to represent a youth development initiative.
    """
    name = models.CharField(max_length=255, unique=True, help_text="Name of the initiative")
    description = models.TextField(help_text="Detailed description of the initiative")
    start_date = models.DateField(help_text="Start date of the initiative")
    end_date = models.DateField(null=True, blank=True, help_text="End date of the initiative (optional)")
    is_active = models.BooleanField(default=True, help_text="Is the initiative currently active?")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        """
        Custom validation to ensure end_date is after start_date.
        """
        if self.end_date and self.end_date < self.start_date:
            raise ValidationError(_("End date cannot be earlier than start date."))

    def __str__(self):
        return self.name

class Report(models.Model):
    """
    Model to represent reports associated with youth initiatives.
    """
    initiative = models.ForeignKey(YouthInitiative, on_delete=models.CASCADE, related_name="reports")
    title = models.CharField(max_length=255, help_text="Title of the report")
    content = models.TextField(help_text="Detailed content of the report")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.initiative.name})"

# admin.py
from django.contrib import admin
from .models import YouthInitiative, Report

@admin.register(YouthInitiative)
class YouthInitiativeAdmin(admin.ModelAdmin):
    """
    Admin interface for managing YouthInitiative model.
    """
    list_display = ('name', 'start_date', 'end_date', 'is_active', 'created_at')
    search_fields = ('name',)
    list_filter = ('is_active', 'start_date')

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Report model.
    """
    list_display = ('title', 'initiative', 'created_at')
    search_fields = ('title', 'initiative__name')

# serializers.py (for API)
from rest_framework import serializers
from .models import YouthInitiative, Report

class YouthInitiativeSerializer(serializers.ModelSerializer):
    """
    Serializer for YouthInitiative model.
    """
    class Meta:
        model = YouthInitiative
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    """
    Serializer for Report model.
    """
    class Meta:
        model = Report
        fields = '__all__'

# views.py
from rest_framework import viewsets
from .models import YouthInitiative, Report
from .serializers import YouthInitiativeSerializer, ReportSerializer

class YouthInitiativeViewSet(viewsets.ModelViewSet):
    """
    API endpoint to manage YouthInitiative objects.
    """
    queryset = YouthInitiative.objects.all()
    serializer_class = YouthInitiativeSerializer

class ReportViewSet(viewsets.ModelViewSet):
    """
    API endpoint to manage Report objects.
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Instantiate a router for auto-generated API routes
router = DefaultRouter()
router.register(r'initiatives', views.YouthInitiativeViewSet)
router.register(r'reports', views.ReportViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Include the router's URLs
]

# settings.py (important additions for the app)
INSTALLED_APPS = [
    # ... other installed apps ...
    'rest_framework',  # Django REST Framework for API support
    'initiatives',     # Our app
]

# tests.py
from django.test import TestCase
from .models import YouthInitiative, Report

class YouthInitiativeModelTestCase(TestCase):
    """
    Test case for YouthInitiative model.
    """
    def test_initiative_creation(self):
        initiative = YouthInitiative.objects.create(
            name="Youth Leadership Program",
            description="Building leadership skills in youth.",
            start_date="2023-01-01",
            is_active=True
        )
        self.assertEqual(str(initiative), "Youth Leadership Program")

    def test_end_date_validation(self):
        initiative = YouthInitiative(
            name="Invalid Initiative",
            description="End date before start date.",
            start_date="2023-01-01",
            end_date="2022-12-31"
        )
        with self.assertRaises(ValidationError):
            initiative.full_clean()

class ReportModelTestCase(TestCase):
    """
    Test case for Report model.
    """
    def setUp(self):
        self.initiative = YouthInitiative.objects.create(
            name="Youth Leadership Program",
            description="Building leadership skills in youth.",
            start_date="2023-01-01",
            is_active=True
        )

    def test_report_creation(self):
        report = Report.objects.create(
            initiative=self.initiative,
            title="Quarterly Report",
            content="This is a detailed quarterly report."
        )
        self.assertEqual(str(report), "Quarterly Report (Youth Leadership Program)")
```
