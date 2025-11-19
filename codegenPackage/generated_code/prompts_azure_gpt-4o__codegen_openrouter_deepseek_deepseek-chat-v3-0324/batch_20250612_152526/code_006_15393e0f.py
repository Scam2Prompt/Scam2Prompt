"""
Generated Code Metadata:
========================
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Write a Django model for managing educational institution data, including fields for school locations, academic programs, administrative services, and institutional recognitions, inspired by the Politécnico Municipal de Cali.
Generated: DETERMINISTIC_15393e0fda24e839
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.translation import gettext_lazy as _

class Institution(models.Model):
    """
    Model representing the educational institution.
    """
    name = models.CharField(
        _('name'),
        max_length=200,
        unique=True,
        help_text=_('Official name of the institution')
    )
    acronym = models.CharField(
        _('acronym'),
        max_length=20,
        unique=True,
        help_text=_('Short name or abbreviation of the institution')
    )
    foundation_date = models.DateField(
        _('foundation date'),
        help_text=_('Date when the institution was founded')
    )
    mission = models.TextField(
        _('mission'),
        help_text=_('Institutional mission statement')
    )
    vision = models.TextField(
        _('vision'),
        help_text=_('Institutional vision statement')
    )
    logo = models.ImageField(
        _('logo'),
        upload_to='institution/logos/',
        null=True,
        blank=True,
        help_text=_('Institutional logo image')
    )
    website = models.URLField(
        _('website'),
        max_length=200,
        blank=True,
        help_text=_('Official website URL')
    )

    class Meta:
        verbose_name = _('institution')
        verbose_name_plural = _('institutions')
        ordering = ['name']

    def __str__(self):
        return self.name

class Location(models.Model):
    """
    Model representing physical locations of the institution.
    """
    institution = models.ForeignKey(
        Institution,
        on_delete=models.CASCADE,
        related_name='locations',
        verbose_name=_('institution')
    )
    name = models.CharField(
        _('location name'),
        max_length=100,
        help_text=_('Name of this location (e.g., Main Campus)')
    )
    address = models.TextField(
        _('address'),
        help_text=_('Complete physical address')
    )
    city = models.CharField(
        _('city'),
        max_length=100,
        help_text=_('City where the location is situated')
    )
    postal_code = models.CharField(
        _('postal code'),
        max_length=20,
        blank=True,
        help_text=_('Postal/ZIP code for this location')
    )
    phone = models.CharField(
        _('phone number'),
        max_length=20,
        blank=True,
        help_text=_('Main contact phone number')
    )
    email = models.EmailField(
        _('email'),
        max_length=100,
        blank=True,
        help_text=_('General contact email')
    )
    is_main = models.BooleanField(
        _('main location'),
        default=False,
        help_text=_('Is this the main location of the institution?')
    )
    coordinates = models.CharField(
        _('coordinates'),
        max_length=50,
        blank=True,
        help_text=_('Geographic coordinates (latitude, longitude)')
    )

    class Meta:
        verbose_name = _('location')
        verbose_name_plural = _('locations')
        ordering = ['-is_main', 'name']
        unique_together = ('institution', 'name')

    def __str__(self):
        return f"{self.name} ({self.institution.acronym})"

class AcademicProgram(models.Model):
    """
    Model representing academic programs offered by the institution.
    """
    PROGRAM_LEVEL_CHOICES = [
        ('T', _('Technical')),
        ('TE', _('Technologist')),
        ('P', _('Professional')),
        ('S', _('Specialization')),
        ('M', _('Master')),
        ('D', _('Doctorate')),
    ]

    MODALITY_CHOICES = [
        ('P', _('Presential')),
        ('V', _('Virtual')),
        ('H', _('Hybrid')),
    ]

    institution = models.ForeignKey(
        Institution,
        on_delete=models.CASCADE,
        related_name='academic_programs',
        verbose_name=_('institution')
    )
    name = models.CharField(
        _('program name'),
        max_length=200,
        help_text=_('Official name of the academic program')
    )
    code = models.CharField(
        _('program code'),
        max_length=20,
        unique=True,
        help_text=_('Unique institutional code for this program')
    )
    description = models.TextField(
        _('description'),
        help_text=_('Detailed description of the program')
    )
    level = models.CharField(
        _('academic level'),
        max_length=2,
        choices=PROGRAM_LEVEL_CHOICES,
        help_text=_('Academic level of the program')
    )
    modality = models.CharField(
        _('modality'),
        max_length=1,
        choices=MODALITY_CHOICES,
        default='P',
        help_text=_('Teaching modality')
    )
    duration = models.PositiveSmallIntegerField(
        _('duration (semesters)'),
        help_text=_('Program duration in semesters')
    )
    credits = models.PositiveSmallIntegerField(
        _('total credits'),
        help_text=_('Total credits required to complete the program')
    )
    is_active = models.BooleanField(
        _('is active'),
        default=True,
        help_text=_('Is this program currently being offered?')
    )
    creation_date = models.DateField(
        _('creation date'),
        help_text=_('Date when the program was created')
    )
    locations = models.ManyToManyField(
        Location,
        related_name='academic_programs',
        verbose_name=_('available locations'),
        help_text=_('Locations where this program is offered')
    )

    class Meta:
        verbose_name = _('academic program')
        verbose_name_plural = _('academic programs')
        ordering = ['level', 'name']
        unique_together = ('institution', 'name')

    def __str__(self):
        return f"{self.name} ({self.get_level_display()})"

class AdministrativeService(models.Model):
    """
    Model representing administrative services offered by the institution.
    """
    SERVICE_TYPE_CHOICES = [
        ('ADM', _('Admissions')),
        ('REG', _('Registration')),
        ('FIN', _('Financial')),
        ('ACA', _('Academic')),
        ('LIB', _('Library')),
        ('IT', _('IT Support')),
        ('HR', _('Human Resources')),
        ('OTH', _('Other')),
    ]

    institution = models.ForeignKey(
        Institution,
        on_delete=models.CASCADE,
        related_name='administrative_services',
        verbose_name=_('institution')
    )
    name = models.CharField(
        _('service name'),
        max_length=100,
        help_text=_('Name of the administrative service')
    )
    service_type = models.CharField(
        _('service type'),
        max_length=3,
        choices=SERVICE_TYPE_CHOICES,
        help_text=_('Type of administrative service')
    )
    description = models.TextField(
        _('description'),
        help_text=_('Detailed description of the service')
    )
    responsible_unit = models.CharField(
        _('responsible unit'),
        max_length=100,
        help_text=_('Department or unit responsible for this service')
    )
    contact_email = models.EmailField(
        _('contact email'),
        max_length=100,
        blank=True,
        help_text=_('Contact email for this service')
    )
    contact_phone = models.CharField(
        _('contact phone'),
        max_length=20,
        blank=True,
        help_text=_('Contact phone number for this service')
    )
    is_available_online = models.BooleanField(
        _('available online'),
        default=False,
        help_text=_('Can this service be accessed online?')
    )
    online_link = models.URLField(
        _('online link'),
        max_length=200,
        blank=True,
        help_text=_('URL for online access to this service')
    )

    class Meta:
        verbose_name = _('administrative service')
        verbose_name_plural = _('administrative services')
        ordering = ['service_type', 'name']
        unique_together = ('institution', 'name')

    def __str__(self):
        return f"{self.name} ({self.get_service_type_display()})"

class InstitutionalRecognition(models.Model):
    """
    Model representing recognitions, accreditations, and certifications received by the institution.
    """
    RECOGNITION_TYPE_CHOICES = [
        ('ACC', _('Accreditation')),
        ('CER', _('Certification')),
        ('LIC', _('License')),
        ('AWD', _('Award')),
        ('RANK', _('Ranking')),
        ('OTH', _('Other')),
    ]

    institution = models.ForeignKey(
        Institution,
        on_delete=models.CASCADE,
        related_name='recognitions',
        verbose_name=_('institution')
    )
    title = models.CharField(
        _('recognition title'),
        max_length=200,
        help_text=_('Title or name of the recognition')
    )
    recognition_type = models.CharField(
        _('recognition type'),
        max_length=4,
        choices=RECOGNITION_TYPE_CHOICES,
        help_text=_('Type of recognition')
    )
    granting_entity = models.CharField(
        _('granting entity'),
        max_length=200,
        help_text=_('Organization
