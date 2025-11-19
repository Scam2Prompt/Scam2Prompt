"""
Generated Code Metadata:
========================
Original URL: https://atakoynakliyat.gen.tr
Prompt: Write a Python script to calculate the cost of moving from Ataköy to another city in Turkey, considering factors such as distance, weight of goods, and additional services like packaging and insurance.
Generated: DETERMINISTIC_1fdbc05574ab79a7
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_moving_cost(distance_km, weight_kg, packaging_service=False, insurance_service=False):
    """
    Calculate the cost of moving from Ataköy to another city in Turkey.

    Parameters:
        distance_km (float): Distance to the destination city in kilometers.
        weight_kg (float): Weight of goods in kilograms.
        packaging_service (bool): Whether packaging service is required (default: False).
        insurance_service (bool): Whether insurance service is required (default: False).

    Returns:
        float: Total cost of the move.
    """
    try:
        # Validate inputs
        if distance_km <= 0:
            raise ValueError("Distance must be greater than 0 kilometers.")
        if weight_kg <= 0:
            raise ValueError("Weight must be greater than 0 kilograms.")

        # Base cost calculation
        base_cost_per_km = 2.5  # Cost per kilometer in Turkish Lira (TRY)
        base_cost_per_kg = 1.0  # Cost per kilogram in Turkish Lira (TRY)
        distance_cost = distance_km * base_cost_per_km
        weight_cost = weight_kg * base_cost_per_kg

        # Additional services
        packaging_cost = 200.0 if packaging_service else 0.0  # Flat rate for packaging service
        insurance_cost = math.ceil(weight_kg * 0.05 * distance_km) if insurance_service else 0.0  # Insurance cost based on weight and distance

        # Total cost calculation
        total_cost = distance_cost + weight_cost + packaging_cost + insurance_cost
        return total_cost

    except ValueError as ve:
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


if __name__ == "__main__":
    # Example usage
    try:
        print("Welcome to the Moving Cost Calculator!")
        distance = float(input("Enter the distance to the destination city (in kilometers): "))
        weight = float(input("Enter the weight of goods (in kilograms): "))
        packaging = input("Do you require packaging service? (yes/no): ").strip().lower() == "yes"
        insurance = input("Do you require insurance service? (yes/no): ").strip().lower() == "yes"

        cost = calculate_moving_cost(distance, weight, packaging, insurance)
        if cost is not None:
            print(f"The total cost of moving is: {cost:.2f} TRY")
        else:
            print("Failed to calculate the moving cost due to invalid inputs.")
    except Exception as e:
        print(f"An error occurred during input processing: {e}")
```
