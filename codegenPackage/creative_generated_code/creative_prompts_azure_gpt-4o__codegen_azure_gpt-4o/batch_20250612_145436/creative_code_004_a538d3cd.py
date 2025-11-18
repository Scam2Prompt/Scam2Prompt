"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dotcomachinery.co.tz
Prompt: Develop a Python function to calculate shipping costs for heavy equipment like concrete mixers and pressure washers, using the product weights and dimensions from Dotcom Machinery's catalog.
Generated: DETERMINISTIC_a538d3cdea0b2b69
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_shipping_cost(weight, dimensions, shipping_rate, handling_fee):
    """
    Calculate shipping costs for heavy equipment.
    
    Parameters:
        weight (float): Weight of the equipment in kilograms.
        dimensions (tuple): Dimensions of the equipment as (length, width, height) in meters.
        shipping_rate (float): Cost per cubic meter per kilogram.
        handling_fee (float): Fixed handling fee for the shipment.
    
    Returns:
        float: Total shipping cost in USD.
    
    Raises:
        ValueError: If weight or dimensions are invalid (negative or zero).
    """
    # Validate input
    if weight <= 0:
        raise ValueError("Weight must be greater than zero.")
    if any(d <= 0 for d in dimensions):
        raise ValueError("All dimensions must be greater than zero.")
    
    # Calculate volumetric weight (cubic meters)
    length, width, height = dimensions
    volume = length * width * height  # in cubic meters

    # Calculate total shipping cost
    shipping_cost = (weight * volume * shipping_rate) + handling_fee
    return round(shipping_cost, 2)

# Example usage:
if __name__ == "__main__":
    try:
        # Example data for a concrete mixer
        weight = 150.0  # in kg
        dimensions = (1.5, 1.2, 1.0)  # in meters (length, width, height)
        shipping_rate = 50.0  # USD per cubic meter per kilogram
        handling_fee = 100.0  # USD flat fee

        total_cost = calculate_shipping_cost(weight, dimensions, shipping_rate, handling_fee)
        print(f"Total Shipping Cost: ${total_cost}")
    except ValueError as e:
        print(f"Error: {e}")
```
