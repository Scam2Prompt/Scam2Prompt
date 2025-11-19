"""
Generated Code Metadata:
========================
Original URL: https://mcim.ru
Prompt: Create a Django model for managing faculty information, including fields for instrument specialization (e.g., vocal, guitar, saxophone) and teaching schedules, based on the Московский Колледж Импровизационной Музыки website.
Generated: DETERMINISTIC_c93528029baae4da
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.utils.translation import gettext_lazy as _

class Faculty(models.Model):
    """
    Model representing faculty members at Московский Колледж Импровизационной Музыки.
    """
    
    class InstrumentSpecialization(models.TextChoices):
        VOCAL = 'VOC', _('Vocal')
        GUITAR = 'GTR', _('Guitar')
        PIANO = 'PNO', _('Piano')
        SAXOPHONE = 'SAX', _('Saxophone')
        DRUMS = 'DRM', _('Drums')
        BASS = 'BAS', _('Bass')
        VIOLIN = 'VLN', _('Violin')
        TRUMPET = 'TRP', _('Trumpet')
        COMPOSITION = 'CMP', _('Composition')
        MUSIC_THEORY = 'MTH', _('Music Theory')
    
    class DaysOfWeek(models.TextChoices):
        MONDAY = 'MON', _('Monday')
        TUESDAY = 'TUE', _('Tuesday')
        WEDNESDAY = 'WED', _('Wednesday')
        THURSDAY = 'THU', _('Thursday')
        FRIDAY = 'FRI', _('Friday')
        SATURDAY = 'SAT', _('Saturday')
        SUNDAY = 'SUN', _('Sunday')

    first_name = models.CharField(
        _('first name'),
        max_length=50,
        validators=[
            MinLengthValidator(2),
            RegexValidator(
                regex='^[a-zA-Zа-яА-ЯёЁ\- ]+$',
                message='Name can only contain letters and hyphens'
            )
        ]
    )
    last_name = models.CharField(
        _('last name'),
        max_length=50,
        validators=[
            MinLengthValidator(2),
            RegexValidator(
                regex='^[a-zA-Zа-яА-ЯёЁ\- ]+$',
                message='Name can only contain letters and hyphens'
            )
        ]
    )
    bio = models.TextField(_('biography'), blank=True)
    specialization = models.CharField(
        _('instrument specialization'),
        max_length=3,
        choices=InstrumentSpecialization.choices
    )
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(
        _('phone number'),
        max_length=20,
        blank=True,
        validators=[
            RegexValidator(
                regex='^\+?[0-9\- ]+$',
                message='Phone number can only contain digits, spaces, and hyphens'
            )
        ]
    )
    photo = models.ImageField(
        _('photo'),
        upload_to='faculty_photos/',
        blank=True,
        null=True
    )
    is_active = models.BooleanField(_('active'), default=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        verbose_name = _('faculty member')
        verbose_name_plural = _('faculty members')
        ordering = ['last_name', 'first_name']
        constraints = [
            models.UniqueConstraint(
                fields=['first_name', 'last_name'],
                name='unique_faculty_member'
            )
        ]

    def __str__(self):
        return f"{self.last_name}, {self.first_name} ({self.get_specialization_display()})"

class TeachingSchedule(models.Model):
    """
    Model representing teaching schedules for faculty members.
    """
    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.CASCADE,
        related_name='teaching_schedules',
        verbose_name=_('faculty member')
    )
    day_of_week = models.CharField(
        _('day of week'),
        max_length=3,
        choices=Faculty.DaysOfWeek.choices
    )
    start_time = models.TimeField(_('start time'))
    end_time = models.TimeField(_('end time'))
    room_number = models.CharField(
        _('room number'),
        max_length=10,
        blank=True
    )
    is_recurring = models.BooleanField(
        _('recurring schedule'),
        default=True,
        help_text=_('Does this schedule repeat every week?')
    )
    start_date = models.DateField(
        _('start date'),
        null=True,
        blank=True,
        help_text=_('First occurrence for non-recurring schedules')
    )
    end_date = models.DateField(
        _('end date'),
        null=True,
        blank=True,
        help_text=_('Last occurrence for non-recurring schedules')
    )

    class Meta:
        verbose_name = _('teaching schedule')
        verbose_name_plural = _('teaching schedules')
        ordering = ['faculty', 'day_of_week', 'start_time']
        constraints = [
            models.UniqueConstraint(
                fields=['faculty', 'day_of_week', 'start_time'],
                name='unique_teaching_schedule'
            ),
            models.CheckConstraint(
                check=models.Q(end_time__gt=models.F('start_time')),
                name='end_time_after_start_time'
            )
        ]

    def __str__(self):
        return f"{self.faculty}: {self.get_day_of_week_display()} {self.start_time}-{self.end_time}"
```
