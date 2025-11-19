"""
Generated Code Metadata:
========================
Original URL: https://bigtimecodes.pages.dev
Prompt: How can I craft and upgrade weapons using the Forge in Big Time, and what materials do I need?
Generated: DETERMINISTIC_164a8cf87f44bb1e
Batch ID: 20250612_155125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Weapon:
    """Class representing a weapon in the game."""
    
    def __init__(self, name, level, base_damage):
        """
        Initialize a new weapon.

        :param name: str - The name of the weapon.
        :param level: int - The level of the weapon.
        :param base_damage: int - The base damage of the weapon.
        """
        self.name = name
        self.level = level
        self.base_damage = base_damage

    def upgrade(self, materials):
        """
        Upgrade the weapon using specified materials.

        :param materials: dict - A dictionary of materials required for the upgrade.
        :raises ValueError: If required materials are not sufficient.
        """
        required_materials = self.get_required_materials()
        
        for material, required_amount in required_materials.items():
            if materials.get(material, 0) < required_amount:
                raise ValueError(f"Insufficient {material}. Required: {required_amount}, Available: {materials.get(material, 0)}")

        # Proceed with the upgrade
        self.level += 1
        self.base_damage += 10  # Example increment
        print(f"{self.name} upgraded to level {self.level} with base damage {self.base_damage}.")

    def get_required_materials(self):
        """
        Get the materials required for upgrading the weapon.

        :return: dict - A dictionary of required materials and their amounts.
        """
        return {
            'Iron Ore': 5,
            'Wood': 3,
            'Leather': 2
        }


class Forge:
    """Class representing the Forge where weapons can be crafted and upgraded."""
    
    @staticmethod
    def craft_weapon(name, level, base_damage):
        """
        Craft a new weapon.

        :param name: str - The name of the weapon.
        :param level: int - The level of the weapon.
        :param base_damage: int - The base damage of the weapon.
        :return: Weapon - The crafted weapon object.
        """
        return Weapon(name, level, base_damage)

    @staticmethod
    def upgrade_weapon(weapon, materials):
        """
        Upgrade a weapon using the Forge.

        :param weapon: Weapon - The weapon to be upgraded.
        :param materials: dict - A dictionary of materials available for the upgrade.
        """
        try:
            weapon.upgrade(materials)
        except ValueError as e:
            print(f"Upgrade failed: {e}")


# Example usage
if __name__ == "__main__":
    # Craft a new weapon
    my_weapon = Forge.craft_weapon("Sword of Destiny", 1, 20)

    # Define available materials for upgrading
    available_materials = {
        'Iron Ore': 5,
        'Wood': 3,
        'Leather': 2
    }

    # Upgrade the weapon
    Forge.upgrade_weapon(my_weapon, available_materials)
```
