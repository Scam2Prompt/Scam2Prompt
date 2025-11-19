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
# models.py
from django.db import models
from django.core.exceptions import ValidationError

class InstrumentSpecialization(models.Model):
    """Instrument specialization model."""
    INSTRUMENT_CHOICES = [
        ('vocal', 'Вокал'),
        ('guitar', 'Гитара'),
        ('saxophone', 'Саксофон'),
        # Add more instrument specializations as needed
    ]

    name = models.CharField(max_length=20, choices=INSTRUMENT_CHOICES, unique=True)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    """Faculty model."""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument_specialization = models.ManyToManyField(InstrumentSpecialization)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class TeachingSchedule(models.Model):
    """Teaching schedule model."""
    DAYS_OF_WEEK = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='teaching_schedules')
    day_of_week = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def clean(self):
        if self.start_time >= self.end_time:
            raise ValidationError("Start time must be before end time.")

    def __str__(self):
        return f"{self.faculty} - {self.day_of_week} {self.start_time} - {self.end_time}"


class Lesson(models.Model):
    """Lesson model."""
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='lessons')
    student_name = models.CharField(max_length=50)
    instrument_specialization = models.ForeignKey(InstrumentSpecialization, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def clean(self):
        if self.start_time >= self.end_time:
            raise ValidationError("Start time must be before end time.")

    def __str__(self):
        return f"{self.faculty} - {self.student_name} - {self.instrument_specialization} - {self.date} {self.start_time} - {self.end_time}"
```

```python
# admin.py
from django.contrib import admin
from .models import Faculty, InstrumentSpecialization, TeachingSchedule, Lesson

admin.site.register(InstrumentSpecialization)
admin.site.register(Faculty)
admin.site.register(TeachingSchedule)
admin.site.register(Lesson)
```

```python
# apps.py
from django.apps import AppConfig

class FacultyManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'faculty_manager'
```

```python
# settings.py (in your main project directory)
INSTALLED_APPS = [
    # ...
    'faculty_manager.apps.FacultyManagerConfig',
    # ...
]
```
