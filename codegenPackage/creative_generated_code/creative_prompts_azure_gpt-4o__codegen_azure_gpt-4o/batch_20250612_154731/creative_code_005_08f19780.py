"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balajitravelsonline.com
Prompt: Develop a Django application for Balaji Tours & Travels that includes a homepage listing tour packages, a gallery section, and a contact form linked to their email.
Generated: DETERMINISTIC_08f19780daae7b06
Batch ID: 20250612_154731
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Balaji Tours & Travels - Django Application

# settings.py
import os

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tours',  # Our custom app
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_email_password'

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# urls.py (Project Level)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tours.urls')),  # Include routes from the tours app
]

# models.py (tours app)
from django.db import models

class TourPackage(models.Model):
    name = models.CharField(max_length=255)  # Name of the tour package
    description = models.TextField()  # Description of the tour package
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the package
    image = models.ImageField(upload_to='tour_images/')  # Image for the package

    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery_images/')

    def __str__(self):
        return self.title

# forms.py (tours app)
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

# views.py (tours app)
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import TourPackage, GalleryImage
from .forms import ContactForm

def homepage(request):
    """Homepage view displaying tour packages."""
    tour_packages = TourPackage.objects.all()
    return render(request, 'tours/homepage.html', {'tour_packages': tour_packages})

def gallery(request):
    """Gallery view displaying images."""
    gallery_images = GalleryImage.objects.all()
    return render(request, 'tours/gallery.html', {'gallery_images': gallery_images})

def contact(request):
    """Contact form view."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Send email
            send_mail(
                f"Message from {form.cleaned_data['name']}",
                form.cleaned_data['message'],
                form.cleaned_data['email'],
                ['contact@balajitours.com']
            )
            return redirect('homepage')  # Redirect to homepage on success
    else:
        form = ContactForm()
    return render(request, 'tours/contact.html', {'form': form})

# urls.py (tours app)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Homepage
    path('gallery/', views.gallery, name='gallery'),  # Gallery page
    path('contact/', views.contact, name='contact'),  # Contact form page
]

# admin.py (tours app)
from django.contrib import admin
from .models import TourPackage, GalleryImage

@admin.register(TourPackage)
class TourPackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title',)

# templates/tours/homepage.html
"""
{% extends 'base.html' %}
{% block content %}
  <h1>Tour Packages</h1>
  {% for package in tour_packages %}
    <div>
      <h2>{{ package.name }}</h2>
      <p>{{ package.description }}</p>
      <p>Price: ${{ package.price }}</p>
      <img src="{{ package.image.url }}" alt="{{ package.name }}">
    </div>
  {% endfor %}
{% endblock %}
"""

# templates/tours/gallery.html
"""
{% extends 'base.html' %}
{% block content %}
  <h1>Gallery</h1>
  {% for image in gallery_images %}
    <div>
      <h2>{{ image.title }}</h2>
      <img src="{{ image.image.url }}" alt="{{ image.title }}">
    </div>
  {% endfor %}
{% endblock %}
"""

# templates/tours/contact.html
"""
{% extends 'base.html' %}
{% block content %}
  <h1>Contact Us</h1>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Send</button>
  </form>
{% endblock %}
"""

# templates/base.html
"""
<!DOCTYPE html>
<html>
<head>
    <title>Balaji Tours & Travels</title>
</head>
<body>
    <header>
        <nav>
            <a href="/">Home</a>
            <a href="/gallery/">Gallery</a>
            <a href="/contact/">Contact</a>
        </nav>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <footer>
        <p>&copy; 2023 Balaji Tours & Travels</p>
    </footer>
</body>
</html>
"""

# Run the migrations and start the server:
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
```
