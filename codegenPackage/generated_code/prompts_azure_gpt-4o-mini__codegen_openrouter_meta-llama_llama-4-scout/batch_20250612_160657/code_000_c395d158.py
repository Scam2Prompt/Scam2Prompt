"""
Generated Code Metadata:
========================
Original URL: https://odasloucabrazzz.blogspot.com
Prompt: Generate a Python script that lists kitchen utensils available at Varejão das Louças, focusing on both rustic and modern styles.
Generated: DETERMINISTIC_c395d158452a4520
Batch ID: 20250612_160657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# kitchen_utensils.py

class KitchenUtensil:
    """Represents a kitchen utensil with its name and style."""

    def __init__(self, name, style):
        """
        Initializes a KitchenUtensil object.

        Args:
            name (str): The name of the kitchen utensil.
            style (str): The style of the kitchen utensil (rustic or modern).
        """
        self.name = name
        self.style = style

    def __repr__(self):
        return f"{self.name} ({self.style})"


class VarejaoDasLoucas:
    """Simulates the Varejão das Louças store with its kitchen utensils."""

    def __init__(self):
        """
        Initializes the Varejão das Louças store with a list of kitchen utensils.
        """
        self.utensils = [
            KitchenUtensil("Wooden Spoon", "rustic"),
            KitchenUtensil("Metal Whisk", "modern"),
            KitchenUtensil("Ceramic Knife", "modern"),
            KitchenUtensil("Bamboo Cutting Board", "rustic"),
            KitchenUtensil("Silicone Spatula", "modern"),
            KitchenUtensil("Cast Iron Skillet", "rustic"),
            KitchenUtensil("Stainless Steel Colander", "modern"),
        ]

    def get_utensils_by_style(self, style=None):
        """
        Retrieves kitchen utensils by style.

        Args:
            style (str, optional): The style of the kitchen utensils to retrieve (rustic, modern, or None for all). Defaults to None.

        Returns:
            list[KitchenUtensil]: A list of kitchen utensils matching the specified style.
        """
        if style is None:
            return self.utensils
        else:
            return [utensil for utensil in self.utensils if utensil.style.lower() == style.lower()]


def main():
    try:
        store = VarejaoDasLoucas()

        print("### All Utensils ###")
        for utensil in store.get_utensils_by_style():
            print(utensil)

        print("\n### Rustic Utensils ###")
        for utensil in store.get_utensils_by_style("rustic"):
            print(utensil)

        print("\n### Modern Utensils ###")
        for utensil in store.get_utensils_by_style("modern"):
            print(utensil)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
