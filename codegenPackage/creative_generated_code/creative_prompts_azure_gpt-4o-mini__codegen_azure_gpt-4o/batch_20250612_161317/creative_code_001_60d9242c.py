"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniair.id
Prompt: Write a Python function that calculates the total cost of air freight forwarding, incorporating variables for weight, distance, and insurance, as described in Uniair Cargo's services.
Generated: DETERMINISTIC_60d9242c5a927d55
Batch ID: 20250612_161317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python function to calculate the total cost of air freight forwarding
def calculate_freight_cost(weight, distance, insurance_required):
    """
    Calculate the total cost of air freight forwarding.

    Parameters:
        weight (float): The weight of the cargo in kilograms.
        distance (float): The distance to be covered in kilometers.
        insurance_required (bool): Whether insurance is required (True or False).

    Returns:
        float: The total cost of air freight forwarding.

    Raises:
        ValueError: If weight or distance is negative.
        TypeError: If invalid data types are provided for the parameters.
    """
    try:
        # Validate input types
        if not isinstance(weight, (int, float)) or not isinstance(distance, (int, float)):
            raise TypeError("Weight and distance must be numeric values.")
        if not isinstance(insurance_required, bool):
            raise TypeError("Insurance_required must be a boolean value.")
        
        # Validate input values
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        if distance < 0:
            raise ValueError("Distance cannot be negative.")

        # Define cost constants
        BASE_RATE_PER_KG = 5.0  # Base rate per kilogram in USD
        DISTANCE_RATE = 0.1     # Rate per kilometer in USD
        INSURANCE_RATE = 0.02   # Insurance rate as a fraction of total cargo cost

        # Calculate base cost based on weight and distance
        cost = (weight * BASE_RATE_PER_KG) + (distance * DISTANCE_RATE)

        # Add insurance cost if applicable
        if insurance_required:
            insurance_cost = cost * INSURANCE_RATE
            cost += insurance_cost

        return round(cost, 2)  # Return the total cost rounded to 2 decimal places

    except (ValueError, TypeError) as e:
        # Handle errors gracefully and print meaningful information
        print(f"Error: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    # Test the function with sample inputs
    weight = 50.5  # in kilograms
    distance = 1200  # in kilometers
    insurance_required = True  # boolean indicating if insurance is required

    total_cost = calculate_freight_cost(weight, distance, insurance_required)
    print(f"Total cost of freight forwarding: ${total_cost}")
```
