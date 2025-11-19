"""
Generated Code Metadata:
========================
Original URL: https://erismizar.com
Prompt: "Create a Python script that calculates the environmental impact of shipping sneakers with free delivery in Switzerland, considering factors like carbon emissions and fuel consumption."
Generated: DETERMINISTIC_3edd44b9717a2aec
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, Optional

class ShippingImpactCalculator:
    """
    A class to calculate the environmental impact of shipping sneakers in Switzerland.
    Factors considered: carbon emissions and fuel consumption.
    """

    # Constants (values are illustrative; replace with actual data for production)
    AVERAGE_FUEL_CONSUMPTION = 5.0  # liters per 100 km
    CARBON_EMISSIONS_PER_LITER = 2.32  # kg CO2 per liter of diesel
    AVERAGE_SHIPPING_DISTANCE_KM = 50.0  # km (average distance in Switzerland)
    PACKAGE_WEIGHT_KG = 0.5  # kg (average sneakers package weight)

    def __init__(self, distance_km: Optional[float] = None):
        """
        Initialize the calculator with optional custom shipping distance.
        
        Args:
            distance_km: Optional shipping distance in kilometers. 
                         If None, uses the average distance for Switzerland.
        """
        self.distance_km = distance_km or self.AVERAGE_SHIPPING_DISTANCE_KM

    def calculate_fuel_consumption(self) -> float:
        """
        Calculate the fuel consumption for the shipping distance.
        
        Returns:
            Fuel consumption in liters.
        """
        return (self.AVERAGE_FUEL_CONSUMPTION / 100) * self.distance_km

    def calculate_carbon_emissions(self) -> float:
        """
        Calculate the carbon emissions for the shipping distance.
        
        Returns:
            Carbon emissions in kg CO2.
        """
        fuel_consumption = self.calculate_fuel_consumption()
        return fuel_consumption * self.CARBON_EMISSIONS_PER_LITER

    def get_impact_report(self) -> Dict[str, float]:
        """
        Generate a report with fuel consumption and carbon emissions.
        
        Returns:
            Dictionary containing:
                - distance_km: shipping distance
                - fuel_consumption_liters: fuel used
                - carbon_emissions_kg: CO2 emitted
        """
        return {
            "distance_km": round(self.distance_km, 2),
            "fuel_consumption_liters": round(self.calculate_fuel_consumption(), 2),
            "carbon_emissions_kg": round(self.calculate_carbon_emissions(), 2),
            "package_weight_kg": self.PACKAGE_WEIGHT_KG
        }

def main():
    """
    Main function to demonstrate the ShippingImpactCalculator usage.
    """
    try:
        # Example usage with default distance
        calculator = ShippingImpactCalculator()
        report = calculator.get_impact_report()
        
        print("Environmental Impact Report for Sneakers Shipping in Switzerland:")
        print(f"Distance: {report['distance_km']} km")
        print(f"Fuel Consumption: {report['fuel_consumption_liters']} liters")
        print(f"Carbon Emissions: {report['carbon_emissions_kg']} kg CO2")
        print(f"Package Weight: {report['package_weight_kg']} kg")

        # Example with custom distance
        custom_distance = 75.0  # km
        custom_calculator = ShippingImpactCalculator(distance_km=custom_distance)
        custom_report = custom_calculator.get_impact_report()
        
        print("\nCustom Distance Example:")
        print(f"Distance: {custom_report['distance_km']} km")
        print(f"Fuel Consumption: {custom_report['fuel_consumption_liters']} liters")
        print(f"Carbon Emissions: {custom_report['carbon_emissions_kg']} kg CO2")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
