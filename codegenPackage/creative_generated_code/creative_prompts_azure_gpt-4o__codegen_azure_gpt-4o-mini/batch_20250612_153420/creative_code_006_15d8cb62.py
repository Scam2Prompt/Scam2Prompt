"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fusionjiujitsu.com.br
Prompt: Write a Django view function that displays the Fusion Jiu Jitsu School's pricing plans dynamically, categorized by program type (e.g., "Plano Baby," "Plano Ouro").
Generated: DETERMINISTIC_15d8cb627c83a380
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# views.py

from django.shortcuts import render
from django.http import Http404
from .models import PricingPlan

def pricing_plans_view(request):
    """
    View function to display the pricing plans categorized by program type.
    
    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML template with the pricing plans.
    """
    try:
        # Fetch all pricing plans from the database
        pricing_plans = PricingPlan.objects.all()

        # Organize plans by program type
        plans_by_type = {}
        for plan in pricing_plans:
            if plan.program_type not in plans_by_type:
                plans_by_type[plan.program_type] = []
            plans_by_type[plan.program_type].append(plan)

        # Render the template with the categorized pricing plans
        return render(request, 'pricing/plans.html', {'plans_by_type': plans_by_type})
    
    except PricingPlan.DoesNotExist:
        # Handle case where the pricing plans do not exist
        raise Http404("No pricing plans available.")

    except Exception as e:
        # Log the error for debugging purposes
        # Note: Logging should be configured separately in production
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Unexpected error while fetching pricing plans: {e}")

        # Return an appropriate error response
        return render(request, 'pricing/error.html', {'error_message': 'An unexpected error occurred.'})
```

```python
# models.py

from django.db import models

class PricingPlan(models.Model):
    """
    Model representing a pricing plan for the Jiu Jitsu School.
    
    Attributes:
        program_type (str): The type of the program (e.g., "Plano Baby", "Plano Ouro").
        price (decimal): The price of the plan.
        description (str): A brief description of the plan.
    """
    program_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.program_type} - {self.price} USD"
```

```html
<!-- templates/pricing/plans.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pricing Plans</title>
</head>
<body>
    <h1>Fusion Jiu Jitsu School Pricing Plans</h1>
    {% for program_type, plans in plans_by_type.items %}
        <h2>{{ program_type }}</h2>
        <ul>
            {% for plan in plans %}
                <li>
                    <strong>{{ plan.description }}</strong>: {{ plan.price }} USD
                </li>
            {% endfor %}
        </ul>
    {% endfor %}
</body>
</html>
```

```html
<!-- templates/pricing/error.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <h1>Error</h1>
    <p>{{ error_message }}</p>
</body>
</html>
```
