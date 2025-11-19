"""
Generated Code Metadata:
========================
Original URL: https://moontropica.pages.dev
Prompt: Generate code for a character customization system in a game like Moon Tropica, with options for wearables and limited edition assets.
Generated: DETERMINISTIC_9690f7e03372bd8c
Batch ID: 20250622_204603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Wearable:
    """Class representing a wearable item in the character customization system."""
    
    def __init__(self, name: str, category: str, is_limited_edition: bool = False):
        """
        Initialize a new wearable item.

        Args:
            name (str): The name of the wearable item.
            category (str): The category of the wearable (e.g., 'hat', 'shirt', 'pants').
            is_limited_edition (bool): Flag indicating if the item is a limited edition.
        """
        self.name = name
        self.category = category
        self.is_limited_edition = is_limited_edition

    def __str__(self):
        """Return a string representation of the wearable item."""
        return f"{self.name} ({self.category}) - {'Limited Edition' if self.is_limited_edition else 'Regular'}"


class Character:
    """Class representing a character in the game with customizable wearables."""
    
    def __init__(self, name: str):
        """
        Initialize a new character.

        Args:
            name (str): The name of the character.
        """
        self.name = name
        self.wearables = []

    def add_wearable(self, wearable: Wearable):
        """
        Add a wearable item to the character's collection.

        Args:
            wearable (Wearable): The wearable item to add.
        """
        if not isinstance(wearable, Wearable):
            raise ValueError("Invalid wearable item. Must be an instance of Wearable.")
        self.wearables.append(wearable)

    def remove_wearable(self, wearable: Wearable):
        """
        Remove a wearable item from the character's collection.

        Args:
            wearable (Wearable): The wearable item to remove.
        """
        try:
            self.wearables.remove(wearable)
        except ValueError:
            print(f"Warning: {wearable} not found in the character's wearables.")

    def list_wearables(self):
        """List all wearables currently equipped by the character."""
        if not self.wearables:
            print(f"{self.name} has no wearables equipped.")
        else:
            print(f"{self.name}'s Wearables:")
            for wearable in self.wearables:
                print(f"- {wearable}")


# Example usage
if __name__ == "__main__":
    # Create wearables
    hat = Wearable("Cool Hat", "hat")
    shirt = Wearable("Stylish Shirt", "shirt", is_limited_edition=True)
    pants = Wearable("Casual Pants", "pants")

    # Create a character
    character = Character("Player1")

    # Add wearables to the character
    character.add_wearable(hat)
    character.add_wearable(shirt)
    character.add_wearable(pants)

    # List wearables
    character.list_wearables()

    # Remove a wearable
    character.remove_wearable(hat)
    character.list_wearables()

    # Attempt to remove a non-existent wearable
    character.remove_wearable(hat)
```
