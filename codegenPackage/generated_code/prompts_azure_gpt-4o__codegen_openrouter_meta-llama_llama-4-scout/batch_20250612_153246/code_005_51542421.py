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
# models.py
from django.db import models
from django.core.exceptions import ValidationError

class MembershipType(models.Model):
    """Represents a PSHP membership type."""
    MEMBERSHIP_TYPE_CHOICES = [
        ('pharmacy_professional', 'Pharmacy Professional'),
        ('pharmacy_student', 'Pharmacy Student'),
    ]

    name = models.CharField(
        max_length=20,
        choices=MEMBERSHIP_TYPE_CHOICES,
        unique=True,
        help_text="The name of the membership type."
    )

    def __str__(self):
        return self.name

class Privilege(models.Model):
    """Represents a privilege associated with a membership type."""
    name = models.CharField(
        max_length=100,
        help_text="The name of the privilege."
    )

    def __str__(self):
        return self.name

class MembershipTypePrivilege(models.Model):
    """Represents a many-to-many relationship between MembershipType and Privilege."""
    membership_type = models.ForeignKey(
        MembershipType,
        on_delete=models.CASCADE,
        related_name='privileges',
        help_text="The membership type associated with the privilege."
    )

    privilege = models.ForeignKey(
        Privilege,
        on_delete=models.CASCADE,
        related_name='membership_types',
        help_text="The privilege associated with the membership type."
    )

    class Meta:
        unique_together = ('membership_type', 'privilege')

    def __str__(self):
        return f"{self.membership_type} - {self.privilege}"

    def clean(self):
        if self.membership_type == self.privilege.membership_types.filter(membership_type=self.membership_type).first():
            raise ValidationError("A membership type cannot have duplicate privileges.")

class PharmacyProfessionalMembership(MembershipType):
    """Represents a pharmacy professional membership."""
    class Meta:
        proxy = True

class PharmacyStudentMembership(MembershipType):
    """Represents a pharmacy student membership."""
    class Meta:
        proxy = True
```

```python
# admin.py
from django.contrib import admin
from .models import MembershipType, Privilege, MembershipTypePrivilege, PharmacyProfessionalMembership, PharmacyStudentMembership

admin.site.register(MembershipType)
admin.site.register(Privilege)
admin.site.register(MembershipTypePrivilege)

@admin.register(PharmacyProfessionalMembership)
class PharmacyProfessionalMembershipAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(PharmacyStudentMembership)
class PharmacyStudentMembershipAdmin(admin.ModelAdmin):
    list_display = ('name',)
```

```python
# apps.py
from django.apps import AppConfig

class MembershipAppConfig(AppConfig):
    name = 'membership'
    verbose_name = "Membership Management"

    def ready(self):
        import membership.signals
```

```python
# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MembershipType, MembershipTypePrivilege

@receiver(post_save, sender=MembershipType)
def create_default_privileges(sender, instance, created, **kwargs):
    if created:
        # Assign default privileges for pharmacy professional membership
        if instance.name == 'pharmacy_professional':
            privilege, _ = Privilege.objects.get_or_create(name='Can view pharmacy professional content')
            MembershipTypePrivilege.objects.create(membership_type=instance, privilege=privilege)

        # Assign default privileges for pharmacy student membership
        elif instance.name == 'pharmacy_student':
            privilege, _ = Privilege.objects.get_or_create(name='Can view pharmacy student content')
            MembershipTypePrivilege.objects.create(membership_type=instance, privilege=privilege)
```
