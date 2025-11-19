"""
Generated Code Metadata:
========================
Original URL: https://tc-harsewinkel.de
Prompt: Suggest a library or framework for building a community engagement platform like the TC Harsewinkel website, and provide an example of how to structure the platform's features.
Generated: DETERMINISTIC_abaf6d7300a0a694
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# community_engagement_platform.py
"""
Community Engagement Platform using Django Framework

This module provides a basic structure for a community engagement platform
similar to TC Harsewinkel website. It includes models, views, and URLs for
core features like announcements, events, and user management.

Dependencies:
- Django (pip install django)
- Django Allauth for authentication (pip install django-allauth)
"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils import timezone
from django.core.validators import FileExtensionValidator

class CustomUser(AbstractUser):
    """
    Custom user model extending Django's AbstractUser
    """
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])]
    )
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Announcement(models.Model):
    """
    Model for community announcements
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('announcement_detail', kwargs={'pk': self.pk})

class Event(models.Model):
    """
    Model for community events
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    organizer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to='event_images/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])]
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'pk': self.pk})

    @property
    def is_upcoming(self):
        return self.start_time > timezone.now()

class EventRegistration(models.Model):
    """
    Model for event registrations
    """
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    additional_info = models.TextField(blank=True)

    class Meta:
        unique_together = ('event', 'user')

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"

# Example views.py content
"""
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Announcement, Event, EventRegistration
from .forms import AnnouncementForm, EventForm

class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'announcements/list.html'
    context_object_name = 'announcements'
    ordering = ['-created_at']
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_pinned=True) | queryset.filter(is_pinned=False)

class AnnouncementCreateView(LoginRequiredMixin, CreateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = 'announcements/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_registered'] = False
        if self.request.user.is_authenticated:
            context['is_registered'] = EventRegistration.objects.filter(
                event=self.object,
                user=self.request.user
            ).exists()
        return context

class EventRegisterView(LoginRequiredMixin, View):
    def post(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        registration, created = EventRegistration.objects.get_or_create(
            event=event,
            user=request.user
        )
        if created:
            messages.success(request, "You have successfully registered for this event!")
        else:
            messages.info(request, "You are already registered for this event.")
        return redirect('event_detail', pk=event.pk)
"""

# Example urls.py content
"""
from django.urls import path
from .views import (
    AnnouncementListView,
    AnnouncementCreateView,
    EventDetailView,
    EventRegisterView
)

urlpatterns = [
    path('announcements/', AnnouncementListView.as_view(), name='announcement_list'),
    path('announcements/new/', AnnouncementCreateView.as_view(), name='announcement_create'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('events/<int:pk>/register/', EventRegisterView.as_view(), name='event_register'),
]
"""

# Example settings.py additions
"""
INSTALLED_APPS = [
    ...
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'community_platform',
]

AUTH_USER_MODEL = 'community_platform.CustomUser'

# Allauth settings
SITE_ID = 1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
"""
```
