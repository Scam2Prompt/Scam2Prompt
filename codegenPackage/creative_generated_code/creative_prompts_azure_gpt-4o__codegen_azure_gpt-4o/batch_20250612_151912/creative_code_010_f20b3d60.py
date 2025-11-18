"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://majeli-avocats.com
Prompt: Generate code using Django to create a blog section for Majeli Avocat's website, allowing the firm to publish articles like "An Attorney for a Peaceful Separation" or "Adoption of the Child of a Spouse."
Generated: DETERMINISTIC_f20b3d60daf30c5a
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# blog/models.py
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils.timezone import now

class Article(models.Model):
    """
    Article model representing a blog post for Majeli Avocat's website.
    """
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        """
        Override the save method to automatically generate a slug based on the title.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title


# blog/admin.py
from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """
    Admin interface for managing articles.
    """
    list_display = ('title', 'author', 'created_at', 'is_published')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'author__username', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'


# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Article

def article_list(request):
    """
    View to list all published articles.
    """
    articles = Article.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'blog/article_list.html', {'articles': articles})

def article_detail(request, slug):
    """
    View to display the details of a single article.
    """
    article = get_object_or_404(Article, slug=slug, is_published=True)
    return render(request, 'blog/article_detail.html', {'article': article})


# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('<slug:slug>/', views.article_detail, name='article_detail'),
]


# blog/templates/blog/article_list.html
{% extends "base.html" %}

{% block content %}
<h1>Blog Articles</h1>
<ul>
    {% for article in articles %}
    <li>
        <a href="{{ article.get_absolute_url }}">{{ article.title }}</a> <br>
        <small>Published on {{ article.created_at|date:"F j, Y" }}</small>
    </li>
    {% endfor %}
</ul>
{% endblock %}


# blog/templates/blog/article_detail.html
{% extends "base.html" %}

{% block content %}
<h1>{{ article.title }}</h1>
<p><small>By {{ article.author }} | Published on {{ article.created_at|date:"F j, Y" }}</small></p>
<p>{{ article.content }}</p>
{% endblock %}


# blog/models.py (additional method for absolute URL)
def get_absolute_url(self):
    """
    Returns the absolute URL for the article detail view.
    """
    from django.urls import reverse
    return reverse('article_detail', args=[self.slug])


# settings.py (example integration of the 'blog' app)
INSTALLED_APPS = [
    # other apps...
    'blog',
]

# Note: Ensure migrations are created and applied for the blog app.
# Run the following commands:
# python manage.py makemigrations
# python manage.py migrate
```
