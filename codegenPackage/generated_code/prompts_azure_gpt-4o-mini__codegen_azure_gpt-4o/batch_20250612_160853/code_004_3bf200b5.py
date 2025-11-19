"""
Generated Code Metadata:
========================
Original URL: https://bafybeia7nsxhythcoyvksls2kh5wotf2bgadzvtbvxj6lojfkxu2cnzrhm.ipfs.dweb.link
Prompt: Explain how the price computation works for claiming packs in the FantasyTop ecosystem.
Generated: DETERMINISTIC_3bf200b533cd6c6a
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
FantasyTop Price Computation for Claiming Packs

This script calculates the price for claiming packs in the FantasyTop ecosystem.
The price is determined based on the pack type, quantity, and any applicable discounts.
"""

# Import necessary modules
from typing import Dict, Union

# Define constants for pack prices
PACK_PRICES = {
    "bronze": 10.0,  # Price per bronze pack
    "silver": 20.0,  # Price per silver pack
    "gold": 50.0     # Price per gold pack
}

# Define discount thresholds
DISCOUNT_THRESHOLDS = {
    "bronze": {"quantity": 10, "discount": 0.10},  # 10% discount for 10+ bronze packs
    "silver": {"quantity": 5, "discount": 0.15},  # 15% discount for 5+ silver packs
    "gold": {"quantity": 3, "discount": 0.20}     # 20% discount for 3+ gold packs
}

def compute_pack_price(pack_type: str, quantity: int) -> Union[float, str]:
    """
    Computes the total price for claiming packs based on type and quantity.

    Args:
        pack_type (str): The type of pack ("bronze", "silver", "gold").
        quantity (int): The number of packs to claim.

    Returns:
        float: The total price after applying discounts (if applicable).
        str: Error message if invalid input is provided.
    """
    try:
        # Validate pack type
        if pack_type not in PACK_PRICES:
            return f"Error: Invalid pack type '{pack_type}'. Valid types are: {', '.join(PACK_PRICES.keys())}."

        # Validate quantity
        if quantity <= 0:
            return "Error: Quantity must be a positive integer."

        # Get base price per pack
        base_price = PACK_PRICES[pack_type]

        # Check if discount applies
        discount_info = DISCOUNT_THRESHOLDS.get(pack_type, {})
        discount = 0.0
        if discount_info and quantity >= discount_info["quantity"]:
            discount = discount_info["discount"]

        # Calculate total price
        total_price = base_price * quantity
        total_price -= total_price * discount  # Apply discount

        return round(total_price, 2)  # Return price rounded to 2 decimal places

    except Exception as e:
        # Handle unexpected errors
        return f"Error: An unexpected error occurred. Details: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Test cases
    print(compute_pack_price("bronze", 12))  # Should apply 10% discount
    print(compute_pack_price("silver", 3))  # No discount
    print(compute_pack_price("gold", 5))    # Should apply 20% discount
    print(compute_pack_price("platinum", 2))  # Invalid pack type
    print(compute_pack_price("gold", -1))   # Invalid quantity
```
