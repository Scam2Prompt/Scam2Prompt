"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtime-codes.pages.dev
Prompt: What are the steps to craft unique armor pieces using the Armory in Big Time?
Generated: DETERMINISTIC_9b39b131e1f5c113
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BigTimeArmory:
    """
    A class to represent the Armory in the game Big Time for crafting unique armor pieces.
    """

    def __init__(self):
        """
        Initialize the Armory with an empty inventory and recipes.
        """
        self.inventory = {}
        self.recipes = {
            'basic_armor': {'materials': {'leather': 5, 'iron': 3}, 'crafted_item': 'Basic Armor'},
            'advanced_armor': {'materials': {'leather': 10, 'iron': 5, 'steel': 2}, 'crafted_item': 'Advanced Armor'}
        }

    def add_material(self, material, quantity):
        """
        Add materials to the inventory.

        :param material: The type of material to be added (str)
        :param quantity: The quantity of the material (int)
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        self.inventory[material] = self.inventory.get(material, 0) + quantity

    def craft_armor(self, recipe_name):
        """
        Craft an armor piece using the specified recipe if materials are available.

        :param recipe_name: The name of the recipe to be used (str)
        :return: The crafted armor piece or an error message (str)
        """
        if recipe_name not in self.recipes:
            return f"Recipe '{recipe_name}' does not exist."

        recipe = self.recipes[recipe_name]
        materials_needed = recipe['materials']
        
        # Check if all materials are available
        for material, required_quantity in materials_needed.items():
            if self.inventory.get(material, 0) < required_quantity:
                return f"Insufficient materials: {material} needed {required_quantity}, available {self.inventory.get(material, 0)}."
        
        # Deduct materials from inventory and craft the item
        for material, required_quantity in materials_needed.items():
            self.inventory[material] -= required_quantity
        
        return f"Crafted: {recipe['crafted_item']}"

    def check_inventory(self):
        """
        Display the current inventory of materials.

        :return: Current inventory (dict)
        """
        return self.inventory


# Example usage
if __name__ == "__main__":
    armory = BigTimeArmory()

    # Adding materials to the inventory
    armory.add_material('leather', 10)
    armory.add_material('iron', 5)
    armory.add_material('steel', 2)

    # Crafting armor pieces
    print(armory.craft_armor('basic_armor'))  # Should succeed
    print(armory.craft_armor('advanced_armor'))  # Should succeed
    print(armory.craft_armor('advanced_armor'))  # Should fail due to insufficient materials

    # Check remaining inventory
    print(armory.check_inventory())
```
