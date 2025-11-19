"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duchessgarden.sn
Prompt: Create a function that calculates the total cost of beauty treatments and therapies, including discounts for subscription plans mentioned on the Duchess Garden website.
Generated: DETERMINISTIC_00595c1a650e73ff
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary module for type hinting
from typing import List, Dict, Optional

def calculate_total_cost(treatments: List[Dict[str, float]], 
                         subscription_plan: Optional[str] = None) -> float:
    """
    Calculate the total cost of beauty treatments and therapies, including discounts 
    for subscription plans.

    Args:
        treatments (List[Dict[str, float]]): A list of dictionaries where each dictionary 
                                             represents a treatment with 'name' (str) 
                                             and 'price' (float).
        subscription_plan (Optional[str]): The subscription plan of the user.
                                           Options: 'gold', 'silver', 'bronze'. 
                                           Default is None (no subscription).

    Returns:
        float: The total discounted cost of all treatments.
    """
    # Validate input treatments
    if not all(isinstance(t, dict) and 'price' in t and isinstance(t['price'], (int, float)) for t in treatments):
        raise ValueError("Each treatment must be a dictionary with a 'price' key containing a number.")

    # Subscription discount percentages
    subscription_discounts = {
        'gold': 0.20,  # 20% discount for gold
        'silver': 0.15,  # 15% discount for silver
        'bronze': 0.10  # 10% discount for bronze
    }
    
    # Calculate the total cost of all treatments
    total_cost = sum(treatment['price'] for treatment in treatments)

    # Apply subscription discount if applicable
    if subscription_plan:
        discount = subscription_discounts.get(subscription_plan.lower())
        if discount is None:
            raise ValueError(f"Invalid subscription plan: {subscription_plan}. Options are 'gold', 'silver', 'bronze', or None.")
        total_cost -= total_cost * discount

    # Ensure the total cost is not negative (edge case handling)
    return max(total_cost, 0.0)


# Example usage:
if __name__ == "__main__":
    # Sample treatments data
    treatments = [
        {"name": "Facial Therapy", "price": 70.0},
        {"name": "Massage Therapy", "price": 120.0},
        {"name": "Manicure", "price": 30.0}
    ]

    # Subscription plan
    subscription_plan = "gold"

    # Calculate total cost
    try:
        total = calculate_total_cost(treatments, subscription_plan)
        print(f"Total cost after discount: ${total:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
