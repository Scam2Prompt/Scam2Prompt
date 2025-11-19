"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seubolodecorado.com.br
Prompt: Generate a Python function that creates a personalized Bentô Cake order for various occasions, including customization options for themes and flavors.
Generated: DETERMINISTIC_d0f8c5378847f449
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BentoCakeOrder:
    """A class to represent a Bentô Cake order."""

    def __init__(self, occasion, flavor, theme):
        """
        Initialize a new Bentô Cake order.

        :param occasion: Occasion for the cake (e.g., birthday, wedding).
        :param flavor: Flavor of the cake (e.g., chocolate, vanilla).
        :param theme: Theme for the cake (e.g., floral, cartoon).
        """
        self.occasion = occasion
        self.flavor = flavor
        self.theme = theme

    def __str__(self):
        """Return a string representation of the cake order."""
        return (f"Bentô Cake Order:\n"
                f" - Occasion: {self.occasion}\n"
                f" - Flavor: {self.flavor}\n"
                f" - Theme: {self.theme}")

def create_bento_cake_order(occasion, flavor, theme):
    """
    Create a personalized Bentô Cake order.

    :param occasion: Occasion for the cake (str).
    :param flavor: Flavor of the cake (str).
    :param theme: Theme for the cake (str).
    :return: A BentoCakeOrder instance.
    :raises ValueError: If any parameter is empty or invalid.
    """

    # Validate input parameters
    if not isinstance(occasion, str) or not occasion.strip():
        raise ValueError("Occasion must be a non-empty string.")
    
    if not isinstance(flavor, str) or not flavor.strip():
        raise ValueError("Flavor must be a non-empty string.")

    if not isinstance(theme, str) or not theme.strip():
        raise ValueError("Theme must be a non-empty string.")

    # Create the Bento Cake order
    order = BentoCakeOrder(occasion, flavor, theme)

    return order

# Example usage
if __name__ == "__main__":
    try:
        order = create_bento_cake_order("Birthday", "Chocolate", "Superhero")
        print(order)
    except ValueError as e:
        print(f"Error creating order: {e}")
```
