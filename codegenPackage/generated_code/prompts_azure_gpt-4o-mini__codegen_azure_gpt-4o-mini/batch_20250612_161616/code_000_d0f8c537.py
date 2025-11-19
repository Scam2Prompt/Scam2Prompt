"""
Generated Code Metadata:
========================
Original URL: https://seubolodecorado.com.br
Prompt: Generate a Python function that creates a personalized Bentô Cake order for various occasions, including customization options for themes and flavors.
Generated: DETERMINISTIC_d0f8c5378847f449
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BentoCakeOrder:
    """
    A class to represent a Bento Cake order with customization options.
    """

    def __init__(self, occasion, theme, flavor, size):
        """
        Initializes a new Bento Cake order.

        :param occasion: The occasion for the cake (e.g., birthday, wedding).
        :param theme: The theme of the cake (e.g., floral, cartoon).
        :param flavor: The flavor of the cake (e.g., chocolate, vanilla).
        :param size: The size of the cake (e.g., small, medium, large).
        """
        self.occasion = occasion
        self.theme = theme
        self.flavor = flavor
        self.size = size

    def __str__(self):
        """
        Returns a string representation of the Bento Cake order.
        """
        return (f"Bento Cake Order:\n"
                f"  Occasion: {self.occasion}\n"
                f"  Theme: {self.theme}\n"
                f"  Flavor: {self.flavor}\n"
                f"  Size: {self.size}")

def create_bento_cake_order(occasion, theme, flavor, size):
    """
    Creates a personalized Bento Cake order.

    :param occasion: The occasion for the cake.
    :param theme: The theme of the cake.
    :param flavor: The flavor of the cake.
    :param size: The size of the cake.
    :return: A BentoCakeOrder object.
    :raises ValueError: If any of the parameters are invalid.
    """
    # Validate inputs
    valid_occasions = ['birthday', 'wedding', 'anniversary', 'graduation']
    valid_themes = ['floral', 'cartoon', 'elegant', 'funny']
    valid_flavors = ['chocolate', 'vanilla', 'red velvet', 'lemon']
    valid_sizes = ['small', 'medium', 'large']

    if occasion not in valid_occasions:
        raise ValueError(f"Invalid occasion: {occasion}. Choose from {valid_occasions}.")
    if theme not in valid_themes:
        raise ValueError(f"Invalid theme: {theme}. Choose from {valid_themes}.")
    if flavor not in valid_flavors:
        raise ValueError(f"Invalid flavor: {flavor}. Choose from {valid_flavors}.")
    if size not in valid_sizes:
        raise ValueError(f"Invalid size: {size}. Choose from {valid_sizes}.")

    # Create and return the Bento Cake order
    return BentoCakeOrder(occasion, theme, flavor, size)

# Example usage
if __name__ == "__main__":
    try:
        order = create_bento_cake_order('birthday', 'floral', 'chocolate', 'medium')
        print(order)
    except ValueError as e:
        print(f"Error creating order: {e}")
```
