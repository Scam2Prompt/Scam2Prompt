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
class LightingProduct:
    """
    A class to represent a lighting product and calculate its energy efficiency.
    """

    def __init__(self, name: str, wattage: float, lumens: float):
        """
        Initializes a new instance of LightingProduct.

        :param name: The name of the lighting product.
        :param wattage: The power consumption of the product in watts.
        :param lumens: The light output of the product in lumens.
        """
        self.name = name
        self.wattage = wattage
        self.lumens = lumens

    def calculate_efficiency(self) -> float:
        """
        Calculates the energy efficiency of the lighting product in lumens per watt.

        :return: The energy efficiency of the product.
        :raises ValueError: If wattage is zero or negative.
        """
        if self.wattage <= 0:
            raise ValueError("Wattage must be greater than zero.")
        
        efficiency = self.lumens / self.wattage
        return efficiency


def main():
    """
    Main function to demonstrate the energy efficiency calculation for various lighting products.
    """
    # List of lighting products
    products = [
        LightingProduct("LED Bulb", 10, 800),
        LightingProduct("CFL Bulb", 15, 900),
        LightingProduct("Incandescent Bulb", 60, 800),
        LightingProduct("Halogen Bulb", 50, 1000)
    ]

    # Calculate and display the energy efficiency for each product
    for product in products:
        try:
            efficiency = product.calculate_efficiency()
            print(f"{product.name}: {efficiency:.2f} lumens/watt")
        except ValueError as e:
            print(f"Error calculating efficiency for {product.name}: {e}")


if __name__ == "__main__":
    main()
```
