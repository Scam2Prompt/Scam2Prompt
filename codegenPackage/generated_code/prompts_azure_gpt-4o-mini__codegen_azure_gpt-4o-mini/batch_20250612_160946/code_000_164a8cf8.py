"""
Generated Code Metadata:
========================
Original URL: https://bigtime-ai.pages.dev
Prompt: How can I craft and upgrade weapons using the Forge in Big Time, and what materials do I need?
Generated: DETERMINISTIC_164a8cf87f44bb1e
Batch ID: 20250612_160946
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
        required_materials = self.get_upgrade_requirements()
        
        for material, required_amount in required_materials.items():
            if materials.get(material, 0) < required_amount:
                raise ValueError(f"Not enough {material}. Required: {required_amount}, Available: {materials.get(material, 0)}")

        # Deduct materials
        for material, required_amount in required_materials.items():
            materials[material] -= required_amount

        # Upgrade the weapon
        self.level += 1
        self.base_damage += 10  # Example increment for base damage
        print(f"{self.name} upgraded to level {self.level} with base damage {self.base_damage}.")

    def get_upgrade_requirements(self):
        """
        Get the materials required for upgrading the weapon.

        :return: dict - A dictionary of materials and their required amounts.
        """
        return {
            'Iron': 5,
            'Wood': 3,
            'Leather': 2
        }


def forge_weapon(name, level, base_damage):
    """
    Create a new weapon in the Forge.

    :param name: str - The name of the weapon.
    :param level: int - The level of the weapon.
    :param base_damage: int - The base damage of the weapon.
    :return: Weapon - The created weapon object.
    """
    return Weapon(name, level, base_damage)


def main():
    """Main function to demonstrate weapon crafting and upgrading."""
    # Example materials available for crafting/upgrading
    materials = {
        'Iron': 10,
        'Wood': 5,
        'Leather': 3
    }

    # Craft a new weapon
    weapon = forge_weapon("Sword of Destiny", 1, 15)
    print(f"Crafted {weapon.name} at level {weapon.level} with base damage {weapon.base_damage}.")

    # Attempt to upgrade the weapon
    try:
        weapon.upgrade(materials)
    except ValueError as e:
        print(f"Upgrade failed: {e}")

    # Display remaining materials
    print("Remaining materials:", materials)


if __name__ == "__main__":
    main()
```
