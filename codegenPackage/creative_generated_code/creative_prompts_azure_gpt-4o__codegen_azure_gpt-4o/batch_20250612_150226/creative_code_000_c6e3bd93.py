"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtime-codes.pages.dev
Prompt: Write a Python script to simulate crafting weapons and armor cosmetics in "Big Time" using $BIGTIME tokens and other materials, referencing the Forge and Armory systems described on the website.
Generated: DETERMINISTIC_c6e3bd93f0360d30
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class ForgeAndArmory:
    """
    Simulates crafting weapons and armor cosmetics using $BIGTIME tokens and other materials.
    """
    
    def __init__(self):
        # Initialize required materials and token balances
        self.bigtime_tokens = 100  # Example token balance
        self.materials = {'iron': 10, 'wood': 10, 'gem': 5}  # Example material inventory
    
    def check_materials(self, required_materials):
        """
        Check if the user has enough materials to craft the item.
        """
        for material, amount in required_materials.items():
            if self.materials.get(material, 0) < amount:
                return False
        return True
    
    def deduct_materials(self, required_materials):
        """
        Deduct the required materials from the inventory.
        """
        for material, amount in required_materials.items():
            self.materials[material] -= amount
    
    def craft_item(self, item_type, bigtime_cost, required_materials):
        """
        Craft a weapon or armor cosmetic.
        
        Args:
            item_type (str): Type of item to craft ('weapon' or 'armor').
            bigtime_cost (int): Cost in $BIGTIME tokens.
            required_materials (dict): Materials required for crafting.
        
        Returns:
            dict: Result of the crafting attempt.
        """
        if self.bigtime_tokens < bigtime_cost:
            return {"success": False, "message": "Insufficient $BIGTIME tokens."}
        
        if not self.check_materials(required_materials):
            return {"success": False, "message": "Insufficient crafting materials."}
        
        # Deduct tokens and materials
        self.bigtime_tokens -= bigtime_cost
        self.deduct_materials(required_materials)
        
        # Simulate crafting success with a random chance
        crafting_success = random.random() < 0.8  # 80% success rate
        
        if crafting_success:
            return {"success": True, "message": f"Successfully crafted {item_type}!"}
        else:
            return {"success": False, "message": f"Crafting {item_type} failed. Try again."}


# Example usage
if __name__ == "__main__":
    forge = ForgeAndArmory()
    
    # Define crafting requirements
    weapon_requirements = {'iron': 5, 'wood': 3}
    armor_requirements = {'iron': 3, 'gem': 2}
    
    # Attempt to craft a weapon
    weapon_result = forge.craft_item(item_type="weapon", bigtime_cost=20, required_materials=weapon_requirements)
    print(weapon_result)
    
    # Attempt to craft armor
    armor_result = forge.craft_item(item_type="armor", bigtime_cost=15, required_materials=armor_requirements)
    print(armor_result)
    
    # Check remaining tokens and materials
    print(f"Remaining BIGTIME tokens: {forge.bigtime_tokens}")
    print(f"Remaining materials: {forge.materials}")
```
