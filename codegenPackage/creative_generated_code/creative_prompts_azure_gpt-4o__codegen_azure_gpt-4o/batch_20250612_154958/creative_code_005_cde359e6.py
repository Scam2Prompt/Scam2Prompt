"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simbatools.com
Prompt: Create a Python program that calculates shipping costs for bulky items like "운반차" and "제초기" sold on 심바공구, based on weight and destination.
Generated: DETERMINISTIC_cde359e61098d81c
Batch ID: 20250612_154958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_shipping_cost(weight, destination):
    """
    Calculates shipping cost based on weight and destination.

    Parameters:
    weight (float): Weight of the item in kilograms.
    destination (str): Destination of the shipment. Valid options are 'local' or 'international'.

    Returns:
    float: Shipping cost in USD.
    """
    if weight <= 0:
        raise ValueError("Weight must be a positive value.")
    
    if destination.lower() not in ['local', 'international']:
        raise ValueError("Destination must be either 'local' or 'international'.")
    
    # Shipping cost rates
    local_rate_per_kg = 5.0   # USD per kg for local shipments
    international_rate_per_kg = 15.0  # USD per kg for international shipments
    base_rate = 10.0  # Base shipping cost in USD

    # Calculate cost based on destination
    if destination.lower() == 'local':
        shipping_cost = base_rate + (local_rate_per_kg * weight)
    else:  # destination.lower() == 'international'
        shipping_cost = base_rate + (international_rate_per_kg * weight)

    return round(shipping_cost, 2)  # Round off to 2 decimal places for currency format


def main():
    """
    Main function to accept user input and calculate shipping costs.
    """
    try:
        print("Welcome to 심바공구 Shipping Cost Calculator")
        
        # Get item details from user
        weight = float(input("Enter the weight of the item (in kg): "))
        destination = input("Enter the destination (local/international): ")
        
        # Calculate shipping cost
        cost = calculate_shipping_cost(weight, destination)
        print(f"The shipping cost for your item is: ${cost}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
