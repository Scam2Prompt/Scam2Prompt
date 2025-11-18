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
from django.core.validators import MaxLengthValidator, MinLengthValidator
import uuid

class User(models.Model):
    """
    Model for storing user information.
    Includes fields for first name, last name, email, membership level, and referral code.
    """

    MEMBERSHIP_LEVELS = [
        ('Free', 'Free'),
        ('Bronze', 'Bronze'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
        ('Platinum', 'Platinum'),
    ]

    # User's first name
    first_name = models.CharField(
        max_length=50, 
        verbose_name="First Name"
    )

    # User's last name
    last_name = models.CharField(
        max_length=50, 
        verbose_name="Last Name"
    )

    # User's email (unique identifier)
    email = models.EmailField(
        unique=True,
        verbose_name="Email Address"
    )

    # Membership level
    membership_level = models.CharField(
        max_length=10,
        choices=MEMBERSHIP_LEVELS,
        default='Free',
        verbose_name="Membership Level"
    )

    # Referral code (unique)
    referral_code = models.CharField(
        max_length=10,
        unique=True,
        default=str(uuid.uuid4())[:10],  # Generate a random 10-character string
        validators=[MinLengthValidator(5), MaxLengthValidator(10)],
        verbose_name="Referral Code"
    )

    # Record creation timestamp
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At"
    )

    # Record update timestamp
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At"
    )

    class Meta:
        """
        Meta options for the User model.
        """
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ['-created_at']  # Order by newest first

    def __str__(self):
        """
        String representation of the User model.
        """
        return f"{self.first_name} {self.last_name} ({self.email})"

    def save(self, *args, **kwargs):
        """
        Custom save method for additional logic before saving the model.
        """
        # Ensure referral code is unique and non-empty
        if not self.referral_code:
            self.referral_code = str(uuid.uuid4())[:10]
        super(User, self).save(*args, **kwargs)
```
