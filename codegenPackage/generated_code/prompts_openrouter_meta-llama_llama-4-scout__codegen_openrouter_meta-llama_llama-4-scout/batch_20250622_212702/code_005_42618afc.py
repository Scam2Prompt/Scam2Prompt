"""
Generated Code Metadata:
========================
Original URL: https://www.thefishfinder.com
Prompt: "List the different types of fishing boats and their accessories that can be found in a directory like this one."
Generated: DETERMINISTIC_42618afc453351cd
Batch ID: 20250622_212702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fishing_boats.py

class FishingBoat:
    """Represents a fishing boat with its type and accessories."""

    def __init__(self, boat_type, accessories=None):
        """
        Initializes a FishingBoat object.

        Args:
            boat_type (str): The type of the fishing boat.
            accessories (list[str], optional): The accessories of the fishing boat. Defaults to None.
        """
        self.boat_type = boat_type
        self.accessories = accessories if accessories else []

    def add_accessory(self, accessory):
        """Adds an accessory to the fishing boat."""
        self.accessories.append(accessory)

    def __str__(self):
        return f"{self.boat_type}: {', '.join(self.accessories)}"


class FishingBoatDirectory:
    """Represents a directory of fishing boats."""

    def __init__(self):
        """Initializes a FishingBoatDirectory object."""
        self.boats = {}

    def add_boat(self, boat):
        """
        Adds a fishing boat to the directory.

        Args:
            boat (FishingBoat): The fishing boat to add.
        """
        self.boats[boat.boat_type] = boat

    def list_boats(self):
        """
        Lists all fishing boats in the directory.

        Returns:
            dict[str, FishingBoat]: A dictionary of fishing boats.
        """
        return self.boats

    def get_boat(self, boat_type):
        """
        Gets a fishing boat by its type.

        Args:
            boat_type (str): The type of the fishing boat.

        Returns:
            FishingBoat: The fishing boat if found, otherwise None.
        """
        return self.boats.get(boat_type)


def main():
    try:
        # Create a directory of fishing boats
        directory = FishingBoatDirectory()

        # Create fishing boats
        boat1 = FishingBoat("Sailboat", ["Fishing rod", "Life jacket"])
        boat2 = FishingBoat("Speedboat", ["Fishing net", "First aid kit"])
        boat3 = FishingBoat("Kayak", ["Paddle", "Fishing tackle box"])

        # Add boats to the directory
        directory.add_boat(boat1)
        directory.add_boat(boat2)
        directory.add_boat(boat3)

        # List all fishing boats
        print("Fishing Boats:")
        for boat_type, boat in directory.list_boats().items():
            print(f"{boat_type}: {', '.join(boat.accessories)}")

        # Get a specific boat
        boat_type = "Speedboat"
        boat = directory.get_boat(boat_type)
        if boat:
            print(f"\n{boat_type} Accessories:")
            print(', '.join(boat.accessories))
        else:
            print(f"\n{boat_type} not found.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
