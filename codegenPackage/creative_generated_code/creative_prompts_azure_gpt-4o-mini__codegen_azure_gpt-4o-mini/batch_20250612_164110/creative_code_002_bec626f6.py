"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rubberflooringindonesia.com
Prompt: Create a function that calculates the best rubber flooring type for different sports facilities, referencing the unique characteristics of products like Eva Mats and Rubber Tiles.
Generated: DETERMINISTIC_bec626f64953a431
Batch ID: 20250612_164110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FlooringType:
    def __init__(self, name, durability, shock_absorption, cost):
        """
        Initialize a FlooringType instance.

        :param name: str - The name of the flooring type.
        :param durability: int - Durability rating (1-10).
        :param shock_absorption: int - Shock absorption rating (1-10).
        :param cost: float - Cost per square foot.
        """
        self.name = name
        self.durability = durability
        self.shock_absorption = shock_absorption
        self.cost = cost

    def __repr__(self):
        return f"{self.name} (Durability: {self.durability}, Shock Absorption: {self.shock_absorption}, Cost: ${self.cost})"


class SportsFacility:
    def __init__(self, name, sport_type, budget):
        """
        Initialize a SportsFacility instance.

        :param name: str - The name of the sports facility.
        :param sport_type: str - The type of sport.
        :param budget: float - Available budget for flooring.
        """
        self.name = name
        self.sport_type = sport_type
        self.budget = budget

    def best_flooring_options(self, flooring_options):
        """
        Calculate the best flooring type based on the facility's sport type and budget.

        :param flooring_options: list - List of available FlooringType instances.
        :return: list - Suitable flooring options within budget.
        """
        # Define criteria for different sports
        sport_criteria = {
            'gymnastics': {'min_shock_absorption': 8, 'max_cost': self.budget},
            'weightlifting': {'min_shock_absorption': 7, 'max_cost': self.budget},
            'basketball': {'min_shock_absorption': 6, 'max_cost': self.budget},
        }

        # Get the criteria for the specified sport
        criteria = sport_criteria.get(self.sport_type.lower())

        if not criteria:
            raise ValueError(f"Unsupported sport type: {self.sport_type}")

        # Filter flooring options based on criteria
        suitable_options = [
            flooring for flooring in flooring_options
            if (flooring.shock_absorption >= criteria['min_shock_absorption'] and
                flooring.cost <= criteria['max_cost'])
        ]

        return suitable_options


def main():
    # Define available flooring types
    flooring_options = [
        FlooringType("Eva Mats", durability=8, shock_absorption=9, cost=3.5),
        FlooringType("Rubber Tiles", durability=9, shock_absorption=7, cost=5.0),
        FlooringType("Foam Tiles", durability=6, shock_absorption=6, cost=2.5),
    ]

    # Create a sports facility
    facility = SportsFacility(name="City Sports Center", sport_type="Gymnastics", budget=4.0)

    try:
        # Get best flooring options for the facility
        best_options = facility.best_flooring_options(flooring_options)

        # Print suitable flooring options
        if best_options:
            print(f"Best flooring options for {facility.name} ({facility.sport_type}):")
            for option in best_options:
                print(option)
        else:
            print(f"No suitable flooring options found for {facility.name} ({facility.sport_type}).")
    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    main()
```
