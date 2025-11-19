"""
Generated Code Metadata:
========================
Original URL: https://udizine.com
Prompt: Generate a code snippet for a retail display system using the Vertik system mentioned on UDIZINE, including features for wall-mounted shelving and adjustable configurations.
Generated: DETERMINISTIC_8693eb78d18a21c6
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Retail Display System using Vertik System
This script simulates a retail display system with wall-mounted shelving and adjustable configurations.
"""

class VertikSystem:
    """
    Represents the Vertik retail display system.
    Provides functionality for wall-mounted shelving and adjustable configurations.
    """

    def __init__(self):
        # Initialize the shelving system with an empty configuration
        self.shelves = []

    def add_shelf(self, position, width, height):
        """
        Adds a shelf to the system.

        :param position: (int) The vertical position of the shelf (in cm).
        :param width: (int) The width of the shelf (in cm).
        :param height: (int) The height of the shelf (in cm).
        :raises ValueError: If position, width, or height are invalid.
        """
        if position < 0 or width <= 0 or height <= 0:
            raise ValueError("Position, width, and height must be positive values.")
        
        shelf = {
            "position": position,
            "width": width,
            "height": height
        }
        self.shelves.append(shelf)

    def remove_shelf(self, position):
        """
        Removes a shelf from the system based on its position.

        :param position: (int) The vertical position of the shelf to remove.
        :raises ValueError: If no shelf exists at the given position.
        """
        for shelf in self.shelves:
            if shelf["position"] == position:
                self.shelves.remove(shelf)
                return
        raise ValueError(f"No shelf found at position {position}.")

    def adjust_shelf(self, old_position, new_position):
        """
        Adjusts the position of an existing shelf.

        :param old_position: (int) The current position of the shelf.
        :param new_position: (int) The new position of the shelf.
        :raises ValueError: If no shelf exists at the old position or if the new position is invalid.
        """
        if new_position < 0:
            raise ValueError("New position must be a positive value.")
        
        for shelf in self.shelves:
            if shelf["position"] == old_position:
                shelf["position"] = new_position
                return
        raise ValueError(f"No shelf found at position {old_position}.")

    def display_configuration(self):
        """
        Displays the current configuration of the shelving system.

        :return: (str) A formatted string of the shelving configuration.
        """
        if not self.shelves:
            return "No shelves configured."
        
        configuration = "Current Shelving Configuration:\n"
        for shelf in sorted(self.shelves, key=lambda x: x["position"]):
            configuration += f"Position: {shelf['position']} cm, Width: {shelf['width']} cm, Height: {shelf['height']} cm\n"
        return configuration


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the Vertik system
        vertik = VertikSystem()

        # Add shelves
        vertik.add_shelf(position=50, width=100, height=30)
        vertik.add_shelf(position=150, width=120, height=40)

        # Display current configuration
        print(vertik.display_configuration())

        # Adjust a shelf's position
        vertik.adjust_shelf(old_position=50, new_position=75)

        # Display updated configuration
        print(vertik.display_configuration())

        # Remove a shelf
        vertik.remove_shelf(position=150)

        # Display final configuration
        print(vertik.display_configuration())

    except ValueError as e:
        print(f"Error: {e}")
```
