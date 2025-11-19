"""
Generated Code Metadata:
========================
Original URL: https://thegladiatorshoes.com
Prompt: Write Python code to create a product filter system for safety shoes based on features like "steel toe," "composite toe," and "metal-free" using the Gladiator Shoes product categories.
Generated: DETERMINISTIC_59d24fd8816606f1
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SafetyShoe:
    """
    A class to represent a safety shoe with various features.
    """

    def __init__(self, name, steel_toe, composite_toe, metal_free):
        """
        Initializes a new SafetyShoe instance.

        :param name: str - The name of the safety shoe.
        :param steel_toe: bool - Indicates if the shoe has a steel toe.
        :param composite_toe: bool - Indicates if the shoe has a composite toe.
        :param metal_free: bool - Indicates if the shoe is metal-free.
        """
        self.name = name
        self.steel_toe = steel_toe
        self.composite_toe = composite_toe
        self.metal_free = metal_free

    def __repr__(self):
        return f"SafetyShoe(name={self.name}, steel_toe={self.steel_toe}, composite_toe={self.composite_toe}, metal_free={self.metal_free})"


class ProductFilter:
    """
    A class to filter safety shoes based on specified features.
    """

    def __init__(self, shoes):
        """
        Initializes the ProductFilter with a list of safety shoes.

        :param shoes: list - A list of SafetyShoe instances.
        """
        self.shoes = shoes

    def filter_by_features(self, steel_toe=None, composite_toe=None, metal_free=None):
        """
        Filters the safety shoes based on the provided features.

        :param steel_toe: bool or None - Filter for steel toe shoes.
        :param composite_toe: bool or None - Filter for composite toe shoes.
        :param metal_free: bool or None - Filter for metal-free shoes.
        :return: list - A list of filtered SafetyShoe instances.
        """
        filtered_shoes = self.shoes

        if steel_toe is not None:
            filtered_shoes = [shoe for shoe in filtered_shoes if shoe.steel_toe == steel_toe]

        if composite_toe is not None:
            filtered_shoes = [shoe for shoe in filtered_shoes if shoe.composite_toe == composite_toe]

        if metal_free is not None:
            filtered_shoes = [shoe for shoe in filtered_shoes if shoe.metal_free == metal_free]

        return filtered_shoes


# Example usage
if __name__ == "__main__":
    # Create a list of safety shoes
    shoes = [
        SafetyShoe("Gladiator Steel Toe", steel_toe=True, composite_toe=False, metal_free=False),
        SafetyShoe("Gladiator Composite Toe", steel_toe=False, composite_toe=True, metal_free=False),
        SafetyShoe("Gladiator Metal-Free", steel_toe=False, composite_toe=False, metal_free=True),
        SafetyShoe("Gladiator All Features", steel_toe=True, composite_toe=True, metal_free=False),
    ]

    # Initialize the product filter
    product_filter = ProductFilter(shoes)

    # Filter shoes based on features
    try:
        filtered_shoes = product_filter.filter_by_features(steel_toe=True)
        print("Filtered Shoes (Steel Toe):", filtered_shoes)

        filtered_shoes = product_filter.filter_by_features(composite_toe=True)
        print("Filtered Shoes (Composite Toe):", filtered_shoes)

        filtered_shoes = product_filter.filter_by_features(metal_free=True)
        print("Filtered Shoes (Metal-Free):", filtered_shoes)

    except Exception as e:
        print(f"An error occurred while filtering shoes: {e}")
```
