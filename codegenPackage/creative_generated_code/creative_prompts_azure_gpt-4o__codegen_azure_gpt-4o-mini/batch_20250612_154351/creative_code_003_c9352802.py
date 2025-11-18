"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mcim.ru
Prompt: Create a Django model for managing faculty information, including fields for instrument specialization (e.g., vocal, guitar, saxophone) and teaching schedules, based on the Московский Колледж Импровизационной Музыки website.
Generated: DETERMINISTIC_c93528029baae4da
Batch ID: 20250612_154351
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

class Faculty(models.Model):
    INSTRUMENT_SPECIALIZATION_CHOICES = [
        ('Vocal', 'Vocal'),
        ('Guitar', 'Guitar'),
        ('Saxophone', 'Saxophone'),
        ('Piano', 'Piano'),
        ('Drums', 'Drums'),
        ('Bass', 'Bass'),
        ('Violin', 'Violin'),
        ('Other', 'Other'),
    ]

    first_name = models.CharField(max_length=50, verbose_name='First Name')
    last_name = models.CharField(max_length=50, verbose_name='Last Name')
    instrument_specialization = models.CharField(
        max_length=20,
        choices=INSTRUMENT_SPECIALIZATION_CHOICES,
        verbose_name='Instrument Specialization'
    )
    email = models.EmailField(max_length=100, unique=True, verbose_name='Email')
    phone_number = models.CharField(max_length=15, blank=True, verbose_name='Phone Number')
    teaching_schedule = models.TextField(blank=True, verbose_name='Teaching Schedule')

    def clean(self):
        """
        Custom validation to check for valid phone number format.
        Raise ValidationError if the phone number is invalid.
        """
        if self.phone_number and not self.phone_number.isdigit():
            raise ValidationError('Phone number must contain only digits.')

    def __str__(self):
        """
        String representation of the Faculty instance.
        """
        return f'{self.first_name} {self.last_name} - {self.instrument_specialization}'

    class Meta:
        verbose_name = 'Faculty Member'
        verbose_name_plural = 'Faculty Members'
        ordering = ['last_name', 'first_name']
```
