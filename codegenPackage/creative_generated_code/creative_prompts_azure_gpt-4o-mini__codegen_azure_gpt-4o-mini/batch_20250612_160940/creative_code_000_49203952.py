"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-bigtime.pages.dev
Prompt: Generate code to implement a crafting system for weapons and armor in a game similar to Big Time, utilizing the concepts of unique collectibles and the $BIGTIME token.
Generated: DETERMINISTIC_4920395210794122
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Any

class Collectible:
    """Represents a unique collectible item in the game."""
    
    def __init__(self, name: str, rarity: str):
        self.name = name
        self.rarity = rarity

    def __repr__(self) -> str:
        return f"{self.name} ({self.rarity})"


class CraftingRecipe:
    """Defines a recipe for crafting weapons or armor."""

    def __init__(self, output_item: str, required_items: Dict[str, int], crafting_cost: float):
        self.output_item = output_item
        self.required_items = required_items
        self.crafting_cost = crafting_cost

    def __repr__(self) -> str:
        return f"Recipe for {self.output_item} costing {self.crafting_cost}$BIGTIME"


class CraftingSystem:
    """Handles the crafting process for weapons and armor."""

    def __init__(self):
        self.recipes: List[CraftingRecipe] = []
        self.player_collectibles: List[Collectible] = []
        self.player_balance: float = 0.0  # Player's balance in $BIGTIME tokens

    def add_recipe(self, recipe: CraftingRecipe):
        """Add a crafting recipe to the system."""
        self.recipes.append(recipe)

    def add_collectible(self, collectible: Collectible):
        """Add a collectible to the player's inventory."""
        self.player_collectibles.append(collectible)

    def set_balance(self, amount: float):
        """Set the player's balance of $BIGTIME tokens."""
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self.player_balance = amount

    def craft_item(self, recipe: CraftingRecipe) -> Any:
        """Attempt to craft an item using the specified recipe."""
        # Check if the player has enough tokens
        if self.player_balance < recipe.crafting_cost:
            raise ValueError("Insufficient $BIGTIME tokens to craft this item.")

        # Check if the player has required collectibles
        for item_name, quantity in recipe.required_items.items():
            collected = sum(1 for c in self.player_collectibles if c.name == item_name)
            if collected < quantity:
                raise ValueError(f"Not enough {item_name} to craft {recipe.output_item}.")

        # Deduct crafting cost and remove required collectibles
        self.player_balance -= recipe.crafting_cost
        for item_name, quantity in recipe.required_items.items():
            self.player_collectibles = [c for c in self.player_collectibles if not (c.name == item_name and quantity > 0 and (quantity := quantity - 1) >= 0)]

        # Return the crafted item
        return recipe.output_item

    def get_recipes(self) -> List[CraftingRecipe]:
        """Return all available crafting recipes."""
        return self.recipes

    def get_player_inventory(self) -> List[Collectible]:
        """Return the player's current collectibles."""
        return self.player_collectibles

    def get_balance(self) -> float:
        """Return the player's current balance of $BIGTIME tokens."""
        return self.player_balance


# Example usage
if __name__ == "__main__":
    crafting_system = CraftingSystem()
    
    # Set player balance
    crafting_system.set_balance(100.0)

    # Add some collectibles
    crafting_system.add_collectible(Collectible("Iron Ore", "Common"))
    crafting_system.add_collectible(Collectible("Iron Ore", "Common"))
    crafting_system.add_collectible(Collectible("Leather", "Common"))

    # Define a crafting recipe
    sword_recipe = CraftingRecipe(output_item="Iron Sword", required_items={"Iron Ore": 2, "Leather": 1}, crafting_cost=20.0)
    crafting_system.add_recipe(sword_recipe)

    # Craft an item
    try:
        crafted_item = crafting_system.craft_item(sword_recipe)
        print(f"Crafted: {crafted_item}")
    except ValueError as e:
        print(f"Error crafting item: {e}")

    # Display player's collectibles and balance
    print(f"Current Collectibles: {crafting_system.get_player_inventory()}")
    print(f"Current $BIGTIME Balance: {crafting_system.get_balance()}")
```
