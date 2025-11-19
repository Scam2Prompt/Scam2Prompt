"""
Generated Code Metadata:
========================
Original URL: https://fullteco.cl
Prompt: Write a Python script that integrates with a lighting design library to create customizable lighting layouts for residential and commercial spaces.
Generated: DETERMINISTIC_3189e9df1f49dfa4
Batch ID: 20250612_155916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# lighting_design.py

"""
Library for creating customizable lighting layouts for residential and commercial spaces.

Classes:
    LightingFixture: Represents a lighting fixture with its properties.
    LightingLayout: Manages a collection of lighting fixtures and provides methods for layout creation.

Exceptions:
    InvalidFixtureError: Raised when a lighting fixture has invalid properties.
"""

import math

class InvalidFixtureError(Exception):
    """Raised when a lighting fixture has invalid properties."""
    pass

class LightingFixture:
    """
    Represents a lighting fixture with its properties.

    Attributes:
        name (str): Name of the lighting fixture.
        type (str): Type of the lighting fixture (e.g., 'recessed', 'surface-mounted').
        wattage (int): Wattage of the lighting fixture.
        lumen_output (int): Lumen output of the lighting fixture.
        mounting_height (float): Mounting height of the lighting fixture in feet.
    """

    def __init__(self, name, type, wattage, lumen_output, mounting_height):
        """
        Initializes a LightingFixture object.

        Args:
            name (str): Name of the lighting fixture.
            type (str): Type of the lighting fixture.
            wattage (int): Wattage of the lighting fixture.
            lumen_output (int): Lumen output of the lighting fixture.
            mounting_height (float): Mounting height of the lighting fixture in feet.

        Raises:
            InvalidFixtureError: If any of the properties are invalid.
        """
        if wattage <= 0:
            raise InvalidFixtureError("Wattage must be greater than zero.")
        if lumen_output <= 0:
            raise InvalidFixtureError("Lumen output must be greater than zero.")
        if mounting_height <= 0:
            raise InvalidFixtureError("Mounting height must be greater than zero.")

        self.name = name
        self.type = type
        self.wattage = wattage
        self.lumen_output = lumen_output
        self.mounting_height = mounting_height

    def __str__(self):
        return f"{self.name} ({self.type}) - {self.wattage}W, {self.lumen_output} lumens"


class LightingLayout:
    """
    Manages a collection of lighting fixtures and provides methods for layout creation.

    Attributes:
        fixtures (list): List of LightingFixture objects.
        space_type (str): Type of space (e.g., 'residential', 'commercial').
        room_size (tuple): Size of the room in feet (length, width).
    """

    def __init__(self, space_type, room_size):
        """
        Initializes a LightingLayout object.

        Args:
            space_type (str): Type of space.
            room_size (tuple): Size of the room in feet (length, width).
        """
        self.fixtures = []
        self.space_type = space_type
        self.room_size = room_size

    def add_fixture(self, fixture):
        """
        Adds a lighting fixture to the layout.

        Args:
            fixture (LightingFixture): LightingFixture object to add.
        """
        self.fixtures.append(fixture)

    def calculate_total_lumen_output(self):
        """
        Calculates the total lumen output of all fixtures in the layout.

        Returns:
            int: Total lumen output.
        """
        return sum(fixture.lumen_output for fixture in self.fixtures)

    def calculate_fixture_spacing(self):
        """
        Calculates the recommended spacing between fixtures based on the room size and fixture mounting height.

        Returns:
            float: Recommended spacing between fixtures in feet.
        """
        room_length, room_width = self.room_size
        mounting_heights = [fixture.mounting_height for fixture in self.fixtures]
        avg_mounting_height = sum(mounting_heights) / len(mounting_heights)
        return math.sqrt(room_length * room_width) / (avg_mounting_height * 2)

    def __str__(self):
        layout_info = f"Lighting Layout for {self.space_type} space ({self.room_size[0]}x{self.room_size[1]} ft)\n"
        fixture_info = "\n".join([str(fixture) for fixture in self.fixtures])
        return layout_info + fixture_info


def main():
    try:
        # Create lighting fixtures
        fixture1 = LightingFixture("Recessed Fixture", "recessed", 9, 800, 10)
        fixture2 = LightingFixture("Surface-Mounted Fixture", "surface-mounted", 12, 1000, 12)

        # Create lighting layout
        layout = LightingLayout("residential", (12, 15))
        layout.add_fixture(fixture1)
        layout.add_fixture(fixture2)

        # Print layout information
        print(layout)
        print(f"Total Lumen Output: {layout.calculate_total_lumen_output()} lumens")
        print(f"Recommended Fixture Spacing: {layout.calculate_fixture_spacing():.2f} ft")

    except InvalidFixtureError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
