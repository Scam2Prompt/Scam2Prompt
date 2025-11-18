"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonaeac.com
Prompt: Build a Django model for storing user information, including membership level and referral code, as described on bonaeac.com.
Generated: DETERMINISTIC_3502abd527e73fe8
Batch ID: 20250612_153812
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
from django.core.exceptions import ValidationError

class UserProfile(models.Model):
    """
    A model to store additional user information such as membership level and referral code.
    """
    
    MEMBERSHIP_LEVELS = (
        ('free', 'Free'),
        ('premium', 'Premium'),
        ('vip', 'VIP'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    membership_level = models.CharField(max_length=10, choices=MEMBERSHIP_LEVELS, default='free')
    referral_code = models.CharField(max_length=20, blank=True, null=True, unique=True)

    def clean(self):
        """
        Custom validation for the UserProfile model.
        Ensures that the referral code is unique.
        """
        if self.referral_code:
            if UserProfile.objects.filter(referral_code=self.referral_code).exists():
                raise ValidationError({'referral_code': 'This referral code is already in use.'})

    def save(self, *args, **kwargs):
        """
        Overriding the save method to include custom validation before saving.
        """
        self.full_clean()  # Validate the model before saving
        super().save(*args, **kwargs)

    def __str__(self):
        """
        String representation of the UserProfile model.
        """
        return f'{self.user.username} - {self.membership_level} Membership'

# Signal to create or update UserProfile when User is created or updated
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver to automatically create a UserProfile when a User is created.
    """
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal receiver to automatically save the UserProfile when the User is saved.
    """
    instance.profile.save()
```
