"""
Generated Code Metadata:
========================
Original URL: https://gematria.com
Prompt: What are some key considerations for developing supplements focused on heart support, digestive health, and hormone & immune system, and how can these be integrated into a product line like Gematria's?
Generated: DETERMINISTIC_094d020f5e14b212
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Supplement:
    """
    A class to represent a dietary supplement.

    Attributes:
        name (str): The name of the supplement.
        ingredients (list): A list of ingredients in the supplement.
        benefits (list): A list of health benefits associated with the supplement.
    """

    def __init__(self, name, ingredients, benefits):
        """
        Initializes a new Supplement instance.

        Args:
            name (str): The name of the supplement.
            ingredients (list): A list of ingredients.
            benefits (list): A list of benefits.
        """
        self.name = name
        self.ingredients = ingredients
        self.benefits = benefits

    def display_info(self):
        """Displays the supplement's information."""
        print(f"Supplement Name: {self.name}")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")
        print("Benefits:")
        for benefit in self.benefits:
            print(f"- {benefit}")

class ProductLine:
    """
    A class to represent a product line of dietary supplements.

    Attributes:
        name (str): The name of the product line.
        supplements (list): A list of supplements in the product line.
    """

    def __init__(self, name):
        """
        Initializes a new ProductLine instance.

        Args:
            name (str): The name of the product line.
        """
        self.name = name
        self.supplements = []

    def add_supplement(self, supplement):
        """
        Adds a supplement to the product line.

        Args:
            supplement (Supplement): The supplement to add.
        """
        if not isinstance(supplement, Supplement):
            raise ValueError("Only Supplement instances can be added.")
        self.supplements.append(supplement)

    def display_product_line(self):
        """Displays the product line's information."""
        print(f"Product Line: {self.name}")
        for supplement in self.supplements:
            supplement.display_info()
            print()  # Add a newline for better readability

# Example usage
if __name__ == "__main__":
    try:
        # Create a product line for heart support
        heart_support_line = ProductLine("Heart Support")

        # Create supplements
        omega_3 = Supplement(
            name="Omega-3 Fish Oil",
            ingredients=["Fish Oil", "Vitamin E"],
            benefits=["Supports heart health", "Reduces inflammation"]
        )

        coq10 = Supplement(
            name="Coenzyme Q10",
            ingredients=["CoQ10", "Gelatin"],
            benefits=["Supports energy production", "Antioxidant properties"]
        )

        # Add supplements to the product line
        heart_support_line.add_supplement(omega_3)
        heart_support_line.add_supplement(coq10)

        # Display the product line
        heart_support_line.display_product_line()

    except Exception as e:
        print(f"An error occurred: {e}")
```
