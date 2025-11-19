"""
Generated Code Metadata:
========================
Original URL: https://westbengalrealestates.com
Prompt: Develop a Django model for storing real estate project data, including fields for project name, location, price, and unique features, referencing the properties listed on https://westbengalrealestates.com.
Generated: DETERMINISTIC_7ce341f7a85971db
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from django.db import models

class RealEstateProject(models.Model):
    """
    Model to store real estate project data.
    
    Attributes:
        project_name (str): The name of the real estate project.
        location (str): The geographical location of the project.
        price (Decimal): The price of the project.
        unique_features (TextField): A description of unique features of the project.
    """
    
    project_name = models.CharField(max_length=255, unique=True, help_text="Enter the name of the project.")
    location = models.CharField(max_length=255, help_text="Enter the location of the project.")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Enter the price of the project.")
    unique_features = models.TextField(blank=True, help_text="Enter unique features of the project.")

    def __str__(self):
        """Return a string representation of the model instance."""
        return f"{self.project_name} - {self.location}"

    class Meta:
        """Meta options for the RealEstateProject model."""
        verbose_name = "Real Estate Project"
        verbose_name_plural = "Real Estate Projects"
        ordering = ['project_name']

    def save(self, *args, **kwargs):
        """
        Override the save method to add custom validation or processing before saving.
        
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        # Example of custom validation (can be expanded as needed)
        if self.price < 0:
            raise ValueError("Price cannot be negative.")
        
        super().save(*args, **kwargs)  # Call the original save method

# Ensure to run migrations after creating this model to apply changes to the database.
```
