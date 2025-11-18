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
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import PricingPlan

def pricing_plans_view(request):
    """
    Django view function to display Fusion Jiu Jitsu School's pricing plans dynamically,
    categorized by program type (e.g., "Plano Baby," "Plano Ouro").

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML response or JSON response with pricing plans categorized by program type.
    """
    try:
        # Fetch all pricing plans from the database
        pricing_plans = PricingPlan.objects.all()

        # Organize pricing plans by program type
        categorized_plans = {}
        for plan in pricing_plans:
            program_type = plan.program_type
            if program_type not in categorized_plans:
                categorized_plans[program_type] = []
            categorized_plans[program_type].append({
                'name': plan.name,
                'price': plan.price,
                'description': plan.description
            })

        # Check if the request is asking for JSON response (e.g., for APIs)
        if request.GET.get('format') == 'json':
            return JsonResponse(categorized_plans, safe=False)

        # Render the pricing plans in an HTML template
        return render(request, 'pricing_plans.html', {'categorized_plans': categorized_plans})
    
    except ObjectDoesNotExist:
        # Handle the case where the PricingPlan model is empty or missing
        return JsonResponse({'error': 'Pricing plans not available.'}, status=404)
    
    except Exception as e:
        # Handle any unexpected errors gracefully
        return JsonResponse({'error': 'An unexpected error occurred.', 'details': str(e)}, status=500)
```

### Notes:
1. This code assumes a `PricingPlan` model exists in your Django app with fields like `program_type`, `name`, `price`, and `description`.
2. Create a corresponding HTML template (`pricing_plans.html`) to display the pricing plans dynamically.
3. Ensure your database is populated with pricing plans for proper functionality.
4. Proper error handling is included for missing data and unexpected runtime errors.
