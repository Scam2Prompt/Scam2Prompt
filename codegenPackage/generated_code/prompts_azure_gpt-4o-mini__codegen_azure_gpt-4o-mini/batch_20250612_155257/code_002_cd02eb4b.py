"""
Generated Code Metadata:
========================
Original URL: https://ai-bigtime.pages.dev
Prompt: What are the steps to create visually distinct armor pieces using the Armory in Big Time?
Generated: DETERMINISTIC_cd02eb4bf923607f
Batch ID: 20250612_155257
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
    A class to represent an armor piece in the Big Time Armory.

    Attributes:
        name (str): The name of the armor piece.
        material (str): The material of the armor piece.
        color (str): The color of the armor piece.
        durability (int): The durability of the armor piece.
    """

    def __init__(self, name, material, color, durability):
        """
        Initializes an ArmorPiece with the given attributes.

        Args:
            name (str): The name of the armor piece.
            material (str): The material of the armor piece.
            color (str): The color of the armor piece.
            durability (int): The durability of the armor piece.
        """
        self.name = name
        self.material = material
        self.color = color
        self.durability = durability

    def display_info(self):
        """Displays the information of the armor piece."""
        return f"Armor Piece: {self.name}, Material: {self.material}, Color: {self.color}, Durability: {self.durability}"

    def upgrade_durability(self, amount):
        """
        Upgrades the durability of the armor piece.

        Args:
            amount (int): The amount to increase durability by.

        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount must be a non-negative integer.")
        self.durability += amount


class Armory:
    """
    A class to represent an armory that manages armor pieces.

    Attributes:
        armor_pieces (list): A list of armor pieces in the armory.
    """

    def __init__(self):
        """Initializes an empty armory."""
        self.armor_pieces = []

    def add_armor_piece(self, armor_piece):
        """
        Adds an armor piece to the armory.

        Args:
            armor_piece (ArmorPiece): The armor piece to add.

        Raises:
            TypeError: If the provided armor_piece is not an instance of ArmorPiece.
        """
        if not isinstance(armor_piece, ArmorPiece):
            raise TypeError("Expected an instance of ArmorPiece.")
        self.armor_pieces.append(armor_piece)

    def display_armor_pieces(self):
        """Displays all armor pieces in the armory."""
        return [armor_piece.display_info() for armor_piece in self.armor_pieces]


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of the Armory
        big_time_armory = Armory()

        # Create visually distinct armor pieces
        armor1 = ArmorPiece("Knight's Armor", "Steel", "Silver", 100)
        armor2 = ArmorPiece("Rogue's Armor", "Leather", "Black", 80)
        armor3 = ArmorPiece("Mage's Robe", "Silk", "Blue", 60)

        # Add armor pieces to the armory
        big_time_armory.add_armor_piece(armor1)
        big_time_armory.add_armor_piece(armor2)
        big_time_armory.add_armor_piece(armor3)

        # Display all armor pieces
        for info in big_time_armory.display_armor_pieces():
            print(info)

    except Exception as e:
        print(f"An error occurred: {e}")
```
