"""
Generated Code Metadata:
========================
Original URL: https://t528.com
Prompt: Write a Python script to calculate the maximum cargo weight for a Boeing 787-9 aircraft based on its cargo dimensions.
Generated: DETERMINISTIC_18fd22afd3d3c664
Batch ID: 20250622_205031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Boeing 787-9 Cargo Weight Calculator

Calculates the maximum cargo weight for a Boeing 787-9 aircraft based on its cargo dimensions.

References:
- Boeing 787-9 Airplane Characteristics Manual
"""

class CargoCompartment:
    def __init__(self, length, width, height, max_load):
        """
        Initialize a cargo compartment.

        Args:
            length (float): Length of the compartment in feet.
            width (float): Width of the compartment in feet.
            height (float): Height of the compartment in feet.
            max_load (float): Maximum load capacity in pounds.
        """
        self.length = length
        self.width = width
        self.height = height
        self.max_load = max_load

    def calculate_volume(self):
        """
        Calculate the volume of the compartment in cubic feet.

        Returns:
            float: Volume of the compartment.
        """
        return self.length * self.width * self.height


class Boeing7879:
    def __init__(self):
        """
        Initialize a Boeing 787-9 aircraft.

        Cargo compartments' dimensions and maximum load capacities are based on the Boeing 787-9 Airplane Characteristics Manual.
        """
        self.compartments = {
            'forward': CargoCompartment(61.4, 15.5, 16.4, 16100),
            'aft': CargoCompartment(59.4, 15.5, 16.4, 14600),
        }

    def calculate_max_cargo_weight(self, length, width, height, density):
        """
        Calculate the maximum cargo weight based on its dimensions and density.

        Args:
            length (float): Length of the cargo in feet.
            width (float): Width of the cargo in feet.
            height (float): Height of the cargo in feet.
            density (float): Density of the cargo in pounds per cubic foot.

        Returns:
            float: Maximum cargo weight.

        Raises:
            ValueError: If the cargo dimensions or density are invalid.
        """
        if length <= 0 or width <= 0 or height <= 0 or density <= 0:
            raise ValueError("Cargo dimensions and density must be positive.")

        cargo_volume = length * width * height
        cargo_weight = cargo_volume * density

        # Check if cargo can fit in any compartment and calculate max weight
        max_weight = 0
        for compartment in self.compartments.values():
            if cargo_volume <= compartment.calculate_volume():
                max_weight = min(max_weight + cargo_weight, compartment.max_load)

        return min(max_weight, self.get_total_max_load())

    def get_total_max_load(self):
        """
        Get the total maximum load capacity of all cargo compartments.

        Returns:
            float: Total maximum load capacity.
        """
        return sum(compartment.max_load for compartment in self.compartments.values())


def main():
    try:
        aircraft = Boeing7879()

        # Example usage
        cargo_length = 10  # feet
        cargo_width = 5   # feet
        cargo_height = 5  # feet
        cargo_density = 10  # pounds per cubic foot

        max_cargo_weight = aircraft.calculate_max_cargo_weight(cargo_length, cargo_width, cargo_height, cargo_density)
        print(f"Maximum cargo weight: {max_cargo_weight} pounds")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
