"""
Generated Code Metadata:
========================
Original URL: https://fullteco.cl
Prompt: Create a function that calculates the energy efficiency of various lighting products, inspired by the offerings of Fullteco Spa in Puerto Montt.
Generated: DETERMINISTIC_ee698a4f2a6fad14
Batch ID: 20250612_155916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# lighting_efficiency_calculator.py

class LightingProduct:
    """Represents a lighting product with its characteristics."""

    def __init__(self, name: str, wattage: float, lumens: float):
        """
        Initializes a LightingProduct instance.

        Args:
        - name (str): The name of the lighting product.
        - wattage (float): The power consumption of the lighting product in watts.
        - lumens (float): The luminous flux of the lighting product in lumens.
        """
        self.name = name
        self.wattage = wattage
        self.lumens = lumens

    def calculate_efficiency(self) -> float:
        """
        Calculates the energy efficiency of the lighting product.

        Returns:
        - float: The energy efficiency in lumens per watt (lm/W).
        """
        if self.wattage <= 0:
            raise ValueError("Wattage must be greater than zero.")
        return self.lumens / self.wattage


class LightingEfficiencyCalculator:
    """Calculates the energy efficiency of various lighting products."""

    def __init__(self):
        """Initializes a LightingEfficiencyCalculator instance."""
        self.products = []

    def add_product(self, product: LightingProduct):
        """
        Adds a lighting product to the calculator.

        Args:
        - product (LightingProduct): The lighting product to add.
        """
        self.products.append(product)

    def calculate_efficiencies(self) -> dict:
        """
        Calculates the energy efficiency of all added lighting products.

        Returns:
        - dict: A dictionary with product names as keys and their efficiencies as values.
        """
        efficiencies = {}
        for product in self.products:
            try:
                efficiency = product.calculate_efficiency()
                efficiencies[product.name] = efficiency
            except Exception as e:
                print(f"Error calculating efficiency for {product.name}: {str(e)}")
        return efficiencies

    def compare_efficiencies(self) -> dict:
        """
        Compares the energy efficiencies of all added lighting products.

        Returns:
        - dict: A dictionary with product names as keys and their efficiency rankings as values.
        """
        efficiencies = self.calculate_efficiencies()
        sorted_efficiencies = sorted(efficiencies.items(), key=lambda x: x[1], reverse=True)
        rankings = {product: rank + 1 for rank, (product, _) in enumerate(sorted_efficiencies)}
        return rankings


def main():
    calculator = LightingEfficiencyCalculator()

    # Example usage:
    product1 = LightingProduct("LED Bulb", 9, 800)
    product2 = LightingProduct("Halogen Bulb", 20, 400)
    product3 = LightingProduct("Energy-Saving Bulb", 11, 950)

    calculator.add_product(product1)
    calculator.add_product(product2)
    calculator.add_product(product3)

    efficiencies = calculator.calculate_efficiencies()
    rankings = calculator.compare_efficiencies()

    print("Energy Efficiencies:")
    for product, efficiency in efficiencies.items():
        print(f"{product}: {efficiency:.2f} lm/W")

    print("\nEfficiency Rankings:")
    for product, ranking in rankings.items():
        print(f"{product}: Rank {ranking}")


if __name__ == "__main__":
    main()
```
