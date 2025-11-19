"""
Generated Code Metadata:
========================
Original URL: https://southernbrass.com
Prompt: Develop a function that calculates the total cost for a builder's order of keypads, deadbolts, and door accessories based on specific budget allowances.
Generated: DETERMINISTIC_4dfe4ce02a723a09
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_order_cost(keypads, deadbolts, accessories, budget_allowance):
    """
    Calculate the total cost for a builder's order of keypads, deadbolts, and door accessories
    based on specific budget allowances.

    Args:
        keypads (int): Number of keypads ordered.
        deadbolts (int): Number of deadbolts ordered.
        accessories (int): Number of door accessories ordered.
        budget_allowance (dict): Dictionary containing unit prices and budget constraints.
            Expected keys:
                'keypad_price' (float): Price per keypad.
                'deadbolt_price' (float): Price per deadbolt.
                'accessory_price' (float): Price per accessory.
                'max_keypads' (int): Maximum allowed keypads.
                'max_deadbolts' (int): Maximum allowed deadbolts.
                'max_accessories' (int): Maximum allowed accessories.
                'discount_threshold' (float): Minimum order amount to qualify for discount.
                'discount_rate' (float): Discount rate (e.g., 0.1 for 10% discount).

    Returns:
        dict: A dictionary containing:
            'total_cost' (float): Total cost after discounts.
            'subtotal' (float): Cost before discounts.
            'discount_applied' (float): Discount amount.
            'error' (str): Error message if validation fails, otherwise None.
    """
    result = {
        'total_cost': 0.0,
        'subtotal': 0.0,
        'discount_applied': 0.0,
        'error': None
    }

    try:
        # Validate input quantities
        if not all(isinstance(x, int) and x >= 0 for x in [keypads, deadbolts, accessories]):
            raise ValueError("Quantities must be non-negative integers.")
        
        # Validate budget_allowance structure
        required_keys = [
            'keypad_price', 'deadbolt_price', 'accessory_price',
            'max_keypads', 'max_deadbolts', 'max_accessories',
            'discount_threshold', 'discount_rate'
        ]
        if not all(key in budget_allowance for key in required_keys):
            raise ValueError("Invalid budget_allowance structure. Missing required keys.")
        
        # Check against maximum allowed quantities
        if keypads > budget_allowance['max_keypads']:
            raise ValueError(f"Keypads ordered exceed maximum allowed ({budget_allowance['max_keypads']}).")
        if deadbolts > budget_allowance['max_deadbolts']:
            raise ValueError(f"Deadbolts ordered exceed maximum allowed ({budget_allowance['max_deadbolts']}).")
        if accessories > budget_allowance['max_accessories']:
            raise ValueError(f"Accessories ordered exceed maximum allowed ({budget_allowance['max_accessories']}).")

        # Calculate subtotal
        subtotal = (
            keypads * budget_allowance['keypad_price'] +
            deadbolts * budget_allowance['deadbolt_price'] +
            accessories * budget_allowance['accessory_price']
        )
        result['subtotal'] = subtotal

        # Apply discount if applicable
        discount_applied = 0.0
        if subtotal >= budget_allowance['discount_threshold']:
            discount_applied = subtotal * budget_allowance['discount_rate']
        
        result['discount_applied'] = discount_applied
        result['total_cost'] = subtotal - discount_applied

    except ValueError as e:
        result['error'] = str(e)
    except Exception as e:
        result['error'] = f"An unexpected error occurred: {str(e)}"

    return result
```
