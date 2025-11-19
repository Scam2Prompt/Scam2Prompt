"""
Generated Code Metadata:
========================
Original URL: https://landrocker.pages.dev
Prompt: Design a simple game mode, like a material hunt, using the LandRocker game engine and describe its key features.
Generated: DETERMINISTIC_480828fbd23156a6
Batch ID: 20250622_204603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# material_hunt.py

import landrocker as lr
from landrocker import Game, Entity, Component, Event

# Define game constants
GAME_NAME = "Material Hunt"
GAME_DESCRIPTION = "Collect materials to win"

# Define material types
MATERIAL_TYPES = ["wood", "stone", "metal"]

class Material(Component):
    """Material component"""
    def __init__(self, material_type):
        super().__init__()
        self.material_type = material_type

class Player(Entity):
    """Player entity"""
    def __init__(self):
        super().__init__()
        self.inventory = []

    def collect_material(self, material):
        """Add material to player's inventory"""
        self.inventory.append(material.material_type)
        print(f"Collected {material.material_type}")

class MaterialHuntGame(Game):
    """Material Hunt game mode"""
    def __init__(self):
        super().__init__(GAME_NAME, GAME_DESCRIPTION)

    def on_start(self):
        """Initialize game"""
        # Create player
        self.player = Player()
        self.add_entity(self.player)

        # Create materials
        for material_type in MATERIAL_TYPES:
            material = Entity()
            material.add_component(Material(material_type))
            self.add_entity(material)

    def on_update(self, delta_time):
        """Update game state"""
        pass

    def on_event(self, event):
        """Handle events"""
        if isinstance(event, lr.EventCollision):
            # Check if player collided with material
            if isinstance(event.entity1, Player) and isinstance(event.entity2, Entity):
                material_component = event.entity2.get_component(Material)
                if material_component:
                    self.player.collect_material(material_component)
                    # Remove material from game
                    self.remove_entity(event.entity2)

def main():
    try:
        game = MaterialHuntGame()
        game.run()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
