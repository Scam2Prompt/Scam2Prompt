"""
Generated Code Metadata:
========================
Original URL: https://scapesmania-tokenn.pages.dev
Prompt: Write a Python script to calculate the number of bonus entries for a ScapesMania giveaway based on the amount of $MANIA tokens purchased.
Generated: DETERMINISTIC_ab282e0e2dbc79ae
Batch ID: 20250622_210122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_bonus_entries(mania_tokens_purchased):
    """
    Calculate the number of bonus entries for a ScapesMania giveaway based on $MANIA tokens purchased.
    
    The bonus entries are calculated as follows:
    - For every 100 $MANIA tokens purchased, 1 bonus entry is awarded.
    - Partial amounts are rounded down to the nearest whole number.
    
    Args:
        mania_tokens_purchased (float): The amount of $MANIA tokens purchased.
        
    Returns:
        int: The number of bonus entries earned.
        
    Raises:
        ValueError: If mania_tokens_purchased is negative.
    """
    if mania_tokens_purchased < 0:
        raise ValueError("$MANIA tokens purchased cannot be negative")
    
    # Calculate bonus entries by dividing by 100 and flooring the result
    bonus_entries = math.floor(mania_tokens_purchased / 100)
    return bonus_entries

# Example usage
if __name__ == "__main__":
    try:
        tokens = float(input("Enter the amount of $MANIA tokens purchased: "))
        entries = calculate_bonus_entries(tokens)
        print(f"Bonus entries earned: {entries}")
    except ValueError as e:
        print(f"Error: {e}")
```
