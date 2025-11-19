"""
Generated Code Metadata:
========================
Original URL: https://bigtimecodes.pages.dev
Prompt: Describe the process of crafting visually distinct armor pieces using the Armory in Big Time.
Generated: DETERMINISTIC_8cc80607ff0440c1
Batch ID: 20250612_155125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ArmorPiece:
    """
    Represents a piece of armor with visual attributes.
    """

    def __init__(self, name, material, color, design):
        """
        Initializes an ArmorPiece with the given attributes.

        :param name: str - The name of the armor piece.
        :param material: str - The material of the armor piece.
        :param color: str - The color of the armor piece.
        :param design: str - The design style of the armor piece.
        """
        self.name = name
        self.material = material
        self.color = color
        self.design = design

    def __str__(self):
        """
        Returns a string representation of the armor piece.
        """
        return f"{self.name} made of {self.material}, colored {self.color}, with {self.design} design."


class Armory:
    """
    Represents an armory that can craft visually distinct armor pieces.
    """

    def __init__(self):
        """
        Initializes an empty armory.
        """
        self.armor_pieces = []

    def craft_armor(self, name, material, color, design):
        """
        Crafts a new armor piece and adds it to the armory.

        :param name: str - The name of the armor piece.
        :param material: str - The material of the armor piece.
        :param color: str - The color of the armor piece.
        :param design: str - The design style of the armor piece.
        :raises ValueError: If any of the parameters are empty strings.
        """
        if not all([name, material, color, design]):
            raise ValueError("All parameters must be non-empty strings.")

        new_armor = ArmorPiece(name, material, color, design)
        self.armor_pieces.append(new_armor)
        print(f"Crafted: {new_armor}")

    def display_armor(self):
        """
        Displays all crafted armor pieces in the armory.
        """
        if not self.armor_pieces:
            print("No armor pieces crafted yet.")
            return

        print("Crafted Armor Pieces:")
        for armor in self.armor_pieces:
            print(armor)


# Example usage
if __name__ == "__main__":
    try:
        armory = Armory()
        armory.craft_armor("Knight's Shield", "Steel", "Silver", "Classic")
        armory.craft_armor("Mage's Robe", "Silk", "Blue", "Elegant")
        armory.display_armor()
    except ValueError as e:
        print(f"Error: {e}")
```
