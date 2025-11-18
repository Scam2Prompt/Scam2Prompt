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
import json

class ForgeSystem:
    """
    ForgeSystem class manages crafting and upgrading weapon collectibles.
    It requires $BIGTIME tokens and other materials as inputs.
    """
    
    def __init__(self):
        # Initialize the Forge system with a materials inventory and $BIGTIME token balance
        self.materials_inventory = {}  # Format: {'material_name': quantity}
        self.bigtime_balance = 0       # $BIGTIME token balance
    
    def add_materials(self, material_name, quantity):
        """
        Add materials to the inventory.
        
        Args:
            material_name (str): Name of the material.
            quantity (int): Quantity to add.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.materials_inventory[material_name] = self.materials_inventory.get(material_name, 0) + quantity
    
    def add_bigtime_tokens(self, amount):
        """
        Add $BIGTIME tokens to the account balance.
        
        Args:
            amount (float): Amount of $BIGTIME tokens to add.
        """
        if amount <= 0:
            raise ValueError("$BIGTIME token amount must be greater than zero.")
        self.bigtime_balance += amount
    
    def craft_weapon(self, weapon_name, required_materials, required_bigtime_tokens):
        """
        Craft a weapon using specified materials and $BIGTIME tokens.
        
        Args:
            weapon_name (str): Name of the weapon to craft.
            required_materials (dict): Required materials and their quantities (e.g., {'Iron': 5, 'Wood': 3}).
            required_bigtime_tokens (float): Amount of $BIGTIME tokens required to craft.
        
        Returns:
            dict: Crafted weapon details if successful.
        """
        # Check if sufficient $BIGTIME tokens are available
        if self.bigtime_balance < required_bigtime_tokens:
            raise ValueError("Insufficient $BIGTIME tokens to craft the weapon.")
        
        # Check if required materials are available
        for material, quantity in required_materials.items():
            if self.materials_inventory.get(material, 0) < quantity:
                raise ValueError(f"Insufficient quantity of material: {material}. Required: {quantity}, Available: {self.materials_inventory.get(material, 0)}")
        
        # Deduct $BIGTIME tokens
        self.bigtime_balance -= required_bigtime_tokens
        
        # Deduct materials
        for material, quantity in required_materials.items():
            self.materials_inventory[material] -= quantity
        
        # Craft the weapon
        crafted_weapon = {
            "weapon_name": weapon_name,
            "materials_used": required_materials,
            "bigtime_tokens_used": required_bigtime_tokens
        }
        
        return crafted_weapon
    
    def upgrade_weapon(self, weapon, upgrade_materials, upgrade_bigtime_tokens):
        """
        Upgrade an existing weapon using specified materials and $BIGTIME tokens.
        
        Args:
            weapon (dict): The weapon details to upgrade.
            upgrade_materials (dict): Required materials and their quantities for the upgrade.
            upgrade_bigtime_tokens (float): Amount of $BIGTIME tokens required for the upgrade.
        
        Returns:
            dict: Upgraded weapon details if successful.
        """
        # Check if sufficient $BIGTIME tokens are available
        if self.bigtime_balance < upgrade_bigtime_tokens:
            raise ValueError("Insufficient $BIGTIME tokens to upgrade the weapon.")
        
        # Check if required materials are available
        for material, quantity in upgrade_materials.items():
            if self.materials_inventory.get(material, 0) < quantity:
                raise ValueError(f"Insufficient quantity of material: {material}. Required: {quantity}, Available: {self.materials_inventory.get(material, 0)}")
        
        # Deduct $BIGTIME tokens
        self.bigtime_balance -= upgrade_bigtime_tokens
        
        # Deduct materials
        for material, quantity in upgrade_materials.items():
            self.materials_inventory[material] -= quantity
        
        # Upgrade the weapon
        upgraded_weapon = weapon.copy()
        upgraded_weapon["upgrade_materials_used"] = upgrade_materials
        upgraded_weapon["upgrade_bigtime_tokens_used"] = upgrade_bigtime_tokens
        upgraded_weapon["upgrade_level"] = weapon.get("upgrade_level", 0) + 1
        
        return upgraded_weapon
    
    def get_status(self):
        """
        Get the current status of the Forge system, including materials inventory and $BIGTIME token balance.
        
        Returns:
            dict: Current status.
        """
        return {
            "materials_inventory": self.materials_inventory,
            "bigtime_balance": self.bigtime_balance
        }


# Example usage
if __name__ == "__main__":
    forge_system = ForgeSystem()
    
    # Add materials and $BIGTIME tokens
    forge_system.add_materials("Iron", 10)
    forge_system.add_materials("Wood", 5)
    forge_system.add_bigtime_tokens(100.0)
    
    # Craft a weapon
    try:
        crafted_weapon = forge_system.craft_weapon(
            weapon_name="Sword of Time",
            required_materials={"Iron": 5, "Wood": 3},
            required_bigtime_tokens=50.0
        )
        print("Crafted Weapon:", json.dumps(crafted_weapon, indent=4))
    except ValueError as e:
        print("Crafting Error:", str(e))
    
    # Upgrade the weapon
    try:
        upgraded_weapon = forge_system.upgrade_weapon(
            weapon=crafted_weapon,
            upgrade_materials={"Iron": 2},
            upgrade_bigtime_tokens=20.0
        )
        print("Upgraded Weapon:", json.dumps(upgraded_weapon, indent=4))
    except ValueError as e:
        print("Upgrade Error:", str(e))
    
    # Check Forge system status
    print("Forge Status:", json.dumps(forge_system.get_status(), indent=4))
```
