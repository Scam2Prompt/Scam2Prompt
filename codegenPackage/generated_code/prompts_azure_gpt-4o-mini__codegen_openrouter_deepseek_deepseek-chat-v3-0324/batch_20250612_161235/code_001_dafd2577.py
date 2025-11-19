"""
Generated Code Metadata:
========================
Original URL: https://www.swellnetwork.tv
Prompt: How can I implement a project-based model for creative services in my application, similar to the approach used by Swell Creative Management?
Generated: DETERMINISTIC_dafd2577ae618af0
Batch ID: 20250612_161235
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
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()

class Client(models.Model):
    """Model representing a client who commissions creative projects."""
    name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20, blank=True)
    company = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    """Model representing a creative project with multiple phases."""
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('paused', 'Paused'),
        ('completed', 'Completed'),
        ('archived', 'Archived'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='projects')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    start_date = models.DateField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    priority = models.PositiveSmallIntegerField(
        default=3,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.client})"

    @property
    def is_active(self):
        return self.status == 'active'

    @property
    def is_overdue(self):
        return self.deadline and self.deadline < timezone.now().date() and self.status != 'completed'

class ProjectPhase(models.Model):
    """Model representing a phase within a creative project."""
    PHASE_TYPES = [
        ('discovery', 'Discovery'),
        ('concept', 'Concept Development'),
        ('production', 'Production'),
        ('review', 'Review & Feedback'),
        ('delivery', 'Delivery'),
        ('other', 'Other'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='phases')
    name = models.CharField(max_length=255)
    phase_type = models.CharField(max_length=20, choices=PHASE_TYPES, default='production')
    description = models.TextField(blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.project.title} - {self.name}"

class Task(models.Model):
    """Model representing a task within a project phase."""
    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
        (4, 'Critical'),
    ]

    phase = models.ForeignKey(ProjectPhase, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    due_date = models.DateField(null=True, blank=True)
    priority = models.PositiveSmallIntegerField(choices=PRIORITY_CHOICES, default=2)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.phase.project.title} - {self.title}"

    def save(self, *args, **kwargs):
        if self.is_completed and not self.completed_at:
            self.completed_at = timezone.now()
        elif not self.is_completed and self.completed_at:
            self.completed_at = None
        super().save(*args, **kwargs)

class Deliverable(models.Model):
    """Model representing a deliverable associated with a project."""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='deliverables')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    is_delivered = models.BooleanField(default=False)
    delivered_at = models.DateTimeField(null=True, blank=True)
    file = models.FileField(upload_to='deliverables/%Y/%m/%d/', null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.project.title} - {self.name}"

    def save(self, *args, **kwargs):
        if self.is_delivered and not self.delivered_at:
            self.delivered_at = timezone.now()
        elif not self.is_delivered and self.delivered_at:
            self.delivered_at = None
        super().save(*args, **kwargs)

class TimeEntry(models.Model):
    """Model for tracking time spent on project tasks."""
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='time_entries')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='time_entries')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True)
    is_billable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def duration(self):
        if self.end_time:
            return (self.end_time - self.start_time).total_seconds() / 3600
        return None

    def __str__(self):
        return f"{self.user} - {self.task} - {self.start_time}"

class ProjectComment(models.Model):
    """Model for comments and feedback on projects."""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Comment by {self.author} on {self.project.title}"
```

```python
# serializers.py
from rest_framework import serializers
from .models import (
    Client, Project, ProjectPhase, Task,
    Deliverable, TimeEntry, ProjectComment
)

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class ProjectPhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPhase
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'completed_at')

class DeliverableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliverable
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'delivered_at')

class TimeEntrySerializer(serializers.ModelSerializer):
    duration = serializers.SerializerMethodField()

    class Meta:
        model = TimeEntry
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def get_duration(self, obj):
        return obj.duration

class ProjectCommentSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.get_full_name', read_only=True)

    class Meta:
        model = ProjectComment
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class ProjectSerializer(serializers.ModelSerializer):
    phases = ProjectPhaseSerializer(many=True, read_only=True)
    deliverables = DeliverableSerializer(many=True, read_only=True)
    comments = ProjectCommentSerializer(many=True, read_only=True)
    client_name = serializers.CharField(source='client.name', read_only=True)
    creator_name = serializers.CharField(source='created_by.get_full_name', read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    is_overdue = serializers
