"""
Generated Code Metadata:
========================
Original URL: https://pediatricdentistinpune.com
Prompt: Develop a Django model for storing pediatric dentist information, including name, qualifications, location, and contact details, based on the structure of the website https://pediatricdentistinpune.com.
Generated: DETERMINISTIC_bc4bd5759148afcc
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

class PediatricDentist(models.Model):
    """
    Model to store information about pediatric dentists.
    """
    
    class QualificationChoices(models.TextChoices):
        BDS = 'BDS', _('Bachelor of Dental Surgery')
        MDS = 'MDS', _('Master of Dental Surgery')
        DDS = 'DDS', _('Doctor of Dental Surgery')
        OTHER = 'OTH', _('Other Qualification')
    
    name = models.CharField(
        _('Full Name'),
        max_length=100,
        help_text=_("Enter the dentist's full name")
    )
    
    qualifications = models.CharField(
        _('Qualifications'),
        max_length=50,
        choices=QualificationChoices.choices,
        default=QualificationChoices.BDS,
        help_text=_("Select the dentist's primary qualification")
    )
    
    other_qualification = models.CharField(
        _('Other Qualification'),
        max_length=100,
        blank=True,
        null=True,
        help_text=_("Specify if 'Other' qualification is selected")
    )
    
    years_of_experience = models.PositiveIntegerField(
        _('Years of Experience'),
        default=0,
        help_text=_("Number of years of experience in pediatric dentistry")
    )
    
    clinic_name = models.CharField(
        _('Clinic/Hospital Name'),
        max_length=100,
        help_text=_("Name of the clinic or hospital where the dentist practices")
    )
    
    address = models.TextField(
        _('Clinic Address'),
        help_text=_("Full address of the clinic")
    )
    
    city = models.CharField(
        _('City'),
        max_length=50,
        default='Pune',
        help_text=_("City where the clinic is located")
    )
    
    pincode = models.CharField(
        _('Pincode'),
        max_length=6,
        validators=[RegexValidator(r'^\d{6}$', _('Enter a valid 6-digit pincode'))],
        help_text=_("6-digit postal code")
    )
    
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message=_("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    )
    phone_number = models.CharField(
        _('Phone Number'),
        validators=[phone_regex],
        max_length=17,
        help_text=_("Contact phone number")
    )
    
    email = models.EmailField(
        _('Email Address'),
        blank=True,
        null=True,
        help_text=_("Professional email address")
    )
    
    website = models.URLField(
        _('Website'),
        blank=True,
        null=True,
        help_text=_("Clinic website URL if available")
    )
    
    consultation_fee = models.DecimalField(
        _('Consultation Fee'),
        max_digits=8,
        decimal_places=2,
        help_text=_("Standard consultation fee in INR")
    )
    
    available_timings = models.CharField(
        _('Available Timings'),
        max_length=100,
        help_text=_("Clinic timings (e.g., '10 AM - 6 PM')")
    )
    
    languages_spoken = models.CharField(
        _('Languages Spoken'),
        max_length=200,
        default='English, Hindi, Marathi',
        help_text=_("Languages the dentist can communicate in")
    )
    
    specializations = models.TextField(
        _('Specializations'),
        blank=True,
        null=True,
        help_text=_("Any special areas of expertise in pediatric dentistry")
    )
    
    is_verified = models.BooleanField(
        _('Verified Profile'),
        default=False,
        help_text=_("Mark as verified if the information has been confirmed")
    )
    
    created_at = models.DateTimeField(
        _('Created At'),
        auto_now_add=True,
        help_text=_("When this record was first created")
    )
    
    updated_at = models.DateTimeField(
        _('Updated At'),
        auto_now=True,
        help_text=_("When this record was last updated")
    )
    
    class Meta:
        verbose_name = _('Pediatric Dentist')
        verbose_name_plural = _('Pediatric Dentists')
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} ({self.clinic_name})"
    
    def get_qualification_display(self):
        if self.qualifications == self.QualificationChoices.OTHER and self.other_qualification:
            return self.other_qualification
        return self.get_qualifications_display()
```
