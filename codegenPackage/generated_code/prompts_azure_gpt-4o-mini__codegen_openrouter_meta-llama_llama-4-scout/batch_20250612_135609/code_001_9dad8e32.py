"""
Generated Code Metadata:
========================
Original URL: https://michelledoylegoldsmith.com
Prompt: Write a function that retrieves and displays unique bespoke jewelry pieces, highlighting unusual colored gemstones and high-quality diamonds.
Generated: DETERMINISTIC_9dad8e329a305e26
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bespoke_jewelry.py

class Gemstone:
    """Represents a gemstone with its characteristics."""

    def __init__(self, name, color, quality):
        """
        Initializes a Gemstone object.

        Args:
            name (str): The name of the gemstone.
            color (str): The color of the gemstone.
            quality (str): The quality of the gemstone.
        """
        self.name = name
        self.color = color
        self.quality = quality

    def __str__(self):
        return f"{self.name} - {self.color} ({self.quality})"


class JewelryPiece:
    """Represents a bespoke jewelry piece."""

    def __init__(self, name, gemstones, diamond_quality):
        """
        Initializes a JewelryPiece object.

        Args:
            name (str): The name of the jewelry piece.
            gemstones (list[Gemstone]): A list of gemstones in the jewelry piece.
            diamond_quality (str): The quality of the diamond in the jewelry piece.
        """
        self.name = name
        self.gemstones = gemstones
        self.diamond_quality = diamond_quality

    def __str__(self):
        gemstones_str = "\n".join(["  - " + str(gemstone) for gemstone in self.gemstones])
        return f"{self.name}\nGemstones:\n{gemstones_str}\nDiamond Quality: {self.diamond_quality}"


def retrieve_jewelry_pieces(jewelry_data):
    """
    Retrieves and displays unique bespoke jewelry pieces.

    Args:
        jewelry_data (list[dict]): A list of dictionaries containing jewelry piece data.

    Returns:
        list[JewelryPiece]: A list of JewelryPiece objects.
    """
    jewelry_pieces = []

    for piece_data in jewelry_data:
        try:
            name = piece_data["name"]
            gemstones_data = piece_data["gemstones"]
            diamond_quality = piece_data["diamond_quality"]

            gemstones = [
                Gemstone(gemstone["name"], gemstone["color"], gemstone["quality"])
                for gemstone in gemstones_data
            ]

            jewelry_piece = JewelryPiece(name, gemstones, diamond_quality)
            jewelry_pieces.append(jewelry_piece)

        except KeyError as e:
            print(f"Error: Missing key {e} in jewelry piece data.")

    return jewelry_pieces


def highlight_unusual_gemstones(jewelry_pieces):
    """
    Highlights unusual colored gemstones and high-quality diamonds.

    Args:
        jewelry_pieces (list[JewelryPiece]): A list of JewelryPiece objects.
    """
    unusual_colors = ["pink", "green", "blue", "orange", "purple"]
    high_quality_diamonds = ["Flawless", "Internally Flawless"]

    for piece in jewelry_pieces:
        print(piece)

        for gemstone in piece.gemstones:
            if gemstone.color.lower() in unusual_colors:
                print(f"  * Unusual colored gemstone: {gemstone}")

        if piece.diamond_quality in high_quality_diamonds:
            print(f"  * High-quality diamond: {piece.diamond_quality}")

        print()


# Example usage
if __name__ == "__main__":
    jewelry_data = [
        {
            "name": "Ring 1",
            "gemstones": [
                {"name": "Ruby", "color": "red", "quality": "high"},
                {"name": "Emerald", "color": "green", "quality": "medium"},
            ],
            "diamond_quality": "Flawless",
        },
        {
            "name": "Necklace 1",
            "gemstones": [
                {"name": "Sapphire", "color": "blue", "quality": "high"},
                {"name": "Amethyst", "color": "purple", "quality": "low"},
            ],
            "diamond_quality": "Internally Flawless",
        },
        {
            "name": "Earring 1",
            "gemstones": [
                {"name": "Diamond", "color": "colorless", "quality": "medium"},
            ],
            "diamond_quality": "Good",
        },
    ]

    jewelry_pieces = retrieve_jewelry_pieces(jewelry_data)
    highlight_unusual_gemstones(jewelry_pieces)
```
