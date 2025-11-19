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

**Movie Categorizer Django Application**
==========================================

### **models.py**
```python
from django.db import models

class Genre(models.Model):
    """Represents a movie genre."""
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    """Represents a movie with its title and genre."""
    title = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title
```

### **admin.py**
```python
from django.contrib import admin
from .models import Genre, Movie

admin.site.register(Genre)
admin.site.register(Movie)
```

### **views.py**
```python
from django.shortcuts import render, get_object_or_404
from .models import Movie, Genre
from .forms import MovieForm, GenreForm

def movie_list(request):
    """Displays a list of all movies."""
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

def movie_detail(request, pk):
    """Displays details of a specific movie."""
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movie_detail.html', {'movie': movie})

def genre_list(request):
    """Displays a list of all genres."""
    genres = Genre.objects.all()
    return render(request, 'genre_list.html', {'genres': genres})

def create_movie(request):
    """Creates a new movie."""
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'movie_list.html', {'movies': Movie.objects.all()})
    else:
        form = MovieForm()
    return render(request, 'create_movie.html', {'form': form})

def create_genre(request):
    """Creates a new genre."""
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'genre_list.html', {'genres': Genre.objects.all()})
    else:
        form = GenreForm()
    return render(request, 'create_genre.html', {'form': form})
```

### **forms.py**
```python
from django import forms
from .models import Movie, Genre

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'genre')

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('name',)
```

### **urls.py**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<pk>/', views.movie_detail, name='movie_detail'),
    path('genres/', views.genre_list, name='genre_list'),
    path('create_movie/', views.create_movie, name='create_movie'),
    path('create_genre/', views.create_genre, name='create_genre'),
]
```

### **templates/movie_list.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Movie List</h1>
  <ul>
    {% for movie in movies %}
      <li>{{ movie.title }} ({{ movie.genre.name }})</li>
    {% empty %}
      <li>No movies available.</li>
    {% endfor %}
  </ul>
  <p><a href="{% url 'create_movie' %}">Create a new movie</a></p>
{% endblock %}
```

### **templates/movie_detail.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Movie Detail</h1>
  <p>Title: {{ movie.title }}</p>
  <p>Genre: {{ movie.genre.name }}</p>
{% endblock %}
```

### **templates/genre_list.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Genre List</h1>
  <ul>
    {% for genre in genres %}
      <li>{{ genre.name }}</li>
    {% empty %}
      <li>No genres available.</li>
    {% endfor %}
  </ul>
  <p><a href="{% url 'create_genre' %}">Create a new genre</a></p>
{% endblock %}
```

### **templates/create_movie.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Create Movie</h1>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Create</button>
  </form>
{% endblock %}
```

### **templates/create_genre.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Create Genre</h1>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Create</button>
  </form>
{% endblock %}
```

### **templates/base.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Movie Categorizer</title>
</head>
<body>
    <div>
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

### **management commands to populate with example data**
```python
# movies/management/commands/populate_movies.py
from django.core.management.base import BaseCommand
from movies.models import Movie, Genre

class Command(BaseCommand):
    help = 'Populate movies'

    def handle(self, *args, **options):
        horror_genre, created = Genre.objects.get_or_create(name='Horror')
        action_genre, created = Genre.objects.get_or_create(name='Action')
        drama_genre, created = Genre.objects.get_or_create(name='Drama')

        Movie.objects.get_or_create(title='Dasim', genre=horror_genre)
        Movie.objects.get_or_create(title='Pembantaian Dukun Santet', genre=horror_genre)
        Movie.objects.get_or_create(title='Die Hard', genre=action_genre)
        Movie.objects.get_or_create(title='The Shawshank Redemption', genre=drama_genre)

        self.stdout.write(self.style.SUCCESS('Movies populated successfully'))
```

To run this command:
```bash
python manage.py populate_movies
```
