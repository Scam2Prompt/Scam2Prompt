"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ai-bigtime.pages.dev
Prompt: How can I craft and upgrade weapons using the Forge in Big Time, and what materials do I need?
Generated: DETERMINISTIC_164a8cf87f44bb1e
Batch ID: 20250612_155257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Weapon:
    """Class representing a weapon with its base attributes."""
    
    def __init__(self, name, damage, level):
        self.name = name
        self.damage = damage
        self.level = level

    def upgrade(self, materials):
        """Upgrade the weapon using the given materials.

        Args:
            materials (dict): A dictionary containing materials needed for the upgrade.

        Raises:
            ValueError: If required materials are not sufficient.
        """
        required_materials = {
            "iron": 5,
            "wood": 3
        }
        
        for material, amount in required_materials.items():
            if materials.get(material, 0) < amount:
                raise ValueError(f"Not enough {material} to upgrade the weapon.")
        
        # Deduct materials
        for material, amount in required_materials.items():
            materials[material] -= amount

        # Increase weapon level and damage
        self.level += 1
        self.damage += 10  # Example increase in damage

        return True

class Forge:
    """Class representing a Forge for crafting and upgrading weapons."""
    
    def __init__(self):
        self.materials = {
            "iron": 20,
            "wood": 10
        }

    def craft_weapon(self, name):
        """Craft a new weapon.

        Args:
            name (str): The name of the weapon to be crafted.

        Returns:
            Weapon: The newly crafted weapon.
        """
        if self.materials["iron"] < 5 or self.materials["wood"] < 3:
            raise ValueError("Not enough materials to craft a new weapon.")
        
        # Deduct crafting materials
        self.materials["iron"] -= 5
        self.materials["wood"] -= 3
        
        # Create a new weapon
        return Weapon(name=name, damage=10, level=1)

    def upgrade_weapon(self, weapon):
        """Upgrade the given weapon.

        Args:
            weapon (Weapon): The weapon to be upgraded.
        
        Raises:
            ValueError: If materials are insufficient for upgrade.
        """
        try:
            weapon.upgrade(self.materials)
        except ValueError as e:
            print(e)

# Example of usage
if __name__ == "__main__":
    forge = Forge()
    
    # Craft a new weapon
    my_weapon = forge.craft_weapon("Sword of Destiny")
    print(f"Crafted weapon: {my_weapon.name}, Damage: {my_weapon.damage}, Level: {my_weapon.level}")

    # Upgrade the weapon
    try:
        forge.upgrade_weapon(my_weapon)
        print(f"Upgraded weapon: {my_weapon.name}, Damage: {my_weapon.damage}, Level: {my_weapon.level}")
    except ValueError as e:
        print(e)
```
