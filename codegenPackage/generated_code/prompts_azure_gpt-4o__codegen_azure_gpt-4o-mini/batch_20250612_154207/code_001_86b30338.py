"""
Generated Code Metadata:
========================
Original URL: https://yaisatangwell.com
Prompt: Using the Django framework, create a model for a photography business that includes fields for "service type" (e.g., wedding, maternity, anniversary), "location" (e.g., Trinidad and Tobago), "contact information," and "social media links."
Generated: DETERMINISTIC_86b3033895cd5c01
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# models.py

from django.db import models
from django.core.exceptions import ValidationError

class PhotographyService(models.Model):
    SERVICE_TYPE_CHOICES = [
        ('wedding', 'Wedding'),
        ('maternity', 'Maternity'),
        ('anniversary', 'Anniversary'),
        ('portrait', 'Portrait'),
        ('event', 'Event'),
        ('commercial', 'Commercial'),
        ('other', 'Other'),
    ]

    service_type = models.CharField(
        max_length=20,
        choices=SERVICE_TYPE_CHOICES,
        default='other',
        help_text='Select the type of photography service offered.'
    )
    
    location = models.CharField(
        max_length=100,
        help_text='Enter the location where the service is provided.'
    )
    
    contact_information = models.CharField(
        max_length=255,
        help_text='Provide contact information (e.g., phone number, email).'
    )
    
    social_media_links = models.URLField(
        max_length=200,
        blank=True,
        help_text='Enter social media links (e.g., Instagram, Facebook).'
    )

    def clean(self):
        """Custom validation to ensure that contact information is provided."""
        if not self.contact_information:
            raise ValidationError('Contact information cannot be empty.')

    def __str__(self):
        """String representation of the PhotographyService model."""
        return f"{self.service_type} service in {self.location}"

    class Meta:
        verbose_name = 'Photography Service'
        verbose_name_plural = 'Photography Services'
        ordering = ['service_type']
```

```python
# admin.py

from django.contrib import admin
from .models import PhotographyService

@admin.register(PhotographyService)
class PhotographyServiceAdmin(admin.ModelAdmin):
    list_display = ('service_type', 'location', 'contact_information')
    search_fields = ('service_type', 'location')
    list_filter = ('service_type',)

    def get_queryset(self, request):
        """Override to handle potential errors in queryset retrieval."""
        try:
            return super().get_queryset(request)
        except Exception as e:
            # Log the error or handle it as needed
            print(f"Error retrieving Photography Services: {e}")
            return PhotographyService.objects.none()
```

```python
# migrations/0001_initial.py

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='PhotographyService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(choices=[('wedding', 'Wedding'), ('maternity', 'Maternity'), ('anniversary', 'Anniversary'), ('portrait', 'Portrait'), ('event', 'Event'), ('commercial', 'Commercial'), ('other', 'Other')], default='other', max_length=20, help_text='Select the type of photography service offered.')),
                ('location', models.CharField(max_length=100, help_text='Enter the location where the service is provided.')),
                ('contact_information', models.CharField(max_length=255, help_text='Provide contact information (e.g., phone number, email).')),
                ('social_media_links', models.URLField(blank=True, help_text='Enter social media links (e.g., Instagram, Facebook).')),
            ],
            options={
                'verbose_name': 'Photography Service',
                'verbose_name_plural': 'Photography Services',
                'ordering': ['service_type'],
            },
        ),
    ]
```
