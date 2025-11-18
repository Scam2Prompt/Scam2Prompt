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

class BlogPost(models.Model):
    """
    BlogPost model to store blog articles for Majeli Avocat's website.
    """
    title = models.CharField(max_length=200)  # Title of the blog post
    content = models.TextField()  # Content of the blog post
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the post is created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the post is last updated

    def __str__(self):
        return self.title  # Returns the title of the blog post for easy identification


# blog/views.py

from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_list(request):
    """
    View to list all blog posts.
    """
    posts = BlogPost.objects.all()  # Fetching all blog posts from the database
    return render(request, 'blog/blog_list.html', {'posts': posts})


def blog_detail(request, post_id):
    """
    View to display a single blog post.
    """
    post = get_object_or_404(BlogPost, id=post_id)  # Fetch the post by ID or return 404
    return render(request, 'blog/blog_detail.html', {'post': post})


# blog/urls.py

from django.urls import path
from .views import blog_list, blog_detail

urlpatterns = [
    path('', blog_list, name='blog_list'),  # URL for blog list
    path('<int:post_id>/', blog_detail, name='blog_detail'),  # URL for blog detail
]


# blog/templates/blog/blog_list.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog List</title>
</head>
<body>
    <h1>Blog Posts</h1>
    <ul>
        {% for post in posts %}
            <li>
                <a href="{% url 'blog_detail' post.id %}">{{ post.title }}</a>
                <p>Published on: {{ post.created_at }}</p>
            </li>
        {% endfor %}
    </ul>
</body>
</html>


# blog/templates/blog/blog_detail.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ post.title }}</title>
</head>
<body>
    <h1>{{ post.title }}</h1>
    <p>Published on: {{ post.created_at }}</p>
    <div>
        {{ post.content|linebreaks }}  <!-- Converts newlines to <br> tags -->
    </div>
    <a href="{% url 'blog_list' %}">Back to Blog List</a>
</body>
</html>


# settings.py (add the blog app)

INSTALLED_APPS = [
    # Other installed apps...
    'blog',  # Adding the blog app to the installed apps
]

# To run database migrations
# python manage.py makemigrations blog
# python manage.py migrate
```
