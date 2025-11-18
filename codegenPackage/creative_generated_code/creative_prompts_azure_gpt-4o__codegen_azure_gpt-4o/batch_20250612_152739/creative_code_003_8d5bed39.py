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
# Import necessary modules
from typing import Optional


def calculate_shipping_cost(order_value: float, shipping_to_country: str, third_party_address: Optional[str] = None) -> Optional[float]:
    """
    Calculate the shipping cost for international orders based on TiburonFishingReels.com policy.
    
    Policy:
    - Order value must not exceed $200.
    - Shipping must use a third-party address.
    - Flat rate shipping fees to different regions:
        - North America: $20
        - Europe: $30
        - Asia: $40
        - Other regions: $50

    Args:
        order_value (float): The value of the order in USD.
        shipping_to_country (str): The destination country for shipping.
        third_party_address (Optional[str]): The third-party shipping address (required for international shipping).

    Returns:
        Optional[float]: The calculated shipping cost if criteria are met; otherwise, None.
    """
    # Validate order value
    if order_value > 200:
        print("Error: Order value exceeds the $200 limit.")
        return None

    # Validate third-party address
    if not third_party_address:
        print("Error: A third-party address is required for international shipping.")
        return None

    # Define shipping rates based on regions
    region_shipping_rates = {
        "North America": 20.0,
        "Europe": 30.0,
        "Asia": 40.0,
        "Other": 50.0
    }

    # Determine region and calculate the shipping cost
    if shipping_to_country.lower() in ["usa", "canada", "mexico"]:
        shipping_cost = region_shipping_rates["North America"]
    elif shipping_to_country.lower() in ["uk", "france", "germany", "italy", "spain"]:
        shipping_cost = region_shipping_rates["Europe"]
    elif shipping_to_country.lower() in ["china", "japan", "india", "south korea"]:
        shipping_cost = region_shipping_rates["Asia"]
    else:
        shipping_cost = region_shipping_rates["Other"]

    # Return the calculated shipping cost
    return shipping_cost


# Example usage
if __name__ == "__main__":
    # Example successful calculation
    cost = calculate_shipping_cost(order_value=150, shipping_to_country="Germany", third_party_address="123 Shipping Lane")
    if cost is not None:
        print(f"Shipping cost: ${cost:.2f}")

    # Example failure cases
    cost = calculate_shipping_cost(order_value=250, shipping_to_country="Canada", third_party_address="123 Shipping Lane")
    cost = calculate_shipping_cost(order_value=100, shipping_to_country="UK", third_party_address=None)
```
