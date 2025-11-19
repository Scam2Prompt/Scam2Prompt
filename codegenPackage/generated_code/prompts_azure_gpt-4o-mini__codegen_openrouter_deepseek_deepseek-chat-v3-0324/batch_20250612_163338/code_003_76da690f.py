"""
Generated Code Metadata:
========================
Original URL: https://codes-bigtime.pages.dev
Prompt: Create a script to manage player workshops for crafting armor cosmetics in Big Time, utilizing the Forge and Armory features.
Generated: DETERMINISTIC_76da690f7da83ed5
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class CraftingMaterial:
    """Represents a crafting material with name and quantity."""
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

class ArmorCosmetic:
    """Represents an armor cosmetic blueprint."""
    def __init__(self, name: str, materials: List[CraftingMaterial], forge_time: int):
        self.name = name
        self.materials = materials
        self.forge_time = forge_time  # in seconds

class Workshop:
    """Manages player workshops for crafting armor cosmetics."""
    def __init__(self):
        self.armory: Dict[str, ArmorCosmetic] = {}  # Blueprint name to ArmorCosmetic
        self.forge_queue: List[Dict] = []  # Items currently being forged
        self.player_materials: Dict[str, int] = {}  # Material name to quantity

    def load_blueprints(self, filepath: str) -> bool:
        """Load armor cosmetic blueprints from a JSON file."""
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
                for item in data.get('blueprints', []):
                    materials = [
                        CraftingMaterial(mat['name'], mat['quantity'])
                        for mat in item.get('materials', [])
                    ]
                    self.armory[item['name']] = ArmorCosmetic(
                        item['name'],
                        materials,
                        item['forge_time']
                    )
            return True
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            print(f"Error loading blueprints: {e}")
            return False

    def add_material(self, name: str, quantity: int) -> None:
        """Add or update player's crafting materials."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.player_materials[name] = self.player_materials.get(name, 0) + quantity

    def can_craft(self, blueprint_name: str) -> bool:
        """Check if player has enough materials to craft an item."""
        if blueprint_name not in self.armory:
            return False
        
        blueprint = self.armory[blueprint_name]
        for material in blueprint.materials:
            if self.player_materials.get(material.name, 0) < material.quantity:
                return False
        return True

    def start_crafting(self, blueprint_name: str) -> bool:
        """Start crafting an armor cosmetic if materials are available."""
        if not self.can_craft(blueprint_name):
            return False
        
        blueprint = self.armory[blueprint_name]
        
        # Deduct materials
        for material in blueprint.materials:
            self.player_materials[material.name] -= material.quantity
        
        # Add to forge queue
        self.forge_queue.append({
            'name': blueprint.name,
            'time_remaining': blueprint.forge_time
        })
        return True

    def update_forge(self, delta_time: int) -> List[str]:
        """Update forge progress and return completed items."""
        completed = []
        for item in self.forge_queue[:]:
            item['time_remaining'] -= delta_time
            if item['time_remaining'] <= 0:
                completed.append(item['name'])
                self.forge_queue.remove(item)
        return completed

    def get_forge_queue(self) -> List[Dict]:
        """Return current forge queue with remaining time."""
        return [{'name': item['name'], 'time_remaining': item['time_remaining']} 
                for item in self.forge_queue]

    def get_materials(self) -> Dict[str, int]:
        """Return copy of player's materials."""
        return self.player_materials.copy()

    def get_blueprints(self) -> List[str]:
        """Return list of available blueprint names."""
        return list(self.armory.keys())

# Example usage
if __name__ == "__main__":
    workshop = Workshop()
    if workshop.load_blueprints('blueprints.json'):
        print("Blueprints loaded successfully")
    
    # Add some materials
    workshop.add_material("metal", 10)
    workshop.add_material("cloth", 5)
    
    # Try to craft
    if workshop.start_crafting("helmet"):
        print("Started crafting helmet")
    
    # Simulate forge progress
    completed = workshop.update_forge(30)
    if completed:
        print(f"Completed: {completed}")
```
