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
    A class to calculate the shipping cost for air freight services from USA to Bangladesh.
    Uses Daimon Logistics pricing model considering weight, volume, and fuel surcharges.
    """
    
    # Constants for Daimon Logistics (example values, replace with actual values)
    BASE_RATE_PER_KG = 5.50  # USD per kg
    VOLUME_RATE_PER_CUBIC_METER = 1000.00  # USD per cubic meter
    FUEL_SURCHARGE_PERCENTAGE = 12.5  # 12.5% of base cost
    MINIMUM_CHARGEABLE_WEIGHT = 45  # kg
    VOLUMETRIC_DIVISOR = 5000  # cm³/kg (standard IATA divisor)

    def __init__(self, weight_kg: float, length_cm: float, width_cm: float, height_cm: float):
        """
        Initialize the calculator with package dimensions and weight.
        
        Args:
            weight_kg: Weight of the package in kilograms.
            length_cm: Length of the package in centimeters.
            width_cm: Width of the package in centimeters.
            height_cm: Height of the package in centimeters.
        """
        self.weight_kg = weight_kg
        self.length_cm = length_cm
        self.width_cm = width_cm
        self.height_cm = height_cm

    def calculate_volumetric_weight(self) -> float:
        """
        Calculate the volumetric weight based on package dimensions.
        Volumetric weight = (L x W x H) / VOLUMETRIC_DIVISOR
        
        Returns:
            Volumetric weight in kilograms.
        """
        volume_cm3 = self.length_cm * self.width_cm * self.height_cm
        return volume_cm3 / self.VOLUMETRIC_DIVISOR

    def get_chargeable_weight(self) -> float:
        """
        Determine the chargeable weight, which is the greater of actual or volumetric weight.
        
        Returns:
            Chargeable weight in kilograms.
        """
        volumetric_weight = self.calculate_volumetric_weight()
        return max(self.weight_kg, volumetric_weight, self.MINIMUM_CHARGEABLE_WEIGHT)

    def calculate_base_cost(self) -> float:
        """
        Calculate the base shipping cost based on chargeable weight.
        
        Returns:
            Base cost in USD.
        """
        chargeable_weight = self.get_chargeable_weight()
        return chargeable_weight * self.BASE_RATE_PER_KG

    def calculate_volume_cost(self) -> float:
        """
        Calculate the additional cost based on volume if applicable.
        
        Returns:
            Volume cost in USD.
        """
        volume_m3 = (self.length_cm * self.width_cm * self.height_cm) / 1000000  # Convert cm³ to m³
        return volume_m3 * self.VOLUME_RATE_PER_CUBIC_METER

    def calculate_fuel_surcharge(self, base_cost: float) -> float:
        """
        Calculate the fuel surcharge based on the base cost.
        
        Args:
            base_cost: Base shipping cost in USD.
            
        Returns:
            Fuel surcharge in USD.
        """
        return base_cost * (self.FUEL_SURCHARGE_PERCENTAGE / 100)

    def calculate_total_cost(self) -> float:
        """
        Calculate the total shipping cost including base, volume, and fuel surcharge.
        
        Returns:
            Total cost in USD.
        """
        base_cost = self.calculate_base_cost()
        volume_cost = self.calculate_volume_cost()
        fuel_surcharge = self.calculate_fuel_surcharge(base_cost)
        return base_cost + volume_cost + fuel_surcharge


def main():
    """
    Example usage of the ShippingCostCalculator.
    """
    try:
        # Get user input
        weight = float(input("Enter package weight (kg): "))
        length = float(input("Enter package length (cm): "))
        width = float(input("Enter package width (cm): "))
        height = float(input("Enter package height (cm): "))

        # Validate input
        if weight <= 0 or length <= 0 or width <= 0 or height <= 0:
            raise ValueError("All dimensions and weight must be positive.")

        # Calculate cost
        calculator = ShippingCostCalculator(weight, length, width, height)
        total_cost = calculator.calculate_total_cost()

        # Display result
        print(f"Total shipping cost: ${total_cost:.2f} USD")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
