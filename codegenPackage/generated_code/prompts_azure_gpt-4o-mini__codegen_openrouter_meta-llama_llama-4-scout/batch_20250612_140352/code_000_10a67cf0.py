"""
Generated Code Metadata:
========================
Original URL: https://airstyleart.co.uk
Prompt: Generate a code snippet for an airbrush nail art application that utilizes stencils for creating geometric designs, as described on Airstyleart.
Generated: DETERMINISTIC_10a67cf0b46ff271
Batch ID: 20250612_140352
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# airbrush_nail_art.py

class Stencil:
    """Represents a stencil for creating geometric designs."""

    def __init__(self, name, shape, dimensions):
        """
        Initializes a Stencil object.

        Args:
            name (str): The name of the stencil.
            shape (str): The shape of the stencil (e.g., circle, square, triangle).
            dimensions (dict): A dictionary containing the dimensions of the stencil (e.g., radius, side_length).
        """
        self.name = name
        self.shape = shape
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name} ({self.shape})"


class NailArt:
    """Represents a nail art design created using stencils."""

    def __init__(self):
        self.stencils = []
        self.design = []

    def add_stencil(self, stencil, x, y):
        """
        Adds a stencil to the nail art design at the specified coordinates.

        Args:
            stencil (Stencil): The stencil to add.
            x (int): The x-coordinate of the stencil.
            y (int): The y-coordinate of the stencil.
        """
        self.stencils.append((stencil, x, y))

    def create_design(self):
        """
        Creates the nail art design by combining the stencils.

        Returns:
            list: A 2D list representing the nail art design.
        """
        # Initialize an empty design
        self.design = [["-" for _ in range(10)] for _ in range(10)]

        # Iterate over the stencils and add them to the design
        for stencil, x, y in self.stencils:
            if stencil.shape == "circle":
                self.add_circle(stencil, x, y)
            elif stencil.shape == "square":
                self.add_square(stencil, x, y)
            elif stencil.shape == "triangle":
                self.add_triangle(stencil, x, y)

        return self.design

    def add_circle(self, stencil, x, y):
        """
        Adds a circle stencil to the design.

        Args:
            stencil (Stencil): The circle stencil.
            x (int): The x-coordinate of the stencil.
            y (int): The y-coordinate of the stencil.
        """
        radius = stencil.dimensions["radius"]
        for i in range(10):
            for j in range(10):
                if (i - x) ** 2 + (j - y) ** 2 <= radius ** 2:
                    self.design[i][j] = "*"

    def add_square(self, stencil, x, y):
        """
        Adds a square stencil to the design.

        Args:
            stencil (Stencil): The square stencil.
            x (int): The x-coordinate of the stencil.
            y (int): The y-coordinate of the stencil.
        """
        side_length = stencil.dimensions["side_length"]
        for i in range(x, x + side_length):
            for j in range(y, y + side_length):
                if 0 <= i < 10 and 0 <= j < 10:
                    self.design[i][j] = "*"

    def add_triangle(self, stencil, x, y):
        """
        Adds a triangle stencil to the design.

        Args:
            stencil (Stencil): The triangle stencil.
            x (int): The x-coordinate of the stencil.
            y (int): The y-coordinate of the stencil.
        """
        side_length = stencil.dimensions["side_length"]
        for i in range(x, x + side_length):
            for j in range(y, y + side_length - i + x):
                if 0 <= i < 10 and 0 <= j < 10:
                    self.design[i][j] = "*"

    def print_design(self):
        """
        Prints the nail art design.
        """
        for row in self.design:
            print(" ".join(row))


def main():
    try:
        # Create stencils
        circle_stencil = Stencil("Circle", "circle", {"radius": 2})
        square_stencil = Stencil("Square", "square", {"side_length": 3})
        triangle_stencil = Stencil("Triangle", "triangle", {"side_length": 4})

        # Create nail art design
        nail_art = NailArt()
        nail_art.add_stencil(circle_stencil, 2, 2)
        nail_art.add_stencil(square_stencil, 5, 5)
        nail_art.add_stencil(triangle_stencil, 1, 6)

        # Create and print the design
        design = nail_art.create_design()
        nail_art.print_design()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
