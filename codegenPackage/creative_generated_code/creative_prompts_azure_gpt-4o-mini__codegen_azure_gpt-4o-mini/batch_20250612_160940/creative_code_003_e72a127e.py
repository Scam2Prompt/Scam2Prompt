"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-bigtime.pages.dev
Prompt: Develop a function to handle the crafting and upgrading of items using materials and the $BIGTIME token, similar to the Forge and Armory systems in Big Time.
Generated: DETERMINISTIC_e72a127eae775523
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Item:
    """Class to represent an item with a name, level, and required materials for crafting/upgrade."""
    
    def __init__(self, name: str, level: int, required_materials: dict):
        self.name = name
        self.level = level
        self.required_materials = required_materials

    def __repr__(self):
        return f"Item(name={self.name}, level={self.level})"


class CraftingSystem:
    """Class to handle crafting and upgrading of items using materials and $BIGTIME tokens."""
    
    def __init__(self, bigtime_tokens: int):
        self.bigtime_tokens = bigtime_tokens

    def craft_item(self, item: Item, available_materials: dict) -> str:
        """
        Craft an item if the player has enough materials and tokens.

        Parameters:
        - item (Item): The item to craft.
        - available_materials (dict): A dictionary of materials available to the player.

        Returns:
        - str: Success or failure message.
        """
        
        # Check if player has enough materials
        for material, quantity in item.required_materials.items():
            if available_materials.get(material, 0) < quantity:
                return f"Insufficient {material}. Required: {quantity}, Available: {available_materials.get(material, 0)}."

        # Check if player has enough $BIGTIME tokens
        upgrade_cost = 100  # Example cost for crafting an item
        if self.bigtime_tokens < upgrade_cost:
            return "Insufficient $BIGTIME tokens for crafting."

        # Perform crafting
        for material, quantity in item.required_materials.items():
            available_materials[material] -= quantity
        
        self.bigtime_tokens -= upgrade_cost
        return f"{item.name} crafted successfully!"

    def upgrade_item(self, item: Item, available_materials: dict) -> str:
        """
        Upgrade an item if the player has enough materials and tokens.

        Parameters:
        - item (Item): The item to upgrade.
        - available_materials (dict): A dictionary of materials available to the player.

        Returns:
        - str: Success or failure message.
        """
        
        # Check if player has enough materials
        upgrade_materials = {material: quantity + 1 for material, quantity in item.required_materials.items()}
        
        for material, quantity in upgrade_materials.items():
            if available_materials.get(material, 0) < quantity:
                return f"Insufficient {material}. Required: {quantity}, Available: {available_materials.get(material, 0)}."

        # Check if player has enough $BIGTIME tokens
        upgrade_cost = 200  # Example cost for upgrading an item
        if self.bigtime_tokens < upgrade_cost:
            return "Insufficient $BIGTIME tokens for upgrading."

        # Perform upgrading
        for material, quantity in upgrade_materials.items():
            available_materials[material] -= quantity
        
        item.level += 1
        self.bigtime_tokens -= upgrade_cost
        return f"{item.name} upgraded to level {item.level} successfully!"


# Example usage
if __name__ == "__main__":
    # Initialize available materials and tokens
    available_materials = {'wood': 10, 'metal': 5, 'fabric': 8}
    bigtime_tokens = 500
    
    # Create a crafting system
    crafting_system = CraftingSystem(bigtime_tokens)

    # Create an item to craft
    sword = Item(name="Sword of Destiny", level=1, required_materials={'wood': 2, 'metal': 3})

    # Attempt to craft the item
    print(crafting_system.craft_item(sword, available_materials))
    
    # Attempt to upgrade the item
    print(crafting_system.upgrade_item(sword, available_materials))
```
