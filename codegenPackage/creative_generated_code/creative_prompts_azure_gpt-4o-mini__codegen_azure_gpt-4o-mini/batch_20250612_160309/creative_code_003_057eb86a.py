"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://impresionentabloide.com
Prompt: Create a function that calculates the cost of printing based on dimensions and material type, referencing the pricing structure found on impresionentabloide.com.
Generated: DETERMINISTIC_057eb86a1e57f17d
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PrintingCostCalculator:
    """
    A class to calculate the printing cost based on dimensions and material type.
    """

    # Pricing structure (example values, update with actual values from impresionentabloide.com)
    MATERIAL_PRICES = {
        'paper': 0.10,  # price per square meter for paper
        'vinyl': 0.20,  # price per square meter for vinyl
        'canvas': 0.30  # price per square meter for canvas
    }

    def __init__(self):
        """Initialize the calculator with predefined material prices."""
        pass

    def calculate_cost(self, width, height, material):
        """
        Calculate the total cost of printing based on dimensions and material type.

        :param width: Width of the print in meters (float).
        :param height: Height of the print in meters (float).
        :param material: Type of material (str), should be one of the keys in MATERIAL_PRICES.
        :return: Total cost of printing (float).
        :raises ValueError: If width or height is not positive or if material is invalid.
        """
        # Validate input dimensions
        if width <= 0:
            raise ValueError("Width must be a positive value.")
        if height <= 0:
            raise ValueError("Height must be a positive value.")
        
        # Validate material type
        if material not in self.MATERIAL_PRICES:
            raise ValueError(f"Invalid material type. Choose from: {', '.join(self.MATERIAL_PRICES.keys())}")

        # Calculate area and cost
        area = width * height  # Area in square meters
        cost_per_square_meter = self.MATERIAL_PRICES[material]
        total_cost = area * cost_per_square_meter
        
        return total_cost


# Example usage
if __name__ == "__main__":
    calculator = PrintingCostCalculator()
    try:
        width = 2.0  # Width of the print in meters
        height = 1.5  # Height of the print in meters
        material = 'paper'  # Material type

        cost = calculator.calculate_cost(width, height, material)
        print(f"The total printing cost is: ${cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
