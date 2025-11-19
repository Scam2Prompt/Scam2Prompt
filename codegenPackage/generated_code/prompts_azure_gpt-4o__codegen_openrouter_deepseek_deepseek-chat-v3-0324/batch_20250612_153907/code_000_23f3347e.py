"""
Generated Code Metadata:
========================
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: Write Python code using Django to create a web application that categorizes profiles into groups like "Real Estate," "Artists," and "Business Owners," similar to the structure on "The Faces Of Sedona and the Verde Valley."
Generated: DETERMINISTIC_23f3347e4dcaa40c
Batch ID: 20250612_153907
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
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class ProfileCategory(models.Model):
    """
    Represents a category for profiles (e.g., Real Estate, Artists, Business Owners)
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Profile Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

class Profile(models.Model):
    """
    Represents a user profile that can be categorized
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    category = models.ForeignKey(ProfileCategory, on_delete=models.SET_NULL, null=True, blank=True)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]
    )
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_featured', 'user__last_name']

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.category})"

# admin.py
from django.contrib import admin
from .models import ProfileCategory, Profile

@admin.register(ProfileCategory)
class ProfileCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'is_featured', 'created_at')
    list_filter = ('category', 'is_featured')
    search_fields = ('user__first_name', 'user__last_name', 'user__email')
    raw_id_fields = ('user',)

# views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import ProfileCategory, Profile

class CategoryListView(ListView):
    """
    Displays a list of all profile categories
    """
    model = ProfileCategory
    template_name = 'profiles/category_list.html'
    context_object_name = 'categories'

class ProfileListByCategoryView(ListView):
    """
    Displays profiles filtered by a specific category
    """
    template_name = 'profiles/profile_list.html'
    context_object_name = 'profiles'
    paginate_by = 20

    def get_queryset(self):
        self.category = get_object_or_404(ProfileCategory, slug=self.kwargs['slug'])
        return Profile.objects.filter(category=self.category).select_related('user', 'category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

class ProfileDetailView(DetailView):
    """
    Displays detailed information about a specific profile
    """
    model = Profile
    template_name = 'profiles/profile_detail.html'
    context_object_name = 'profile'
    slug_field = 'user__username'
    slug_url_kwarg = 'username'

# urls.py
from django.urls import path
from .views import CategoryListView, ProfileListByCategoryView, ProfileDetailView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/<slug:slug>/', ProfileListByCategoryView.as_view(), name='profile_list_by_category'),
    path('profile/<str:username>/', ProfileDetailView.as_view(), name='profile_detail'),
]

# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['category', 'bio', 'website', 'phone', 'address', 'profile_picture', 'is_featured']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }

# templates/profiles/category_list.html
{% extends "base.html" %}

{% block content %}
<h1>Profile Categories</h1>
<ul>
    {% for category in categories %}
    <li>
        <a href="{% url 'profile_list_by_category' category.slug %}">
            {{ category.name }}
        </a>
    </li>
    {% endfor %}
</ul>
{% endblock %}

# templates/profiles/profile_list.html
{% extends "base.html" %}

{% block content %}
<h1>Profiles in {{ category.name }}</h1>
{% if profiles %}
    <div class="profile-grid">
        {% for profile in profiles %}
        <div class="profile-card">
            {% if profile.profile_picture %}
            <img src="{{ profile.profile_picture.url }}" alt="{{ profile.user.get_full_name }}">
            {% endif %}
            <h3>
                <a href="{% url 'profile_detail' profile.user.username %}">
                    {{ profile.user.get_full_name }}
                </a>
            </h3>
            <p>{{ profile.bio|truncatewords:20 }}</p>
        </div>
        {% endfor %}
    </div>
{% else %}
    <p>No profiles found in this category.</p>
{% endif %}
{% endblock %}

# templates/profiles/profile_detail.html
{% extends "base.html" %}

{% block content %}
<div class="profile-detail">
    {% if profile.profile_picture %}
    <img src="{{ profile.profile_picture.url }}" alt="{{ profile.user.get_full_name }}" class="profile-image">
    {% endif %}
    
    <h1>{{ profile.user.get_full_name }}</h1>
    <p class="category">{{ profile.category }}</p>
    
    {% if profile.bio %}
    <div class="bio">
        <h2>About</h2>
        <p>{{ profile.bio }}</p>
    </div>
    {% endif %}
    
    <div class="contact-info">
        <h2>Contact Information</h2>
        {% if profile.website %}
        <p><strong>Website:</strong> <a href="{{ profile.website }}" target="_blank">{{ profile.website }}</a></p>
        {% endif %}
        {% if profile.phone %}
        <p><strong>Phone:</strong> {{ profile.phone }}</p>
        {% endif %}
        {% if profile.address %}
        <p><strong>Address:</strong> {{ profile.address }}</p>
        {% endif %}
    </div>
</div>
{% endblock %}
```
