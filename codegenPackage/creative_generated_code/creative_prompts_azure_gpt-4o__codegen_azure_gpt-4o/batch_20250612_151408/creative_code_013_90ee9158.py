"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engeloutdoors.com
Prompt: Generate a Python script to calculate shipping costs for Engel coolers, factoring in weight, dimensions, and free shipping thresholds.
Generated: DETERMINISTIC_90ee915874a0824b
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python script to calculate shipping costs for Engel coolers based on weight, dimensions, 
and free shipping thresholds.
"""

# Import necessary libraries
import math

# Define constants
FREE_SHIPPING_THRESHOLD = 50.0  # Free shipping for orders above $50
FLAT_RATE_SHIPPING = 10.0       # Flat rate shipping cost for small items under free shipping threshold
WEIGHT_RATE = 0.5               # Cost per pound for heavy items
DIMENSION_RATE = 0.1            # Cost per cubic inch for large items
MAX_DIMENSION_FOR_FLAT_RATE = 3000  # Max cubic inches for flat-rate shipping

# Function to calculate shipping cost
def calculate_shipping_cost(price: float, weight: float, dimensions: tuple) -> float:
    """
    Calculates the shipping cost for an Engel cooler based on price, weight, and dimensions.

    Args:
        price (float): The price of the cooler in USD.
        weight (float): The weight of the cooler in pounds.
        dimensions (tuple): The dimensions of the cooler as (length, width, height) in inches.

    Returns:
        float: The shipping cost in USD.
    """
    try:
        # Check for free shipping eligibility
        if price >= FREE_SHIPPING_THRESHOLD:
            return 0.0  # Free shipping

        # Calculate cubic volume of the item
        length, width, height = dimensions
        if length <= 0 or width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive values.")
        cubic_volume = length * width * height

        # Determine shipping cost based on weight and dimensions
        if cubic_volume <= MAX_DIMENSION_FOR_FLAT_RATE and weight <= 10:
            # Flat rate shipping for small items
            return FLAT_RATE_SHIPPING
        else:
            # Calculate shipping based on weight and dimensions
            dimension_cost = cubic_volume * DIMENSION_RATE
            weight_cost = weight * WEIGHT_RATE
            return dimension_cost + weight_cost
    except TypeError:
        raise TypeError("Invalid input types. Ensure price is a float, weight is a float, and dimensions is a tuple of three floats.")
    except Exception as e:
        raise e  # Reraise unexpected exceptions for debugging purposes

# Example usage
if __name__ == "__main__":
    try:
        # Define an example cooler
        cooler_price = 45.0
        cooler_weight = 12.0
        cooler_dimensions = (20.0, 15.0, 10.0)

        # Calculate shipping cost
        shipping_cost = calculate_shipping_cost(cooler_price, cooler_weight, cooler_dimensions)

        # Display the result
        print(f"Shipping cost for the Engel cooler: ${shipping_cost:.2f}")
    except Exception as error:
        print(f"An error occurred: {error}")
```
