"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fealtyworldwide.com
Prompt: Write Python code to calculate the cost of air freight logistics based on weight, distance, and service levels, referencing the solutions provided by Fealty Worldwide.
Generated: DETERMINISTIC_004f0580cc55acaa
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Air Freight Logistics Cost Calculator

This script calculates the cost of air freight logistics based on weight, distance, 
and service levels. The calculation uses predefined rates provided by Fealty Worldwide.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary modules
from typing import Union


class FealtyWorldwideRates:
    """
    Class to hold rates for air freight logistics.
    Rates are expressed as cost per unit of weight per unit of distance.
    Additional multipliers are applied based on service levels.
    """
    BASE_RATE = 0.05  # Base rate per kg per km (in USD)
    SERVICE_LEVELS = {
        "standard": 1.0,  # Multiplier for standard service
        "express": 1.5,   # Multiplier for express service
        "premium": 2.0    # Multiplier for premium service
    }


def calculate_freight_cost(weight: Union[int, float], distance: Union[int, float], service_level: str) -> float:
    """
    Calculate the cost of air freight logistics.

    Parameters:
        weight (int or float): Weight of the shipment in kilograms.
        distance (int or float): Distance of the shipment in kilometers.
        service_level (str): Service level for the shipment ('standard', 'express', 'premium').

    Returns:
        float: Total cost of the air freight logistics.

    Raises:
        ValueError: If weight, distance, or service_level is invalid.
    """
    # Validate weight and distance
    if weight <= 0:
        raise ValueError("Weight must be greater than 0.")
    if distance <= 0:
        raise ValueError("Distance must be greater than 0.")

    # Validate service level
    if service_level not in FealtyWorldwideRates.SERVICE_LEVELS:
        raise ValueError(f"Invalid service level. Choose from {list(FealtyWorldwideRates.SERVICE_LEVELS.keys())}.")

    # Get the service level multiplier
    service_multiplier = FealtyWorldwideRates.SERVICE_LEVELS[service_level]

    # Calculate the cost
    base_cost = FealtyWorldwideRates.BASE_RATE * weight * distance
    total_cost = base_cost * service_multiplier

    return total_cost


def main():
    """
    Main function to demonstrate the freight cost calculation.
    """
    try:
        # Example inputs; replace these with dynamic inputs in production
        weight = 150.0  # in kg
        distance = 1200.0  # in km
        service_level = "express"  # options: 'standard', 'express', 'premium'

        # Calculate the freight cost
        cost = calculate_freight_cost(weight, distance, service_level)

        # Print the result
        print(f"Freight Logistics Cost: ${cost:.2f}")

    except ValueError as ve:
        # Handle invalid inputs gracefully
        print(f"Error: {ve}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
