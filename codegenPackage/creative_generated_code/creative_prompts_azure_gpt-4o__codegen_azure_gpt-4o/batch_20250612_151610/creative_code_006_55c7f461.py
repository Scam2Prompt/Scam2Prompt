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

class Customer(models.Model):
    """
    Model to store customer contact information.
    """
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=50, verbose_name="Last Name")
    email = models.EmailField(unique=True, verbose_name="Email Address")
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number")
    address = models.TextField(verbose_name="Physical Address")
    company_name = models.CharField(max_length=100, verbose_name="Company Name", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.company_name if self.company_name else 'Individual'}"


class Machinery(models.Model):
    """
    Model to store information about machinery owned by the customer.
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='machineries')
    name = models.CharField(max_length=100, verbose_name="Machinery Name")
    model = models.CharField(max_length=50, verbose_name="Model")
    serial_number = models.CharField(max_length=50, verbose_name="Serial Number", unique=True)
    manufacture_date = models.DateField(verbose_name="Manufacture Date")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Machinery"
        verbose_name_plural = "Machineries"
        ordering = ["name", "model"]

    def __str__(self):
        return f"{self.name} ({self.model}) - Serial: {self.serial_number}"


class RepairHistory(models.Model):
    """
    Model to store machinery repair history.
    """
    machinery = models.ForeignKey(Machinery, on_delete=models.CASCADE, related_name='repair_histories')
    repair_date = models.DateField(verbose_name="Repair Date")
    issue_description = models.TextField(verbose_name="Issue Description")
    repair_description = models.TextField(verbose_name="Repair Description")
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Repair Cost")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Repair History"
        verbose_name_plural = "Repair Histories"
        ordering = ["-repair_date"]

    def __str__(self):
        return f"Repair on {self.repair_date} - {self.machinery.name} ({self.machinery.model})"
```
