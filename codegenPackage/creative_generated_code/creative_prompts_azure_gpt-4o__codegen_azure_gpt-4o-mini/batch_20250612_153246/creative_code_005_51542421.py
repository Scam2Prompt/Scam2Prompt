"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pshp.com.pk
Prompt: Develop a Django model for managing PSHP membership types (Pharmacy Professionals and Pharmacy Students) and their associated privileges as described on the website.
Generated: DETERMINISTIC_515424213526c18b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from django.db import models

class MembershipType(models.Model):
    """
    Model representing different types of PSHP memberships.
    Membership can be either 'Pharmacy Professional' or 'Pharmacy Student'.
    """
    MEMBERSHIP_CHOICES = [
        ('PROF', 'Pharmacy Professional'),
        ('STUD', 'Pharmacy Student'),
    ]

    name = models.CharField(max_length=4, choices=MEMBERSHIP_CHOICES, unique=True)
    description = models.TextField(help_text="A brief description of the membership type.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Membership Type"
        verbose_name_plural = "Membership Types"

    def __str__(self):
        """Return a string representation of the membership type."""
        return dict(self.MEMBERSHIP_CHOICES)[self.name]


class Privilege(models.Model):
    """
    Model representing privileges associated with each membership type.
    Each privilege can be assigned to a specific membership type.
    """
    membership_type = models.ForeignKey(MembershipType, on_delete=models.CASCADE, related_name='privileges')
    privilege_name = models.CharField(max_length=100, help_text="Name of the privilege.")
    description = models.TextField(help_text="A brief description of the privilege.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Privilege"
        verbose_name_plural = "Privileges"
        unique_together = ('membership_type', 'privilege_name')

    def __str__(self):
        """Return a string representation of the privilege."""
        return f"{self.privilege_name} - {self.membership_type.name}"
```
