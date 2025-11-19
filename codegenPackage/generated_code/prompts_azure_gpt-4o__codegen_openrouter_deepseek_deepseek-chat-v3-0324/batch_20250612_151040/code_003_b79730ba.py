"""
Generated Code Metadata:
========================
Original URL: https://fodyem.com
Prompt: Write code to display a list of blog posts, such as "Le Tourisme en Afrique : Un Boom Annoncé d’Ici 2030," with publication dates and comments, using Flask or Django.
Generated: DETERMINISTIC_b79730ba16cc52fa
Batch ID: 20250612_151040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blog_app/views.py
from django.shortcuts import render
from django.views import View
from .models import BlogPost, Comment

class BlogPostListView(View):
    def get(self, request):
        try:
            blog_posts = BlogPost.objects.all().order_by('-publication_date')
            context = {
                'blog_posts': blog_posts
            }
            return render(request, 'blog/post_list.html', context)
        except Exception as e:
            # Log the error in production
            return render(request, 'blog/error.html', {'error': str(e)})

# blog_app/models.py
from django.db import models
from django.utils import timezone

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'Comment by {self.author} on {self.blog_post.title}'

# blog_app/templates/blog/post_list.html
<!DOCTYPE html>
<html>
<head>
    <title>Blog Posts</title>
    <style>
        .post { margin-bottom: 2rem; padding-bottom: 1rem; border-bottom: 1px solid #eee; }
        .post-title { font-size: 1.5rem; margin-bottom: 0.5rem; }
        .post-date { color: #666; font-size: 0.9rem; }
        .comments { margin-top: 1rem; }
        .comment { padding: 0.5rem; background: #f9f9f9; margin-bottom: 0.5rem; }
    </style>
</head>
<body>
    <h1>Blog Posts</h1>
    
    {% for post in blog_posts %}
    <div class="post">
        <h2 class="post-title">{{ post.title }}</h2>
        <div class="post-date">Published on: {{ post.publication_date|date:"F d, Y" }}</div>
        <p>{{ post.content }}</p>
        
        <div class="comments">
            <h3>Comments</h3>
            {% for comment in post.comments.all %}
                <div class="comment">
                    <strong>{{ comment.author }}</strong> - {{ comment.created_date|date:"F d, Y H:i" }}
                    <p>{{ comment.text }}</p>
                </div>
            {% empty %}
                <p>No comments yet.</p>
            {% endfor %}
        </div>
    </div>
    {% empty %}
    <p>No blog posts available.</p>
    {% endfor %}
</body>
</html>

# blog_app/urls.py
from django.urls import path
from .views import BlogPostListView

urlpatterns = [
    path('', BlogPostListView.as_view(), name='post_list'),
]

# blog_app/templates/blog/error.html
<!DOCTYPE html>
<html>
<head>
    <title>Error</title>
</head>
<body>
    <h1>An error occurred</h1>
    <p>{{ error }}</p>
</body>
</html>
```
