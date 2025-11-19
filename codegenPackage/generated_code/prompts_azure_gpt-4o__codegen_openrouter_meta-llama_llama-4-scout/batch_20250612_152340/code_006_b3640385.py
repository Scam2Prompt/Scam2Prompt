"""
Generated Code Metadata:
========================
Original URL: https://treehousesessions.co.uk
Prompt: Develop a Django app to showcase artist profiles and performance details, inspired by the structure of the "Tree House Sessions" website.
Generated: DETERMINISTIC_b3640385bb0aa210
Batch ID: 20250612_152340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**models.py**
```python
from django.db import models
from django.utils import timezone

class Artist(models.Model):
    """Artist Profile Model"""
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='artist_images', blank=True)

    def __str__(self):
        return self.name

class Performance(models.Model):
    """Performance Model"""
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='performances')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date = models.DateField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.artist.name} - {self.title}"

class Session(models.Model):
    """Session Model"""
    performance = models.OneToOneField(Performance, on_delete=models.CASCADE, related_name='session')
    video_url = models.URLField(blank=True)
    audio_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.performance.artist.name} - {self.performance.title} Session"

class Song(models.Model):
    """Song Model"""
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE, related_name='songs', blank=True, null=True)

    def __str__(self):
        return self.title
```

**views.py**
```python
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Artist, Performance, Session, Song

class ArtistListView(ListView):
    """Artist List View"""
    model = Artist
    template_name = 'artist_list.html'
    context_object_name = 'artists'

class ArtistDetailView(DetailView):
    """Artist Detail View"""
    model = Artist
    template_name = 'artist_detail.html'
    context_object_name = 'artist'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['performances'] = Performance.objects.filter(artist=self.object)
        return context

class PerformanceDetailView(DetailView):
    """Performance Detail View"""
    model = Performance
    template_name = 'performance_detail.html'
    context_object_name = 'performance'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['session'] = Session.objects.filter(performance=self.object).first()
        context['songs'] = Song.objects.filter(performance=self.object)
        return context
```

**urls.py**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('artists/', views.ArtistListView.as_view(), name='artist_list'),
    path('artists/<int:pk>/', views.ArtistDetailView.as_view(), name='artist_detail'),
    path('performances/<int:pk>/', views.PerformanceDetailView.as_view(), name='performance_detail'),
]
```

**templates/artist_list.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Artists</h1>
  <ul>
    {% for artist in artists %}
      <li>
        <a href="{% url 'artist_detail' artist.pk %}">{{ artist.name }}</a>
      </li>
    {% empty %}
      <li>No artists found.</li>
    {% endfor %}
  </ul>
{% endblock %}
```

**templates/artist_detail.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>{{ artist.name }}</h1>
  <p>{{ artist.bio }}</p>
  <img src="{{ artist.image.url }}" alt="{{ artist.name }}">

  <h2>Performances</h2>
  <ul>
    {% for performance in performances %}
      <li>
        <a href="{% url 'performance_detail' performance.pk %}">{{ performance.title }}</a>
      </li>
    {% empty %}
      <li>No performances found.</li>
    {% endfor %}
  </ul>
{% endblock %}
```

**templates/performance_detail.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>{{ performance.title }}</h1>
  <p>{{ performance.description }}</p>
  <p>Date: {{ performance.date }}</p>
  <p>Location: {{ performance.location }}</p>

  {% if session %}
    <h2>Session</h2>
    <p>Video: <a href="{{ session.video_url }}">{{ session.video_url }}</a></p>
    <p>Audio: <a href="{{ session.audio_url }}">{{ session.audio_url }}</a></p>
  {% endif %}

  <h2>Songs</h2>
  <ul>
    {% for song in songs %}
      <li>{{ song.title }}</li>
    {% empty %}
      <li>No songs found.</li>
    {% endfor %}
  </ul>
{% endblock %}
```

**admin.py**
```python
from django.contrib import admin
from .models import Artist, Performance, Session, Song

admin.site.register(Artist)
admin.site.register(Performance)
admin.site.register(Session)
admin.site.register(Song)
```

**apps.py**
```python
from django.apps import AppConfig

class MusicAppConfig(AppConfig):
    name = 'music'
    verbose_name = 'Music App'
```

**settings.py (relevant parts)**
```python
INSTALLED_APPS = [
    # ...
    'music.apps.MusicAppConfig',
    # ...
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

TEMPLATES = [
    {
        # ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # ...
    },
]
```

**urls.py (main project)**
```python
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('music.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
