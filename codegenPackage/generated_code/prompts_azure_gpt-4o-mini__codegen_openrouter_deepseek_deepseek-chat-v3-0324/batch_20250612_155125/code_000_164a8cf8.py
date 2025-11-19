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
# Forge system for crafting and upgrading weapons in Big Time

class Weapon:
    """Represents a weapon in the game."""
    def __init__(self, name, base_damage, rarity, level=1):
        self.name = name
        self.base_damage = base_damage
        self.rarity = rarity  # Common, Uncommon, Rare, Epic, Legendary
        self.level = level
        self.current_damage = self.calculate_damage()
    
    def calculate_damage(self):
        """Calculate weapon damage based on level and rarity."""
        rarity_multiplier = {
            'Common': 1.0,
            'Uncommon': 1.2,
            'Rare': 1.5,
            'Epic': 1.8,
            'Legendary': 2.2
        }
        return self.base_damage * rarity_multiplier[self.rarity] * (1 + (self.level - 1) * 0.1)
    
    def __str__(self):
        return f"{self.name} (Lvl {self.level} {self.rarity}): {self.current_damage:.1f} damage"

class Forge:
    """Handles weapon crafting and upgrading."""
    def __init__(self):
        self.recipes = {
            'Sword': {
                'materials': {'Iron': 5, 'Coal': 2},
                'base_damage': 10,
                'rarity': 'Common'
            },
            'Axe': {
                'materials': {'Iron': 7, 'Coal': 3},
                'base_damage': 15,
                'rarity': 'Common'
            },
            'Bow': {
                'materials': {'Wood': 10, 'String': 3},
                'base_damage': 12,
                'rarity': 'Common'
            }
        }
        
        self.upgrade_costs = {
            'Common': {'Iron': 3, 'Coal': 1},
            'Uncommon': {'Iron': 5, 'Mithril': 2},
            'Rare': {'Mithril': 5, 'Crystal': 1},
            'Epic': {'Crystal': 3, 'Dragon Scale': 1},
            'Legendary': {'Dragon Scale': 3, 'Star Metal': 1}
        }
    
    def craft_weapon(self, weapon_type, inventory):
        """Craft a new weapon if materials are available."""
        if weapon_type not in self.recipes:
            raise ValueError(f"Unknown weapon type: {weapon_type}")
        
        recipe = self.recipes[weapon_type]
        
        # Check if player has enough materials
        for material, amount in recipe['materials'].items():
            if inventory.get(material, 0) < amount:
                raise ValueError(f"Not enough {material} to craft {weapon_type}")
        
        # Deduct materials from inventory
        for material, amount in recipe['materials'].items():
            inventory[material] -= amount
        
        # Create and return new weapon
        return Weapon(
            name=weapon_type,
            base_damage=recipe['base_damage'],
            rarity=recipe['rarity']
        )
    
    def upgrade_weapon(self, weapon, inventory):
        """Upgrade a weapon if materials are available."""
        if weapon.rarity not in self.upgrade_costs:
            raise ValueError(f"Cannot upgrade {weapon.rarity} weapons")
        
        cost = self.upgrade_costs[weapon.rarity]
        
        # Check if player has enough materials
        for material, amount in cost.items():
            if inventory.get(material, 0) < amount:
                raise ValueError(f"Not enough {material} to upgrade {weapon.name}")
        
        # Deduct materials from inventory
        for material, amount in cost.items():
            inventory[material] -= amount
        
        # Upgrade the weapon
        weapon.level += 1
        weapon.current_damage = weapon.calculate_damage()
        
        # Check for rarity upgrade
        if weapon.level % 5 == 0:
            rarities = list(self.upgrade_costs.keys())
            current_index = rarities.index(weapon.rarity)
            if current_index < len(rarities) - 1:
                weapon.rarity = rarities[current_index + 1]
        
        return weapon

# Example usage
if __name__ == "__main__":
    # Initialize forge and player inventory
    forge = Forge()
    inventory = {
        'Iron': 20,
        'Coal': 10,
        'Wood': 15,
        'String': 5,
        'Mithril': 8,
        'Crystal': 3,
        'Dragon Scale': 1,
        'Star Metal': 0
    }
    
    try:
        # Craft a sword
        sword = forge.craft_weapon('Sword', inventory)
        print(f"Crafted: {sword}")
        
        # Upgrade the sword multiple times
        for _ in range(6):
            sword = forge.upgrade_weapon(sword, inventory)
            print(f"Upgraded: {sword}")
            
    except ValueError as e:
        print(f"Error: {e}")
```
