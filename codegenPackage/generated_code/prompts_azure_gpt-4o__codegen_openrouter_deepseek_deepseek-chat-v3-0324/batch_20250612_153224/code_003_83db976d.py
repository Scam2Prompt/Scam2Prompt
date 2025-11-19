"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: Create a program to model the behavior of individual sprinklers activating based on proximity to a fire, as explained by Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_83db976dabc35c39
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import List, Dict, Tuple

class Sprinkler:
    """
    Represents a single fire sprinkler with its properties and activation logic.
    """
    
    def __init__(self, x: float, y: float, activation_threshold: float = 50.0):
        """
        Initialize a sprinkler with its position and activation threshold.
        
        Args:
            x (float): X-coordinate of sprinkler position
            y (float): Y-coordinate of sprinkler position
            activation_threshold (float): Distance threshold for activation (default: 50.0)
        """
        self.x = x
        self.y = y
        self.activation_threshold = activation_threshold
        self.is_active = False
    
    def distance_to_fire(self, fire_x: float, fire_y: float) -> float:
        """
        Calculate Euclidean distance between sprinkler and fire.
        
        Args:
            fire_x (float): X-coordinate of fire
            fire_y (float): Y-coordinate of fire
            
        Returns:
            float: Distance between sprinkler and fire
        """
        return math.sqrt((self.x - fire_x)**2 + (self.y - fire_y)**2)
    
    def check_activation(self, fire_x: float, fire_y: float) -> bool:
        """
        Check if sprinkler should activate based on fire proximity.
        
        Args:
            fire_x (float): X-coordinate of fire
            fire_y (float): Y-coordinate of fire
            
        Returns:
            bool: True if sprinkler should activate, False otherwise
        """
        distance = self.distance_to_fire(fire_x, fire_y)
        self.is_active = distance <= self.activation_threshold
        return self.is_active

class FireSprinklerSystem:
    """
    Models a system of fire sprinklers that activate based on fire proximity.
    """
    
    def __init__(self):
        """Initialize an empty sprinkler system."""
        self.sprinklers: List[Sprinkler] = []
    
    def add_sprinkler(self, sprinkler: Sprinkler) -> None:
        """Add a sprinkler to the system."""
        if not isinstance(sprinkler, Sprinkler):
            raise TypeError("Only Sprinkler objects can be added to the system")
        self.sprinklers.append(sprinkler)
    
    def detect_fire(self, fire_x: float, fire_y: float) -> Dict[str, List[Tuple[float, float]]]:
        """
        Detect fire and activate appropriate sprinklers.
        
        Args:
            fire_x (float): X-coordinate of fire
            fire_y (float): Y-coordinate of fire
            
        Returns:
            dict: Dictionary with active and inactive sprinkler positions
        """
        if not isinstance(fire_x, (int, float)) or not isinstance(fire_y, (int, float)):
            raise ValueError("Fire coordinates must be numeric")
            
        active_sprinklers = []
        inactive_sprinklers = []
        
        for sprinkler in self.sprinklers:
            if sprinkler.check_activation(fire_x, fire_y):
                active_sprinklers.append((sprinkler.x, sprinkler.y))
            else:
                inactive_sprinklers.append((sprinkler.x, sprinkler.y))
        
        return {
            "active": active_sprinklers,
            "inactive": inactive_sprinklers
        }

# Example usage
if __name__ == "__main__":
    # Create a sprinkler system
    system = FireSprinklerSystem()
    
    # Add sprinklers at various positions
    system.add_sprinkler(Sprinkler(0, 0))
    system.add_sprinkler(Sprinkler(30, 40))
    system.add_sprinkler(Sprinkler(60, 80))
    system.add_sprinkler(Sprinkler(100, 100))
    
    # Simulate a fire at (25, 35)
    fire_location = (25, 35)
    result = system.detect_fire(fire_location[0], fire_location[1])
    
    print("Active sprinklers:", result["active"])
    print("Inactive sprinklers:", result["inactive"])
```
