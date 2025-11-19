"""
Generated Code Metadata:
========================
Original URL: https://race-ridefire.cc
Prompt: Create a product description for a new line of cycling helmets inspired by Giro’s Helios Spherical helmet, including code snippets for generating product specifications and comparisons.
Generated: DETERMINISTIC_74054b433faf875f
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CyclingHelmet:
    """
    A class to represent a cycling helmet with specifications and comparisons.
    """

    def __init__(self, name, weight, material, price, features):
        """
        Initializes a new CyclingHelmet instance.

        :param name: str - The name of the helmet
        :param weight: float - The weight of the helmet in grams
        :param material: str - The material of the helmet
        :param price: float - The price of the helmet in USD
        :param features: list - A list of features of the helmet
        """
        self.name = name
        self.weight = weight
        self.material = material
        self.price = price
        self.features = features

    def display_specifications(self):
        """
        Displays the specifications of the helmet.
        """
        specs = (
            f"Helmet Name: {self.name}\n"
            f"Weight: {self.weight} grams\n"
            f"Material: {self.material}\n"
            f"Price: ${self.price:.2f}\n"
            f"Features: {', '.join(self.features)}\n"
        )
        print(specs)

    def compare_with(self, other_helmet):
        """
        Compares this helmet with another helmet.

        :param other_helmet: CyclingHelmet - Another helmet to compare with
        :return: str - Comparison result
        """
        comparison = (
            f"Comparing {self.name} with {other_helmet.name}:\n"
            f"Weight Difference: {self.weight - other_helmet.weight} grams\n"
            f"Price Difference: ${self.price - other_helmet.price:.2f}\n"
        )
        return comparison


def main():
    """
    Main function to create helmet instances and display their specifications and comparisons.
    """
    try:
        # Create instances of CyclingHelmet
        helmet1 = CyclingHelmet(
            name="Giro Helios Spherical",
            weight=300,
            material="Polycarbonate",
            price=299.99,
            features=["Spherical design", "MIPS technology", "Ventilation system"]
        )

        helmet2 = CyclingHelmet(
            name="Giro Aether Spherical",
            weight=250,
            material="EPS foam",
            price=349.99,
            features=["Spherical design", "MIPS technology", "Lightweight"]
        )

        # Display specifications
        helmet1.display_specifications()
        helmet2.display_specifications()

        # Compare helmets
        comparison_result = helmet1.compare_with(helmet2)
        print(comparison_result)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
