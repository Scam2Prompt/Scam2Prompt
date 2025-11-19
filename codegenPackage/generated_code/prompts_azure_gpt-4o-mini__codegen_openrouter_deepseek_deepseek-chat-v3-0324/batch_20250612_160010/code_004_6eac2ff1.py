"""
Generated Code Metadata:
========================
Original URL: https://rentsy.pro
Prompt: How can I design a user interface that supports multiple languages for a rental application like Rentsy?
Generated: DETERMINISTIC_6eac2ff1e4895b17
Batch ID: 20250612_160010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# rental_app/translation.py
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import translation

def set_language(request):
    """
    View to set the user's language preference and redirect back to previous page.
    """
    if request.method == 'POST':
        language = request.POST.get('language', settings.LANGUAGE_CODE)
        if language in [lang[0] for lang in settings.LANGUAGES]:
            translation.activate(language)
            request.session[translation.LANGUAGE_SESSION_KEY] = language
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('home')))

# rental_app/context_processors.py
from django.conf import settings

def language_context(request):
    """
    Context processor to make LANGUAGES available in all templates.
    """
    return {
        'LANGUAGES': settings.LANGUAGES,
        'CURRENT_LANGUAGE': translation.get_language(),
    }

# rental_app/settings.py (partial)
# Add these to your Django settings

MIDDLEWARE = [
    # ... other middleware ...
    'django.middleware.locale.LocaleMiddleware',
    # ... other middleware ...
]

LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('en', _('English')),
    ('es', _('Spanish')),
    ('fr', _('French')),
    ('de', _('German')),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

# rental_app/urls.py
from django.urls import path
from .translation import set_language

urlpatterns = [
    # ... other URLs ...
    path('set-language/', set_language, name='set_language'),
]

# templates/base.html (partial)
{% load i18n %}

<!DOCTYPE html>
<html lang="{{ CURRENT_LANGUAGE }}">
<head>
    <!-- ... other head elements ... -->
</head>
<body>
    <!-- Language selector dropdown -->
    <div class="language-selector">
        <form action="{% url 'set_language' %}" method="post">
            {% csrf_token %}
            <select name="language" onchange="this.form.submit()">
                {% for code, name in LANGUAGES %}
                    <option value="{{ code }}" {% if code == CURRENT_LANGUAGE %}selected{% endif %}>
                        {{ name }}
                    </option>
                {% endfor %}
            </select>
        </form>
    </div>

    <!-- Example of translated content -->
    <h1>{% trans "Welcome to Rentsy" %}</h1>
    <p>{% trans "Find your perfect rental property today!" %}</p>
    
    <!-- ... rest of the template ... -->
</body>
</html>

# Create translation files (run these commands)
# django-admin makemessages -l en
# django-admin makemessages -l es
# django-admin makemessages -l fr
# django-admin makemessages -l de
# Then edit the .po files in locale directories and compile with:
# django-admin compilemessages
```
