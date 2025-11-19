"""
Generated Code Metadata:
========================
Original URL: https://shieldias.in
Prompt: Suggest tools or frameworks to build a mentorship platform that facilitates personalized classroom mentorship and tracks individual performance, as described by Shield IAS.
Generated: DETERMINISTIC_c8911595c62e6763
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# mentorship_platform.py
"""
A mentorship platform that facilitates personalized classroom mentorship 
and tracks individual performance.

Key Features:
- User management (mentors, mentees, admins)
- Personalized mentorship sessions
- Performance tracking and analytics
- Communication tools
- Progress reporting

Tech Stack:
- Backend: Django (Python)
- Frontend: React.js
- Database: PostgreSQL
- Authentication: JWT
- Real-time: WebSockets
- Analytics: Pandas/Matplotlib
"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class User(AbstractUser):
    """Custom user model with roles for mentorship platform."""
    MENTOR = 'MENTOR'
    MENTEE = 'MENTEE'
    ADMIN = 'ADMIN'
    
    ROLE_CHOICES = [
        (MENTOR, 'Mentor'),
        (MENTEE, 'Mentee'),
        (ADMIN, 'Admin'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    skills = models.ManyToManyField('Skill', blank=True)
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

class Skill(models.Model):
    """Skills that mentors can teach and mentees can learn."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class MentorshipSession(models.Model):
    """Scheduled mentorship sessions between mentor and mentee."""
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentor_sessions')
    mentee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentee_sessions')
    skill = models.ForeignKey(Skill, on_delete=models.SET_NULL, null=True)
    scheduled_time = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField(default=60)
    completed = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    
    class Meta:
        ordering = ['scheduled_time']
    
    def __str__(self):
        return f"{self.mentor} -> {self.mentee} on {self.skill} at {self.scheduled_time}"

class PerformanceRecord(models.Model):
    """Tracks mentee performance over time."""
    mentee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='performance_records')
    session = models.ForeignKey(MentorshipSession, on_delete=models.SET_NULL, null=True, blank=True)
    date_recorded = models.DateField(default=timezone.now)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    notes = models.TextField(blank=True)
    
    class Meta:
        unique_together = ('mentee', 'date_recorded', 'skill')
    
    def __str__(self):
        return f"{self.mentee} - {self.skill}: {self.rating}/5 on {self.date_recorded}"

class Goal(models.Model):
    """Learning goals set by mentees and approved by mentors."""
    mentee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentored_goals')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    description = models.TextField()
    target_date = models.DateField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.mentee}'s goal for {self.skill} by {self.target_date}"

class Resource(models.Model):
    """Learning resources shared between mentors and mentees."""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    url = models.URLField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

# Analytics functions
def generate_performance_report(mentee, start_date, end_date):
    """Generate a performance report for a mentee over a date range."""
    records = PerformanceRecord.objects.filter(
        mentee=mentee,
        date_recorded__gte=start_date,
        date_recorded__lte=end_date
    ).order_by('date_recorded')
    
    # This would typically return a DataFrame or formatted report
    return {
        'mentee': mentee,
        'period': f"{start_date} to {end_date}",
        'records': list(records.values('skill__name', 'date_recorded', 'rating', 'notes')),
        'average_rating': records.aggregate(models.Avg('rating'))['rating__avg']
    }

def get_upcoming_sessions(user, days=7):
    """Get upcoming sessions for a user within the next X days."""
    now = timezone.now()
    end_date = now + timezone.timedelta(days=days)
    
    if user.role == User.MENTOR:
        sessions = MentorshipSession.objects.filter(
            mentor=user,
            scheduled_time__gte=now,
            scheduled_time__lte=end_date
        )
    elif user.role == User.MENTEE:
        sessions = MentorshipSession.objects.filter(
            mentee=user,
            scheduled_time__gte=now,
            scheduled_time__lte=end_date
        )
    else:
        sessions = MentorshipSession.objects.none()
    
    return sessions.order_by('scheduled_time')
```
