"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rplanet-io.vercel.app
Prompt: Develop a strategy simulation algorithm in Python for managing troops on the R-Planet map, including ally and enemy locations, artifact activation, and masick taming.
Generated: DETERMINISTIC_96bafc1599b02a32
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

# Game constants
MAP_WIDTH = 100
MAP_HEIGHT = 100
MAX_TROOPS = 500
ARTIFACT_EFFECT_RADIUS = 10
MASICK_TAME_PROBABILITY = 0.2

# Classes for game entities
class Troop:
    """Represents a troop with position and allegiance."""
    def __init__(self, id, x, y, allegiance):
        self.id = id
        self.x = x
        self.y = y
        self.allegiance = allegiance  # 'ally' or 'enemy'

    def move(self, dx, dy):
        """Move the troop by the specified delta."""
        self.x = max(0, min(MAP_WIDTH, self.x + dx))
        self.y = max(0, min(MAP_HEIGHT, self.y + dy))

class Artifact:
    """Represents an artifact with activation state."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.active = False

    def activate(self):
        """Activate the artifact."""
        self.active = True

    def deactivate(self):
        """Deactivate the artifact."""
        self.active = False

class Masick:
    """Represents a wild masick creature that can be tamed."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tamed = False

    def attempt_taming(self):
        """Try to tame the masick based on probability."""
        if random.random() < MASICK_TAME_PROBABILITY:
            self.tamed = True

# Game functions
def distance(x1, y1, x2, y2):
    """Calculate the Euclidean distance between two points."""
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def manage_troops(troops, artifact, masicks):
    """
    Main strategy simulation algorithm to manage troops.
    - Troops move towards enemies or artifacts.
    - Artifact provides a boost to allies within its effect radius.
    - Attempt to tame masicks in proximity.
    """
    for troop in troops:
        # Handle troop movement
        if troop.allegiance == 'ally':
            # Move towards the artifact if it's active
            if artifact.active:
                dx = artifact.x - troop.x
                dy = artifact.y - troop.y
                troop.move(dx // abs(dx) if dx != 0 else 0, dy // abs(dy) if dy != 0 else 0)
            else:
                # Random movement if artifact is not active
                troop.move(random.randint(-1, 1), random.randint(-1, 1))
        elif troop.allegiance == 'enemy':
            # Enemies move randomly
            troop.move(random.randint(-1, 1), random.randint(-1, 1))

        # Check proximity to artifact
        if distance(troop.x, troop.y, artifact.x, artifact.y) <= ARTIFACT_EFFECT_RADIUS:
            if troop.allegiance == 'ally' and artifact.active:
                # Allies within radius benefit from artifact effects (placeholder for enhancement logic)
                print(f"Troop {troop.id} benefitting from artifact effects.")

    # Handle masick taming
    for masick in masicks:
        if not masick.tamed:
            for troop in troops:
                if troop.allegiance == 'ally' and distance(troop.x, troop.y, masick.x, masick.y) <= ARTIFACT_EFFECT_RADIUS:
                    masick.attempt_taming()
                    if masick.tamed:
                        print(f"Masick at ({masick.x}, {masick.y}) has been tamed.")
                        break

# Example game setup
def setup_game():
    """Setup initial game state with troops, artifact, and masicks."""
    troops = [Troop(id=i, x=random.randint(0, MAP_WIDTH), y=random.randint(0, MAP_HEIGHT),
                    allegiance=random.choice(['ally', 'enemy'])) for i in range(MAX_TROOPS)]
    artifact = Artifact(x=random.randint(0, MAP_WIDTH), y=random.randint(0, MAP_HEIGHT))
    masicks = [Masick(x=random.randint(0, MAP_WIDTH), y=random.randint(0, MAP_HEIGHT)) for _ in range(5)]

    return troops, artifact, masicks

def main():
    """Main simulation loop."""
    troops, artifact, masicks = setup_game()

    try:
        artifact.activate()  # Activate artifact for demonstration purposes

        # Run the simulation for a few steps
        for step in range(10):
            print(f"Simulation step {step + 1}")
            manage_troops(troops, artifact, masicks)

    except Exception as e:
        print(f"An error occurred during the simulation: {e}")
    finally:
        artifact.deactivate()  # Ensure artifact is deactivated at the end of the simulation

if __name__ == "__main__":
    main()
```
