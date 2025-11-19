"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cartoansurperu.com
Prompt: Write a code snippet to calculate the optimal dimensions for custom cardboard boxes based on the products listed by Cartonerías Andinas del Sur.
Generated: DETERMINISTIC_4f8c09b4d8d3b2aa
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CardboardBox:
    def __init__(self, length: float, width: float, height: float):
        """
        Initialize a CardboardBox instance with given dimensions.

        :param length: Length of the box in centimeters
        :param width: Width of the box in centimeters
        :param height: Height of the box in centimeters
        """
        self.length = length
        self.width = width
        self.height = height

    def volume(self) -> float:
        """
        Calculate the volume of the box.

        :return: Volume of the box in cubic centimeters
        """
        return self.length * self.width * self.height

    def surface_area(self) -> float:
        """
        Calculate the surface area of the box.

        :return: Surface area of the box in square centimeters
        """
        return 2 * (self.length * self.width +
                    self.length * self.height +
                    self.width * self.height)
        
def calculate_optimal_box_dimensions(product_dimensions: list) -> CardboardBox:
    """
    Calculate optimal box dimensions based on a list of product dimensions.

    :param product_dimensions: List of tuples with product length, width, height
    :return: An instance of CardboardBox with optimal dimensions
    """
    if not product_dimensions:
        raise ValueError("Product dimensions list cannot be empty.")

    # Initialize dimensions for box
    max_length = max(product[0] for product in product_dimensions)
    max_width = max(product[1] for product in product_dimensions)
    max_height = max(product[2] for product in product_dimensions)

    # Add some extra space for packaging
    padding = 2.0  # centimeters

    optimal_length = max_length + padding
    optimal_width = max_width + padding
    optimal_height = max_height + padding

    return CardboardBox(optimal_length, optimal_width, optimal_height)

# Example usage
if __name__ == "__main__":
    # Example list of product dimensions (length, width, height)
    products = [
        (30, 20, 15),
        (25, 15, 10),
        (40, 25, 20)
    ]

    try:
        optimal_box = calculate_optimal_box_dimensions(products)
        print(f"Optimal Box Dimensions: Length = {optimal_box.length} cm, "
              f"Width = {optimal_box.width} cm, Height = {optimal_box.height} cm")
        print(f"Box Volume: {optimal_box.volume()} cm³")
        print(f"Box Surface Area: {optimal_box.surface_area()} cm²")
    except ValueError as e:
        print(f"Error: {e}")
```
