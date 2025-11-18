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
from typing import List, Tuple

# Constants for the simulation
MAP_SIZE = 10  # Define the size of the R-Planet map
NUM_ALLIES = 5  # Number of ally troops
NUM_ENEMIES = 5  # Number of enemy troops
NUM_ARTIFACTS = 3  # Number of artifacts

# Define troop types
class Troop:
    def __init__(self, name: str, position: Tuple[int, int], is_ally: bool):
        self.name = name
        self.position = position
        self.is_ally = is_ally

    def move(self, new_position: Tuple[int, int]):
        """Move the troop to a new position on the map."""
        if 0 <= new_position[0] < MAP_SIZE and 0 <= new_position[1] < MAP_SIZE:
            self.position = new_position
        else:
            raise ValueError("New position is out of bounds.")

class Artifact:
    def __init__(self, position: Tuple[int, int], activated: bool = False):
        self.position = position
        self.activated = activated

    def activate(self):
        """Activate the artifact."""
        if not self.activated:
            self.activated = True
        else:
            raise RuntimeError("Artifact already activated.")

class RPlanetSimulation:
    def __init__(self):
        self.allies: List[Troop] = self.generate_troops(is_ally=True, num=NUM_ALLIES)
        self.enemies: List[Troop] = self.generate_troops(is_ally=False, num=NUM_ENEMIES)
        self.artifacts: List[Artifact] = self.generate_artifacts(num=NUM_ARTIFACTS)

    def generate_troops(self, is_ally: bool, num: int) -> List[Troop]:
        """Generate troops and ensure they do not overlap."""
        troops = []
        while len(troops) < num:
            position = (random.randint(0, MAP_SIZE - 1), random.randint(0, MAP_SIZE - 1))
            if not any(t.position == position for t in troops):
                troops.append(Troop(name=f"{'Ally' if is_ally else 'Enemy'} Troop {len(troops) + 1}", position=position, is_ally=is_ally))
        return troops

    def generate_artifacts(self, num: int) -> List[Artifact]:
        """Generate artifacts and ensure they do not overlap with troops."""
        artifacts = []
        while len(artifacts) < num:
            position = (random.randint(0, MAP_SIZE - 1), random.randint(0, MAP_SIZE - 1))
            if not any(t.position == position for t in self.allies + self.enemies):
                artifacts.append(Artifact(position=position))
        return artifacts

    def run_simulation(self):
        """Run the simulation for a defined number of turns."""
        try:
            for turn in range(1, 11):  # Simulate for 10 turns
                print(f"Turn {turn}:")
                self.move_troops()
                self.check_artifacts()
                self.display_status()
        except Exception as e:
            print(f"Error during simulation: {e}")

    def move_troops(self):
        """Randomly move each troop."""
        for troop in self.allies + self.enemies:
            new_position = (troop.position[0] + random.choice([-1, 0, 1]), troop.position[1] + random.choice([-1, 0, 1]))
            try:
                troop.move(new_position)
            except ValueError as e:
                print(f"Troop {troop.name} could not move: {e}")

    def check_artifacts(self):
        """Check if any troops are on the artifacts to activate them."""
        for artifact in self.artifacts:
            for troop in self.allies + self.enemies:
                if troop.position == artifact.position and not artifact.activated:
                    try:
                        artifact.activate()
                        print(f"{troop.name} activated an artifact at {artifact.position}.")
                    except RuntimeError as e:
                        print(f"Could not activate artifact: {e}")

    def display_status(self):
        """Display the current status of allies, enemies, and artifacts."""
        print("Allies:")
        for ally in self.allies:
            print(f" - {ally.name} at {ally.position}")

        print("Enemies:")
        for enemy in self.enemies:
            print(f" - {enemy.name} at {enemy.position}")

        print("Artifacts:")
        for artifact in self.artifacts:
            status = "Activated" if artifact.activated else "Deactivated"
            print(f" - Artifact at {artifact.position}: {status}")

if __name__ == "__main__":
    simulation = RPlanetSimulation()
    simulation.run_simulation()
```
