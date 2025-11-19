"""
Generated Code Metadata:
========================
Original URL: https://meghbd.com
Prompt: Create a Python function to calculate the cost of hosting plans based on the pricing and features provided on the Megh iTech website.
Generated: DETERMINISTIC_454576bbd5c05ecf
Batch ID: 20250612_145136
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_hosting_cost(plan_name, duration_months, additional_features=None):
    """
    Calculate the total cost of a hosting plan based on the selected plan, duration, and additional features.
    
    Args:
        plan_name (str): Name of the hosting plan (e.g., 'Basic', 'Standard', 'Premium').
        duration_months (int): Duration of the hosting plan in months.
        additional_features (dict, optional): Dictionary of additional features and their quantities.
            Example: {'SSL': 1, 'Backup': 2}
    
    Returns:
        float: Total cost of the hosting plan including additional features.
    
    Raises:
        ValueError: If invalid plan name or negative duration is provided.
    """
    # Define base pricing for hosting plans (monthly)
    PLAN_PRICES = {
        'Basic': 5.99,
        'Standard': 12.99,
        'Premium': 24.99
    }
    
    # Define pricing for additional features (one-time or monthly)
    FEATURE_PRICES = {
        'SSL': {'type': 'monthly', 'price': 2.99},
        'Backup': {'type': 'monthly', 'price': 1.50},
        'CDN': {'type': 'one-time', 'price': 9.99},
        'DedicatedIP': {'type': 'monthly', 'price': 3.99}
    }
    
    # Validate input parameters
    if plan_name not in PLAN_PRICES:
        raise ValueError(f"Invalid plan name. Available plans: {', '.join(PLAN_PRICES.keys())}")
    
    if duration_months <= 0:
        raise ValueError("Duration must be a positive number of months")
    
    # Calculate base plan cost
    base_cost = PLAN_PRICES[plan_name] * duration_months
    
    # Initialize additional features cost
    additional_cost = 0.0
    
    # Calculate cost for additional features if provided
    if additional_features:
        for feature, quantity in additional_features.items():
            if feature not in FEATURE_PRICES:
                raise ValueError(f"Invalid feature: {feature}")
            
            if quantity <= 0:
                raise ValueError(f"Quantity for {feature} must be positive")
            
            feature_info = FEATURE_PRICES[feature]
            if feature_info['type'] == 'monthly':
                additional_cost += feature_info['price'] * quantity * duration_months
            else:  # one-time
                additional_cost += feature_info['price'] * quantity
    
    # Calculate total cost
    total_cost = base_cost + additional_cost
    
    return round(total_cost, 2)
```
