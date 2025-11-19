"""
Generated Code Metadata:
========================
Original URL: https://cartoansurperu.com
Prompt: Write a Python code snippet to calculate the required size of a corrugated cardboard box for a specific product, considering its dimensions and weight, using Cartonerías Andinas del Sur's product specifications.
Generated: DETERMINISTIC_ed88dfa1ea57e050
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# corrugated_box_calculator.py

class Product:
    """Represents a product with dimensions and weight."""

    def __init__(self, length, width, height, weight):
        """
        Initializes a Product instance.

        Args:
            length (float): Product length in cm.
            width (float): Product width in cm.
            height (float): Product height in cm.
            weight (float): Product weight in kg.
        """
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight


class CorrugatedBox:
    """Calculates the required size of a corrugated cardboard box."""

    def __init__(self, product):
        """
        Initializes a CorrugatedBox instance.

        Args:
            product (Product): Product instance.
        """
        self.product = product

    def calculate_box_size(self):
        """
        Calculates the required size of the corrugated cardboard box.

        Returns:
            dict: Box dimensions (length, width, height) in cm.
        """
        # Cartonerías Andinas del Sur's product specifications
        # Assume a 5 cm margin for each side
        box_length = self.product.length + 10
        box_width = self.product.width + 10
        box_height = self.product.height + 5  # Less height margin

        # Ensure box dimensions are multiples of 5 ( corrugated cardboard standard)
        box_length = self._round_to_multiple(box_length, 5)
        box_width = self._round_to_multiple(box_width, 5)
        box_height = self._round_to_multiple(box_height, 5)

        return {"length": box_length, "width": box_width, "height": box_height}

    def calculate_box_thickness(self):
        """
        Calculates the required thickness of the corrugated cardboard box based on product weight.

        Returns:
            str: Box thickness (e.g., "E", "B", "A", etc.).
        """
        if self.product.weight <= 5:
            return "E"
        elif self.product.weight <= 10:
            return "B"
        elif self.product.weight <= 20:
            return "A"
        else:
            raise ValueError("Product weight exceeds maximum allowed value")

    @staticmethod
    def _round_to_multiple(value, multiple):
        """
        Rounds a value to the nearest multiple.

        Args:
            value (float): Value to round.
            multiple (int): Multiple to round to.

        Returns:
            int: Rounded value.
        """
        return multiple * round(value / multiple)


def main():
    try:
        product = Product(30, 20, 15, 8)
        box = CorrugatedBox(product)
        box_size = box.calculate_box_size()
        box_thickness = box.calculate_box_thickness()

        print("Box Size:")
        print(f"  Length: {box_size['length']} cm")
        print(f"  Width: {box_size['width']} cm")
        print(f"  Height: {box_size['height']} cm")
        print(f"Box Thickness: {box_thickness}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
