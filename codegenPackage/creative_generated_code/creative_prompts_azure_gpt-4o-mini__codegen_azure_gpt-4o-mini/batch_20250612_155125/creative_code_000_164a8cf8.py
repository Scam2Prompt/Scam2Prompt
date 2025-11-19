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

```python
class Weapon:
    """Class representing a weapon with its base attributes."""
    
    def __init__(self, name, damage, level):
        self.name = name
        self.damage = damage
        self.level = level

    def upgrade(self, materials):
        """Upgrade the weapon using specified materials."""
        # Check if the necessary materials are available
        if self.can_upgrade(materials):
            self.level += 1
            self.damage += 10  # Increment damage for simplicity
            print(f"{self.name} upgraded to level {self.level} with increased damage of {self.damage}!")
        else:
            print(f"Upgrade failed: not enough materials to upgrade {self.name}.")

    def can_upgrade(self, materials):
        """Check if the weapon can be upgraded with the given materials."""
        required_materials = {"iron": 5, "gem": 2}  # Example materials needed for upgrade
        for mat, qty in required_materials.items():
            if materials.get(mat, 0) < qty:
                return False
        return True


class Forge:
    """Class representing the Forge where weapons can be crafted and upgraded."""
    
    def __init__(self):
        self.weapons = []

    def craft_weapon(self, name, materials):
        """Craft a new weapon if materials are sufficient."""
        # Example crafting requirements
        required_materials = {"iron": 10, "gem": 3}
        
        if self.can_craft(materials, required_materials):
            new_weapon = Weapon(name, damage=20, level=1)  # Initial values for a new weapon
            self.weapons.append(new_weapon)
            print(f"{name} crafted successfully!")
        else:
            print(f"Crafting failed: not enough materials to craft {name}.")

    def can_craft(self, materials, required_materials):
        """Check if the necessary materials are available to craft a weapon."""
        for mat, qty in required_materials.items():
            if materials.get(mat, 0) < qty:
                return False
        return True


def main():
    """Main function to demonstrate crafting and upgrading weapons."""
    # Sample materials available for crafting/upgrading
    materials = {
        "iron": 15,
        "gem": 5
    }
    
    # Create a forge instance
    forge = Forge()

    # Craft a new weapon
    forge.craft_weapon("Sword of Destiny", materials)
    
    # Upgrade the crafted weapon
    if forge.weapons:  # Check if any weapons were crafted
        crafted_weapon = forge.weapons[0]
        crafted_weapon.upgrade(materials)

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
```
