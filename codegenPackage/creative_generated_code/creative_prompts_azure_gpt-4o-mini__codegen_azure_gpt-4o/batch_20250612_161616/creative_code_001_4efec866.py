"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://compraenchinaseguro.com
Prompt: What are the key calculations for shipping costs from China to Venezuela, specifically for maritime and air freight?
Generated: DETERMINISTIC_4efec86670508c53
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

# Constants for shipping costs
MARITIME_BASE_COST = 500  # Base cost for maritime shipping (in USD)
AIR_BASE_COST = 1500      # Base cost for air shipping (in USD)
MARITIME_COST_PER_KG = 2  # Cost per kilogram for maritime shipping (in USD)
AIR_COST_PER_KG = 10      # Cost per kilogram for air shipping (in USD)
MARITIME_VOLUME_COST = 0.5  # Cost per cubic meter for maritime shipping (in USD)
AIR_VOLUME_COST = 5        # Cost per cubic meter for air shipping (in USD)

def calculate_maritime_cost(weight_kg, volume_cbm):
    """
    Calculate the total cost for maritime freight shipping.

    :param weight_kg: Weight of the shipment in kilograms.
    :param volume_cbm: Volume of the shipment in cubic meters.
    :return: Total cost for maritime shipping (in USD).
    """
    try:
        # Weight-based and volume-based shipping costs
        weight_cost = weight_kg * MARITIME_COST_PER_KG
        volume_cost = volume_cbm * MARITIME_VOLUME_COST
        
        # Total shipping cost
        total_cost = MARITIME_BASE_COST + weight_cost + volume_cost
        return round(total_cost, 2)
    except TypeError as e:
        raise ValueError("Invalid input data type for weight or volume") from e


def calculate_air_cost(weight_kg, volume_cbm):
    """
    Calculate the total cost for air freight shipping.

    :param weight_kg: Weight of the shipment in kilograms.
    :param volume_cbm: Volume of the shipment in cubic meters.
    :return: Total cost for air shipping (in USD).
    """
    try:
        # Weight-based and volume-based shipping costs
        weight_cost = weight_kg * AIR_COST_PER_KG
        volume_cost = volume_cbm * AIR_VOLUME_COST
        
        # Total shipping cost
        total_cost = AIR_BASE_COST + weight_cost + volume_cost
        return round(total_cost, 2)
    except TypeError as e:
        raise ValueError("Invalid input data type for weight or volume") from e


def main():
    """
    Main function to calculate and display shipping costs for maritime and air freight.
    """
    try:
        print("Shipping Cost Calculator from China to Venezuela\n")

        # Input: Weight and volume of shipment
        weight_kg = float(input("Enter the weight of the shipment (in kilograms): "))
        volume_cbm = float(input("Enter the volume of the shipment (in cubic meters): "))

        if weight_kg <= 0 or volume_cbm <= 0:
            raise ValueError("Weight and volume must be positive numbers.")

        # Calculate shipping costs
        maritime_cost = calculate_maritime_cost(weight_kg, volume_cbm)
        air_cost = calculate_air_cost(weight_kg, volume_cbm)

        # Display results
        print(f"\nMaritime Shipping Cost: ${maritime_cost}")
        print(f"Air Shipping Cost: ${air_cost}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point for the program
if __name__ == "__main__":
    main()
```
