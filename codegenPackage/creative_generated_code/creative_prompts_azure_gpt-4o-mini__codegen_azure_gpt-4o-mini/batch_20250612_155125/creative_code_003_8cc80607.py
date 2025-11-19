"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtimecodes.pages.dev
Prompt: Describe the process of crafting visually distinct armor pieces using the Armory in Big Time.
Generated: DETERMINISTIC_8cc80607ff0440c1
Batch ID: 20250612_155125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ArmorPiece:
    """Class representing a piece of armor."""

    def __init__(self, name: str, material: str, color: str, durability: int):
        """
        Initializes an armor piece with the given attributes.

        Args:
            name (str): The name of the armor piece.
            material (str): The material the armor is made from.
            color (str): The color of the armor piece.
            durability (int): The durability rating of the armor piece.
        """
        self.name = name
        self.material = material
        self.color = color
        self.durability = durability

    def __repr__(self):
        """Returns a string representation of the armor piece."""
        return f"{self.name} made of {self.material} - Color: {self.color}, Durability: {self.durability}"

class Armory:
    """Class representing an armory where armor pieces can be crafted."""

    def __init__(self):
        """Initializes an empty armory."""
        self.armor_pieces = []

    def craft_armor(self, name: str, material: str, color: str, durability: int) -> ArmorPiece:
        """
        Crafts a new armor piece with the given attributes.

        Args:
            name (str): The name of the armor piece.
            material (str): The material the armor is made from.
            color (str): The color of the armor piece.
            durability (int): The durability rating of the armor piece.

        Returns:
            ArmorPiece: The newly crafted armor piece.
        
        Raises:
            ValueError: If durability is not a positive integer.
        """
        if durability <= 0:
            raise ValueError("Durability must be a positive integer.")

        armor_piece = ArmorPiece(name, material, color, durability)
        self.armor_pieces.append(armor_piece)
        return armor_piece

    def display_armor(self):
        """Displays all crafted armor pieces in the armory."""
        if not self.armor_pieces:
            print("No armor pieces in the armory.")
        for armor in self.armor_pieces:
            print(armor)

def main():
    """Main function to demonstrate the use of the Armory class."""
    try:
        # Create an instance of the Armory
        armory = Armory()

        # Craft visually distinct armor pieces
        armory.craft_armor("Knight's Shield", "Steel", "Silver", 100)
        armory.craft_armor("Mage's Robe", "Cotton", "Blue", 50)
        armory.craft_armor("Rogue's Hood", "Leather", "Black", 75)

        # Display all crafted armor pieces
        armory.display_armor()

    except ValueError as e:
        print(f"Error crafting armor: {e}")

if __name__ == "__main__":
    main()
```
