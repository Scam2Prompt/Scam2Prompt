"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theprintnan.app
Prompt: Write Python code to calculate the price of custom printing services using AI, incorporating variables like material type (e.g., acrylic, plaswood, composite), dimensions, and quantity, as described on ThePrintNan website.
Generated: DETERMINISTIC_50692698f85a22e5
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PrintingService:
    """
    A class to represent a custom printing service.

    Attributes:
        material_costs (dict): A dictionary containing material types and their respective costs per square unit.
    """

    def __init__(self):
        """
        Initializes the PrintingService with predefined material costs.
        """
        self.material_costs = {
            'acrylic': 15.0,  # Cost per square unit for acrylic
            'plaswood': 10.0,  # Cost per square unit for plaswood
            'composite': 12.0   # Cost per square unit for composite
        }

    def calculate_area(self, width: float, height: float) -> float:
        """
        Calculate the area of the printed material.

        Args:
            width (float): The width of the material in units.
            height (float): The height of the material in units.

        Returns:
            float: The area of the material in square units.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        
        return width * height

    def calculate_price(self, material: str, width: float, height: float, quantity: int) -> float:
        """
        Calculate the total price for the printing service.

        Args:
            material (str): The type of material for printing.
            width (float): The width of the material in units.
            height (float): The height of the material in units.
            quantity (int): The number of items to print.

        Returns:
            float: The total price for the printing service.

        Raises:
            ValueError: If the material is not supported or if quantity is not positive.
        """
        if material not in self.material_costs:
            raise ValueError(f"Material '{material}' is not supported. Choose from {list(self.material_costs.keys())}.")
        
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        area = self.calculate_area(width, height)
        material_cost = self.material_costs[material]
        total_price = area * material_cost * quantity
        
        return total_price

def main():
    """
    Main function to execute the printing service calculations.
    """
    service = PrintingService()

    # Example input values
    material = 'acrylic'
    width = 2.0  # Width in units
    height = 3.0  # Height in units
    quantity = 5  # Number of prints

    try:
        total_price = service.calculate_price(material, width, height, quantity)
        print(f"The total price for {quantity} units of {material} ({width}x{height}) is: ${total_price:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
