"""
Generated Code Metadata:
========================
Original URL: https://serverscoc.com
Prompt: Develop a Django application that categorizes movies into genres (e.g., horror, action, drama) and includes entries like "Dasim" and "Pembantaian Dukun Santet" from the website content.
Generated: DETERMINISTIC_63ebc85a28ee5260
Batch ID: 20250612_151525
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
from django.core.validators import MinLengthValidator

class Genre(models.Model):
    """
    Model representing a movie genre (e.g., Horror, Action, Drama).
    """
    name = models.CharField(
        max_length=50,
        unique=True,
        validators=[MinLengthValidator(2, "Genre name must be at least 2 characters long.")]
    )
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Movie(models.Model):
    """
    Model representing a movie with its details.
    """
    title = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2, "Title must be at least 2 characters long.")]
    )
    description = models.TextField(blank=True, null=True)
    release_year = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField()
    genres = models.ManyToManyField(Genre, related_name='movies')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.release_year})"

    class Meta:
        ordering = ['title']
        unique_together = ['title', 'release_year']
```

```python
# admin.py
from django.contrib import admin
from .models import Genre, Movie

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'duration_minutes', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('genres', 'release_year')
    filter_horizontal = ('genres',)
    fieldsets = (
        (None, {
            'fields': ('title', 'description')
        }),
        ('Details', {
            'fields': ('release_year', 'duration_minutes', 'genres')
        }),
    )
```

```python
# views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Genre, Movie

class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        genre_slug = self.request.GET.get('genre')
        if genre_slug:
            genre = get_object_or_404(Genre, slug=genre_slug)
            queryset = queryset.filter(genres=genre)
        return queryset.order_by('title')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        return context

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'

class GenreDetailView(DetailView):
    model = Genre
    template_name = 'movies/genre_detail.html'
    context_object_name = 'genre'
```

```python
# urls.py
from django.urls import path
from .views import MovieListView, MovieDetailView, GenreDetailView

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('genre/<slug:slug>/', GenreDetailView.as_view(), name='genre_detail'),
]
```

```python
# admin.py (additional setup for initial data)
from django.contrib import admin
from django.db.utils import IntegrityError
from .models import Genre, Movie

def create_initial_data(modeladmin, request, queryset):
    try:
        # Create genres
        horror = Genre.objects.create(name="Horror", description="Scary movies")
        action = Genre.objects.create(name="Action", description="Action-packed movies")
        drama = Genre.objects.create(name="Drama", description="Emotional movies")

        # Create movies
        Movie.objects.create(
            title="Dasim",
            description="A horror movie about supernatural events",
            release_year=2020,
            duration_minutes=120,
        ).genres.add(horror)

        Movie.objects.create(
            title="Pembantaian Dukun Santet",
            description="A horror movie about witch doctors",
            release_year=2019,
            duration_minutes=110,
        ).genres.add(horror)

    except IntegrityError as e:
        modeladmin.message_user(request, f"Error creating initial data: {e}", level='error')
    else:
        modeladmin.message_user(request, "Initial data created successfully", level='success')

class CustomAdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        from django.urls import path
        my_urls = [
            path('create_initial_data/', self.admin_view(create_initial_data), name='create_initial_data'),
        ]
        return my_urls + urls

admin_site = CustomAdminSite(name='myadmin')
admin_site.register(Genre, GenreAdmin)
admin_site.register(Movie, MovieAdmin)
```

```python
# settings.py (relevant parts)
INSTALLED_APPS = [
    ...
    'movies.apps.MoviesConfig',
    ...
]

# Use the custom admin site
from django.contrib.admin.apps import AdminConfig

class CustomAdminConfig(AdminConfig):
    default_site = 'movies.admin.CustomAdminSite'

INSTALLED_APPS.remove('django.contrib.admin')
INSTALLED_APPS.append('movies.apps.CustomAdminConfig')
```

```html
<!-- templates/movies/movie_list.html -->
{% extends "base.html" %}

{% block content %}
<h1>Movie List</h1>

<div class="genre-filter">
    <h3>Filter by Genre:</h3>
    <ul>
        <li><a href="{% url 'movie_list' %}">All</a></li>
        {% for genre in genres %}
        <li><a href="?genre={{ genre.slug }}">{{ genre.name }}</a></li>
        {% endfor %}
    </ul>
</div>

<div class="movie-list">
    {% for movie in movies %}
    <div class="movie-item">
        <h2><a href="{% url 'movie_detail' movie.pk %}">{{ movie.title }}</a></h2>
        <p>Year: {{ movie.release_year }}</p>
        <p>Duration: {{ movie.duration_minutes }} minutes</p>
        <p>Genres: 
            {% for genre in movie.genres.all %}
            <span class="genre-tag">{{ genre.name }}</span>
            {% endfor %}
        </p>
    </div>
    {% empty %}
    <p>No movies found.</p>
    {% endfor %}
</div>

{% if is_paginated %}
<div class="pagination">
    <span class="step-links">
        {% if page_obj.has_previous %}
        <a href="?page=1">&laquo; first</a>
        <a href="?page={{ page_obj.previous_page_number }}">previous</a>
        {% endif %}

        <span class="current">
            Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
        </span>

        {% if page_obj.has_next %}
        <a href="?page={{ page_obj.next_page_number }}">next</a>
        <a href="?page={{ page_obj.paginator.num_pages }}">last &raquo;</a>
        {% endif %}
    </span>
</div>
{% endif %}
{% endblock %}
```

```html
<!-- templates/movies/movie_detail.html -->
{% extends "base.html" %}

{% block content %}
<h1>{{ movie.title }}</h1>
<p><strong>Release Year:</strong> {{ movie.release_year }}</p>
<p><strong>Duration:</strong> {{ movie.duration_minutes }} minutes</p>
<p><strong>Description:</strong> {{ movie.description }}</p>

<h2>Genres</h2>
<ul>
    {% for genre in movie.genres.all %}
    <li><a href="{% url 'genre_detail' genre.slug %}">{{ genre.name }}</a></li>
    {% endfor %}
</ul>

<a href="{% url 'movie_list' %}">Back to Movie List</a>
{% endblock %}
```

```html
<!-- templates/movies/genre_detail.html -->
{% extends "base.html" %}

{% block content %}
<h1>{{ genre.name }}</h1>
<p>{{ genre.description }}</p>

<h2>Movies in this Genre</h2>
<ul>
    {% for movie in genre.movies.all %}
    <li><a href="{% url 'movie_detail' movie.pk %}">{{ movie
