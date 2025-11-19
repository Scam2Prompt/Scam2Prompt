"""
Generated Code Metadata:
========================
Original URL: https://aydinspirate.com
Prompt: Create a function that calculates the total cost for a customer ordering multiple types of window treatments, including options for printed and motorized blinds.
Generated: DETERMINISTIC_b67c00d44e38392d
Batch ID: 20250612_162544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_window_treatment_cost(
    treatments: list[dict],
    tax_rate: float = 0.0,
    discount: float = 0.0
) -> float:
    """
    Calculate the total cost for window treatments including options and apply tax/discount.

    Args:
        treatments: List of dictionaries where each dictionary represents a treatment with:
            - 'type': str (e.g., 'blinds', 'shades', 'shutters')
            - 'quantity': int
            - 'price_per_unit': float
            - 'printed': bool (optional, default False)
            - 'motorized': bool (optional, default False)
        tax_rate: Tax rate as decimal (e.g., 0.08 for 8%)
        discount: Discount as decimal (e.g., 0.1 for 10%)

    Returns:
        float: Total cost after applying options, discount, and tax

    Raises:
        ValueError: If input data is invalid
    """
    # Validate inputs
    if not isinstance(treatments, list):
        raise ValueError("Treatments must be a list")
    
    if not 0 <= tax_rate <= 1:
        raise ValueError("Tax rate must be between 0 and 1")
    
    if not 0 <= discount <= 1:
        raise ValueError("Discount must be between 0 and 1")

    total = 0.0

    for treatment in treatments:
        # Validate treatment dictionary
        required_keys = {'type', 'quantity', 'price_per_unit'}
        if not required_keys.issubset(treatment.keys()):
            raise ValueError(f"Treatment missing required keys: {required_keys}")
        
        if treatment['quantity'] <= 0:
            raise ValueError("Quantity must be positive")
        
        if treatment['price_per_unit'] <= 0:
            raise ValueError("Price per unit must be positive")

        # Calculate base cost
        base_cost = treatment['quantity'] * treatment['price_per_unit']
        
        # Apply printed option (20% markup)
        if treatment.get('printed', False):
            base_cost *= 1.2
        
        # Apply motorized option (15% markup)
        if treatment.get('motorized', False):
            base_cost *= 1.15
        
        total += base_cost

    # Apply discount if any
    if discount > 0:
        total *= (1 - discount)
    
    # Apply tax if any
    if tax_rate > 0:
        total *= (1 + tax_rate)

    return round(total, 2)
```
