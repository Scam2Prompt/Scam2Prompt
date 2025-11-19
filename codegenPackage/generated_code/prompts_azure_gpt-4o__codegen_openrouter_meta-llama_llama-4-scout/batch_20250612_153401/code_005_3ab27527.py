"""
Generated Code Metadata:
========================
Original URL: https://cooperativacooprometa.com
Prompt: Provide code examples for implementing multilingual support (e.g., English, Türkçe, Español) in a CMS similar to Nexelit.
Generated: DETERMINISTIC_3ab2752758a13298
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Multilingual Support Implementation**
=====================================

### Language Model

```python
# models.py
from django.db import models

class Language(models.Model):
    """Represents a language."""
    code = models.CharField(max_length=5, unique=True)  # e.g., en, tr, es
    name = models.CharField(max_length=50)  # e.g., English, Türkçe, Español

    def __str__(self):
        return self.name
```

### Translation Model

```python
# models.py (continued)
class Translation(models.Model):
    """Represents a translation for a given text."""
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    key = models.CharField(max_length=255)  # e.g., page_title, button_label

    def __str__(self):
        return f"{self.language} - {self.text}"
```

### Content Model with Multilingual Support

```python
# models.py (continued)
from django.db import models

class Content(models.Model):
    """Represents a content item with multilingual support."""
    title = models.CharField(max_length=255)
    translations = models.ManyToManyField(Translation)

    def get_translation(self, language_code):
        try:
            return self.translations.get(language__code=language_code)
        except Translation.DoesNotExist:
            return None

    def __str__(self):
        return self.title
```

### Locale Settings

```python
# settings.py
LOCALE_SETTINGS = {
    'languages': [
        {'code': 'en', 'name': 'English'},
        {'code': 'tr', 'name': 'Türkçe'},
        {'code': 'es', 'name': 'Español'},
    ],
    'default_language': 'en',
}
```

### Translation Utilities

```python
# utils.py
from django.utils.translation import gettext as _
from .models import Language, Translation

def get_language_code(request):
    return request.LANGUAGE_CODE

def translate_text(text_key, language_code):
    try:
        translation = Translation.objects.get(key=text_key, language__code=language_code)
        return translation.text
    except Translation.DoesNotExist:
        return _(text_key)
```

### Views with Multilingual Support

```python
# views.py
from django.shortcuts import render
from .models import Content
from .utils import get_language_code, translate_text

def content_detail(request, pk):
    content = Content.objects.get(pk=pk)
    language_code = get_language_code(request)
    translation = content.get_translation(language_code)
    if translation:
        content_title = translation.text
    else:
        content_title = content.title

    return render(request, 'content_detail.html', {
        'content_title': content_title,
    })
```

### Template Example

```html
<!-- content_detail.html -->
<h1>{{ content_title }}</h1>
```

### Middleware for Setting Language

```python
# middleware.py
from django.utils.translation import activate
from .utils import get_language_code

class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        activate(get_language_code(request))
        return self.get_response(request)
```

### URLs

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('content/<pk>/', views.content_detail, name='content_detail'),
]
```
