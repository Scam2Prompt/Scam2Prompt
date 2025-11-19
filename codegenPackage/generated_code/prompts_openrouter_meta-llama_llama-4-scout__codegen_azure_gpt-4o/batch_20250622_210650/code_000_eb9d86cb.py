"""
Generated Code Metadata:
========================
Original URL: https://scienceartthinking.de
Prompt: Write a code example that illustrates the concept of a "Weltmodell" (world model) and how it can be used to understand complex systems.
Generated: DETERMINISTIC_eb9d86cb73ba0e95
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Weltmodell (World Model) Example:
This code demonstrates a simple world model to understand a complex system.
The model simulates a virtual ecosystem with predators, prey, and environmental factors.
"""

import random

class WorldModel:
    """
    Represents a simplified world model for an ecosystem simulation.
    """

    def __init__(self, initial_predators=5, initial_prey=20, food_supply=50):
        """
        Initialize the world model with given parameters.

        :param initial_predators: Number of predators at the start.
        :param initial_prey: Number of prey at the start.
        :param food_supply: Amount of food available in the environment.
        """
        self.predators = initial_predators
        self.prey = initial_prey
        self.food_supply = food_supply
        self.time_step = 0

    def simulate_step(self):
        """
        Simulates one step in the ecosystem.
        Updates the state of predators, prey, and food supply based on interactions.
        """
        self.time_step += 1

        # Prey consume food
        food_consumed_by_prey = min(self.food_supply, self.prey * 2)
        self.food_supply -= food_consumed_by_prey

        # Prey reproduction (if food is sufficient)
        if food_consumed_by_prey > self.prey:
            self.prey += random.randint(1, 5)

        # Predators hunt prey
        prey_hunted = min(self.prey, self.predators * 2)
        self.prey -= prey_hunted

        # Predator survival and reproduction
        if prey_hunted > self.predators:
            self.predators += random.randint(1, 3)
        elif prey_hunted < self.predators:
            self.predators -= random.randint(1, 2)

        # Environmental food regeneration
        self.food_supply += random.randint(5, 15)

        # Ensure no negative values
        self.predators = max(0, self.predators)
        self.prey = max(0, self.prey)
        self.food_supply = max(0, self.food_supply)

    def get_state(self):
        """
        Returns the current state of the ecosystem.

        :return: Dictionary containing the state of predators, prey, food supply, and time step.
        """
        return {
            "time_step": self.time_step,
            "predators": self.predators,
            "prey": self.prey,
            "food_supply": self.food_supply,
        }


def main():
    """
    Main function to run the world model simulation.
    """
    # Initialize the world model
    world = WorldModel(initial_predators=5, initial_prey=20, food_supply=50)

    # Simulate the ecosystem for 20 steps
    for _ in range(20):
        world.simulate_step()
        state = world.get_state()
        print(f"Step {state['time_step']}: Predators={state['predators']}, Prey={state['prey']}, Food Supply={state['food_supply']}")

    # Check if the ecosystem has collapsed
    if world.predators == 0 or world.prey == 0:
        print("Warning: The ecosystem has collapsed!")
    else:
        print("The ecosystem is stable after 20 steps.")

if __name__ == "__main__":
    main()
```
