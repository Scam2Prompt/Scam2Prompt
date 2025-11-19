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

class MembershipType(models.Model):
    """
    Model representing different types of PSHP memberships.
    """
    MEMBERSHIP_CHOICES = [
        ('PP', 'Pharmacy Professional'),
        ('PS', 'Pharmacy Student'),
    ]

    membership_type = models.CharField(
        max_length=2,
        choices=MEMBERSHIP_CHOICES,
        unique=True,
        verbose_name='Membership Type'
    )
    
    privileges = models.TextField(
        help_text='List of privileges associated with this membership type.',
        verbose_name='Privileges'
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')

    class Meta:
        verbose_name = 'Membership Type'
        verbose_name_plural = 'Membership Types'
        ordering = ['membership_type']

    def __str__(self):
        return self.get_membership_type_display()

    def clean(self):
        """
        Custom validation to ensure that privileges are not empty.
        """
        if not self.privileges.strip():
            raise ValidationError('Privileges cannot be empty.')

    def save(self, *args, **kwargs):
        """
        Override save method to perform custom validation before saving.
        """
        self.clean()  # Call the clean method to validate
        super().save(*args, **kwargs)  # Call the original save method
```
