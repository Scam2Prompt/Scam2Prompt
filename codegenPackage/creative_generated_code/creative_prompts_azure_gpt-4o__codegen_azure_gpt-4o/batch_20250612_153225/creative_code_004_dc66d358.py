"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perumakers.org
Prompt: Suggest tools or frameworks to develop a blog platform for an NGO like Perú Makers, emphasizing ease of use for community engagement.
Generated: DETERMINISTIC_dc66d358b78da896
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python script using the Django framework, which is one of the most popular tools for creating blog platforms. It fulfills the requirements and best practices for building a blog platform for an NGO like Perú Makers.

```python
# blog_platform.py

"""
This script sets up a basic blog platform for an NGO using the Django framework.
It includes the necessary models, views, and configurations to start building a blog platform.
"""

import os
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.urls import path
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# ------------------------------ Models ------------------------------

class BlogPost(models.Model):
    """
    Model representing a blog post.
    """
    title = models.CharField(max_length=200, help_text="Enter the blog post title.")
    author = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Author of the blog post.")
    content = models.TextField(help_text="Content of the blog post.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time when the blog post was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time when the blog post was last updated.")

    def __str__(self):
        return self.title

    def clean(self):
        """
        Custom validation logic for the BlogPost model.
        """
        if len(self.title) < 5:
            raise ValidationError("Title must be at least 5 characters long.")

# ------------------------------ Views ------------------------------

def blog_list(request):
    """
    View to display a list of all blog posts.
    """
    posts = BlogPost.objects.all().order_by('-created_at')  # Order by latest post
    return render(request, 'blog_list.html', {'posts': posts})

def blog_detail(request, post_id):
    """
    View to display details of a single blog post.
    """
    try:
        post = get_object_or_404(BlogPost, pk=post_id)
        return render(request, 'blog_detail.html', {'post': post})
    except Http404:
        return HttpResponse("Blog post not found.", status=404)

# ------------------------------ URL Patterns ------------------------------

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('post/<int:post_id>/', blog_detail, name='blog_detail'),
]

# ------------------------------ Settings ------------------------------

# Django settings (minimal for this example). You would normally use a settings.py file.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_KEY = 'your-secret-key'
DEBUG = True  # Set to False for production
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog_platform',  # App name
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.auth.AuthenticationMiddleware',
    'django.middleware.messages.MessageMiddleware',
]

ROOT_URLCONF = 'blog_platform'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {'context_processors': ['django.template.context_processors.request']},
    },
]

WSGI_APPLICATION = 'blog_platform.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# ------------------------------ Templates ------------------------------

# blog_list.html (basic template for blog list)
"""
<!DOCTYPE html>
<html>
<head>
    <title>Blog Posts</title>
</head>
<body>
    <h1>Blog Posts</h1>
    <ul>
    {% for post in posts %}
        <li>
            <a href="/post/{{ post.id }}/">{{ post.title }}</a>
            <small>by {{ post.author.username }} on {{ post.created_at }}</small>
        </li>
    {% endfor %}
    </ul>
</body>
</html>
"""

# blog_detail.html (basic template for blog detail)
"""
<!DOCTYPE html>
<html>
<head>
    <title>{{ post.title }}</title>
</head>
<body>
    <h1>{{ post.title }}</h1>
    <p><small>by {{ post.author.username }} on {{ post.created_at }}</small></p>
    <div>{{ post.content }}</div>
</body>
</html>
"""

```

This code sets up a basic Django project for the blog platform. It includes models for blog posts, views to display a list of posts and individual post details, simple URL routing, and minimal templates for rendering the data. For better user engagement, additional features such as comments, user registration, and activity logs may be implemented.
