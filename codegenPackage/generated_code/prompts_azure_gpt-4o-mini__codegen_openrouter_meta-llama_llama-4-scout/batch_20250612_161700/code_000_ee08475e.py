"""
Generated Code Metadata:
========================
Original URL: https://geddesign.it
Prompt: Generate a code snippet for an e-commerce website that showcases high-quality, restored furniture, focusing on antique seating with modern upholstery.
Generated: DETERMINISTIC_ee08475e0ab51f99
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# furniture.py

class Furniture:
    def __init__(self, id, name, description, price, upholstery):
        """
        Initialize a Furniture object.

        Args:
            id (int): Unique identifier for the furniture piece.
            name (str): Name of the furniture piece.
            description (str): Description of the furniture piece.
            price (float): Price of the furniture piece.
            upholstery (str): Type of upholstery used.
        """
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.upholstery = upholstery

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class AntiqueSeating(Furniture):
    def __init__(self, id, name, description, price, upholstery, era):
        """
        Initialize an AntiqueSeating object.

        Args:
            id (int): Unique identifier for the furniture piece.
            name (str): Name of the furniture piece.
            description (str): Description of the furniture piece.
            price (float): Price of the furniture piece.
            upholstery (str): Type of upholstery used.
            era (str): Era in which the furniture piece was created.
        """
        super().__init__(id, name, description, price, upholstery)
        self.era = era

    def __str__(self):
        return f"{self.name} ({self.era}) - ${self.price:.2f}"


class FurnitureStore:
    def __init__(self):
        """
        Initialize a FurnitureStore object.
        """
        self.furniture = []

    def add_furniture(self, furniture):
        """
        Add a furniture piece to the store.

        Args:
            furniture (Furniture): Furniture piece to add.
        """
        self.furniture.append(furniture)

    def get_furniture(self, id):
        """
        Get a furniture piece by its ID.

        Args:
            id (int): ID of the furniture piece.

        Returns:
            Furniture: Furniture piece with the given ID, or None if not found.
        """
        for furniture in self.furniture:
            if furniture.id == id:
                return furniture
        return None

    def display_furniture(self):
        """
        Display all furniture pieces in the store.
        """
        for furniture in self.furniture:
            print(furniture)


def main():
    try:
        # Create a furniture store
        store = FurnitureStore()

        # Create some antique seating pieces
        chair1 = AntiqueSeating(1, "Victorian Armchair", "A beautifully restored Victorian armchair with modern upholstery.", 1200.0, "Velvet", "Victorian")
        chair2 = AntiqueSeating(2, "Art Deco Chair", "A stylish Art Deco chair with sleek lines and modern upholstery.", 900.0, "Leather", "Art Deco")
        sofa = AntiqueSeating(3, "Antique Sofa", "A fully restored antique sofa with plush modern upholstery.", 2500.0, "Cotton", "Antique")

        # Add furniture pieces to the store
        store.add_furniture(chair1)
        store.add_furniture(chair2)
        store.add_furniture(sofa)

        # Display all furniture pieces
        print("Furniture Pieces:")
        store.display_furniture()

        # Get a furniture piece by its ID
        furniture_id = 2
        furniture = store.get_furniture(furniture_id)
        if furniture:
            print(f"\nFurniture Piece {furniture_id}:")
            print(furniture)
            print(f"Description: {furniture.description}")
            print(f"Upholstery: {furniture.upholstery}")
            if isinstance(furniture, AntiqueSeating):
                print(f"Era: {furniture.era}")
        else:
            print(f"\nFurniture piece with ID {furniture_id} not found.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
