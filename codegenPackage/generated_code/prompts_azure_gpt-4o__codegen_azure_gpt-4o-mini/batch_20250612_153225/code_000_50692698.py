"""
Generated Code Metadata:
========================
Original URL: https://theprintnan.app
Prompt: Write Python code to calculate the price of custom printing services using AI, incorporating variables like material type (e.g., acrylic, plaswood, composite), dimensions, and quantity, as described on ThePrintNan website.
Generated: DETERMINISTIC_50692698f85a22e5
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CustomPrintingService:
    """
    A class to calculate the price of custom printing services based on material type,
    dimensions, and quantity.
    """

    MATERIAL_PRICES = {
        'acrylic': 20.0,  # Price per square unit for acrylic
        'plaswood': 15.0,  # Price per square unit for plaswood
        'composite': 10.0,  # Price per square unit for composite
    }

    def __init__(self, material: str, width: float, height: float, quantity: int):
        """
        Initializes the CustomPrintingService with material type, dimensions, and quantity.

        :param material: The type of material for printing.
        :param width: The width of the print in units.
        :param height: The height of the print in units.
        :param quantity: The number of prints to be produced.
        """
        self.material = material.lower()
        self.width = width
        self.height = height
        self.quantity = quantity

        # Validate inputs
        self.validate_inputs()

    def validate_inputs(self):
        """
        Validates the input parameters to ensure they are correct.
        Raises ValueError if any input is invalid.
        """
        if self.material not in self.MATERIAL_PRICES:
            raise ValueError(f"Invalid material type: {self.material}. "
                             f"Available options: {', '.join(self.MATERIAL_PRICES.keys())}.")
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        if self.quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

    def calculate_area(self) -> float:
        """
        Calculates the area of the print.

        :return: The area in square units.
        """
        return self.width * self.height

    def calculate_price(self) -> float:
        """
        Calculates the total price for the custom printing service.

        :return: The total price based on material, dimensions, and quantity.
        """
        area = self.calculate_area()
        price_per_unit = self.MATERIAL_PRICES[self.material]
        total_price = area * price_per_unit * self.quantity
        return total_price

    def get_price_summary(self) -> str:
        """
        Generates a summary of the pricing details.

        :return: A formatted string summarizing the price calculation.
        """
        total_price = self.calculate_price()
        return (f"Material: {self.material.capitalize()}\n"
                f"Dimensions: {self.width} x {self.height} units\n"
                f"Quantity: {self.quantity}\n"
                f"Total Price: ${total_price:.2f}")


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of CustomPrintingService
        printing_service = CustomPrintingService(material='acrylic', width=2.5, height=3.0, quantity=10)
        
        # Print the price summary
        print(printing_service.get_price_summary())
    except ValueError as e:
        print(f"Error: {e}")
```
