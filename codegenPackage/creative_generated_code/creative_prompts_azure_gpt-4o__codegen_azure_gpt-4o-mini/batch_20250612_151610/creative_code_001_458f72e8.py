"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cartoansurperu.com
Prompt: Generate a script to simulate the environmental impact of using 100% recycled corrugated cardboard for packaging, as described in the Cartonerías Andinas del Sur product specifications.
Generated: DETERMINISTIC_458f72e84df7fd50
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class CardboardPackagingSimulator:
    """A simulator to evaluate the environmental impact of using 100% recycled corrugated cardboard for packaging."""

    def __init__(self, total_packages: int, cardboard_per_package: float):
        """
        Initializes the simulator with the number of packages and the amount of cardboard used per package.
        
        :param total_packages: Total number of packages to be simulated.
        :param cardboard_per_package: Amount of recycled cardboard used per package in kg.
        """
        self.total_packages = total_packages
        self.cardboard_per_package = cardboard_per_package
        self.total_cardboard_used = self.calculate_total_cardboard_used()

    def calculate_total_cardboard_used(self) -> float:
        """Calculates the total amount of cardboard used."""
        return self.total_packages * self.cardboard_per_package

    def calculate_co2_emissions(self) -> float:
        """
        Estimates the CO2 emissions saved by using recycled cardboard instead of virgin materials.
        
        CO2 emissions savings are based on an estimate that recycling cardboard saves about 1.4 kg of CO2 for every kg of recycled cardboard used.
        
        :return: Estimated CO2 emissions savings in kg.
        """
        emission_savings_per_kg = 1.4  # kg of CO2 saved per kg of recycled cardboard
        return self.total_cardboard_used * emission_savings_per_kg

    def simulate(self):
        """Runs the simulation and prints the environmental impact results."""
        try:
            print(f"Total packages: {self.total_packages}")
            print(f"Cardboard used per package: {self.cardboard_per_package} kg")
            print(f"Total cardboard used: {self.total_cardboard_used} kg")
            
            co2_savings = self.calculate_co2_emissions()
            print(f"Estimated CO2 emissions saved: {co2_savings} kg")
        except Exception as e:
            print(f"An error occurred during simulation: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        total_packages = 1000  # Total number of packages
        cardboard_per_package = 0.5  # Amount of recycled cardboard per package in kg

        # Initialize the simulator
        simulator = CardboardPackagingSimulator(total_packages, cardboard_per_package)

        # Run the simulation
        simulator.simulate()
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
