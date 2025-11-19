"""
Generated Code Metadata:
========================
Original URL: https://saltydazeusvi.com
Prompt: Write a Python function that retrieves and displays the available boat options for charters offered by Salty Daze Charters, including details about the Salt Decks and other vessels.
Generated: DETERMINISTIC_ba2832c332123ba9
Batch ID: 20250612_163117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# boat_options.py

class Boat:
    """Represents a boat offered by Salty Daze Charters."""

    def __init__(self, name, capacity, description, amenities=None):
        """
        Initializes a Boat object.

        Args:
            name (str): The name of the boat.
            capacity (int): The maximum capacity of the boat.
            description (str): A brief description of the boat.
            amenities (list[str], optional): A list of amenities offered by the boat. Defaults to None.
        """
        self.name = name
        self.capacity = capacity
        self.description = description
        self.amenities = amenities if amenities else []

    def __str__(self):
        return f"{self.name} - Capacity: {self.capacity}"


class SaltyDazeCharters:
    """Represents Salty Daze Charters and their available boat options."""

    def __init__(self):
        """
        Initializes a SaltyDazeCharters object with available boat options.
        """
        self.boats = [
            Boat(
                "Salt Decks",
                6,
                "Our flagship vessel, perfect for sunset cruises and snorkeling trips.",
                ["Wi-Fi", "Snorkeling gear", "Catering"],
            ),
            Boat(
                "Sea Dog",
                8,
                "A sturdy vessel ideal for fishing charters and island hopping.",
                ["Fishing gear", "Catering", "Shade canopy"],
            ),
            Boat(
                "Tidal Wave",
                12,
                "Our largest vessel, great for group charters and events.",
                ["Wi-Fi", "Catering", "Dancing floor"],
            ),
        ]

    def get_boat_options(self):
        """
        Retrieves and displays the available boat options.

        Returns:
            list[Boat]: A list of available Boat objects.
        """
        return self.boats

    def display_boat_options(self):
        """
        Displays the available boat options with their details.
        """
        try:
            boat_options = self.get_boat_options()
            if not boat_options:
                print("No boat options available.")
                return

            for boat in boat_options:
                print(boat)
                print(f"  Description: {boat.description}")
                if boat.amenities:
                    print(f"  Amenities: {', '.join(boat.amenities)}")
                print()
        except Exception as e:
            print(f"An error occurred: {str(e)}")


def main():
    charters = SaltyDazeCharters()
    charters.display_boat_options()


if __name__ == "__main__":
    main()
```
