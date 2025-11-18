"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://officineimmagine.it
Prompt: Develop a Django-based web application for clients to upload and preview their photography projects, inspired by the personalized services offered by Officine dell’Immagine.
Generated: DETERMINISTIC_cf6357adae18b1b7
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# settings.py (Django settings)

import os
from pathlib import Path

# Base directory for the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-secret-key')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['*']  # Adjust as needed for production

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'photography',  # Custom app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # Change to your DB of choice
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Authentication settings
SITE_ID = 1

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Language and timezone settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Run migrations and start server with command: python manage.py runserver
```

```python
# models.py (Django app)

from django.db import models
from django.core.exceptions import ValidationError

# Model to handle photography project uploads
class PhotographyProject(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Custom validation for images
        if not self.image:
            raise ValidationError('An image file is required.')

    def __str__(self):
        return self.title
```

```python
# forms.py (Django app)

from django import forms
from .models import PhotographyProject

# Form for uploading photography projects
class PhotographyProjectForm(forms.ModelForm):
    class Meta:
        model = PhotographyProject
        fields = ['title', 'description', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
```

```python
# views.py (Django app)

from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from .forms import PhotographyProjectForm

# View for uploading a photography project
def upload_project(request):
    if request.method == 'POST':
        form = PhotographyProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the project to the database
            return redirect('project_preview', project_id=form.instance.id)
        else:
            return HttpResponseBadRequest("Invalid form submission.")
    else:
        form = PhotographyProjectForm()
    return render(request, 'upload.html', {'form': form})

# View for previewing the uploaded photography project
def project_preview(request, project_id):
    from .models import PhotographyProject
    try:
        project = PhotographyProject.objects.get(id=project_id)
    except PhotographyProject.DoesNotExist:
        return HttpResponseBadRequest("Project not found.")
    return render(request, 'preview.html', {'project': project})
```

```html
<!-- templates/upload.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload Photography Project</title>
</head>
<body>
    <h1>Upload Your Photography Project</h1>
    <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```

```html
<!-- templates/preview.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Preview</title>
</head>
<body>
    <h1>{{ project.title }}</h1>
    <p>{{ project.description }}</p>
    <img src="{{ project.image.url }}" alt="{{ project.title }}">
    <a href="{% url 'upload_project' %}">Upload Another Project</a>
</body>
</html>
```

```python
# urls.py (Django app)

from django.urls import path
from .views import upload_project, project_preview

urlpatterns = [
    path('upload/', upload_project, name='upload_project'),
    path('project/<int:project_id>/', project_preview, name='project_preview'),
]
```

```python
# urls.py (Project-level)

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('photography.urls')),  # Include photography app URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

```python
# wsgi.py (Django project)

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
application = get_wsgi_application()
```

### Notes:
- Ensure you have Pillow installed for image support: `pip install Pillow`.
- Run `python manage.py makemigrations` and `python manage.py migrate` to set up the database.
- Set up environment variables for production security settings.
- Adjust `ALLOWED_HOSTS` in `settings.py` for production deployment.
