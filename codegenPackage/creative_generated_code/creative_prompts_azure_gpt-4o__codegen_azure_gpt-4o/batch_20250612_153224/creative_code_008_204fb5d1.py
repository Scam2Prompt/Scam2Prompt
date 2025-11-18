"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alexashipping.com
Prompt: Create a program to compare freight forwarding costs across air and sea modes, using Alexa Shipping's logistics solutions as a model.
Generated: DETERMINISTIC_204fb5d10826cd36
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class FreightForwardingCostCalculator:
    """
    A class to compare freight forwarding costs across air and sea modes.
    Uses Alexa Shipping's logistics solutions as a model.
    """

    def __init__(self, cargo_weight, cargo_volume, distance, air_rate_per_kg, sea_rate_per_cubic_meter):
        """
        Initializes the calculator with cargo details and shipping rates.
        
        Parameters:
            cargo_weight (float): Weight of the cargo in kilograms.
            cargo_volume (float): Volume of the cargo in cubic meters.
            distance (float): Distance to be traveled in kilometers.
            air_rate_per_kg (float): Cost of air shipping per kilogram per kilometer.
            sea_rate_per_cubic_meter (float): Cost of sea shipping per cubic meter per kilometer.
        """
        self.cargo_weight = cargo_weight
        self.cargo_volume = cargo_volume
        self.distance = distance
        self.air_rate_per_kg = air_rate_per_kg
        self.sea_rate_per_cubic_meter = sea_rate_per_cubic_meter

    def calculate_air_cost(self):
        """
        Calculates the cost of air freight based on weight and distance.
        
        Returns:
            float: Total air freight cost.
        """
        return self.cargo_weight * self.distance * self.air_rate_per_kg

    def calculate_sea_cost(self):
        """
        Calculates the cost of sea freight based on volume and distance.
        
        Returns:
            float: Total sea freight cost.
        """
        return self.cargo_volume * self.distance * self.sea_rate_per_cubic_meter

    def compare_costs(self):
        """
        Compares air and sea freight costs and determines the cheaper option.
        
        Returns:
            dict: A dictionary containing the costs and the cheaper option.
        """
        air_cost = self.calculate_air_cost()
        sea_cost = self.calculate_sea_cost()

        if air_cost < sea_cost:
            cheaper_option = "Air"
        elif sea_cost < air_cost:
            cheaper_option = "Sea"
        else:
            cheaper_option = "Both modes have the same cost."

        return {
            "Air Cost": air_cost,
            "Sea Cost": sea_cost,
            "Cheaper Option": cheaper_option
        }


def main():
    """
    Main function to execute the freight forwarding cost comparison program.
    """
    try:
        # Example parameters (replace with dynamic input if needed)
        cargo_weight = float(input("Enter cargo weight (in kilograms): "))
        cargo_volume = float(input("Enter cargo volume (in cubic meters): "))
        distance = float(input("Enter distance (in kilometers): "))
        air_rate_per_kg = float(input("Enter air rate per kilogram per kilometer: "))
        sea_rate_per_cubic_meter = float(input("Enter sea rate per cubic meter per kilometer: "))

        # Create an instance of the calculator
        calculator = FreightForwardingCostCalculator(
            cargo_weight, cargo_volume, distance, air_rate_per_kg, sea_rate_per_cubic_meter
        )

        # Compare costs
        result = calculator.compare_costs()

        # Output results
        print(json.dumps(result, indent=4))

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
