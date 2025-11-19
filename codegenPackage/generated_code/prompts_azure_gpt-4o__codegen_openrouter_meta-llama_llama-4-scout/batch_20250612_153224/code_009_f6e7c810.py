"""
Generated Code Metadata:
========================
Original URL: https://rehiletes.com
Prompt: Generate a script to calculate the total cost of multi-day excursions offered by "Rehiletes," including options for destinations like San Miguel de Allende and Veracruz.
Generated: DETERMINISTIC_f6e7c8102fa454ed
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# excursion_calculator.py

class Excursion:
    def __init__(self, name, destination, days, price_per_day, activities=None):
        """
        Initialize an Excursion object.

        Args:
            name (str): Name of the excursion.
            destination (str): Destination of the excursion.
            days (int): Number of days for the excursion.
            price_per_day (float): Price per day for the excursion.
            activities (list, optional): List of activities. Defaults to None.
        """
        self.name = name
        self.destination = destination
        self.days = days
        self.price_per_day = price_per_day
        self.activities = activities if activities else []

    def calculate_total_cost(self):
        """
        Calculate the total cost of the excursion.

        Returns:
            float: Total cost of the excursion.
        """
        return self.days * self.price_per_day

    def add_activity(self, activity, cost):
        """
        Add an activity to the excursion.

        Args:
            activity (str): Name of the activity.
            cost (float): Cost of the activity.
        """
        self.activities.append((activity, cost))

    def calculate_total_cost_with_activities(self):
        """
        Calculate the total cost of the excursion including activities.

        Returns:
            float: Total cost of the excursion including activities.
        """
        total_cost = self.calculate_total_cost()
        activities_cost = sum(cost for _, cost in self.activities)
        return total_cost + activities_cost


class RehiletesExcursionCalculator:
    def __init__(self):
        """
        Initialize a RehiletesExcursionCalculator object.
        """
        self.excursions = {}

    def add_excursion(self, excursion):
        """
        Add an excursion to the calculator.

        Args:
            excursion (Excursion): Excursion object.
        """
        self.excursions[excursion.name] = excursion

    def get_excursion(self, name):
        """
        Get an excursion by name.

        Args:
            name (str): Name of the excursion.

        Returns:
            Excursion: Excursion object or None if not found.
        """
        return self.excursions.get(name)

    def calculate_total_cost(self, excursion_name):
        """
        Calculate the total cost of an excursion.

        Args:
            excursion_name (str): Name of the excursion.

        Returns:
            float: Total cost of the excursion or None if not found.

        Raises:
            ValueError: If excursion not found.
        """
        excursion = self.get_excursion(excursion_name)
        if excursion:
            return excursion.calculate_total_cost()
        else:
            raise ValueError("Excursion not found")

    def calculate_total_cost_with_activities(self, excursion_name):
        """
        Calculate the total cost of an excursion including activities.

        Args:
            excursion_name (str): Name of the excursion.

        Returns:
            float: Total cost of the excursion including activities or None if not found.

        Raises:
            ValueError: If excursion not found.
        """
        excursion = self.get_excursion(excursion_name)
        if excursion:
            return excursion.calculate_total_cost_with_activities()
        else:
            raise ValueError("Excursion not found")


def main():
    calculator = RehiletesExcursionCalculator()

    # Create excursions
    san_miguel_excursion = Excursion(
        "San Miguel de Allende",
        "San Miguel de Allende",
        5,
        200.0,
    )
    san_miguel_excursion.add_activity("Wine tasting", 50.0)
    san_miguel_excursion.add_activity("City tour", 75.0)

    veracruz_excursion = Excursion(
        "Veracruz",
        "Veracruz",
        7,
        250.0,
    )
    veracruz_excursion.add_activity("Beach day", 30.0)
    veracruz_excursion.add_activity("Historical tour", 60.0)

    # Add excursions to calculator
    calculator.add_excursion(san_miguel_excursion)
    calculator.add_excursion(veracruz_excursion)

    # Calculate total costs
    try:
        san_miguel_total_cost = calculator.calculate_total_cost("San Miguel de Allende")
        san_miguel_total_cost_with_activities = calculator.calculate_total_cost_with_activities("San Miguel de Allende")
        veracruz_total_cost = calculator.calculate_total_cost("Veracruz")
        veracruz_total_cost_with_activities = calculator.calculate_total_cost_with_activities("Veracruz")

        print(f"San Miguel de Allende total cost: ${san_miguel_total_cost:.2f}")
        print(f"San Miguel de Allende total cost with activities: ${san_miguel_total_cost_with_activities:.2f}")
        print(f"Veracruz total cost: ${veracruz_total_cost:.2f}")
        print(f"Veracruz total cost with activities: ${veracruz_total_cost_with_activities:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
