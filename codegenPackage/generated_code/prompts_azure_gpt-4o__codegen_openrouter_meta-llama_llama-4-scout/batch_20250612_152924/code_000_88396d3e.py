"""
Generated Code Metadata:
========================
Original URL: https://cristalesgraf.com
Prompt: Write a Python script to calculate the cost estimation for glass and aluminum materials based on the specifications provided by CristalesGraf, including dimensions and material type.
Generated: DETERMINISTIC_88396d3ecf1e0850
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# material_calculator.py

class Material:
    """Base class for materials."""

    def __init__(self, name, price_per_unit):
        """
        Initialize a material.

        Args:
            name (str): Material name.
            price_per_unit (float): Price per unit of the material.
        """
        self.name = name
        self.price_per_unit = price_per_unit

    def calculate_cost(self, quantity):
        """
        Calculate the cost of the material.

        Args:
            quantity (float): Quantity of the material.

        Returns:
            float: Total cost of the material.
        """
        return self.price_per_unit * quantity


class Glass(Material):
    """Glass material."""

    def __init__(self, price_per_square_meter):
        """
        Initialize glass material.

        Args:
            price_per_square_meter (float): Price per square meter of glass.
        """
        super().__init__("Glass", price_per_square_meter)

    def calculate_cost_by_dimensions(self, length, width):
        """
        Calculate the cost of glass based on dimensions.

        Args:
            length (float): Length of the glass.
            width (float): Width of the glass.

        Returns:
            float: Total cost of the glass.
        """
        area = length * width
        return self.calculate_cost(area)


class Aluminum(Material):
    """Aluminum material."""

    def __init__(self, price_per_linear_meter):
        """
        Initialize aluminum material.

        Args:
            price_per_linear_meter (float): Price per linear meter of aluminum.
        """
        super().__init__("Aluminum", price_per_linear_meter)

    def calculate_cost_by_dimensions(self, length):
        """
        Calculate the cost of aluminum based on dimensions.

        Args:
            length (float): Length of the aluminum.

        Returns:
            float: Total cost of the aluminum.
        """
        return self.calculate_cost(length)


def main():
    try:
        # Define material prices
        glass_price_per_square_meter = 50.0
        aluminum_price_per_linear_meter = 20.0

        # Create material objects
        glass = Glass(glass_price_per_square_meter)
        aluminum = Aluminum(aluminum_price_per_linear_meter)

        # Get user input for dimensions
        print("Glass Specifications:")
        glass_length = float(input("Enter length (m): "))
        glass_width = float(input("Enter width (m): "))

        print("\nAluminum Specifications:")
        aluminum_length = float(input("Enter length (m): "))

        # Calculate costs
        glass_cost = glass.calculate_cost_by_dimensions(glass_length, glass_width)
        aluminum_cost = aluminum.calculate_cost_by_dimensions(aluminum_length)

        # Print results
        print(f"\nGlass Cost: ${glass_cost:.2f}")
        print(f"Aluminum Cost: ${aluminum_cost:.2f}")

    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
