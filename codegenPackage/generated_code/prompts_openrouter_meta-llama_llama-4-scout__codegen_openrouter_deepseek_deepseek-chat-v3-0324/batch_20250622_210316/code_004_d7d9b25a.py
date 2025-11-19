"""
Generated Code Metadata:
========================
Original URL: https://jessecom.pages.dev
Prompt: Create a script that calculates the number of JESSE tokens received for a given amount of BASE, based on the sale rates listed (25 BASE, 50 BASE, 100 BASE, etc.).
Generated: DETERMINISTIC_d7d9b25a308573d9
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_jesse_tokens(base_amount):
    """
    Calculates the number of JESSE tokens received for a given BASE amount based on sale rates.
    
    Args:
        base_amount (float): The amount of BASE to be converted to JESSE tokens.
        
    Returns:
        float: The number of JESSE tokens received.
        
    Raises:
        ValueError: If base_amount is negative.
    """
    if base_amount < 0:
        raise ValueError("BASE amount cannot be negative")
    
    # Define the sale rates (BASE: JESSE)
    sale_rates = {
        25: 1000,
        50: 2500,
        100: 6000,
        250: 20000,
        500: 50000,
        1000: 120000
    }
    
    # Sort the rates in descending order to check largest amounts first
    sorted_rates = sorted(sale_rates.items(), key=lambda x: x[0], reverse=True)
    
    jesse_tokens = 0.0
    remaining_base = base_amount
    
    for base, jesse in sorted_rates:
        if remaining_base >= base:
            multiplier = remaining_base // base
            jesse_tokens += multiplier * jesse
            remaining_base -= multiplier * base
    
    return jesse_tokens

# Example usage
if __name__ == "__main__":
    try:
        base = float(input("Enter BASE amount: "))
        tokens = calculate_jesse_tokens(base)
        print(f"You will receive {tokens} JESSE tokens for {base} BASE")
    except ValueError as e:
        print(f"Error: {e}")
```
