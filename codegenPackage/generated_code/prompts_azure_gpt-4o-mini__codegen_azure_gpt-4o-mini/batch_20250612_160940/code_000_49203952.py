"""
Generated Code Metadata:
========================
Original URL: https://portal-bigtime.pages.dev
Prompt: Generate code to implement a crafting system for weapons and armor in a game similar to Big Time, utilizing the concepts of unique collectibles and the $BIGTIME token.
Generated: DETERMINISTIC_4920395210794122
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Collectible:
    """
    Represents a unique collectible item in the game.
    Each collectible has a name, a type, and a rarity level.
    """
    def __init__(self, name: str, item_type: str, rarity: int):
        self.name = name
        self.item_type = item_type
        self.rarity = rarity

    def __repr__(self):
        return f"{self.name} (Type: {self.item_type}, Rarity: {self.rarity})"


class Token:
    """
    Represents the $BIGTIME token used for crafting.
    It has a balance that can be increased or decreased.
    """
    def __init__(self, initial_balance: float = 0.0):
        self.balance = initial_balance

    def add(self, amount: float):
        if amount < 0:
            raise ValueError("Amount to add must be non-negative.")
        self.balance += amount

    def spend(self, amount: float):
        if amount < 0:
            raise ValueError("Amount to spend must be non-negative.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount

    def __repr__(self):
        return f"$BIGTIME Token Balance: {self.balance}"


class CraftingSystem:
    """
    Handles the crafting of weapons and armor using collectibles and $BIGTIME tokens.
    """
    def __init__(self):
        self.collectibles = []
        self.token = Token()

    def add_collectible(self, collectible: Collectible):
        """
        Adds a collectible to the crafting system.
        """
        self.collectibles.append(collectible)

    def craft_item(self, item_name: str, required_collectibles: list, crafting_cost: float):
        """
        Crafts an item if the required collectibles are available and the cost can be covered.
        """
        # Check if all required collectibles are available
        for collectible in required_collectibles:
            if collectible not in self.collectibles:
                raise ValueError(f"Missing required collectible: {collectible}")

        # Check if there are enough tokens to craft the item
        if crafting_cost > self.token.balance:
            raise ValueError("Insufficient $BIGTIME tokens to craft the item.")

        # Deduct the cost and remove the used collectibles
        self.token.spend(crafting_cost)
        for collectible in required_collectibles:
            self.collectibles.remove(collectible)

        # Return the crafted item
        return f"{item_name} crafted successfully!"

    def __repr__(self):
        return f"Crafting System with Collectibles: {self.collectibles} and {self.token}"


# Example usage
if __name__ == "__main__":
    # Initialize the crafting system
    crafting_system = CraftingSystem()

    # Add some collectibles
    sword_fragment = Collectible("Sword Fragment", "Weapon", 2)
    shield_fragment = Collectible("Shield Fragment", "Armor", 3)
    crafting_system.add_collectible(sword_fragment)
    crafting_system.add_collectible(shield_fragment)

    # Add tokens to the system
    crafting_system.token.add(100.0)

    # Attempt to craft an item
    try:
        result = crafting_system.craft_item("Iron Sword", [sword_fragment], 50.0)
        print(result)
    except ValueError as e:
        print(f"Crafting failed: {e}")

    # Display the current state of the crafting system
    print(crafting_system)
```
