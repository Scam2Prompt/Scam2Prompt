"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fullteco.cl
Prompt: Create a function that calculates the energy efficiency of various lighting products, inspired by the offerings of Fullteco Spa in Puerto Montt.
Generated: DETERMINISTIC_ee698a4f2a6fad14
Batch ID: 20250612_155916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LightingProduct:
    """
    A class to represent a lighting product and calculate its energy efficiency.
    """

    def __init__(self, name: str, wattage: float, lumens: float) -> None:
        """
        Initializes the LightingProduct with a name, wattage, and lumens output.

        :param name: The name of the lighting product.
        :param wattage: The power consumption of the lighting product in watts.
        :param lumens: The light output of the lighting product in lumens.
        """
        if wattage <= 0:
            raise ValueError("Wattage must be a positive number.")
        if lumens <= 0:
            raise ValueError("Lumens must be a positive number.")
        
        self.name = name
        self.wattage = wattage
        self.lumens = lumens

    def calculate_efficiency(self) -> float:
        """
        Calculates the energy efficiency of the lighting product in lumens per watt.

        :return: The energy efficiency of the lighting product in lumens per watt.
        """
        efficiency = self.lumens / self.wattage
        return efficiency

def display_energy_efficiency(products: list) -> None:
    """
    Displays the energy efficiency of a list of lighting products.

    :param products: A list of LightingProduct instances.
    """
    if not isinstance(products, list):
        raise TypeError("Expected a list of LightingProduct instances.")
    
    for product in products:
        if not isinstance(product, LightingProduct):
            raise TypeError("All items in the list must be instances of LightingProduct.")
        
        try:
            efficiency = product.calculate_efficiency()
            print(f"Product: {product.name}, Efficiency: {efficiency:.2f} lumens/watt")
        except Exception as e:
            print(f"Error calculating efficiency for {product.name}: {e}")

# Example Usage:
if __name__ == "__main__":
    # Create instances of LightingProduct
    products = [
        LightingProduct("LED Bulb 10W", 10, 800),
        LightingProduct("CFL Bulb 15W", 15, 1050),
        LightingProduct("Halogen Bulb 50W", 50, 1000),
    ]

    # Display energy efficiencies
    display_energy_efficiency(products)
```
