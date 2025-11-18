"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trackdieselperu.com
Prompt: Write a Django model for storing customer contact information and machinery repair history, tailored to the services provided by Track Diesel Peru.
Generated: DETERMINISTIC_55c7f46152aab222
Batch ID: 20250612_151610
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

class Customer(models.Model):
    """
    Model to store customer contact information.
    """
    first_name = models.CharField(max_length=50, help_text="Customer's first name.")
    last_name = models.CharField(max_length=50, help_text="Customer's last name.")
    email = models.EmailField(unique=True, help_text="Customer's email address.")
    phone_number = models.CharField(max_length=15, blank=True, help_text="Customer's phone number.")
    address = models.TextField(blank=True, help_text="Customer's address.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the customer record was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the customer record was last updated.")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def clean(self):
        """
        Custom validation to ensure that either email or phone number is provided.
        """
        if not self.email and not self.phone_number:
            raise ValidationError("At least one of email or phone number must be provided.")

class RepairHistory(models.Model):
    """
    Model to store machinery repair history for customers.
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='repair_histories', help_text="Reference to the associated customer.")
    machinery_type = models.CharField(max_length=100, help_text="Type of machinery that was repaired.")
    repair_date = models.DateTimeField(help_text="Date when the repair was completed.")
    description = models.TextField(help_text="Description of the repair work done.")
    cost = models.DecimalField(max_digits=10, decimal_places=2, help_text="Cost of the repair.")

    def __str__(self):
        return f"Repair for {self.machinery_type} on {self.repair_date.strftime('%Y-%m-%d')}"

    def clean(self):
        """
        Custom validation to ensure repair date is not in the future.
        """
        if self.repair_date > timezone.now():
            raise ValidationError("Repair date cannot be in the future.")

    class Meta:
        verbose_name_plural = "Repair Histories"
        ordering = ['-repair_date']
```
