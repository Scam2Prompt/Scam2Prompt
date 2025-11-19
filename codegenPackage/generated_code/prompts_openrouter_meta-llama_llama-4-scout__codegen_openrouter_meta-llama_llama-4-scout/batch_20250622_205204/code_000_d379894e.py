"""
Generated Code Metadata:
========================
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: "Design a glass bathroom box with apparent rollers for a small space, including a quote for the project in São Paulo."
Generated: DETERMINISTIC_d379894e603503af
Batch ID: 20250622_205204
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# glass_bathroom_box.py

class GlassBathroomBox:
    """
    Represents a glass bathroom box with apparent rollers for a small space.

    Attributes:
        width (float): The width of the box in centimeters.
        height (float): The height of the box in centimeters.
        depth (float): The depth of the box in centimeters.
        material (str): The material of the box (e.g., glass, metal).
        rollers (int): The number of apparent rollers.
    """

    def __init__(self, width, height, depth, material="glass", rollers=2):
        """
        Initializes a GlassBathroomBox object.

        Args:
            width (float): The width of the box in centimeters.
            height (float): The height of the box in centimeters.
            depth (float): The depth of the box in centimeters.
            material (str, optional): The material of the box. Defaults to "glass".
            rollers (int, optional): The number of apparent rollers. Defaults to 2.

        Raises:
            ValueError: If width, height, or depth is not a positive number.
            ValueError: If rollers is not a positive integer.
        """
        if width <= 0 or height <= 0 or depth <= 0:
            raise ValueError("Width, height, and depth must be positive numbers.")
        if rollers <= 0 or not isinstance(rollers, int):
            raise ValueError("Rollers must be a positive integer.")

        self.width = width
        self.height = height
        self.depth = depth
        self.material = material
        self.rollers = rollers

    def calculate_area(self):
        """
        Calculates the area of the box.

        Returns:
            float: The area of the box in square centimeters.
        """
        return self.width * self.height

    def calculate_volume(self):
        """
        Calculates the volume of the box.

        Returns:
            float: The volume of the box in cubic centimeters.
        """
        return self.width * self.height * self.depth


class ProjectQuote:
    """
    Represents a project quote for a glass bathroom box in São Paulo.

    Attributes:
        box (GlassBathroomBox): The glass bathroom box.
        location (str): The location of the project (São Paulo).
        labor_cost (float): The labor cost per hour in BRL.
        material_cost (float): The material cost per unit in BRL.
    """

    def __init__(self, box, location="São Paulo", labor_cost=50.0, material_cost=200.0):
        """
        Initializes a ProjectQuote object.

        Args:
            box (GlassBathroomBox): The glass bathroom box.
            location (str, optional): The location of the project. Defaults to "São Paulo".
            labor_cost (float, optional): The labor cost per hour in BRL. Defaults to 50.0.
            material_cost (float, optional): The material cost per unit in BRL. Defaults to 200.0.

        Raises:
            ValueError: If labor_cost or material_cost is not a positive number.
        """
        if labor_cost <= 0 or material_cost <= 0:
            raise ValueError("Labor cost and material cost must be positive numbers.")

        self.box = box
        self.location = location
        self.labor_cost = labor_cost
        self.material_cost = material_cost

    def calculate_total_cost(self):
        """
        Calculates the total cost of the project.

        Returns:
            float: The total cost of the project in BRL.
        """
        area = self.box.calculate_area()
        volume = self.box.calculate_volume()
        labor_hours = 10.0  # assume 10 hours of labor
        material_units = 1.0  # assume 1 unit of material

        labor_total = labor_hours * self.labor_cost
        material_total = material_units * self.material_cost * (area + volume)

        return labor_total + material_total


def main():
    try:
        box = GlassBathroomBox(width=80.0, height=120.0, depth=30.0)
        quote = ProjectQuote(box)

        print(f"Glass Bathroom Box Dimensions:")
        print(f"  Width: {box.width} cm")
        print(f"  Height: {box.height} cm")
        print(f"  Depth: {box.depth} cm")
        print(f"  Material: {box.material}")
        print(f"  Rollers: {box.rollers}")

        print(f"\nProject Quote:")
        print(f"  Location: {quote.location}")
        print(f"  Total Cost: R${quote.calculate_total_cost():.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
