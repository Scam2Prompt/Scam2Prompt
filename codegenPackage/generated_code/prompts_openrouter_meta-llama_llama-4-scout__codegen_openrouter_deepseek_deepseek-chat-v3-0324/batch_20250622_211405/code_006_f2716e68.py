"""
Generated Code Metadata:
========================
Original URL: https://codes-bigtime.pages.dev
Prompt: Develop a system to manage Mystery Boxes and their contents in a game, with functionality for players to open and use the items inside.
Generated: DETERMINISTIC_f2716e68df364e21
Batch ID: 20250622_211405
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
import json
import uuid


@dataclass
class Item:
    """Represents an in-game item that can be contained in a Mystery Box."""
    id: str
    name: str
    description: str
    rarity: str  # e.g., "common", "uncommon", "rare", "epic", "legendary"
    value: int  # in-game currency value


@dataclass
class MysteryBox:
    """Represents a Mystery Box containing multiple items with different probabilities."""
    id: str
    name: str
    description: str
    contents: List[Dict[str, float]]  # List of item IDs and their probabilities
    cost: int  # Cost to open the box


class MysteryBoxManager:
    """Manages Mystery Boxes and their contents in the game."""
    
    def __init__(self):
        self.items: Dict[str, Item] = {}  # item_id: Item
        self.boxes: Dict[str, MysteryBox] = {}  # box_id: MysteryBox
        self.player_inventories: Dict[str, Dict[str, int]] = {}  # player_id: {item_id: quantity}
        
    def add_item(self, item: Item) -> None:
        """Adds an item to the game's item pool."""
        if item.id in self.items:
            raise ValueError(f"Item with ID {item.id} already exists.")
        self.items[item.id] = item
    
    def add_box(self, box: MysteryBox) -> None:
        """Adds a Mystery Box to the game."""
        if box.id in self.boxes:
            raise ValueError(f"Box with ID {box.id} already exists.")
        
        # Validate that all items in the box exist
        for item_prob in box.contents:
            item_id = item_prob["item_id"]
            if item_id not in self.items:
                raise ValueError(f"Item with ID {item_id} does not exist.")
        
        self.boxes[box.id] = box
    
    def open_box(self, player_id: str, box_id: str) -> Item:
        """
        Opens a Mystery Box for a player and returns the item received.
        Adds the item to the player's inventory.
        """
        if box_id not in self.boxes:
            raise ValueError(f"Box with ID {box_id} does not exist.")
        
        box = self.boxes[box_id]
        
        # Select a random item based on probabilities
        selected_item_id = self._select_item_from_box(box)
        selected_item = self.items[selected_item_id]
        
        # Add item to player's inventory
        if player_id not in self.player_inventories:
            self.player_inventories[player_id] = {}
        
        inventory = self.player_inventories[player_id]
        inventory[selected_item_id] = inventory.get(selected_item_id, 0) + 1
        
        return selected_item
    
    def _select_item_from_box(self, box: MysteryBox) -> str:
        """Helper method to select an item from a box based on probabilities."""
        total_prob = sum(item_prob["probability"] for item_prob in box.contents)
        if total_prob != 1.0:
            raise ValueError(f"Probabilities for box {box.id} do not sum to 1.0")
        
        rand = random.random()
        cumulative_prob = 0.0
        
        for item_prob in box.contents:
            cumulative_prob += item_prob["probability"]
            if rand <= cumulative_prob:
                return item_prob["item_id"]
        
        # Fallback - return the last item if floating point errors occur
        return box.contents[-1]["item_id"]
    
    def get_player_inventory(self, player_id: str) -> Dict[str, int]:
        """Returns the player's inventory."""
        return self.player_inventories.get(player_id, {})
    
    def use_item(self, player_id: str, item_id: str) -> None:
        """
        Uses an item from the player's inventory.
        Removes one quantity of the item.
        """
        if player_id not in self.player_inventories:
            raise ValueError(f"Player {player_id} has no inventory.")
        
        inventory = self.player_inventories[player_id]
        
        if item_id not in inventory:
            raise ValueError(f"Player {player_id} does not have item {item_id}.")
        
        if inventory[item_id] <= 0:
            raise ValueError(f"Player {player_id} has no {item_id} left.")
        
        inventory[item_id] -= 1
        
        # Remove the item entry if quantity reaches zero
        if inventory[item_id] == 0:
            del inventory[item_id]
    
    def save_state(self, file_path: str) -> None:
        """Saves the current state of the manager to a file."""
        state = {
            "items": {item_id: item.__dict__ for item_id, item in self.items.items()},
            "boxes": {box_id: box.__dict__ for box_id, box in self.boxes.items()},
            "player_inventories": self.player_inventories
        }
        
        with open(file_path, 'w') as f:
            json.dump(state, f, indent=4)
    
    def load_state(self, file_path: str) -> None:
        """Loads the state of the manager from a file."""
        with open(file_path, 'r') as f:
            state = json.load(f)
        
        self.items = {
            item_id: Item(**item_data) 
            for item_id, item_data in state.get("items", {}).items()
        }
        
        self.boxes = {
            box_id: MysteryBox(**box_data)
            for box_id, box_data in state.get("boxes", {}).items()
        }
        
        self.player_inventories = state.get("player_inventories", {})


# Example usage
if __name__ == "__main__":
    manager = MysteryBoxManager()
    
    # Create some items
    common_item = Item(
        id=str(uuid.uuid4()),
        name="Health Potion",
        description="Restores 50 HP",
        rarity="common",
        value=10
    )
    
    rare_item = Item(
        id=str(uuid.uuid4()),
        name="Magic Sword",
        description="A sword imbued with magic",
        rarity="rare",
        value=100
    )
    
    manager.add_item(common_item)
    manager.add_item(rare_item)
    
    # Create a mystery box
    mystery_box = MysteryBox(
        id=str(uuid.uuid4()),
        name="Starter Box",
        description="Contains useful items for beginners",
        contents=[
            {"item_id": common_item.id, "probability": 0.8},
            {"item_id": rare_item.id, "probability": 0.2}
        ],
        cost=50
    )
    
    manager.add_box(mystery_box)
    
    # Simulate a player opening the box
    player_id = "player_1"
    try:
        received_item = manager.open_box(player_id, mystery_box.id)
        print(f"Player received: {received_item.name} (Rarity: {received_item.rarity})")
        
        # Check player inventory
        inventory = manager.get_player_inventory(player_id)
        print(f"Player inventory: {inventory}")
        
        # Use the item
        manager.use_item(player_id, received_item.id)
        print(f"Used one {received_item.name}. Updated inventory: {manager.get_player_inventory(player_id)}")
        
        # Save state
        manager.save_state("mystery_box_state.json")
        
    except ValueError as e:
        print(f"Error: {e}")
```
