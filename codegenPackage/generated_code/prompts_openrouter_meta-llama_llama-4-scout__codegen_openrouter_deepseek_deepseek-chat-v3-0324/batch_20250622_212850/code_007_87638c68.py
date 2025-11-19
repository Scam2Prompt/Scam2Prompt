"""
Generated Code Metadata:
========================
Original URL: https://www.prointegrationfuture.asia
Prompt: Develop a basic data model and database schema to manage exhibitor information, products, and visitor interactions for the Pro Integration Future Asia event.
Generated: DETERMINISTIC_87638c681f59f81b
Batch ID: 20250622_212850
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
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.translation import gettext_lazy as _

class Exhibitor(models.Model):
    """
    Represents an exhibitor participating in the event.
    """
    class CompanySize(models.TextChoices):
        SMALL = 'S', _('Small (1-50 employees)')
        MEDIUM = 'M', _('Medium (51-500 employees)')
        LARGE = 'L', _('Large (500+ employees)')

    name = models.CharField(
        max_length=200,
        verbose_name=_("Company Name"),
        help_text=_("Official name of the exhibiting company")
    )
    description = models.TextField(
        verbose_name=_("Company Description"),
        help_text=_("Brief description of the company and its offerings")
    )
    logo = models.ImageField(
        upload_to='exhibitors/logos/',
        null=True,
        blank=True,
        verbose_name=_("Company Logo")
    )
    website = models.URLField(
        max_length=200,
        blank=True,
        verbose_name=_("Website URL")
    )
    contact_email = models.EmailField(
        max_length=100,
        verbose_name=_("Contact Email")
    )
    contact_phone = models.CharField(
        max_length=20,
        verbose_name=_("Contact Phone")
    )
    company_size = models.CharField(
        max_length=1,
        choices=CompanySize.choices,
        verbose_name=_("Company Size")
    )
    booth_number = models.CharField(
        max_length=10,
        verbose_name=_("Booth Number")
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Active Exhibitor")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created At")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated At")
    )

    class Meta:
        verbose_name = _("Exhibitor")
        verbose_name_plural = _("Exhibitors")
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    """
    Represents a product or service offered by an exhibitor.
    """
    exhibitor = models.ForeignKey(
        Exhibitor,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name=_("Exhibitor")
    )
    name = models.CharField(
        max_length=200,
        verbose_name=_("Product Name")
    )
    description = models.TextField(
        verbose_name=_("Product Description")
    )
    category = models.CharField(
        max_length=100,
        verbose_name=_("Product Category")
    )
    image = models.ImageField(
        upload_to='products/images/',
        null=True,
        blank=True,
        verbose_name=_("Product Image")
    )
    brochure = models.FileField(
        upload_to='products/brochures/',
        null=True,
        blank=True,
        verbose_name=_("Product Brochure")
    )
    is_featured = models.BooleanField(
        default=False,
        verbose_name=_("Featured Product")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created At")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated At")
    )

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.exhibitor.name})"

class Visitor(models.Model):
    """
    Represents a visitor attending the event.
    """
    class VisitorType(models.TextChoices):
        GENERAL = 'G', _('General Visitor')
        VIP = 'V', _('VIP Visitor')
        PRESS = 'P', _('Press/Media')
        SPEAKER = 'S', _('Speaker/Presenter')

    first_name = models.CharField(
        max_length=100,
        verbose_name=_("First Name")
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name=_("Last Name")
    )
    email = models.EmailField(
        max_length=100,
        unique=True,
        verbose_name=_("Email Address")
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name=_("Phone Number")
    )
    company = models.CharField(
        max_length=200,
        blank=True,
        verbose_name=_("Company Name")
    )
    job_title = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Job Title")
    )
    visitor_type = models.CharField(
        max_length=1,
        choices=VisitorType.choices,
        default=VisitorType.GENERAL,
        verbose_name=_("Visitor Type")
    )
    badge_id = models.CharField(
        max_length=20,
        unique=True,
        verbose_name=_("Badge ID")
    )
    registration_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Registration Date")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated At")
    )

    class Meta:
        verbose_name = _("Visitor")
        verbose_name_plural = _("Visitors")
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Interaction(models.Model):
    """
    Represents an interaction between a visitor and an exhibitor/product.
    """
    class InteractionType(models.TextChoices):
        BOOTH_VISIT = 'B', _('Booth Visit')
        PRODUCT_DEMO = 'D', _('Product Demo')
        MEETING = 'M', _('Scheduled Meeting')
        MATERIAL_DOWNLOAD = 'L', _('Material Download')

    visitor = models.ForeignKey(
        Visitor,
        on_delete=models.CASCADE,
        related_name='interactions',
        verbose_name=_("Visitor")
    )
    exhibitor = models.ForeignKey(
        Exhibitor,
        on_delete=models.CASCADE,
        related_name='interactions',
        verbose_name=_("Exhibitor")
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='interactions',
        verbose_name=_("Product")
    )
    interaction_type = models.CharField(
        max_length=1,
        choices=InteractionType.choices,
        verbose_name=_("Interaction Type")
    )
    notes = models.TextField(
        blank=True,
        verbose_name=_("Interaction Notes")
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Interaction Time")
    )
    duration = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text=_("Duration in minutes"),
        verbose_name=_("Duration")
    )
    follow_up_required = models.BooleanField(
        default=False,
        verbose_name=_("Follow Up Required")
    )
    follow_up_notes = models.TextField(
        blank=True,
        verbose_name=_("Follow Up Notes")
    )

    class Meta:
        verbose_name = _("Interaction")
        verbose_name_plural = _("Interactions")
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.visitor} - {self.exhibitor} ({self.get_interaction_type_display()})"

class Lead(models.Model):
    """
    Represents a sales lead generated from visitor interactions.
    """
    class LeadStatus(models.TextChoices):
        NEW = 'N', _('New')
        CONTACTED = 'C', _('Contacted')
        QUALIFIED = 'Q', _('Qualified')
        LOST = 'L', _('Lost')
        WON = 'W', _('Won')

    interaction = models.OneToOneField(
        Interaction,
        on_delete=models.CASCADE,
        related_name='lead',
        verbose_name=_("Interaction")
    )
    status = models.CharField(
        max_length=1,
        choices=LeadStatus.choices,
        default=LeadStatus.NEW,
        verbose_name=_("Lead Status")
    )
    potential_value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name=_("Potential Value")
    )
    probability = models.PositiveIntegerField(
        validators=[MaxLengthValidator(100)],
        default=0,
        verbose_name=_("Probability (%)")
    )
    expected_close_date = models.DateField(
        null=True,
        blank=True,
        verbose_name=_("Expected Close Date")
    )
    notes = models.TextField(
        blank=True,
        verbose_name=_("Lead Notes")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created At")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated At")
    )

    class Meta:
        verbose_name = _("Lead")
        verbose_name_plural = _("Leads")
        ordering = ['-created_at']

    def __str__(self):
        return f"Lead #{self.id} - {self.interaction.visitor}"
```
