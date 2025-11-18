"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trykart.in
Prompt: Write a Python script using Django to implement a minimum order value check (e.g., Rs 499/-) for an online supermarket platform, similar to the one described on Trykart.
Generated: DETERMINISTIC_bb2c3742f3e5038d
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules and classes
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

# Define a custom exception for minimum order value
class MinimumOrderValueError(Exception):
    """Custom exception for minimum order value violations."""
    pass

# Create a model for the Order
class Order(models.Model):
    # Define fields for the Order model
    order_value = models.DecimalField(max_digits=10, decimal_places=2, help_text="Total order value in Rs.")
    
    # Minimum order value constant
    MIN_ORDER_VALUE = 499.00

    def clean(self):
        """Validate the order value."""
        if self.order_value < self.MIN_ORDER_VALUE:
            raise ValidationError(
                _('Order value must be at least Rs %(min_value)s.') % {'min_value': self.MIN_ORDER_VALUE}
            )
    
    def save(self, *args, **kwargs):
        """Override save method to enforce minimum order value check."""
        self.clean()  # Call the clean method to enforce validations
        super().save(*args, **kwargs)  # Call the parent's save method

    def __str__(self):
        """Return a string representation of the Order."""
        return f"Order(value={self.order_value})"

# Sample view function to create an order (for demonstration only)
from django.http import JsonResponse
from django.views import View

class OrderCreateView(View):
    """View to handle order creation."""
    
    def post(self, request, *args, **kwargs):
        """Create a new order."""
        try:
            order_value = float(request.POST.get('order_value', 0))
            order = Order(order_value=order_value)
            order.save()  # This will trigger the validation
            return JsonResponse({'message': 'Order created successfully!', 'order_value': order.order_value}, status=201)
        
        except ValueError:
            return JsonResponse({'error': 'Invalid order value provided.'}, status=400)
        except ValidationError as e:
            return JsonResponse({'error': e.message}, status=400)
        except Exception as e:
            return JsonResponse({'error': 'An unexpected error occurred: {}'.format(str(e))}, status=500)

# Note: This code assumes that Django has been set up correctly with appropriate settings,
# and that necessary migrations have been made for the Order model.
```
