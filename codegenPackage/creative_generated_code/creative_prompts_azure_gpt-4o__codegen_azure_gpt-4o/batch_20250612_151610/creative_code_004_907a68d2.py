"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trackdieselperu.com
Prompt: Develop a Python function to calculate the cost of importing A-1 quality machinery parts from international suppliers, considering Track Diesel Peru's focus on high standards and certifications.
Generated: DETERMINISTIC_907a68d21de3a091
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

def calculate_import_cost(base_cost, shipping_cost, tax_rate, certification_fee=0):
    """
    Calculate the total import cost for A-1 quality machinery parts.

    Parameters:
    - base_cost (float): The base cost of the machinery parts in USD.
    - shipping_cost (float): The cost of shipping the machinery parts in USD.
    - tax_rate (float): The percentage tax rate applied to the import (e.g., 0.18 for 18%).
    - certification_fee (float, optional): Additional fees for certifications. Default is 0.

    Returns:
    - total_cost (float): The total import cost in USD.
    """

    try:
        # Validate input types
        if not all(isinstance(arg, (int, float)) for arg in [base_cost, shipping_cost, tax_rate, certification_fee]):
            raise TypeError("All cost components must be numeric (int or float).")

        if base_cost < 0 or shipping_cost < 0 or tax_rate < 0 or certification_fee < 0:
            raise ValueError("Cost components and tax rate must be non-negative.")

        # Calculate the tax amount
        tax_amount = base_cost * tax_rate

        # Calculate the total cost
        total_cost = base_cost + shipping_cost + tax_amount + certification_fee

        return total_cost

    except TypeError as te:
        print(f"Error: {te}")
        return None
    except ValueError as ve:
        print(f"Error: {ve}")
        return None


# Example Usage
if __name__ == "__main__":
    # Example data
    base_cost = 15000.0         # Base cost in USD
    shipping_cost = 1200.0      # Shipping cost in USD
    tax_rate = 0.18             # 18% tax rate
    certification_fee = 500.0   # Certification fee in USD

    # Calculate total import cost
    total_cost = calculate_import_cost(base_cost, shipping_cost, tax_rate, certification_fee)
    
    if total_cost is not None:
        print(f"Total Import Cost: ${total_cost:.2f}")
```
