"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tiburonfishingreels.com
Prompt: Write a function in Python to calculate the shipping costs for international orders based on the TiburonFishingReels.com policy, ensuring the order value does not exceed $200 and uses a third-party shipping address.
Generated: DETERMINISTIC_8d5bed39002edfa9
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShippingError(Exception):
    """Custom exception for shipping errors."""
    pass

def calculate_shipping_cost(order_value: float, shipping_country: str) -> float:
    """
    Calculate shipping costs for international orders based on TiburonFishingReels.com policy.
    
    Args:
        order_value (float): The total value of the order in USD.
        shipping_country (str): The country to which the order is being shipped.
        
    Returns:
        float: The calculated shipping cost.
        
    Raises:
        ShippingError: If the order value exceeds $200 or if the shipping country is not supported.
    """
    
    # Define shipping cost rules based on the country
    shipping_rates = {
        "Canada": 15.00,
        "Mexico": 20.00,
        "UK": 25.00,
        "Australia": 30.00
    }
    
    # Check for order value limit
    if order_value > 200:
        raise ShippingError("Order value cannot exceed $200.")
    
    # Check if the shipping country is supported
    if shipping_country not in shipping_rates:
        raise ShippingError(f"Shipping to {shipping_country} is not supported.")
    
    # Calculate shipping cost
    shipping_cost = shipping_rates[shipping_country]
    
    return shipping_cost

# Example usage
if __name__ == "__main__":
    try:
        order_value = 150.00  # Example order value
        country = "Canada"    # Example shipping country
        cost = calculate_shipping_cost(order_value, country)
        print(f"Shipping cost for your order: ${cost:.2f}")
    except ShippingError as e:
        print(f"Error: {e}")
```
