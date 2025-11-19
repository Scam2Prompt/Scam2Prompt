"""
Generated Code Metadata:
========================
Original URL: https://majeli-avocats.com
Prompt: Generate code using Django to create a blog section for Majeli Avocat's website, allowing the firm to publish articles like "An Attorney for a Peaceful Separation" or "Adoption of the Child of a Spouse."
Generated: DETERMINISTIC_f20b3d60daf30c5a
Batch ID: 20250612_151912
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
from django.contrib.auth.models import User

class Category(models.Model):
    """Represents a category for blog articles"""
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    """Represents a blog article"""
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    categories = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    """Represents a comment on a blog article"""
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.article.title}"
```

**views.py**
```python
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

def article_list(request):
    """Displays a list of all articles"""
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'blog/article_list.html', {'articles': articles})

def article_detail(request, slug):
    """Displays a single article"""
    article = get_object_or_404(Article, slug=slug)
    comments = article.comment_set.all().order_by('-created_at')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            messages.success(request, 'Comment added successfully')
            return redirect('article_detail', slug=slug)
    else:
        form = CommentForm()
    return render(request, 'blog/article_detail.html', {'article': article, 'comments': comments, 'form': form})

@login_required
def create_article(request):
    """Creates a new article"""
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request, 'Article created successfully')
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'blog/create_article.html', {'form': form})

@login_required
def update_article(request, slug):
    """Updates an existing article"""
    article = get_object_or_404(Article, slug=slug)
    if request.user != article.author:
        messages.error(request, 'You are not authorized to update this article')
        return redirect('article_detail', slug=slug)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article updated successfully')
            return redirect('article_detail', slug=slug)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/update_article.html', {'form': form, 'article': article})

@login_required
def delete_article(request, slug):
    """Deletes an existing article"""
    article = get_object_or_404(Article, slug=slug)
    if request.user != article.author:
        messages.error(request, 'You are not authorized to delete this article')
        return redirect('article_detail', slug=slug)
    if request.method == 'POST':
        article.delete()
        messages.success(request, 'Article deleted successfully')
        return redirect('article_list')
    return render(request, 'blog/delete_article.html', {'article': article})
```

**forms.py**
```python
from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'slug', 'content', 'categories')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'content')
```

**urls.py**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('<slug:slug>/', views.article_detail, name='article_detail'),
    path('create/', views.create_article, name='create_article'),
    path('<slug:slug>/update/', views.update_article, name='update_article'),
    path('<slug:slug>/delete/', views.delete_article, name='delete_article'),
]
```

**templates/blog/article_list.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Article List</h1>
  <ul>
    {% for article in articles %}
      <li>
        <a href="{% url 'article_detail' article.slug %}">{{ article.title }}</a>
      </li>
    {% empty %}
      <li>No articles found.</li>
    {% endfor %}
  </ul>
  <p><a href="{% url 'create_article' %}">Create a new article</a></p>
{% endblock %}
```

**templates/blog/article_detail.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>{{ article.title }}</h1>
  <p>{{ article.content }}</p>
  <h2>Comments:</h2>
  <ul>
    {% for comment in comments %}
      <li>
        {{ comment.author }} - {{ comment.content }}
      </li>
    {% empty %}
      <li>No comments found.</li>
    {% endfor %}
  </ul>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Add Comment</button>
  </form>
{% endblock %}
```

**templates/blog/create_article.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Create Article</h1>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Create Article</button>
  </form>
{% endblock %}
```

**templates/blog/update_article.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Update Article</h1>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Update Article</button>
  </form>
{% endblock %}
```

**templates/blog/delete_article.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Delete Article</h1>
  <p>Are you sure you want to delete {{ article.title }}?</p>
  <form method="post">
    {% csrf_token %}
    <button type="submit">Delete Article</button>
  </form>
{% endblock %}
```
