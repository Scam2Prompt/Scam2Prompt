"""
Generated Code Metadata:
========================
Original URL: https://pshp.com.pk
Prompt: Develop a Django model for managing PSHP membership types (Pharmacy Professionals and Pharmacy Students) and their associated privileges as described on the website.
Generated: DETERMINISTIC_515424213526c18b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class MembershipType(models.Model):
    """
    Represents different types of PSHP memberships.
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="The name of the membership type (e.g., 'Pharmacy Professional', 'Pharmacy Student')"
    )
    description = models.TextField(
        blank=True,
        help_text="A detailed description of this membership type"
    )
    annual_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Annual membership fee for this type"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Whether this membership type is currently available"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Membership Type"
        verbose_name_plural = "Membership Types"
        ordering = ['name']

    def __str__(self):
        return self.name

    def clean(self):
        if self.annual_fee < 0:
            raise ValidationError(_('Annual fee cannot be negative.'))

class Privilege(models.Model):
    """
    Represents privileges associated with membership types.
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Name of the privilege (e.g., 'Access to Journals', 'Conference Discounts')"
    )
    description = models.TextField(
        blank=True,
        help_text="Detailed description of what this privilege entails"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Privilege"
        verbose_name_plural = "Privileges"
        ordering = ['name']

    def __str__(self):
        return self.name

class MembershipTypePrivilege(models.Model):
    """
    Junction table linking membership types to their privileges.
    """
    membership_type = models.ForeignKey(
        MembershipType,
        on_delete=models.CASCADE,
        related_name='privileges'
    )
    privilege = models.ForeignKey(
        Privilege,
        on_delete=models.CASCADE,
        related_name='membership_types'
    )
    notes = models.TextField(
        blank=True,
        help_text="Any special notes about this privilege for this membership type"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Membership Type Privilege"
        verbose_name_plural = "Membership Type Privileges"
        unique_together = ('membership_type', 'privilege')
        ordering = ['membership_type', 'privilege']

    def __str__(self):
        return f"{self.membership_type} - {self.privilege}"

class MembershipApplication(models.Model):
    """
    Tracks applications for membership.
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('expired', 'Expired'),
    ]

    applicant = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='membership_applications'
    )
    membership_type = models.ForeignKey(
        MembershipType,
        on_delete=models.PROTECT,
        related_name='applications'
    )
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    status_date = models.DateTimeField(auto_now=True)
    notes = models.TextField(
        blank=True,
        help_text="Any notes about this application"
    )

    class Meta:
        verbose_name = "Membership Application"
        verbose_name_plural = "Membership Applications"
        ordering = ['-application_date']

    def __str__(self):
        return f"{self.applicant} - {self.membership_type} ({self.status})"

    def clean(self):
        if not self.membership_type.is_active:
            raise ValidationError(_('Cannot apply for an inactive membership type.'))
```
