"""
Generated Code Metadata:
========================
Original URL: https://bigtime-codes.pages.dev
Prompt: What are the steps to craft unique armor pieces using the Armory in Big Time?
Generated: DETERMINISTIC_9b39b131e1f5c113
Batch ID: 20250612_164304
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
    A class to represent an armor piece in the Big Time game.
    """

    def __init__(self, name, material, defense_rating):
        """
        Initializes an ArmorPiece instance.

        :param name: str - The name of the armor piece.
        :param material: str - The material used to craft the armor.
        :param defense_rating: int - The defense rating of the armor piece.
        """
        self.name = name
        self.material = material
        self.defense_rating = defense_rating

    def __str__(self):
        """
        Returns a string representation of the armor piece.
        """
        return f"{self.name} (Material: {self.material}, Defense: {self.defense_rating})"


class Armory:
    """
    A class to represent the Armory where armor pieces can be crafted.
    """

    def __init__(self):
        """
        Initializes the Armory with an empty inventory of armor pieces.
        """
        self.inventory = []

    def craft_armor(self, name, material, defense_rating):
        """
        Crafts a new armor piece and adds it to the inventory.

        :param name: str - The name of the armor piece.
        :param material: str - The material used to craft the armor.
        :param defense_rating: int - The defense rating of the armor piece.
        :raises ValueError: If defense_rating is not a positive integer.
        """
        if defense_rating <= 0:
            raise ValueError("Defense rating must be a positive integer.")

        new_armor = ArmorPiece(name, material, defense_rating)
        self.inventory.append(new_armor)
        print(f"Crafted: {new_armor}")

    def show_inventory(self):
        """
        Displays the current inventory of armor pieces.
        """
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for armor in self.inventory:
                print(armor)


def main():
    """
    Main function to demonstrate the crafting of unique armor pieces.
    """
    armory = Armory()

    try:
        # Crafting unique armor pieces
        armory.craft_armor("Dragon Scale Armor", "Dragon Scales", 150)
        armory.craft_armor("Knight's Plate", "Steel", 100)
        armory.craft_armor("Elven Leather", "Leather", 75)

        # Display the inventory
        armory.show_inventory()

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
