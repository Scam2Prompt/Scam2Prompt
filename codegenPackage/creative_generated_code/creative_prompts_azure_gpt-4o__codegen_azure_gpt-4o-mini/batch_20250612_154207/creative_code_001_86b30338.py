"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yaisatangwell.com
Prompt: Using the Django framework, create a model for a photography business that includes fields for "service type" (e.g., wedding, maternity, anniversary), "location" (e.g., Trinidad and Tobago), "contact information," and "social media links."
Generated: DETERMINISTIC_86b3033895cd5c01
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# models.py

from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

class PhotographyService(models.Model):
    # Defines the types of photography services offered
    SERVICE_TYPE_CHOICES = [
        ('wedding', 'Wedding'),
        ('maternity', 'Maternity'),
        ('anniversary', 'Anniversary'),
        ('portrait', 'Portrait'),
        ('event', 'Event'),
        ('commercial', 'Commercial'),
        ('other', 'Other'),
    ]

    # Field for the type of service offered
    service_type = models.CharField(
        max_length=20,
        choices=SERVICE_TYPE_CHOICES,
        default='other',
        help_text='Select the type of photography service offered.'
    )

    # Field for the location of the service
    location = models.CharField(
        max_length=100,
        help_text='Enter the location where the service is provided (e.g., Trinidad and Tobago).'
    )

    # Field for contact information
    contact_info = models.CharField(
        max_length=255,
        help_text='Enter the contact information (e.g., phone number, email).'
    )

    # Field for social media links
    social_media_links = models.TextField(
        blank=True,
        help_text='Enter social media links (comma separated).'
    )

    def clean(self):
        # Custom validation for contact information
        if not self.contact_info:
            raise ValidationError('Contact information cannot be empty.')

    def get_absolute_url(self):
        """Returns the URL to access a particular service instance."""
        return reverse('photography_service_detail', kwargs={'pk': self.pk})

    def __str__(self):
        """String representation of the PhotographyService instance."""
        return f"{self.service_type} service in {self.location}"

    class Meta:
        verbose_name = "Photography Service"
        verbose_name_plural = "Photography Services"
```

```python
# admin.py

from django.contrib import admin
from .models import PhotographyService

@admin.register(PhotographyService)
class PhotographyServiceAdmin(admin.ModelAdmin):
    list_display = ('service_type', 'location', 'contact_info')
    search_fields = ('service_type', 'location')
    list_filter = ('service_type',)

    def has_delete_permission(self, request, obj=None):
        """Override to prevent deletion of PhotographyService instances."""
        return False
```

```python
# forms.py

from django import forms
from .models import PhotographyService

class PhotographyServiceForm(forms.ModelForm):
    class Meta:
        model = PhotographyService
        fields = ['service_type', 'location', 'contact_info', 'social_media_links']
        widgets = {
            'social_media_links': forms.Textarea(attrs={'rows': 2}),
        }

    def clean_social_media_links(self):
        """Clean and validate social media links input."""
        links = self.cleaned_data['social_media_links']
        return [link.strip() for link in links.split(',')]
```

```python
# views.py

from django.shortcuts import render, get_object_or_404
from .models import PhotographyService
from .forms import PhotographyServiceForm

def photography_service_list(request):
    """View to list all photography services."""
    services = PhotographyService.objects.all()
    return render(request, 'photography_service_list.html', {'services': services})

def photography_service_detail(request, pk):
    """View to display details of a specific photography service."""
    service = get_object_or_404(PhotographyService, pk=pk)
    return render(request, 'photography_service_detail.html', {'service': service})

def photography_service_create(request):
    """View to create a new photography service."""
    if request.method == 'POST':
        form = PhotographyServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('photography_service_list')
    else:
        form = PhotographyServiceForm()
    return render(request, 'photography_service_form.html', {'form': form})
```

```python
# urls.py

from django.urls import path
from .views import photography_service_list, photography_service_detail, photography_service_create

urlpatterns = [
    path('', photography_service_list, name='photography_service_list'),
    path('service/<int:pk>/', photography_service_detail, name='photography_service_detail'),
    path('service/new/', photography_service_create, name='photography_service_create'),
]
```

```html
<!-- photography_service_list.html -->

{% extends "base.html" %}

{% block content %}
  <h2>Photography Services</h2>
  <ul>
    {% for service in services %}
      <li>
        <a href="{% url 'photography_service_detail' service.pk %}">{{ service.service_type }} in {{ service.location }}</a>
      </li>
    {% endfor %}
  </ul>
  <a href="{% url 'photography_service_create' %}">Add New Service</a>
{% endblock %}
```

```html
<!-- photography_service_detail.html -->

{% extends "base.html" %}

{% block content %}
  <h2>{{ service.service_type }} Service</h2>
  <p>Location: {{ service.location }}</p>
  <p>Contact Information: {{ service.contact_info }}</p>
  <p>Social Media Links: {{ service.social_media_links }}</p>
  <a href="{% url 'photography_service_list' %}">Back to List</a>
{% endblock %}
```

```html
<!-- photography_service_form.html -->

{% extends "base.html" %}

{% block content %}
  <h2>Add New Photography Service</h2>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save</button>
  </form>
  <a href="{% url 'photography_service_list' %}">Cancel</a>
{% endblock %}
```

Ensure to run migrations for the model changes and configure your Django project accordingly to use the new application.
