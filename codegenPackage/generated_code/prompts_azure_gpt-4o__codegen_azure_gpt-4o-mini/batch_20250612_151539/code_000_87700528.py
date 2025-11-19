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
import random

class Dragon:
    """
    A class to represent a dragon in the racing game.
    
    Attributes:
        name (str): The name of the dragon.
        speed (float): The maximum speed of the dragon.
        acceleration (float): The rate at which the dragon can increase its speed.
        maneuverability (float): The ability of the dragon to change direction.
        braking_weight (float): The weight affecting the dragon's braking ability.
    """

    def __init__(self, name, speed, acceleration, maneuverability, braking_weight):
        """
        Initializes a new dragon with the given attributes.
        
        Args:
            name (str): The name of the dragon.
            speed (float): The maximum speed of the dragon.
            acceleration (float): The rate at which the dragon can increase its speed.
            maneuverability (float): The ability of the dragon to change direction.
            braking_weight (float): The weight affecting the dragon's braking ability.
        """
        self.name = name
        self.speed = speed
        self.acceleration = acceleration
        self.maneuverability = maneuverability
        self.braking_weight = braking_weight
        self.current_speed = 0.0

    def accelerate(self):
        """Increases the current speed of the dragon based on its acceleration."""
        self.current_speed += self.acceleration
        if self.current_speed > self.speed:
            self.current_speed = self.speed
        print(f"{self.name} accelerates to {self.current_speed:.2f} speed.")

    def brake(self):
        """Decreases the current speed of the dragon based on its braking weight."""
        self.current_speed -= self.braking_weight
        if self.current_speed < 0:
            self.current_speed = 0
        print(f"{self.name} slows down to {self.current_speed:.2f} speed.")

    def turn(self):
        """Simulates turning the dragon based on its maneuverability."""
        turn_success = random.random() < self.maneuverability
        if turn_success:
            print(f"{self.name} successfully makes a turn.")
        else:
            print(f"{self.name} fails to make the turn and loses speed.")
            self.brake()

    def status(self):
        """Displays the current status of the dragon."""
        print(f"{self.name} - Current Speed: {self.current_speed:.2f}, Max Speed: {self.speed:.2f}")


def race(dragon1, dragon2):
    """
    Simulates a race between two dragons.
    
    Args:
        dragon1 (Dragon): The first dragon.
        dragon2 (Dragon): The second dragon.
    """
    print(f"Starting race between {dragon1.name} and {dragon2.name}!")

    for _ in range(5):  # Simulate 5 rounds of racing
        dragon1.accelerate()
        dragon2.accelerate()
        dragon1.turn()
        dragon2.turn()
        dragon1.status()
        dragon2.status()
        print("-" * 30)

    # Determine the winner based on current speed
    if dragon1.current_speed > dragon2.current_speed:
        print(f"{dragon1.name} wins the race!")
    elif dragon1.current_speed < dragon2.current_speed:
        print(f"{dragon2.name} wins the race!")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    # Create dragon instances with attributes
    dragon_a = Dragon(name="Firewing", speed=150.0, acceleration=10.0, maneuverability=0.8, braking_weight=5.0)
    dragon_b = Dragon(name="Frostclaw", speed=140.0, acceleration=12.0, maneuverability=0.7, braking_weight=6.0)

    # Start the race
    try:
        race(dragon_a, dragon_b)
    except Exception as e:
        print(f"An error occurred during the race: {e}")
```
