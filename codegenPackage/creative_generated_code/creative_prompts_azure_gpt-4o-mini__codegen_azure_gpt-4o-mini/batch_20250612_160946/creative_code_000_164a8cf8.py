"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtime-ai.pages.dev
Prompt: How can I craft and upgrade weapons using the Forge in Big Time, and what materials do I need?
Generated: DETERMINISTIC_164a8cf87f44bb1e
Batch ID: 20250612_160946
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
        """Upgrade the weapon using the provided materials."""
        if self.can_upgrade(materials):
            self.level += 1
            self.damage += self.level * 2  # Increase damage based on level
            return True
        return False

    def can_upgrade(self, materials):
        """Check if the necessary materials for upgrading are available."""
        return all(materials.get(req, 0) >= amount for req, amount in self.required_materials().items())

    def required_materials(self):
        """Define materials required for upgrading the weapon."""
        return {
            "iron_ore": 5 * self.level,
            "magic_crystal": 2 * self.level,
        }


class Forge:
    """Class representing a Forge where weapons can be crafted and upgraded."""
    
    @staticmethod
    def craft_weapon(name, base_damage):
        """Craft a new weapon."""
        # Example base level for new weapons
        return Weapon(name, base_damage, level=1)

    @staticmethod
    def upgrade_weapon(weapon, materials):
        """Upgrade the provided weapon."""
        # Attempt to upgrade the weapon and provide feedback
        if weapon.upgrade(materials):
            return f"{weapon.name} upgraded to level {weapon.level} with {weapon.damage} damage."
        else:
            return f"Upgrade failed for {weapon.name}. Check materials."


# Example Usage
if __name__ == "__main__":
    try:
        # Craft a new sword
        sword = Forge.craft_weapon("Excalibur", 10)

        # Materials needed for upgrading
        materials = {
            "iron_ore": 10,
            "magic_crystal": 4,
        }

        # Attempt to upgrade the sword
        result = Forge.upgrade_weapon(sword, materials)
        print(result)  # Output upgrade result
    except Exception as e:
        print(f"An error occurred: {e}")
```
