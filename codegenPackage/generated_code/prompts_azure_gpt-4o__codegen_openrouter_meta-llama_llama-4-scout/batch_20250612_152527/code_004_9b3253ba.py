"""
Generated Code Metadata:
========================
Original URL: https://iebcatitiribi.edu.co
Prompt: Write code to create a searchable gallery feature for an educational institution's website, similar to the "Galería" section on the IEBCA website.
Generated: DETERMINISTIC_9b3253baebe7ee55
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Searchable Gallery Feature**
=====================================

### Gallery Model

```python
# models/gallery.py

from django.db import models

class GalleryItem(models.Model):
    """Represents a single item in the gallery."""
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='gallery/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

### Gallery View

```python
# views/gallery.py

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import GalleryItem
from .forms import GallerySearchForm

def gallery(request):
    """Displays the searchable gallery."""
    search_form = GallerySearchForm(request.GET or None)
    gallery_items = GalleryItem.objects.all()

    if search_form.is_valid():
        query = search_form.cleaned_data['query']
        if query:
            gallery_items = gallery_items.filter(title__icontains=query)

    paginator = Paginator(gallery_items, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'gallery.html', {
        'search_form': search_form,
        'page_obj': page_obj,
    })

def gallery_item_detail(request, pk):
    """Displays a single gallery item's details."""
    gallery_item = get_object_or_404(GalleryItem, pk=pk)
    return render(request, 'gallery_item_detail.html', {
        'gallery_item': gallery_item,
    })
```

### Gallery Form

```python
# forms/gallery.py

from django import forms

class GallerySearchForm(forms.Form):
    """Handles search queries for the gallery."""
    query = forms.CharField(max_length=255, required=False)
```

### Gallery URLs

```python
# urls/gallery.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('<pk>/', views.gallery_item_detail, name='gallery_item_detail'),
]
```

### Gallery Template (gallery.html)

```html
<!-- templates/gallery.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>Gallery</h1>
  <form method="get">
    {{ search_form.as_p }}
    <button type="submit">Search</button>
  </form>

  <div class="gallery">
    {% for item in page_obj %}
      <div class="gallery-item">
        <img src="{{ item.image.url }}" alt="{{ item.title }}">
        <h2>{{ item.title }}</h2>
        <p>{{ item.description }}</p>
        <a href="{% url 'gallery_item_detail' item.pk %}">View Details</a>
      </div>
    {% empty %}
      <p>No items found.</p>
    {% endfor %}
  </div>

  {% if page_obj.has_previous or page_obj.has_next %}
    <div class="pagination">
      {% if page_obj.has_previous %}
        <a href="?page={{ page_obj.previous_page_number }}">Previous</a>
      {% endif %}
      {% for num in page_obj.paginator.page_range %}
        {% if num == page_obj.number %}
          <span>{{ num }}</span>
        {% else %}
          <a href="?page={{ num }}">{{ num }}</a>
        {% endif %}
      {% endfor %}
      {% if page_obj.has_next %}
        <a href="?page={{ page_obj.next_page_number }}">Next</a>
      {% endif %}
    </div>
  {% endif %}
{% endblock %}
```

### Gallery Item Detail Template (gallery_item_detail.html)

```html
<!-- templates/gallery_item_detail.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>{{ gallery_item.title }}</h1>
  <img src="{{ gallery_item.image.url }}" alt="{{ gallery_item.title }}">
  <p>{{ gallery_item.description }}</p>
{% endblock %}
```

### Project Settings (settings.py)

```python
# settings.py

INSTALLED_APPS = [
    # ...
    'gallery',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

### URL Configuration (urls.py)

```python
# urls.py

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gallery/', include('gallery.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

### Requirements (requirements.txt)

```
Django==4.1.3
Pillow==9.2.0
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```
