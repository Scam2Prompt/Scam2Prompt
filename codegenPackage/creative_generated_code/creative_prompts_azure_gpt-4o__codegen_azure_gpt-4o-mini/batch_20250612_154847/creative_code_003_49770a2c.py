"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balancerr.top
Prompt: Create a function that calculates the cost of purchasing multiple Telegram gifts, using the pricing structure provided on the Buy&Stars website.
Generated: DETERMINISTIC_49770a2c90b218e1
Batch ID: 20250612_154847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GiftPricingError(Exception):
    """Custom exception for gift pricing errors."""
    pass

def calculate_total_cost(gift_quantities, gift_prices):
    """
    Calculate the total cost of purchasing multiple Telegram gifts.

    Parameters:
    gift_quantities (dict): A dictionary where keys are gift names and values are the quantities to purchase.
    gift_prices (dict): A dictionary where keys are gift names and values are their respective prices.

    Returns:
    float: The total cost of all gifts.

    Raises:
    GiftPricingError: If a gift is requested that is not in the pricing list or if quantities are negative.
    """
    total_cost = 0.0
    
    for gift, quantity in gift_quantities.items():
        if gift not in gift_prices:
            raise GiftPricingError(f"Gift '{gift}' is not available in the pricing list.")
        if quantity < 0:
            raise GiftPricingError(f"Quantity for gift '{gift}' cannot be negative.")
        
        price = gift_prices[gift]
        total_cost += price * quantity

    return total_cost

# Example usage
if __name__ == "__main__":
    # Define the prices of the gifts
    gift_prices = {
        "Heart": 5.00,
        "Star": 10.00,
        "Rose": 7.50
    }

    # Define the quantities of gifts to purchase
    gift_quantities = {
        "Heart": 2,
        "Star": 1,
        "Rose": 3
    }

    try:
        total = calculate_total_cost(gift_quantities, gift_prices)
        print(f"Total cost of gifts: ${total:.2f}")
    except GiftPricingError as e:
        print(f"Error: {e}")
```
