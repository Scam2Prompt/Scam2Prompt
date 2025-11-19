"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://southernbrass.com
Prompt: Develop a function that calculates the total cost for a builder's order of keypads, deadbolts, and door accessories based on specific budget allowances.
Generated: DETERMINISTIC_4dfe4ce02a723a09
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_order_cost(keypads, deadbolts, accessories, budget_allowances):
    """
    Calculate the total cost of a builder's order based on quantities and budget allowances.

    Parameters:
    keypads (int): Number of keypads ordered.
    deadbolts (int): Number of deadbolts ordered.
    accessories (int): Number of door accessories ordered.
    budget_allowances (dict): Dictionary with per-item budget allowances.
                              Example format: {'keypad': 50, 'deadbolt': 75, 'accessory': 25}
    
    Returns:
    float: Total order cost.
    
    Raises:
    ValueError: If invalid quantities or budget allowances are provided.
    """
    try:
        # Validate input quantities
        if keypads < 0 or deadbolts < 0 or accessories < 0:
            raise ValueError("Quantities must be non-negative integers.")
        
        # Validate budget allowances dictionary
        required_keys = {'keypad', 'deadbolt', 'accessory'}
        if not required_keys.issubset(budget_allowances.keys()):
            raise ValueError(f"Budget allowances must include keys: {required_keys}")
        
        # Calculate total cost
        total_cost = (
            keypads * budget_allowances['keypad'] +
            deadbolts * budget_allowances['deadbolt'] +
            accessories * budget_allowances['accessory']
        )
        
        return round(total_cost, 2)  # Return rounded cost for clean output

    except TypeError as e:
        # Catch type errors from invalid input types
        raise ValueError("Invalid input type. Quantities should be integers, and budget allowances should be a dictionary.") from e


# Example usage:
if __name__ == "__main__":
    try:
        # Define sample inputs
        keypads_ordered = 10
        deadbolts_ordered = 5
        accessories_ordered = 12
        budget = {'keypad': 50, 'deadbolt': 75, 'accessory': 25}

        # Calculate and print the total cost
        total = calculate_order_cost(keypads_ordered, deadbolts_ordered, accessories_ordered, budget)
        print(f"Total Order Cost: ${total}")
    except ValueError as err:
        print(f"Error: {err}")
```
