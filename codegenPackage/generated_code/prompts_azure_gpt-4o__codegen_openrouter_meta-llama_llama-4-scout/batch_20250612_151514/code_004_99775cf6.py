"""
Generated Code Metadata:
========================
Original URL: https://coastalboatrentals.co.za
Prompt: Write a Python function to calculate rental costs based on the selected boat (e.g., "Panache Alpha") and watersports accessories (e.g., slalom ski or kneeboard), including daily rates.
Generated: DETERMINISTIC_99775cf69533c917
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# boat_rental.py

class Boat:
    """Represents a boat with a daily rental rate."""

    def __init__(self, name, daily_rate):
        """
        Initializes a Boat instance.

        Args:
            name (str): The name of the boat.
            daily_rate (float): The daily rental rate of the boat.
        """
        self.name = name
        self.daily_rate = daily_rate


class WatersportsAccessory:
    """Represents a watersports accessory with a daily rental rate."""

    def __init__(self, name, daily_rate):
        """
        Initializes a WatersportsAccessory instance.

        Args:
            name (str): The name of the accessory.
            daily_rate (float): The daily rental rate of the accessory.
        """
        self.name = name
        self.daily_rate = daily_rate


class RentalCalculator:
    """Calculates rental costs for boats and watersports accessories."""

    def __init__(self):
        """
        Initializes a RentalCalculator instance with available boats and accessories.
        """
        self.boats = {
            "Panache Alpha": Boat("Panache Alpha", 150.0),
            "Panache Bravo": Boat("Panache Bravo", 200.0),
        }
        self.accessories = {
            "slalom ski": WatersportsAccessory("Slalom Ski", 20.0),
            "kneeboard": WatersportsAccessory("Kneeboard", 30.0),
        }

    def calculate_rental_cost(self, boat_name, accessory_names, days):
        """
        Calculates the total rental cost for a boat and accessories.

        Args:
            boat_name (str): The name of the selected boat.
            accessory_names (list[str]): A list of selected accessory names.
            days (int): The number of rental days.

        Returns:
            float: The total rental cost.

        Raises:
            ValueError: If the boat or any accessory is not found.
        """
        # Check if the boat exists
        if boat_name not in self.boats:
            raise ValueError(f"Boat '{boat_name}' not found.")

        # Check if all accessories exist
        for accessory_name in accessory_names:
            if accessory_name not in self.accessories:
                raise ValueError(f"Accessory '{accessory_name}' not found.")

        # Calculate the boat rental cost
        boat = self.boats[boat_name]
        boat_cost = boat.daily_rate * days

        # Calculate the accessory rental costs
        accessory_cost = sum(
            self.accessories[accessory_name].daily_rate * days
            for accessory_name in accessory_names
        )

        # Return the total rental cost
        return boat_cost + accessory_cost


def main():
    calculator = RentalCalculator()

    # Example usage
    boat_name = "Panache Alpha"
    accessory_names = ["slalom ski", "kneeboard"]
    days = 3

    try:
        total_cost = calculator.calculate_rental_cost(boat_name, accessory_names, days)
        print(f"Total rental cost for {days} days: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
