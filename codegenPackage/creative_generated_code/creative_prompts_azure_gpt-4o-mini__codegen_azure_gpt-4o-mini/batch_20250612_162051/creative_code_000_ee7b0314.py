"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shishehbalkon.ir
Prompt: Write a code snippet to calculate the price of balcony glass based on the area in square meters and color, as detailed on the website for شیشه بالکن.
Generated: DETERMINISTIC_ee7b03146472fba2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BalconyGlassCalculator:
    """
    A class to calculate the price of balcony glass based on area and color.
    """

    # Price per square meter for each color
    PRICE_PER_SQ_M = {
        'clear': 100.0,
        'tinted': 120.0,
        'frosted': 150.0,
        'reflective': 180.0
    }

    def __init__(self, area: float, color: str):
        """
        Initializes the BalconyGlassCalculator with the specified area and color.

        :param area: Area in square meters
        :param color: Color of the glass
        """
        self.area = area
        self.color = color.lower()

    def validate_inputs(self):
        """
        Validates the inputs for area and color.

        :raises ValueError: If area is negative or color is not supported
        """
        if self.area < 0:
            raise ValueError("Area cannot be negative.")
        if self.color not in self.PRICE_PER_SQ_M:
            raise ValueError(f"Color '{self.color}' is not supported. "
                             f"Supported colors are: {', '.join(self.PRICE_PER_SQ_M.keys())}")

    def calculate_price(self) -> float:
        """
        Calculates the total price based on area and color.

        :return: Total price for the balcony glass
        """
        self.validate_inputs()
        price_per_sqm = self.PRICE_PER_SQ_M[self.color]
        total_price = self.area * price_per_sqm
        return total_price


def main():
    """
    Main function to demonstrate the BalconyGlassCalculator.
    """
    try:
        # Example inputs
        area = 10.0  # Area in square meters
        color = 'tinted'  # Color of the glass

        # Create an instance of the calculator
        calculator = BalconyGlassCalculator(area, color)

        # Calculate and print the total price
        total_price = calculator.calculate_price()
        print(f"The total price for {area} sqm of {color} balcony glass is: {total_price:.2f} units.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
