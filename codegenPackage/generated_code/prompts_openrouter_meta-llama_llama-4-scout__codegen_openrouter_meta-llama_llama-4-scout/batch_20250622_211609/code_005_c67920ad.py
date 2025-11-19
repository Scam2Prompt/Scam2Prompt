"""
Generated Code Metadata:
========================
Original URL: https://graffian.com
Prompt: Write a short program to calculate the environmental impact of sourcing cooking oils from various regions, considering factors like carbon footprint and fair trade practices.
Generated: DETERMINISTIC_c67920ad605f2b25
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# environmental_impact_calculator.py

class CookingOil:
    """Represents a cooking oil with its environmental impact data."""

    def __init__(self, name, region, carbon_footprint, fair_trade_certified):
        """
        Initializes a CookingOil object.

        Args:
            name (str): Name of the cooking oil.
            region (str): Region where the cooking oil is sourced.
            carbon_footprint (float): Carbon footprint of the cooking oil in kg CO2e per liter.
            fair_trade_certified (bool): Whether the cooking oil is fair trade certified.
        """
        self.name = name
        self.region = region
        self.carbon_footprint = carbon_footprint
        self.fair_trade_certified = fair_trade_certified

    def __str__(self):
        return f"{self.name} from {self.region}"


class EnvironmentalImpactCalculator:
    """Calculates the environmental impact of sourcing cooking oils."""

    def __init__(self):
        self.cooking_oils = []

    def add_cooking_oil(self, cooking_oil):
        """
        Adds a cooking oil to the calculator.

        Args:
            cooking_oil (CookingOil): Cooking oil to add.
        """
        self.cooking_oils.append(cooking_oil)

    def calculate_total_carbon_footprint(self):
        """
        Calculates the total carbon footprint of all cooking oils.

        Returns:
            float: Total carbon footprint in kg CO2e per liter.
        """
        return sum(oil.carbon_footprint for oil in self.cooking_oils)

    def get_fair_trade_cooking_oils(self):
        """
        Gets a list of fair trade certified cooking oils.

        Returns:
            list[CookingOil]: List of fair trade certified cooking oils.
        """
        return [oil for oil in self.cooking_oils if oil.fair_trade_certified]

    def print_environmental_impact_report(self):
        """
        Prints an environmental impact report for all cooking oils.
        """
        print("Environmental Impact Report:")
        for oil in self.cooking_oils:
            print(f"  - {oil}:")
            print(f"    - Carbon Footprint: {oil.carbon_footprint} kg CO2e per liter")
            print(f"    - Fair Trade Certified: {oil.fair_trade_certified}")
        print(f"Total Carbon Footprint: {self.calculate_total_carbon_footprint()} kg CO2e per liter")
        print(f"Fair Trade Certified Cooking Oils: {len(self.get_fair_trade_cooking_oils())}")


def main():
    try:
        calculator = EnvironmentalImpactCalculator()

        # Add cooking oils
        calculator.add_cooking_oil(CookingOil("Palm Oil", "Southeast Asia", 2.5, False))
        calculator.add_cooking_oil(CookingOil("Olive Oil", "Mediterranean", 1.2, True))
        calculator.add_cooking_oil(CookingOil("Coconut Oil", "South Asia", 1.8, False))
        calculator.add_cooking_oil(CookingOil("Avocado Oil", "South America", 1.5, True))

        # Print environmental impact report
        calculator.print_environmental_impact_report()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
