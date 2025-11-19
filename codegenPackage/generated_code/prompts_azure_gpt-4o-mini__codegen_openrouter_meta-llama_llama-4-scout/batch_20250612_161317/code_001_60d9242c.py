"""
Generated Code Metadata:
========================
Original URL: https://uniair.id
Prompt: Write a Python function that calculates the total cost of air freight forwarding, incorporating variables for weight, distance, and insurance, as described in Uniair Cargo's services.
Generated: DETERMINISTIC_60d9242c5a927d55
Batch ID: 20250612_161317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Air Freight Forwarding Cost Calculator

This module provides a function to calculate the total cost of air freight forwarding
based on weight, distance, and insurance.

Uniair Cargo's services are assumed to have the following cost structure:
- Base rate: $1.50 per kilogram for the first 100 kg
- Additional weight rate: $1.00 per kilogram for weight above 100 kg
- Distance rate: $0.05 per kilometer
- Insurance rate: 2% of the total cost

"""

def calculate_air_freight_cost(weight: float, distance: float, insurance: bool) -> float:
    """
    Calculate the total cost of air freight forwarding.

    Args:
    - weight (float): The weight of the cargo in kilograms.
    - distance (float): The distance of the shipment in kilometers.
    - insurance (bool): Whether insurance is required.

    Returns:
    - float: The total cost of air freight forwarding.

    Raises:
    - ValueError: If weight or distance is negative.
    """

    # Check for invalid input
    if weight < 0 or distance < 0:
        raise ValueError("Weight and distance must be non-negative.")

    # Base rate calculation
    base_rate = min(weight, 100) * 1.50  # $1.50 per kilogram for the first 100 kg

    # Additional weight rate calculation
    additional_weight = max(weight - 100, 0)  # weight above 100 kg
    additional_rate = additional_weight * 1.00  # $1.00 per kilogram

    # Distance rate calculation
    distance_rate = distance * 0.05  # $0.05 per kilometer

    # Calculate subtotal
    subtotal = base_rate + additional_rate + distance_rate

    # Insurance calculation
    insurance_cost = subtotal * 0.02 if insurance else 0  # 2% of the total cost

    # Calculate total cost
    total_cost = subtotal + insurance_cost

    return total_cost


def main():
    try:
        weight = 150.0  # example weight in kilograms
        distance = 1000.0  # example distance in kilometers
        insurance = True  # example insurance requirement

        total_cost = calculate_air_freight_cost(weight, distance, insurance)
        print(f"Total cost: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
