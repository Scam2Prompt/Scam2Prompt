"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtimecodes.pages.dev
Prompt: How can I craft and upgrade weapons using the Forge in Big Time, and what materials do I need?
Generated: DETERMINISTIC_164a8cf87f44bb1e
Batch ID: 20250612_155125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is an example Python code for a simplified weapon crafting and upgrading system. This code follows best practices, is well-documented, and includes error handling.

```python
import random

class Forge:
    """
    A class to represent the Forge for crafting and upgrading weapons.
    """
    def __init__(self):
        # Initialize available materials in the Forge
        self.materials = {
            "Iron": 10,
            "Wood": 15,
            "Steel": 5,
            "Gold": 1,
            "Magic Essence": 3
        }
        self.weapons = []  # List to store crafted weapons

    def display_materials(self):
        """
        Display the available materials in the Forge.
        """
        print("Available Materials:")
        for material, quantity in self.materials.items():
            print(f"{material}: {quantity}")

    def craft_weapon(self, weapon_name, required_materials):
        """
        Craft a weapon using the specified materials.

        Args:
            weapon_name (str): The name of the weapon to craft.
            required_materials (dict): Materials needed to craft the weapon.
        """
        # Check if required materials are available
        try:
            for material, quantity in required_materials.items():
                if self.materials.get(material, 0) < quantity:
                    raise ValueError(f"Not enough {material}. Required: {quantity}, Available: {self.materials.get(material, 0)}")

            # Deduct materials and craft the weapon
            for material, quantity in required_materials.items():
                self.materials[material] -= quantity

            self.weapons.append({"name": weapon_name, "level": 1})
            print(f"Weapon '{weapon_name}' crafted successfully!")

        except ValueError as e:
            print(f"Error crafting weapon: {e}")

    def upgrade_weapon(self, weapon_name, upgrade_material):
        """
        Upgrade a weapon using the specified material.

        Args:
            weapon_name (str): The name of the weapon to upgrade.
            upgrade_material (str): The material needed for upgrading.
        """
        try:
            # Find the weapon in the list
            weapon = next((w for w in self.weapons if w['name'] == weapon_name), None)

            if not weapon:
                raise ValueError(f"Weapon '{weapon_name}' not found.")

            # Check if enough upgrade material is available
            if self.materials.get(upgrade_material, 0) < 1:
                raise ValueError(f"Not enough {upgrade_material} for upgrading. Required: 1, Available: {self.materials.get(upgrade_material, 0)}")

            # Deduct material and upgrade the weapon
            self.materials[upgrade_material] -= 1
            weapon['level'] += 1
            print(f"Weapon '{weapon_name}' upgraded to level {weapon['level']}!")

        except ValueError as e:
            print(f"Error upgrading weapon: {e}")

    def list_weapons(self):
        """
        List all crafted weapons and their levels.
        """
        if not self.weapons:
            print("No weapons have been crafted yet.")
        else:
            print("Crafted Weapons:")
            for weapon in self.weapons:
                print(f"Name: {weapon['name']}, Level: {weapon['level']}")


# Example Usage:
if __name__ == "__main__":
    forge = Forge()

    # Display available materials
    forge.display_materials()

    # Craft a weapon
    forge.craft_weapon("Sword of Flames", {"Iron": 3, "Wood": 2, "Magic Essence": 1})

    # List crafted weapons
    forge.list_weapons()

    # Upgrade a weapon
    forge.upgrade_weapon("Sword of Flames", "Magic Essence")

    # List weapons after upgrade
    forge.list_weapons()

    # Try to upgrade with insufficient materials
    forge.upgrade_weapon("Sword of Flames", "Gold")

    # Display remaining materials
    forge.display_materials()
```

This code is ready to run and can be extended further to fit specific game logic.
