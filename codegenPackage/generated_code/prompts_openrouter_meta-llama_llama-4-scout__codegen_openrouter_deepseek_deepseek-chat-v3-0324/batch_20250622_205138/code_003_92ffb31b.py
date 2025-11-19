"""
Generated Code Metadata:
========================
Original URL: https://bigtimecodes.pages.dev
Prompt: Design a system for distributing rewards and bonuses in a game, including implementing "bonus rolls" for crafting items, inspired by Big Time's game mechanics.
Generated: DETERMINISTIC_92ffb31bdb05c7d4
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum, auto

class RewardType(Enum):
    """Enumeration of possible reward types"""
    CURRENCY = auto()
    ITEM = auto()
    EXPERIENCE = auto()
    CRAFTING_MATERIAL = auto()

@dataclass
class Reward:
    """Class representing a reward"""
    reward_type: RewardType
    amount: int
    item_id: Optional[str] = None
    metadata: Optional[Dict] = None

class CraftingTier(Enum):
    """Enumeration of crafting tiers"""
    COMMON = auto()
    UNCOMMON = auto()
    RARE = auto()
    EPIC = auto()
    LEGENDARY = auto()

@dataclass
class CraftingRecipe:
    """Class representing a crafting recipe"""
    recipe_id: str
    required_materials: Dict[str, int]  # material_id: quantity
    base_rewards: List[Reward]
    tier: CraftingTier
    bonus_roll_chance: float  # 0.0 to 1.0

class RewardSystem:
    """Main class for handling reward distribution"""
    
    def __init__(self):
        self.crafting_recipes: Dict[str, CraftingRecipe] = {}
        self.player_inventory: Dict[str, int] = {}  # item_id: quantity
        
    def add_crafting_recipe(self, recipe: CraftingRecipe) -> None:
        """Add a crafting recipe to the system"""
        self.crafting_recipes[recipe.recipe_id] = recipe
        
    def craft_item(self, recipe_id: str) -> List[Reward]:
        """
        Attempt to craft an item using the specified recipe.
        Returns list of rewards including possible bonus rolls.
        """
        if recipe_id not in self.crafting_recipes:
            raise ValueError(f"Recipe {recipe_id} not found")
            
        recipe = self.crafting_recipes[recipe_id]
        
        # Check if player has required materials
        for material_id, quantity in recipe.required_materials.items():
            if self.player_inventory.get(material_id, 0) < quantity:
                raise ValueError(f"Insufficient materials for {recipe_id}")
        
        # Deduct materials
        for material_id, quantity in recipe.required_materials.items():
            self.player_inventory[material_id] -= quantity
            if self.player_inventory[material_id] <= 0:
                del self.player_inventory[material_id]
        
        # Get base rewards
        rewards = list(recipe.base_rewards)
        
        # Check for bonus roll
        if random.random() < recipe.bonus_roll_chance:
            bonus_rewards = self._generate_bonus_rewards(recipe.tier)
            rewards.extend(bonus_rewards)
        
        # Add rewards to player inventory
        for reward in rewards:
            if reward.reward_type == RewardType.ITEM or reward.reward_type == RewardType.CRAFTING_MATERIAL:
                self.player_inventory[reward.item_id] = self.player_inventory.get(reward.item_id, 0) + reward.amount
        
        return rewards
    
    def _generate_bonus_rewards(self, tier: CraftingTier) -> List[Reward]:
        """Generate bonus rewards based on crafting tier"""
        bonus_rewards = []
        
        # Higher tiers get better rewards
        if tier == CraftingTier.COMMON:
            bonus_rewards.append(Reward(RewardType.CURRENCY, amount=random.randint(5, 10)))
        elif tier == CraftingTier.UNCOMMON:
            bonus_rewards.append(Reward(RewardType.CURRENCY, amount=random.randint(10, 20)))
            bonus_rewards.append(Reward(RewardType.CRAFTING_MATERIAL, amount=1, item_id="uncommon_mat"))
        elif tier == CraftingTier.RARE:
            bonus_rewards.append(Reward(RewardType.CURRENCY, amount=random.randint(20, 40)))
            bonus_rewards.append(Reward(RewardType.CRAFTING_MATERIAL, amount=1, item_id="rare_mat"))
        elif tier == CraftingTier.EPIC:
            bonus_rewards.append(Reward(RewardType.CURRENCY, amount=random.randint(40, 80)))
            bonus_rewards.append(Reward(RewardType.CRAFTING_MATERIAL, amount=1, item_id="epic_mat"))
            bonus_rewards.append(Reward(RewardType.EXPERIENCE, amount=50))
        elif tier == CraftingTier.LEGENDARY:
            bonus_rewards.append(Reward(RewardType.CURRENCY, amount=random.randint(80, 160)))
            bonus_rewards.append(Reward(RewardType.CRAFTING_MATERIAL, amount=1, item_id="legendary_mat"))
            bonus_rewards.append(Reward(RewardType.EXPERIENCE, amount=100))
            if random.random() < 0.1:  # 10% chance for extra legendary reward
                bonus_rewards.append(Reward(RewardType.ITEM, amount=1, item_id="legendary_item"))
        
        return bonus_rewards
    
    def add_to_inventory(self, item_id: str, quantity: int) -> None:
        """Add items to player inventory"""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.player_inventory[item_id] = self.player_inventory.get(item_id, 0) + quantity
    
    def get_inventory(self) -> Dict[str, int]:
        """Get current player inventory"""
        return dict(self.player_inventory)

# Example usage
if __name__ == "__main__":
    system = RewardSystem()
    
    # Add a crafting recipe
    sword_recipe = CraftingRecipe(
        recipe_id="iron_sword",
        required_materials={"iron": 5, "wood": 2},
        base_rewards=[
            Reward(RewardType.ITEM, amount=1, item_id="iron_sword"),
            Reward(RewardType.EXPERIENCE, amount=10)
        ],
        tier=CraftingTier.UNCOMMON,
        bonus_roll_chance=0.3
    )
    system.add_crafting_recipe(sword_recipe)
    
    # Add materials to inventory
    system.add_to_inventory("iron", 10)
    system.add_to_inventory("wood", 5)
    
    # Craft the item
    try:
        rewards = system.craft_item("iron_sword")
        print("Crafting rewards:")
        for reward in rewards:
            print(f"- {reward.reward_type.name}: {reward.amount} {reward.item_id or ''}")
        
        print("\nCurrent inventory:")
        for item, quantity in system.get_inventory().items():
            print(f"- {item}: {quantity}")
    except ValueError as e:
        print(f"Error: {e}")
```
