"""
Generated Code Metadata:
========================
Original URL: https://wsgg.pages.dev
Prompt: Provide an example of how to display a user's inventory and rewards in a game interface, inspired by the Wall Street Games platform.
Generated: DETERMINISTIC_bdfaa6e9456ef577
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class InventoryItem:
    """Represents an item in the user's inventory."""
    def __init__(self, item_id: str, name: str, quantity: int, rarity: str):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.rarity = rarity

    def to_dict(self) -> Dict:
        """Convert the item to a dictionary for serialization."""
        return {
            'item_id': self.item_id,
            'name': self.name,
            'quantity': self.quantity,
            'rarity': self.rarity
        }

class Reward:
    """Represents a reward the user has earned."""
    def __init__(self, reward_id: str, name: str, points: int, is_claimed: bool):
        self.reward_id = reward_id
        self.name = name
        self.points = points
        self.is_claimed = is_claimed

    def to_dict(self) -> Dict:
        """Convert the reward to a dictionary for serialization."""
        return {
            'reward_id': self.reward_id,
            'name': self.name,
            'points': self.points,
            'is_claimed': self.is_claimed
        }

class UserInventory:
    """Manages the user's inventory and rewards."""
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.inventory: List[InventoryItem] = []
        self.rewards: List[Reward] = []

    def add_item(self, item: InventoryItem) -> None:
        """Add an item to the inventory."""
        self.inventory.append(item)

    def add_reward(self, reward: Reward) -> None:
        """Add a reward to the user's rewards."""
        self.rewards.append(reward)

    def claim_reward(self, reward_id: str) -> bool:
        """Mark a reward as claimed."""
        for reward in self.rewards:
            if reward.reward_id == reward_id and not reward.is_claimed:
                reward.is_claimed = True
                return True
        return False

    def get_inventory_json(self) -> str:
        """Return the inventory as a JSON string."""
        inventory_data = [item.to_dict() for item in self.inventory]
        return json.dumps({'inventory': inventory_data}, indent=2)

    def get_rewards_json(self) -> str:
        """Return the rewards as a JSON string."""
        rewards_data = [reward.to_dict() for reward in self.rewards]
        return json.dumps({'rewards': rewards_data}, indent=2)

    def save_to_file(self, filename: str) -> bool:
        """Save the inventory and rewards to a file."""
        try:
            data = {
                'user_id': self.user_id,
                'inventory': [item.to_dict() for item in self.inventory],
                'rewards': [reward.to_dict() for reward in self.rewards]
            }
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving inventory: {e}")
            return False

    @classmethod
    def load_from_file(cls, filename: str) -> Optional['UserInventory']:
        """Load inventory and rewards from a file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            user_inventory = cls(data['user_id'])
            for item_data in data['inventory']:
                user_inventory.add_item(InventoryItem(**item_data))
            for reward_data in data['rewards']:
                user_inventory.add_reward(Reward(**reward_data))
            return user_inventory
        except Exception as e:
            print(f"Error loading inventory: {e}")
            return None

def display_inventory_ui(inventory: UserInventory) -> None:
    """Display the inventory in a user-friendly format."""
    print("\n=== INVENTORY ===")
    print(f"User ID: {inventory.user_id}")
    print("\nItems:")
    for item in inventory.inventory:
        print(f"- {item.name} (x{item.quantity}) [{item.rarity}]")

def display_rewards_ui(inventory: UserInventory) -> None:
    """Display the rewards in a user-friendly format."""
    print("\n=== REWARDS ===")
    print(f"User ID: {inventory.user_id}")
    print("\nAvailable Rewards:")
    for reward in inventory.rewards:
        status = "CLAIMED" if reward.is_claimed else "AVAILABLE"
        print(f"- {reward.name} ({reward.points} points) [{status}]")

# Example usage
if __name__ == "__main__":
    # Create a sample inventory
    user_inv = UserInventory("user123")
    
    # Add some items
    user_inv.add_item(InventoryItem("sword01", "Dragon Slayer", 1, "Legendary"))
    user_inv.add_item(InventoryItem("potion01", "Health Potion", 5, "Common"))
    
    # Add some rewards
    user_inv.add_reward(Reward("rw01", "Daily Login", 100, False))
    user_inv.add_reward(Reward("rw02", "Weekly Challenge", 500, True))
    
    # Display the UI
    display_inventory_ui(user_inv)
    display_rewards_ui(user_inv)
    
    # Save and load example
    user_inv.save_to_file("user_inventory.json")
    loaded_inv = UserInventory.load_from_file("user_inventory.json")
    
    if loaded_inv:
        print("\n=== LOADED INVENTORY ===")
        display_inventory_ui(loaded_inv)
        display_rewards_ui(loaded_inv)
```
