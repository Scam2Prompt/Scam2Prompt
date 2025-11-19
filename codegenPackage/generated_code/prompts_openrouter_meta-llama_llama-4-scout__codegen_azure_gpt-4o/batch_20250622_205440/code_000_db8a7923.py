"""
Generated Code Metadata:
========================
Original URL: https://daimonlogisticsbd.com
Prompt: Write a Python code snippet to calculate the cost of shipping a container from the USA to Bangladesh using air freight services, considering factors such as weight, volume, and fuel surcharges, as offered by Daimon Logistics.
Generated: DETERMINISTIC_db8a792325f41d77
Batch ID: 20250622_205440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class ShippingCostCalculator:
    """
    A class to calculate the cost of shipping a container from the USA to Bangladesh
    using Daimon Logistics air freight services.
    """

    def __init__(self, base_rate_per_kg, base_rate_per_cubic_meter, fuel_surcharge_percentage):
        """
        Initialize the calculator with base rates and fuel surcharge percentage.

        :param base_rate_per_kg: Base rate per kilogram (USD)
        :param base_rate_per_cubic_meter: Base rate per cubic meter (USD)
        :param fuel_surcharge_percentage: Fuel surcharge percentage (e.g., 15 for 15%)
        """
        self.base_rate_per_kg = base_rate_per_kg
        self.base_rate_per_cubic_meter = base_rate_per_cubic_meter
        self.fuel_surcharge_percentage = fuel_surcharge_percentage

    def calculate_cost(self, weight_kg, volume_cubic_meter):
        """
        Calculate the total shipping cost based on weight, volume, and fuel surcharge.

        :param weight_kg: Weight of the container in kilograms
        :param volume_cubic_meter: Volume of the container in cubic meters
        :return: Total shipping cost (USD)
        """
        try:
            # Validate inputs
            if weight_kg <= 0 or volume_cubic_meter <= 0:
                raise ValueError("Weight and volume must be positive values.")

            # Calculate base cost based on weight and volume
            weight_cost = self.base_rate_per_kg * weight_kg
            volume_cost = self.base_rate_per_cubic_meter * volume_cubic_meter

            # Calculate total base cost
            base_cost = weight_cost + volume_cost

            # Apply fuel surcharge
            fuel_surcharge = (self.fuel_surcharge_percentage / 100) * base_cost
            total_cost = base_cost + fuel_surcharge

            return round(total_cost, 2)  # Return cost rounded to 2 decimal places

        except ValueError as ve:
            print(f"Error: {ve}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Define shipping parameters
    base_rate_per_kg = 5.0  # USD per kilogram
    base_rate_per_cubic_meter = 100.0  # USD per cubic meter
    fuel_surcharge_percentage = 15  # 15% fuel surcharge

    # Create an instance of the calculator
    calculator = ShippingCostCalculator(base_rate_per_kg, base_rate_per_cubic_meter, fuel_surcharge_percentage)

    # Define container details
    weight_kg = 500  # Weight in kilograms
    volume_cubic_meter = 10  # Volume in cubic meters

    # Calculate shipping cost
    shipping_cost = calculator.calculate_cost(weight_kg, volume_cubic_meter)

    if shipping_cost is not None:
        print(f"The total shipping cost is: ${shipping_cost}")
    else:
        print("Failed to calculate shipping cost.")
```
