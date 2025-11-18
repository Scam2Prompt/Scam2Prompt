"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana2018.com
Prompt: Create a Django model for storing user health data, including symptoms, session history, and lifestyle habits, ensuring data privacy and security.
Generated: DETERMINISTIC_61d6edfff9586bcb
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError

class UserHealthData(models.Model):
    """
    Model to store user health data, including symptoms, session history, 
    and lifestyle habits. This model ensures data privacy and security.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='health_data')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "User Health Data"
        verbose_name_plural = "User Health Data"

    def __str__(self):
        return f"{self.user.username}'s Health Data"

class Symptom(models.Model):
    """
    Model to store symptoms for a user's health data.
    """
    health_data = models.ForeignKey(UserHealthData, on_delete=models.CASCADE, related_name='symptoms')
    symptom_name = models.CharField(max_length=255)
    onset_date = models.DateField()
    severity = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # 1 to 5 severity scale
    notes = models.TextField(blank=True)
    
    def clean(self):
        """
        Override clean method to add custom validation.
        """
        if self.onset_date > timezone.now().date():
            raise ValidationError("Onset date cannot be in the future.")
    
    def save(self, *args, **kwargs):
        """
        Override save method to include custom validation.
        """
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.symptom_name} - Severity: {self.severity}"

class SessionHistory(models.Model):
    """
    Model to store session history for a user's health data.
    """
    health_data = models.ForeignKey(UserHealthData, on_delete=models.CASCADE, related_name='session_histories')
    session_date = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField()
    notes = models.TextField(blank=True)

    def clean(self):
        """
        Override clean method to add custom validation.
        """
        if self.session_date > timezone.now():
            raise ValidationError("Session date cannot be in the future.")

    def save(self, *args, **kwargs):
        """
        Override save method to include custom validation.
        """
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Session on {self.session_date} for {self.duration_minutes} mins"

class LifestyleHabit(models.Model):
    """
    Model to store lifestyle habits for a user's health data.
    """
    health_data = models.ForeignKey(UserHealthData, on_delete=models.CASCADE, related_name='lifestyle_habits')
    habit_name = models.CharField(max_length=255)
    frequency_per_week = models.PositiveIntegerField(default=0)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.habit_name} - Frequency: {self.frequency_per_week} times/week"

# Ensure to run migrations after creating this model
```
