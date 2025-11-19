"""
Generated Code Metadata:
========================
Original URL: https://superdar.com
Prompt: Design a decorative table with a unique shape, such as an ellipse or a circle, using solid wood, inspired by the tables on the Мебели Амотем website.
Generated: DETERMINISTIC_d6d61769588fc622
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class Table:
    def __init__(self, shape, width, length, material, thickness):
        """
        Initialize a Table object.

        Args:
            shape (str): The shape of the table (e.g., ellipse, circle).
            width (float): The width of the table.
            length (float): The length of the table.
            material (str): The material used for the table (e.g., solid wood).
            thickness (float): The thickness of the table.
        """
        self.shape = shape
        self.width = width
        self.length = length
        self.material = material
        self.thickness = thickness

    def calculate_area(self):
        """
        Calculate the area of the table.

        Returns:
            float: The area of the table.
        """
        if self.shape.lower() == "ellipse":
            return math.pi * (self.width / 2) * (self.length / 2)
        elif self.shape.lower() == "circle":
            return math.pi * (self.width / 2) ** 2
        else:
            raise ValueError("Unsupported shape")

    def calculate_perimeter(self):
        """
        Calculate the perimeter of the table.

        Returns:
            float: The perimeter of the table.
        """
        if self.shape.lower() == "ellipse":
            # Approximation of the ellipse perimeter using Ramanujan's formula
            h = ((self.width / 2 - self.length / 2) ** 2) / ((self.width / 2 + self.length / 2) ** 2)
            return math.pi * (self.width + self.length) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))
        elif self.shape.lower() == "circle":
            return 2 * math.pi * (self.width / 2)
        else:
            raise ValueError("Unsupported shape")

    def __str__(self):
        return f"Table({self.shape}, {self.width}, {self.length}, {self.material}, {self.thickness})"


class SolidWoodTable(Table):
    def __init__(self, shape, width, length, thickness, wood_type):
        """
        Initialize a SolidWoodTable object.

        Args:
            shape (str): The shape of the table (e.g., ellipse, circle).
            width (float): The width of the table.
            length (float): The length of the table.
            thickness (float): The thickness of the table.
            wood_type (str): The type of solid wood used.
        """
        super().__init__(shape, width, length, "solid wood", thickness)
        self.wood_type = wood_type

    def __str__(self):
        return f"SolidWoodTable({self.shape}, {self.width}, {self.length}, {self.thickness}, {self.wood_type})"


def create_decorative_table(shape, width, length, thickness, wood_type):
    """
    Create a decorative table with a unique shape.

    Args:
        shape (str): The shape of the table (e.g., ellipse, circle).
        width (float): The width of the table.
        length (float): The length of the table.
        thickness (float): The thickness of the table.
        wood_type (str): The type of solid wood used.

    Returns:
        SolidWoodTable: A SolidWoodTable object.

    Raises:
        ValueError: If the shape is not supported.
    """
    try:
        table = SolidWoodTable(shape, width, length, thickness, wood_type)
        print(f"Table area: {table.calculate_area():.2f}")
        print(f"Table perimeter: {table.calculate_perimeter():.2f}")
        return table
    except ValueError as e:
        print(f"Error: {e}")
        return None


# Example usage
if __name__ == "__main__":
    table = create_decorative_table("ellipse", 100, 150, 5, "oak")
    print(table)
```

```python
# Run this code in your environment 
if __name__ == "__main__":
    main = create_decorative_table("ellipse", 100, 150, 5, "oak")
```
