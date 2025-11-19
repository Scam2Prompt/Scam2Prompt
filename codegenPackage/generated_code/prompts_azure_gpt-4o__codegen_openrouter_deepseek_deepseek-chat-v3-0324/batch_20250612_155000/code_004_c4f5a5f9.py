"""
Generated Code Metadata:
========================
Original URL: https://linktre.me
Prompt: Write code to implement a verification badge system for user profiles, similar to the "selo de autenticidade" feature described on "Bio.links."
Generated: DETERMINISTIC_c4f5a5f94d6dbbf4
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class VerificationBadge(models.Model):
    """
    Model representing a verification badge that can be assigned to users.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    icon = models.ImageField(upload_to='verification_badges/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Verification Badge")
        verbose_name_plural = _("Verification Badges")

    def __str__(self):
        return self.name

class UserVerification(models.Model):
    """
    Model representing the relationship between users and verification badges.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='verifications')
    badge = models.ForeignKey(VerificationBadge, on_delete=models.CASCADE)
    verified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, 
                                  related_name='verified_users')
    verification_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    verification_reason = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('user', 'badge')
        verbose_name = _("User Verification")
        verbose_name_plural = _("User Verifications")

    def __str__(self):
        return f"{self.user.username} - {self.badge.name}"

    def clean(self):
        if self.verified_by and self.verified_by == self.user:
            raise ValidationError(_("A user cannot verify themselves."))

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

def get_user_verification_badges(user):
    """
    Returns all active verification badges for a given user.
    """
    return UserVerification.objects.filter(user=user, is_active=True).select_related('badge')

def verify_user(user, badge, verified_by, reason=None):
    """
    Verifies a user with a specific badge.
    """
    verification, created = UserVerification.objects.get_or_create(
        user=user,
        badge=badge,
        defaults={
            'verified_by': verified_by,
            'verification_reason': reason,
            'is_active': True
        }
    )
    
    if not created:
        verification.verified_by = verified_by
        verification.verification_reason = reason
        verification.is_active = True
        verification.save()
    
    return verification

def revoke_verification(user, badge, revoked_by, reason=None):
    """
    Revokes a verification from a user.
    """
    try:
        verification = UserVerification.objects.get(user=user, badge=badge, is_active=True)
        verification.is_active = False
        verification.verified_by = revoked_by
        verification.verification_reason = reason or f"Revoked by {revoked_by.username}"
        verification.save()
        return True
    except UserVerification.DoesNotExist:
        return False
```
