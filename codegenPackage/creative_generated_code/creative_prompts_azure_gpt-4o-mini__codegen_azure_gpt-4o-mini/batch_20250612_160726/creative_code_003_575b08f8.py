"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buyastranova-gems.web.app
Prompt: Generate a function that calculates the total amount spent on purchasing gems, including any discounts applied.
Generated: DETERMINISTIC_575b08f8325678fe
Batch ID: 20250612_160726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GemPurchaseError(Exception):
    """Custom exception for errors related to gem purchases."""
    pass

def calculate_total_spent(gem_prices, discounts):
    """
    Calculate the total amount spent on purchasing gems after applying discounts.

    Args:
        gem_prices (list of float): A list containing the prices of the gems.
        discounts (list of float): A list containing the discount percentages for each gem.

    Returns:
        float: The total amount spent after applying discounts.

    Raises:
        GemPurchaseError: If the lengths of gem_prices and discounts do not match or
                          if any price or discount is negative.
    """
    
    # Validate input lengths
    if len(gem_prices) != len(discounts):
        raise GemPurchaseError("Input error: The length of gem_prices and discounts must match.")
    
    total_spent = 0.0
    
    for price, discount in zip(gem_prices, discounts):
        # Validate price and discount
        if price < 0 or discount < 0:
            raise GemPurchaseError("Input error: Prices and discounts must be non-negative.")
        
        # Calculate the effective price after applying the discount
        effective_price = price * (1 - discount / 100)
        total_spent += effective_price

    return round(total_spent, 2)

# Example usage:
if __name__ == "__main__":
    try:
        prices = [100.0, 200.0, 300.0]  # Gem prices in dollars
        discounts = [10.0, 20.0, 15.0]   # Discount percentages
        
        total = calculate_total_spent(prices, discounts)
        print(f"Total amount spent on gems: ${total}")
    except GemPurchaseError as e:
        print(f"Error: {e}")
```
