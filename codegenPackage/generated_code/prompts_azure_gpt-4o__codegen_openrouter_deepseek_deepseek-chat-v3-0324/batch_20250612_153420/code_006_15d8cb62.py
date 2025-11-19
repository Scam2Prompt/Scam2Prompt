"""
Generated Code Metadata:
========================
Original URL: https://fusionjiujitsu.com.br
Prompt: Write a Django view function that displays the Fusion Jiu Jitsu School's pricing plans dynamically, categorized by program type (e.g., "Plano Baby," "Plano Ouro").
Generated: DETERMINISTIC_15d8cb627c83a380
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from django.shortcuts import render
from django.http import Http404
from .models import PricingPlan

def pricing_plans_view(request):
    """
    View function to display Fusion Jiu Jitsu School's pricing plans
    dynamically categorized by program type.
    """
    try:
        # Get all active pricing plans ordered by program type and price
        plans = PricingPlan.objects.filter(is_active=True).order_by('program_type', 'price')
        
        if not plans.exists():
            raise PricingPlan.DoesNotExist("No pricing plans available")
            
        # Categorize plans by program type
        categorized_plans = {}
        for plan in plans:
            if plan.program_type not in categorized_plans:
                categorized_plans[plan.program_type] = []
            categorized_plans[plan.program_type].append(plan)
            
        context = {
            'categorized_plans': categorized_plans,
            'page_title': 'Fusion Jiu Jitsu - Pricing Plans'
        }
        
        return render(request, 'pricing/plans.html', context)
        
    except PricingPlan.DoesNotExist:
        raise Http404("Pricing information is currently unavailable")
    except Exception as e:
        # Log the error for debugging (in production you'd use proper logging)
        print(f"Error retrieving pricing plans: {str(e)}")
        raise Http404("An error occurred while retrieving pricing information")
```
