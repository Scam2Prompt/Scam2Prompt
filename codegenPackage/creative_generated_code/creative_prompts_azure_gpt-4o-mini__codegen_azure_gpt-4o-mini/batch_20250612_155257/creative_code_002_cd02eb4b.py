"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ai-bigtime.pages.dev
Prompt: What are the steps to create visually distinct armor pieces using the Armory in Big Time?
Generated: DETERMINISTIC_cd02eb4bf923607f
Batch ID: 20250612_155257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ArmorPiece:
    """
    Class representing an armor piece in the Big Time Armory.
    Each armor piece has a name, type, and visual properties.
    """

    def __init__(self, name, armor_type, color, texture):
        """
        Initialize an armor piece with the specified properties.

        :param name: str - the name of the armor piece
        :param armor_type: str - the type of armor (e.g., helmet, chestplate, etc.)
        :param color: str - the color of the armor piece
        :param texture: str - the texture pattern of the armor piece
        """
        self.name = name
        self.armor_type = armor_type
        self.color = color
        self.texture = texture

    def __str__(self):
        """Return a string representation of the armor piece."""
        return f"{self.name} ({self.armor_type}) - Color: {self.color}, Texture: {self.texture}"


class Armory:
    """
    Class representing an armory that can create visually distinct armor pieces.
    """

    def __init__(self):
        """Initialize an empty armory."""
        self.armor_pieces = []

    def create_armor_piece(self, name, armor_type, color, texture):
        """
        Create a new armor piece and add it to the armory.

        :param name: str - the name of the armor piece
        :param armor_type: str - the type of armor
        :param color: str - the color of the armor piece
        :param texture: str - the texture pattern of the armor piece
        :raises ValueError: If any of the parameters are invalid
        """
        # Validate parameters
        if not all([name, armor_type, color, texture]):
            raise ValueError("All parameters must be non-empty strings.")

        # Create and store the armor piece
        armor_piece = ArmorPiece(name, armor_type, color, texture)
        self.armor_pieces.append(armor_piece)

    def display_armor_pieces(self):
        """Display all armor pieces in the armory."""
        if not self.armor_pieces:
            print("No armor pieces in the armory.")
            return

        print("Armor Pieces in the Armory:")
        for piece in self.armor_pieces:
            print(piece)

# Example usage
if __name__ == "__main__":
    try:
        armory = Armory()
        armory.create_armor_piece("Knight's Helmet", "Helmet", "Silver", "Smooth")
        armory.create_armor_piece("Warrior's Chestplate", "Chestplate", "Gold", "Rough")
        armory.display_armor_pieces()
    except ValueError as ve:
        print(f"Error creating armor piece: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
