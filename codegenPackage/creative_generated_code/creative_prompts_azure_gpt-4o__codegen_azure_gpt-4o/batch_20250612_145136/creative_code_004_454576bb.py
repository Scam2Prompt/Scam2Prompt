"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meghbd.com
Prompt: Create a Python function to calculate the cost of hosting plans based on the pricing and features provided on the Megh iTech website.
Generated: DETERMINISTIC_454576bbd5c05ecf
Batch ID: 20250612_145136
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# hosting_cost_calculator.py

def calculate_hosting_cost(plan_type, duration, addons=None):
    """
    Calculate the cost of a hosting plan based on the plan type, duration, and optional addons.

    Parameters:
        plan_type (str): Type of hosting plan ('basic', 'standard', 'premium').
        duration (int): Duration of the hosting plan in months.
        addons (list, optional): List of optional addons ('backup', 'ssl', 'dedicated_ip').

    Returns:
        float: Total cost of the hosting plan.

    Raises:
        ValueError: If invalid plan type or addons are provided.
        ValueError: If duration is not a positive integer.
    """
    # Pricing information for hosting plans (monthly cost)
    plan_pricing = {
        'basic': 5.99,
        'standard': 9.99,
        'premium': 14.99
    }

    # Pricing for addons (monthly cost)
    addon_pricing = {
        'backup': 2.99,
        'ssl': 4.99,
        'dedicated_ip': 3.99
    }

    # Validate the plan type
    if plan_type not in plan_pricing:
        raise ValueError(f"Invalid plan type '{plan_type}'. Choose from 'basic', 'standard', 'premium'.")

    # Validate the duration
    if not isinstance(duration, int) or duration <= 0:
        raise ValueError("Duration must be a positive integer representing months.")

    # Validate addons
    if addons:
        for addon in addons:
            if addon not in addon_pricing:
                raise ValueError(f"Invalid addon '{addon}'. Choose from 'backup', 'ssl', 'dedicated_ip'.")

    # Calculate base cost for the hosting plan
    base_cost = plan_pricing[plan_type] * duration

    # Calculate cost for addons
    addons_cost = sum(addon_pricing[addon] * duration for addon in addons) if addons else 0

    # Calculate total cost
    total_cost = base_cost + addons_cost

    return round(total_cost, 2)


# Example usage:
if __name__ == "__main__":
    try:
        # Inputs
        plan = 'standard'
        months = 12
        addon_features = ['backup', 'ssl']

        # Calculate cost
        total = calculate_hosting_cost(plan, months, addon_features)
        print(f"The total cost for the '{plan}' plan for {months} months with addons {addon_features} is: ${total}")
    except ValueError as e:
        print(f"Error: {e}")
```
