"""
Generated Code Metadata:
========================
Original URL: https://whelps.io
Prompt: Write a Python script to simulate the racing mechanics of WhelpS: Slipstream, incorporating attributes like speed, acceleration, maneuverability, and braking weight for different dragon characters.
Generated: DETERMINISTIC_8770052860f5838e
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# whelp_racing_mechanics.py

class Dragon:
    """Represents a dragon character with racing attributes."""

    def __init__(self, name, speed, acceleration, maneuverability, braking_weight):
        """
        Initializes a Dragon object.

        Args:
            name (str): The dragon's name.
            speed (float): The dragon's maximum speed.
            acceleration (float): The dragon's acceleration rate.
            maneuverability (float): The dragon's maneuverability rating.
            braking_weight (float): The dragon's braking weight.
        """
        self.name = name
        self.speed = speed
        self.acceleration = acceleration
        self.maneuverability = maneuverability
        self.braking_weight = braking_weight
        self.current_speed = 0.0

    def accelerate(self):
        """Increases the dragon's speed based on its acceleration rate."""
        if self.current_speed < self.speed:
            self.current_speed = min(self.current_speed + self.acceleration, self.speed)

    def brake(self):
        """Decreases the dragon's speed based on its braking weight."""
        if self.current_speed > 0:
            self.current_speed = max(self.current_speed - self.braking_weight, 0)

    def turn(self):
        """Affects the dragon's speed based on its maneuverability."""
        if self.current_speed > 0:
            self.current_speed *= self.maneuverability / 10

    def __str__(self):
        return f"{self.name} - Speed: {self.current_speed:.2f}, Max Speed: {self.speed:.2f}"


class RacingSimulator:
    """Simulates a racing environment for multiple dragons."""

    def __init__(self):
        self.dragons = []

    def add_dragon(self, dragon):
        """Adds a dragon to the racing simulator."""
        self.dragons.append(dragon)

    def simulate_race(self, iterations):
        """
        Simulates a racing competition among the added dragons.

        Args:
            iterations (int): The number of iterations to simulate.
        """
        for i in range(iterations):
            print(f"\nIteration {i+1}:")
            for dragon in self.dragons:
                dragon.accelerate()
                print(dragon)

            # Allow dragons to brake and turn occasionally
            for dragon in self.dragons:
                if i % 5 == 0:  # Brake every 5 iterations
                    dragon.brake()
                if i % 3 == 0:  # Turn every 3 iterations
                    dragon.turn()

        print("\nFinal Standings:")
        for i, dragon in enumerate(sorted(self.dragons, key=lambda x: x.current_speed, reverse=True)):
            print(f"{i+1}. {dragon}")


if __name__ == "__main__":
    simulator = RacingSimulator()

    # Create dragon characters
    dragon1 = Dragon("Ember", 100.0, 5.0, 8.0, 2.0)
    dragon2 = Dragon("Frostbite", 90.0, 4.5, 9.0, 2.5)
    dragon3 = Dragon("Inferno", 110.0, 5.5, 7.0, 1.8)

    # Add dragons to the simulator
    simulator.add_dragon(dragon1)
    simulator.add_dragon(dragon2)
    simulator.add_dragon(dragon3)

    # Simulate a 20-iteration race
    simulator.simulate_race(20)
```
