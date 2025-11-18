"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whelps.io
Prompt: Write a Python script to simulate the racing mechanics of WhelpS: Slipstream, incorporating attributes like speed, acceleration, maneuverability, and braking weight for different dragon characters.
Generated: DETERMINISTIC_8770052860f5838e
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

# Define the Dragon class
class Dragon:
    def __init__(self, name, speed, acceleration, maneuverability, braking_weight):
        """
        Initializes a Dragon object with its attributes.

        :param name: Name of the dragon (str)
        :param speed: Base speed of the dragon (int)
        :param acceleration: Acceleration rate of the dragon (int)
        :param maneuverability: Maneuverability stat of the dragon (int)
        :param braking_weight: Braking weight (ability to decelerate) of the dragon (int)
        """
        self.name = name
        self.speed = speed
        self.acceleration = acceleration
        self.maneuverability = maneuverability
        self.braking_weight = braking_weight
        self.current_speed = 0

    def accelerate(self):
        """
        Simulates the dragon accelerating, increasing its current speed
        based on its acceleration attribute.
        """
        self.current_speed += self.acceleration
        if self.current_speed > self.speed:
            self.current_speed = self.speed  # Cap the speed at the dragon's max speed.

    def brake(self):
        """
        Simulates the dragon braking, decreasing its current speed
        based on its braking weight attribute.
        """
        self.current_speed -= self.braking_weight
        if self.current_speed < 0:
            self.current_speed = 0  # Ensure speed doesn't go below zero.

    def maneuver(self):
        """
        Simulates the dragon's ability to maneuver, returning a success/failure
        based on its maneuverability stat.
        """
        return random.random() < self.maneuverability / 100

    def __str__(self):
        """
        Returns a string representation of the dragon's current stats.
        """
        return (f"{self.name} - Current Speed: {self.current_speed}, "
                f"Max Speed: {self.speed}, Acceleration: {self.acceleration}, "
                f"Maneuverability: {self.maneuverability}, Braking Weight: {self.braking_weight}")


# Race simulation function
def simulate_race(dragons, race_length):
    """
    Simulates a race between dragons.

    :param dragons: List of Dragon objects participating in the race
    :param race_length: Length of the race (int)
    """
    positions = {dragon.name: 0 for dragon in dragons}  # Track positions of dragons
    
    print("Race Start!")
    print("-" * 30)

    for lap in range(1, race_length + 1):
        print(f"Lap {lap}:")
        for dragon in dragons:
            if dragon.maneuver():
                dragon.accelerate()  # Accelerate if maneuver is successful
            else:
                dragon.brake()  # Brake if maneuver fails

            # Update dragon's position
            positions[dragon.name] += dragon.current_speed

            # Print lap summary for this dragon
            print(f"{dragon.name}: Current Speed: {dragon.current_speed}, Total Distance: {positions[dragon.name]}")

        print("-" * 30)

    # Determine the winner
    winner = max(positions, key=positions.get)
    print(f"The winner is {winner} with a total distance of {positions[winner]} units!")


# Main script
if __name__ == "__main__":
    try:
        # Create dragons
        dragons = [
            Dragon("Flamewing", speed=120, acceleration=20, maneuverability=80, braking_weight=15),
            Dragon("Stormscale", speed=90, acceleration=25, maneuverability=85, braking_weight=20),
            Dragon("Shadowclaw", speed=110, acceleration=18, maneuverability=75, braking_weight=10),
            Dragon("Frostfang", speed=100, acceleration=22, maneuverability=90, braking_weight=18),
        ]

        # Simulate a race with 5 laps
        simulate_race(dragons, race_length=5)
    except Exception as e:
        print(f"An error occurred: {e}")
```
