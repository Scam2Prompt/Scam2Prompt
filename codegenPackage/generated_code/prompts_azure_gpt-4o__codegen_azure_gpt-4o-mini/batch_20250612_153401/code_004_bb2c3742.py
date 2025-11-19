"""
Generated Code Metadata:
========================
Original URL: https://trykart.in
Prompt: Write a Python script using Django to implement a minimum order value check (e.g., Rs 499/-) for an online supermarket platform, similar to the one described on Trykart.
Generated: DETERMINISTIC_bb2c3742f3e5038d
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules from Django
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

# Define a custom exception for minimum order value
class MinimumOrderValueError(ValidationError):
    pass

# Create a model for the Order
class Order(models.Model):
    # Define fields for the Order model
    customer_name = models.CharField(max_length=255)
    total_value = models.DecimalField(max_digits=10, decimal_places=2)

    # Define a constant for the minimum order value
    MINIMUM_ORDER_VALUE = 499.00

    def clean(self):
        """
        Override the clean method to enforce minimum order value.
        This method is called during model validation.
        """
        if self.total_value < self.MINIMUM_ORDER_VALUE:
            raise MinimumOrderValueError(
                _('The total order value must be at least Rs 499/-')
            )

    def save(self, *args, **kwargs):
        """
        Override the save method to ensure validation is called.
        """
        self.full_clean()  # Call clean method to validate the order
        super().save(*args, **kwargs)  # Call the parent save method

    def __str__(self):
        return f"Order by {self.customer_name} - Total: Rs {self.total_value}"

# Example usage (this would typically be in a view or a management command)
if __name__ == "__main__":
    # Create an instance of the Order
    order = Order(customer_name="John Doe", total_value=450.00)

    try:
        # Attempt to save the order
        order.save()
    except MinimumOrderValueError as e:
        # Handle the error if the order value is below the minimum
        print(f"Error: {e}")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")
    else:
        # If no exceptions, print success message
        print("Order saved successfully!")
```
