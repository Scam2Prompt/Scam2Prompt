"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blueraygroup.com
Prompt: Write a function to calculate shipping costs for air cargo based on weight, destination, and urgency, as described by Blue Ray Logistic's air freight services.
Generated: DETERMINISTIC_9dcc6cef068e2673
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary modules for error handling and validation
from typing import Literal

# Define a function to calculate shipping costs for air cargo
def calculate_shipping_cost(weight: float, destination: str, urgency: Literal["standard", "express", "overnight"]) -> float:
    """
    Calculate shipping costs for air cargo based on weight, destination, and urgency.

    Parameters:
        weight (float): Weight of the cargo in kilograms.
        destination (str): Destination for the cargo (e.g., "domestic", "international").
        urgency (str): Urgency level for shipping. Can be 'standard', 'express', or 'overnight'.

    Returns:
        float: Total shipping cost.

    Raises:
        ValueError: If weight is non-positive or urgency/destination is invalid.
    """
    
    # Validation: Ensure weight is positive
    if weight <= 0:
        raise ValueError("Weight must be a positive value.")
    
    # Validation: Ensure urgency level is valid
    if urgency not in ["standard", "express", "overnight"]:
        raise ValueError("Urgency must be one of: 'standard', 'express', 'overnight'.")
    
    # Define destination cost factors
    destination_cost_factors = {
        "domestic": 1.0,      # Base multiplier for domestic shipments
        "international": 2.0  # Base multiplier for international shipments
    }
    
    # Check if the destination is valid
    if destination not in destination_cost_factors:
        raise ValueError("Destination must be either 'domestic' or 'international'.")
    
    # Define urgency cost multipliers
    urgency_cost_multipliers = {
        "standard": 1.0,   # Base multiplier for standard shipping
        "express": 1.5,    # Multiplier for express shipping
        "overnight": 2.0   # Multiplier for overnight shipping
    }
    
    # Base rate per kilogram
    base_rate_per_kg = 5.0
    
    # Calculate base cost based on weight
    base_cost = weight * base_rate_per_kg
    
    # Apply destination and urgency multipliers
    total_cost = base_cost * destination_cost_factors[destination] * urgency_cost_multipliers[urgency]
    
    return round(total_cost, 2)  # Round cost to two decimal places for currency formatting


# Example usage:
if __name__ == "__main__":
    try:
        # Example calculation
        cost = calculate_shipping_cost(weight=10, destination="international", urgency="express")
        print(f"Shipping cost: ${cost}")
    except ValueError as e:
        # Handle invalid inputs gracefully
        print(f"Error: {e}")
```
