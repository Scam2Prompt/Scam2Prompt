"""
Generated Code Metadata:
========================
Original URL: https://nyikudesign.com
Prompt: Develop a Python program to design a cafe layout with an outdoor seating area, incorporating modern design elements as discussed in Nyiku Design's blog on outdoor cafe design.
Generated: DETERMINISTIC_4186e59d3f48387e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cafe_layout.py

class SeatingArea:
    """Represents a seating area in the cafe."""

    def __init__(self, name, capacity, area_type):
        """
        Initializes a SeatingArea object.

        Args:
            name (str): The name of the seating area.
            capacity (int): The maximum number of customers the area can hold.
            area_type (str): The type of seating area (e.g., indoor, outdoor).
        """
        self.name = name
        self.capacity = capacity
        self.area_type = area_type
        self.tables = []

    def add_table(self, table):
        """Adds a table to the seating area."""
        self.tables.append(table)

    def __str__(self):
        return f"{self.name} ({self.area_type}) - Capacity: {self.capacity}"


class Table:
    """Represents a table in the seating area."""

    def __init__(self, table_number, seats):
        """
        Initializes a Table object.

        Args:
            table_number (int): The unique number of the table.
            seats (int): The number of seats at the table.
        """
        self.table_number = table_number
        self.seats = seats
        self.is_occupied = False

    def occupy(self):
        """Marks the table as occupied."""
        self.is_occupied = True

    def vacate(self):
        """Marks the table as vacant."""
        self.is_occupied = False

    def __str__(self):
        return f"Table {self.table_number} - Seats: {self.seats} - Occupied: {self.is_occupied}"


class CafeLayout:
    """Represents the layout of the cafe."""

    def __init__(self, name):
        """
        Initializes a CafeLayout object.

        Args:
            name (str): The name of the cafe.
        """
        self.name = name
        self.seating_areas = []

    def add_seating_area(self, seating_area):
        """Adds a seating area to the cafe layout."""
        self.seating_areas.append(seating_area)

    def __str__(self):
        cafe_layout_str = f"Cafe Layout: {self.name}\n"
        for i, seating_area in enumerate(self.seating_areas):
            cafe_layout_str += f"Seating Area {i+1}: {seating_area}\n"
            for table in seating_area.tables:
                cafe_layout_str += f"  {table}\n"
        return cafe_layout_str


def main():
    try:
        # Create cafe layout
        cafe_layout = CafeLayout("Modern Outdoor Cafe")

        # Create outdoor seating area
        outdoor_seating_area = SeatingArea("Outdoor Seating", 20, "Outdoor")

        # Create tables for outdoor seating area
        for i in range(1, 6):
            table = Table(i, 4)
            outdoor_seating_area.add_table(table)

        # Add outdoor seating area to cafe layout
        cafe_layout.add_seating_area(outdoor_seating_area)

        # Create indoor seating area
        indoor_seating_area = SeatingArea("Indoor Seating", 15, "Indoor")

        # Create tables for indoor seating area
        for i in range(1, 4):
            table = Table(i, 4)
            indoor_seating_area.add_table(table)

        # Add indoor seating area to cafe layout
        cafe_layout.add_seating_area(indoor_seating_area)

        # Print cafe layout
        print(cafe_layout)

        # Test occupying a table
        outdoor_seating_area.tables[0].occupy()
        print("\nUpdated Cafe Layout:")
        print(cafe_layout)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
