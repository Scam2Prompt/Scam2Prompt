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
# landroker_material_hunt.py
# A simple material hunt game mode for the LandRocker game engine

import random
import time
from typing import List, Dict, Optional

class MaterialHuntGame:
    """
    A simple material hunt game mode where players collect materials within a time limit.
    Key Features:
    - Randomized material spawns
    - Time-based gameplay
    - Score tracking
    - Multiple difficulty levels
    - Material collection effects
    """
    
    def __init__(self, difficulty: str = "medium"):
        """
        Initialize the material hunt game.
        
        Args:
            difficulty: Game difficulty ('easy', 'medium', 'hard')
        """
        self.difficulty = difficulty
        self.score = 0
        self.time_remaining = 0
        self.materials_collected: Dict[str, int] = {}
        self.active_materials: List[Dict] = []
        self.game_active = False
        
        # Difficulty settings
        self.difficulty_settings = {
            "easy": {"time_limit": 300, "spawn_rate": 10, "material_value": 10},
            "medium": {"time_limit": 240, "spawn_rate": 7, "material_value": 15},
            "hard": {"time_limit": 180, "spawn_rate": 5, "material_value": 20}
        }
        
        # Available materials with their properties
        self.available_materials = [
            {"name": "Iron", "rarity": "common", "color": (169, 169, 169)},
            {"name": "Gold", "rarity": "uncommon", "color": (255, 215, 0)},
            {"name": "Diamond", "rarity": "rare", "color": (185, 242, 255)},
            {"name": "Uranium", "rarity": "epic", "color": (0, 255, 0)},
            {"name": "Dark Matter", "rarity": "legendary", "color": (75, 0, 130)}
        ]
    
    def start_game(self):
        """Initialize and start the game with current difficulty settings."""
        if self.game_active:
            raise RuntimeError("Game is already running")
            
        settings = self.difficulty_settings[self.difficulty]
        self.time_remaining = settings["time_limit"]
        self.score = 0
        self.materials_collected = {}
        self.active_materials = []
        self.game_active = True
        
        # Initial material spawn
        self._spawn_materials()
        
    def end_game(self):
        """End the current game session."""
        if not self.game_active:
            raise RuntimeError("No active game to end")
            
        self.game_active = False
        return {
            "score": self.score,
            "materials_collected": self.materials_collected,
            "time_remaining": self.time_remaining
        }
    
    def update(self, delta_time: float):
        """
        Update game state.
        
        Args:
            delta_time: Time since last update in seconds
        """
        if not self.game_active:
            return
            
        self.time_remaining -= delta_time
        
        if self.time_remaining <= 0:
            self.end_game()
            return
            
        # Random chance to spawn new materials
        settings = self.difficulty_settings[self.difficulty]
        if random.random() < 1.0 / settings["spawn_rate"]:
            self._spawn_materials()
    
    def collect_material(self, material_id: int) -> Optional[Dict]:
        """
        Attempt to collect a material.
        
        Args:
            material_id: ID of material to collect
            
        Returns:
            Dictionary with collection info or None if invalid
        """
        if not self.game_active:
            return None
            
        for material in self.active_materials:
            if material["id"] == material_id:
                self.active_materials.remove(material)
                
                # Update score and collection count
                material_value = self.difficulty_settings[self.difficulty]["material_value"]
                rarity_multiplier = {
                    "common": 1,
                    "uncommon": 2,
                    "rare": 3,
                    "epic": 5,
                    "legendary": 10
                }[material["rarity"]]
                
                points = material_value * rarity_multiplier
                self.score += points
                
                # Track collected materials
                material_name = material["name"]
                self.materials_collected[material_name] = self.materials_collected.get(material_name, 0) + 1
                
                return {
                    "material": material_name,
                    "points": points,
                    "rarity": material["rarity"]
                }
        
        return None
    
    def _spawn_materials(self):
        """Spawn new materials in the game world."""
        if not self.game_active:
            return
            
        settings = self.difficulty_settings[self.difficulty]
        spawn_count = random.randint(1, 3)
        
        for _ in range(spawn_count):
            material = random.choice(self.available_materials).copy()
            material["id"] = random.randint(1000, 9999)
            material["position"] = (
                random.uniform(-50, 50),
                random.uniform(-50, 50),
                random.uniform(-50, 50)
            )
            self.active_materials.append(material)
    
    def get_game_state(self) -> Dict:
        """
        Get current game state for rendering/UI.
        
        Returns:
            Dictionary containing current game state
        """
        return {
            "score": self.score,
            "time_remaining": max(0, self.time_remaining),
            "materials_collected": self.materials_collected,
            "active_materials": self.active_materials,
            "game_active": self.game_active,
            "difficulty": self.difficulty
        }
    
    def set_difficulty(self, difficulty: str):
        """
        Change game difficulty.
        
        Args:
            difficulty: New difficulty level ('easy', 'medium', 'hard')
        """
        if difficulty not in self.difficulty_settings:
            raise ValueError(f"Invalid difficulty: {difficulty}")
            
        self.difficulty = difficulty
```
