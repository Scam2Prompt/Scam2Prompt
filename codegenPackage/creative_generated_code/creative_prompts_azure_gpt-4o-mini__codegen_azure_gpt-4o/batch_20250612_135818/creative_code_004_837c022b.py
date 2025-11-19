"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ahopefulme.com
Prompt: Suggest a library for developing a motivational blog platform that includes user-generated content and community interactions, reflecting the community aspects of HopefulMe.
Generated: DETERMINISTIC_837c022b08b58497
Batch ID: 20250612_135818
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python code using Django, an excellent library/framework for developing web platforms
# that include user-generated content and community interactions.

# Install Django by running: pip install django

# Create a Django project and app first:
# django-admin startproject motivational_blog
# python manage.py startapp blog

# Below is the code for "models.py" in the "blog" app.
from django.db import models
from django.contrib.auth.models import User

# Define the models for user-generated content and community interactions
class Profile(models.Model):
    """Profile model to extend user information."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Post(models.Model):
    """Model for blog posts."""
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    """Model for comments on blog posts."""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"

class Like(models.Model):
    """Model for handling likes on posts."""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('post', 'user')  # Ensure a user can like a post only once

    def __str__(self):
        return f"{self.user.username} liked {self.post.title}"

# Code for "views.py" to handle user-generated content.
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post, Comment, Like

def index(request):
    """Homepage view to list all posts."""
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, post_id):
    """View to display a single post details."""
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    likes = post.likes.count()
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'likes': likes})

@csrf_exempt
def like_post(request, post_id):
    """API endpoint to like a post."""
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        user = request.user
        if not Like.objects.filter(post=post, user=user).exists():
            Like.objects.create(post=post, user=user)
            return JsonResponse({'message': 'Liked successfully.'}, status=201)
        return JsonResponse({'message': 'Already liked.'}, status=400)
    return JsonResponse({'error': 'Invalid request method.'}, status=405)

# Code for "admin.py" to manage models in the admin interface.
from django.contrib import admin
from .models import Profile, Post, Comment, Like

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'author__username')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    search_fields = ('author__username', 'post__title')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'user')

# Code for "urls.py" to define routing for views.
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
]

# Example template snippet (blog/index.html).
'''
{% for post in posts %}
    <h2><a href="{% url 'post_detail' post.id %}">{{ post.title }}</a></h2>
    <p>{{ post.content|truncatewords:30 }}</p>
    <p>Likes: {{ post.likes.count }}</p>
    <hr>
{% endfor %}
'''

# Example template snippet (blog/post_detail.html).
'''
<h1>{{ post.title }}</h1>
<p>{{ post.content }}</p>
<p>Likes: {{ likes }}</p>
<h3>Comments:</h3>
<ul>
    {% for comment in comments %}
        <li>{{ comment.author.username }}: {{ comment.content }}</li>
    {% endfor %}
</ul>
'''

# To use this code:
# 1. Configure settings.py for database and static files.
# 2. Run migrations: python manage.py makemigrations && python manage.py migrate
# 3. Create an admin user: python manage.py createsuperuser
# 4. Start the server: python manage.py runserver
```
