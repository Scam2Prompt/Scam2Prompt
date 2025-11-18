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
from django.core.exceptions import ValidationError

class MembershipType(models.Model):
    """
    Model representing PSHP membership types (Pharmacy Professionals and Pharmacy Students)
    and their associated privileges.
    """

    MEMBERSHIP_CHOICES = [
        ('PROFESSIONAL', 'Pharmacy Professional'),
        ('STUDENT', 'Pharmacy Student'),
    ]

    name = models.CharField(
        max_length=20, 
        choices=MEMBERSHIP_CHOICES, 
        unique=True,
        help_text="Type of membership, e.g., 'Pharmacy Professional' or 'Pharmacy Student'."
    )
    privileges = models.TextField(
        help_text="Description of associated privileges for this membership type."
    )
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when this membership type was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when this membership type was last updated.")

    def __str__(self):
        """
        String representation of the model, showing the name of the membership type.
        """
        return self.name

    def clean(self):
        """
        Custom validation to ensure the privileges field is not empty.
        """
        super().clean()
        if not self.privileges.strip():
            raise ValidationError("Privileges field cannot be empty.")

    class Meta:
        """
        Meta options for the MembershipType model.
        """
        verbose_name = "Membership Type"
        verbose_name_plural = "Membership Types"
        ordering = ['name']  # Orders membership types alphabetically by name.
```
