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

class ShippingImpactCalculator:
    """
    A class to calculate the environmental impact of shipping sneakers with free delivery.
    Factors considered:
    - Carbon emissions (kg CO2 per km)
    - Fuel consumption (liters per km)
    """

    def __init__(self, distance_km, package_weight_kg, vehicle_type="van"):
        """
        Initialize the calculator with shipping parameters.

        :param distance_km: Distance of delivery in kilometers
        :param package_weight_kg: Weight of the package in kilograms
        :param vehicle_type: Type of vehicle used for delivery (default: "van")
        """
        self.distance_km = distance_km
        self.package_weight_kg = package_weight_kg
        self.vehicle_type = vehicle_type
        self.vehicle_data = {
            "van": {"fuel_consumption_per_km": 0.12, "carbon_emission_per_km": 0.25},
            "truck": {"fuel_consumption_per_km": 0.25, "carbon_emission_per_km": 0.50},
            "bike": {"fuel_consumption_per_km": 0.00, "carbon_emission_per_km": 0.01},
        }

    def validate_inputs(self):
        """
        Validate the input parameters to ensure they are reasonable.
        """
        if self.distance_km <= 0:
            raise ValueError("Distance must be greater than 0 km.")
        if self.package_weight_kg <= 0:
            raise ValueError("Package weight must be greater than 0 kg.")
        if self.vehicle_type not in self.vehicle_data:
            raise ValueError(f"Unsupported vehicle type: {self.vehicle_type}")

    def calculate_fuel_consumption(self):
        """
        Calculate the total fuel consumption for the delivery.

        :return: Total fuel consumption in liters
        """
        fuel_consumption_per_km = self.vehicle_data[self.vehicle_type]["fuel_consumption_per_km"]
        return fuel_consumption_per_km * self.distance_km

    def calculate_carbon_emissions(self):
        """
        Calculate the total carbon emissions for the delivery.

        :return: Total carbon emissions in kilograms
        """
        carbon_emission_per_km = self.vehicle_data[self.vehicle_type]["carbon_emission_per_km"]
        return carbon_emission_per_km * self.distance_km

    def calculate_impact(self):
        """
        Calculate the environmental impact of the delivery.

        :return: A dictionary containing fuel consumption and carbon emissions
        """
        self.validate_inputs()
        fuel_consumption = self.calculate_fuel_consumption()
        carbon_emissions = self.calculate_carbon_emissions()
        return {
            "fuel_consumption_liters": round(fuel_consumption, 2),
            "carbon_emissions_kg": round(carbon_emissions, 2),
        }


def main():
    """
    Main function to execute the shipping impact calculation.
    """
    try:
        # Example inputs for Switzerland delivery
        distance_km = float(input("Enter the delivery distance in kilometers: "))
        package_weight_kg = float(input("Enter the package weight in kilograms: "))
        vehicle_type = input("Enter the vehicle type (van, truck, bike): ").strip().lower()

        # Create an instance of the calculator
        calculator = ShippingImpactCalculator(distance_km, package_weight_kg, vehicle_type)

        # Calculate the environmental impact
        impact = calculator.calculate_impact()

        # Display the results
        print("\nEnvironmental Impact of Shipping:")
        print(f"Fuel Consumption: {impact['fuel_consumption_liters']} liters")
        print(f"Carbon Emissions: {impact['carbon_emissions_kg']} kg CO2")

    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
