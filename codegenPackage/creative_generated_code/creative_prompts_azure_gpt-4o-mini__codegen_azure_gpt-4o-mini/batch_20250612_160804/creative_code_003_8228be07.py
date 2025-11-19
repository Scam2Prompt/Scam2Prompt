"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prize-render.net
Prompt: Create a grocery shopping list for a Mexican cucumber salad, detailing ingredient quantities and potential substitutes.
Generated: DETERMINISTIC_8228be07a3b8878c
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GroceryItem:
    """Class to represent an item in the grocery list."""
    
    def __init__(self, name: str, quantity: str, substitutes: list):
        """
        Initialize a grocery item.

        :param name: Name of the ingredient
        :param quantity: Quantity required for the recipe
        :param substitutes: List of potential substitutes for the ingredient
        """
        self.name = name
        self.quantity = quantity
        self.substitutes = substitutes

    def __repr__(self):
        """Return a string representation of the grocery item."""
        return f"{self.name}: {self.quantity} (Substitutes: {', '.join(self.substitutes)})"


class GroceryList:
    """Class to manage a grocery shopping list."""
    
    def __init__(self):
        """Initialize an empty grocery list."""
        self.items = []

    def add_item(self, name: str, quantity: str, substitutes: list):
        """
        Add an item to the grocery list.

        :param name: Name of the ingredient
        :param quantity: Quantity required for the recipe
        :param substitutes: List of potential substitutes for the ingredient
        """
        try:
            item = GroceryItem(name, quantity, substitutes)
            self.items.append(item)
        except Exception as e:
            print(f"Error adding item '{name}': {e}")

    def display_list(self):
        """Display the entire grocery list."""
        print("Grocery Shopping List:")
        for item in self.items:
            print(item)


def create_mexican_cucumber_salad_list():
    """Create a grocery list for Mexican cucumber salad."""
    grocery_list = GroceryList()
    
    grocery_list.add_item("Cucumbers", "2 medium", ["Zucchini", "Celery"])
    grocery_list.add_item("Tomatoes", "2 medium", ["Red bell pepper", "Cherry tomatoes"])
    grocery_list.add_item("Red onion", "1 small", ["Green onion", "Shallots"])
    grocery_list.add_item("Cilantro", "1/4 cup, chopped", ["Parsley", "Basil"])
    grocery_list.add_item("Lime", "1, juiced", ["Lemon", "Vinegar"])
    grocery_list.add_item("Olive oil", "2 tablespoons", ["Canola oil", "Avocado oil"])
    grocery_list.add_item("Salt", "to taste", ["Sea salt", "Kosher salt"])
    grocery_list.add_item("Black pepper", "to taste", ["White pepper", "Cayenne pepper"])

    return grocery_list


if __name__ == "__main__":
    # Create and display the grocery list for Mexican cucumber salad
    salad_grocery_list = create_mexican_cucumber_salad_list()
    salad_grocery_list.display_list()
```
