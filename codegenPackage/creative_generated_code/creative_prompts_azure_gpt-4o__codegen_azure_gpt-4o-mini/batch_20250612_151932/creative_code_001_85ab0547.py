"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ai-bigtime.pages.dev
Prompt: Generate code to craft and upgrade weapon collectibles using the Forge system in Big Time, incorporating $BIGTIME tokens and other materials as inputs.
Generated: DETERMINISTIC_85ab0547a430aaaf
Batch ID: 20250612_151932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WeaponCollectible:
    """Class representing a weapon collectible in Big Time."""

    def __init__(self, name, level=1):
        """
        Initialize a new weapon collectible.

        :param name: Name of the weapon collectible.
        :param level: Level of the weapon, defaults to 1.
        """
        self.name = name
        self.level = level

    def __repr__(self):
        return f"{self.name} (Level: {self.level})"


class ForgeSystem:
    """Class representing the Forge system for crafting and upgrading weapon collectibles."""

    def __init__(self):
        """Initialize the Forge system."""
        self.wallet = 0  # Initialize $BIGTIME tokens
        self.materials = {}  # Store collected materials

    def add_tokens(self, amount):
        """
        Add $BIGTIME tokens to the wallet.

        :param amount: The amount of tokens to add.
        """
        if amount < 0:
            raise ValueError("Amount of tokens to add must be non-negative.")
        self.wallet += amount

    def add_material(self, material, quantity):
        """
        Add materials to the Forge system.

        :param material: The material type to add.
        :param quantity: The quantity of the material to add.
        """
        if quantity < 0:
            raise ValueError("Quantity of material must be non-negative.")
        
        if material in self.materials:
            self.materials[material] += quantity
        else:
            self.materials[material] = quantity

    def craft_weapon(self, name):
        """
        Craft a new weapon collectible.

        :param name: The name of the weapon to craft.
        :return: A new WeaponCollectible instance.
        """
        if self.wallet < 10:  # Example cost for crafting
            raise RuntimeError("Insufficient $BIGTIME tokens to craft a weapon.")
        
        # Deduct cost for crafting
        self.wallet -= 10
        return WeaponCollectible(name)

    def upgrade_weapon(self, weapon, required_materials):
        """
        Upgrade an existing weapon collectible.

        :param weapon: An instance of WeaponCollectible to upgrade.
        :param required_materials: A dictionary of materials required for the upgrade.
        :return: The upgraded WeaponCollectible instance.
        """
        # Check if enough materials are available
        for material, quantity in required_materials.items():
            if self.materials.get(material, 0) < quantity:
                raise RuntimeError(f"Insufficient materials: {material} needed: {quantity}, available: {self.materials.get(material, 0)}")

        # Check if enough $BIGTIME tokens are available for upgrading
        upgrade_cost = weapon.level * 5  # Example cost scaling with level
        if self.wallet < upgrade_cost:
            raise RuntimeError("Insufficient $BIGTIME tokens for upgrade.")

        # Deduct tokens and materials used for upgrade
        self.wallet -= upgrade_cost
        for material, quantity in required_materials.items():
            self.materials[material] -= quantity
        
        # Upgrade the weapon
        weapon.level += 1
        return weapon


# Example usage
if __name__ == '__main__':
    forge = ForgeSystem()
    forge.add_tokens(50)  # Add tokens to the forge
    forge.add_material('Iron', 5)  # Add materials
    forge.add_material('Steel', 3)

    # Craft a new weapon
    my_weapon = forge.craft_weapon('Excalibur')
    print(my_weapon)

    # Upgrade the weapon
    try:
        upgraded_weapon = forge.upgrade_weapon(my_weapon, {'Iron': 3, 'Steel': 2})
        print(upgraded_weapon)
    except RuntimeError as e:
        print(f"Error during upgrade: {e}")
```
