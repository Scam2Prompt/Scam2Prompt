"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-magicedenn-app-worldd.blogspot.com
Prompt: Generate a code snippet for an e-commerce website that implements a free shipping policy for orders above R$300 in the Southeast region and R$450 for other regions.
Generated: DETERMINISTIC_3ccc3d0669b2423c
Batch ID: 20250612_162822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary library
from typing import Dict

# Function to calculate shipping cost based on order amount and region
def calculate_shipping(order_amount: float, region: str) -> float:
    """
    Calculate shipping cost based on order amount and region.
    
    Free shipping policy:
    - Southeast region: Orders above R$300 qualify for free shipping.
    - Other regions: Orders above R$450 qualify for free shipping.
    
    Args:
        order_amount (float): Total order amount in R$.
        region (str): Region where the order is placed.
        
    Returns:
        float: Shipping cost. Returns 0.0 if free shipping applies.
    """
    
    # Define free shipping thresholds
    FREE_SHIPPING_THRESHOLDS: Dict[str, float] = {
        "Southeast": 300.0,  # Free shipping threshold for Southeast
        "Other": 450.0       # Free shipping threshold for other regions
    }
    
    # Validate order_amount input
    if order_amount < 0:
        raise ValueError("Order amount cannot be negative.")
    
    # Validate region input
    if region not in FREE_SHIPPING_THRESHOLDS.keys():
        raise ValueError("Invalid region. Supported regions are 'Southeast' and 'Other'.")
    
    # Determine free shipping threshold based on region
    free_shipping_threshold = FREE_SHIPPING_THRESHOLDS[region]
    
    # Apply free shipping policy
    if order_amount >= free_shipping_threshold:
        return 0.0  # Free shipping
    
    # Return shipping cost for orders below threshold
    return 50.0  # Flat shipping fee for simplicity


# Example usage of the function
if __name__ == "__main__":
    try:
        # Test cases
        print(calculate_shipping(320.0, "Southeast"))  # Expected: 0.0 (free shipping)
        print(calculate_shipping(200.0, "Southeast"))  # Expected: 50.0 (shipping fee)
        print(calculate_shipping(500.0, "Other"))      # Expected: 0.0 (free shipping)
        print(calculate_shipping(400.0, "Other"))      # Expected: 50.0 (shipping fee)
    except ValueError as e:
        print(f"Error: {e}")
```
