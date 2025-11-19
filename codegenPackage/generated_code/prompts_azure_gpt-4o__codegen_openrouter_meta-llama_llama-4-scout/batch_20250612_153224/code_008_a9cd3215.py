"""
Generated Code Metadata:
========================
Original URL: https://atilumber.com
Prompt: Write a script to calculate the cost of timber products based on dimensions and species, referencing the categories of softwood, hardwood, and sawn timber from Askar Trading International.
Generated: DETERMINISTIC_a9cd3215e972cd59
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# timber_cost_calculator.py

class TimberProduct:
    """Represents a timber product with dimensions and species."""

    def __init__(self, length, width, thickness, species):
        """
        Initializes a TimberProduct.

        Args:
            length (float): Length in meters.
            width (float): Width in meters.
            thickness (float): Thickness in meters.
            species (str): Species of the timber product.
        """
        self.length = length
        self.width = width
        self.thickness = thickness
        self.species = species

    def calculate_volume(self):
        """Calculates the volume of the timber product in cubic meters."""
        return self.length * self.width * self.thickness


class TimberCostCalculator:
    """Calculates the cost of timber products based on dimensions and species."""

    def __init__(self):
        # Price per cubic meter for each species and category
        self.prices = {
            "softwood": {
                "pine": 500,
                "spruce": 450,
                "fir": 475
            },
            "hardwood": {
                "oak": 800,
                "maple": 700,
                "cherry": 750
            },
            "sawn_timber": {
                "pine": 600,
                "oak": 900,
                "teak": 1000
            }
        }

    def calculate_cost(self, timber_product):
        """
        Calculates the cost of a timber product.

        Args:
            timber_product (TimberProduct): The timber product.

        Returns:
            float: The cost of the timber product.

        Raises:
            ValueError: If the species is not found.
        """
        volume = timber_product.calculate_volume()
        species = timber_product.species.lower()

        # Determine the category and species price
        for category, species_prices in self.prices.items():
            if species in [s.lower() for s in species_prices.keys()]:
                species_price = next((price for s, price in species_prices.items() if s.lower() == species), None)
                if species_price is not None:
                    return volume * species_price

        # If species is not found, raise an error
        raise ValueError(f"Species '{timber_product.species}' not found.")

def main():
    calculator = TimberCostCalculator()

    # Example usage:
    try:
        product1 = TimberProduct(2, 0.1, 0.05, "Pine")
        cost1 = calculator.calculate_cost(product1)
        print(f"Cost of {product1.species} timber product: ${cost1:.2f}")

        product2 = TimberProduct(3, 0.2, 0.1, "Oak")
        cost2 = calculator.calculate_cost(product2)
        print(f"Cost of {product2.species} timber product: ${cost2:.2f}")

        product3 = TimberProduct(1, 0.05, 0.025, "Invalid Species")
        cost3 = calculator.calculate_cost(product3)
        print(f"Cost of {product3.species} timber product: ${cost3:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
