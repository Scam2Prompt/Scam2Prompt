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
from django.core.validators import URLValidator, EmailValidator, RegexValidator

class PhotographyBusiness(models.Model):
    """
    Model representing a photography business.

    Attributes:
        service_types (list): List of available service types.
        location (str): Location of the photography business.
        contact_information (str): Contact information of the photography business.
        social_media_links (dict): Social media links of the photography business.
    """

    class ServiceType(models.TextChoices):
        """Enum for service types."""
        WEDDING = 'wedding', 'Wedding'
        MATERNITY = 'maternity', 'Maternity'
        ANNIVERSARY = 'anniversary', 'Anniversary'
        OTHER = 'other', 'Other'

    class Meta:
        verbose_name = 'Photography Business'
        verbose_name_plural = 'Photography Businesses'

    service_types = models.ManyToManyField(
        ServiceType,
        help_text='Select the service types offered by the business.'
    )
    location = models.CharField(
        max_length=255,
        help_text='Enter the location of the photography business.'
    )
    phone_number = models.CharField(
        max_length=20,
        validators=[RegexValidator(r'^\d{3}-\d{3}-\d{4}$', 'Invalid phone number format. Use XXX-XXX-XXXX.')],
        help_text='Enter the phone number of the photography business (XXX-XXX-XXXX).'
    )
    email = models.EmailField(
        max_length=255,
        validators=[EmailValidator],
        help_text='Enter the email address of the photography business.'
    )
    website = models.CharField(
        max_length=255,
        validators=[URLValidator],
        help_text='Enter the website URL of the photography business.',
        blank=True,
        null=True
    )
    social_media_links = models.JSONField(
        help_text='Enter the social media links of the photography business.',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'Photography Business - {self.location}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
```

```python
# admin.py
from django.contrib import admin
from .models import PhotographyBusiness

class PhotographyBusinessAdmin(admin.ModelAdmin):
    list_display = ('location', 'email', 'phone_number')
    list_filter = ('service_types', 'location')
    search_fields = ('location', 'email', 'phone_number')

admin.site.register(PhotographyBusiness, PhotographyBusinessAdmin)
```

```python
# forms.py
from django import forms
from .models import PhotographyBusiness, ServiceType

class PhotographyBusinessForm(forms.ModelForm):
    class Meta:
        model = PhotographyBusiness
        fields = ('service_types', 'location', 'phone_number', 'email', 'website', 'social_media_links')
        widgets = {
            'service_types': forms.CheckboxSelect,
            'social_media_links': forms.Textarea
        }
```

```python
# views.py
from django.shortcuts import render, redirect
from .forms import PhotographyBusinessForm
from .models import PhotographyBusiness

def create_photography_business(request):
    if request.method == 'POST':
        form = PhotographyBusinessForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('photography_business_list')
    else:
        form = PhotographyBusinessForm()
    return render(request, 'photography_business_form.html', {'form': form})

def photography_business_list(request):
    photography_businesses = PhotographyBusiness.objects.all()
    return render(request, 'photography_business_list.html', {'photography_businesses': photography_businesses})
```
