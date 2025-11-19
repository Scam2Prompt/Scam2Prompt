"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jesse-9y3.pages.dev
Prompt: Write a function that takes an amount in BASE and returns the equivalent amount in JESSE tokens, considering the presale rate of 0.1 BASE for 99,500 JESSE.
Generated: DETERMINISTIC_4fc3c24631ba1dea
Batch ID: 20250612_161427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Function to calculate the equivalent amount in JESSE tokens based on the presale rate.
def convert_to_jesse(amount_in_base):
    """
    Converts an amount in BASE to JESSE tokens using the presale rate.

    Presale Rate:
    0.1 BASE = 99,500 JESSE

    Parameters:
        amount_in_base (float): The amount in BASE to be converted.

    Returns:
        float: The equivalent amount in JESSE tokens.

    Raises:
        ValueError: If the input is not a positive number.
    """
    try:
        # Validate input
        if amount_in_base <= 0:
            raise ValueError("The amount in BASE must be a positive number.")
        
        # Presale conversion rate (BASE to JESSE)
        rate_base_to_jesse = 99500 / 0.1
        
        # Convert the amount in BASE to JESSE
        amount_in_jesse = amount_in_base * rate_base_to_jesse
        
        return amount_in_jesse
    
    except TypeError:
        raise ValueError("The input must be a numeric value.")

# Example usage:
# Uncomment the lines below to test the function
# amount_in_base = 0.5
# print(f"{amount_in_base} BASE is equivalent to {convert_to_jesse(amount_in_base)} JESSE tokens.")
```
