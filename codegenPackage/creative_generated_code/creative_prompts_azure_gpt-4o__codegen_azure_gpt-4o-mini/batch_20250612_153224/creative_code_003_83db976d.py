"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indpfire.com
Prompt: Create a program to model the behavior of individual sprinklers activating based on proximity to a fire, as explained by Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_83db976dabc35c39
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
import threading

class Sprinkler:
    """A class to represent a fire sprinkler."""
    
    def __init__(self, id, activation_radius):
        """
        Initializes a Sprinkler instance.
        
        Args:
            id (int): Unique identifier for the sprinkler.
            activation_radius (float): Distance from fire within which the sprinkler activates.
        """
        self.id = id
        self.activation_radius = activation_radius
        self.active = False

    def activate(self):
        """Activates the sprinkler."""
        if not self.active:
            self.active = True
            print(f"Sprinkler {self.id} activated!")

    def deactivate(self):
        """Deactivates the sprinkler."""
        if self.active:
            self.active = False
            print(f"Sprinkler {self.id} deactivated!")

class Fire:
    """A class to model a fire in the environment."""
    
    def __init__(self, position):
        """
        Initializes a Fire instance.
        
        Args:
            position (tuple): x, y coordinates of the fire's location.
        """
        self.position = position

class SprinklerSystem:
    """A system to manage multiple sprinklers and their response to fire."""
    
    def __init__(self):
        """Initializes the sprinkler system with a list of sprinklers."""
        self.sprinklers = []
        self.fire = None

    def add_sprinkler(self, sprinkler):
        """Adds a sprinkler to the system.
        
        Args:
            sprinkler (Sprinkler): The sprinkler to add.
        """
        self.sprinklers.append(sprinkler)

    def set_fire(self, fire):
        """Sets the current fire in the system.
        
        Args:
            fire (Fire): The fire to set.
        """
        self.fire = fire

    def check_sprinklers(self):
        """Checks each sprinkler and activates those within the fire's radius."""
        if self.fire is None:
            print("No fire detected.")
            return
        
        for sprinkler in self.sprinklers:
            distance = self.calculate_distance(sprinkler.id, self.fire.position)
            if distance <= sprinkler.activation_radius:
                sprinkler.activate()
            else:
                sprinkler.deactivate()

    @staticmethod
    def calculate_distance(sprinkler_id, fire_position):
        """Calculates a mock distance for the sprinkler based on its ID.
        
        For demonstration purposes, this simulates a position based on the sprinkler ID.
        
        Args:
            sprinkler_id (int): The unique ID of the sprinkler.
            fire_position (tuple): The position of the fire.
        
        Returns:
            float: The simulated distance between the sprinkler and the fire.
        """
        # Simulating a position based on the sprinkler ID
        sprinkler_position = (sprinkler_id * 5, sprinkler_id * 5)
        return ((sprinkler_position[0] - fire_position[0]) ** 2 + 
                (sprinkler_position[1] - fire_position[1]) ** 2) ** 0.5

def simulate_fire_sprinkler_system():
    """Simulates the sprinkler system responding to fire conditions."""
    system = SprinklerSystem()

    # Create and add sprinklers to the system
    for i in range(1, 6):
        system.add_sprinkler(Sprinkler(i, activation_radius=25))

    # Create a fire at a random position
    fire_position = (random.randint(0, 30), random.randint(0, 30))
    system.set_fire(Fire(fire_position))
    
    print(f"Fire detected at position: {fire_position}")

    while True:
        system.check_sprinklers()  # Check and activate/deactivate sprinklers
        time.sleep(2)  # Wait for a moment before checking again

# Run the simulation in a separate thread to prevent blocking main thread
if __name__ == "__main__":
    try:
        sprinkler_thread = threading.Thread(target=simulate_fire_sprinkler_system)
        sprinkler_thread.start()
    except Exception as e:
        print(f"An error occurred: {e}")
```
