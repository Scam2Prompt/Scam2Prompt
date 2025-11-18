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
import time

class Dragon:
    """A class representing a dragon character in the race."""
    
    def __init__(self, name, speed, acceleration, maneuverability, braking_weight):
        """
        Initializes a new dragon with the given attributes.

        Args:
            name (str): The name of the dragon.
            speed (float): The maximum speed of the dragon.
            acceleration (float): The rate of speed increase.
            maneuverability (float): The ability to change direction.
            braking_weight (float): The weight affecting the braking performance.
        """
        self.name = name
        self.speed = speed
        self.acceleration = acceleration
        self.maneuverability = maneuverability
        self.braking_weight = braking_weight
        self.current_speed = 0.0
        self.distance_traveled = 0.0

    def accelerate(self, time_elapsed):
        """Increases the speed of the dragon based on acceleration and time."""
        speed_increase = self.acceleration * time_elapsed
        self.current_speed = min(self.current_speed + speed_increase, self.speed)

    def brake(self, time_elapsed):
        """Decreases the speed of the dragon based on braking weight and time."""
        speed_decrease = self.braking_weight * time_elapsed
        self.current_speed = max(self.current_speed - speed_decrease, 0)

    def turn(self):
        """Simulates the turning maneuver of the dragon."""
        # Maneuver is successful if a random number is less than dragon's maneuverability
        return random.random() < self.maneuverability

    def move(self, time_elapsed):
        """Updates the distance traveled based on current speed."""
        self.distance_traveled += self.current_speed * time_elapsed

    def reset(self):
        """Resets the dragon's state for a new race."""
        self.current_speed = 0.0
        self.distance_traveled = 0.0

class Race:
    """A class to simulate a race between dragons."""
    
    def __init__(self, dragons, race_distance):
        """
        Initializes a race with the given dragons and distance.

        Args:
            dragons (list): List of Dragon objects participating in the race.
            race_distance (float): The total distance of the race.
        """
        self.dragons = dragons
        self.race_distance = race_distance

    def start(self):
        """Starts the race and displays the results."""
        race_time = 0
        finished_dragons = []

        while len(finished_dragons) < len(self.dragons):
            time.sleep(1)  # Simulate the passage of time
            race_time += 1

            for dragon in self.dragons:
                # Simulate acceleration and movement
                dragon.accelerate(1)
                if random.random() < 0.1:  # 10% chance to need to turn
                    if not dragon.turn():
                        print(f"{dragon.name} failed to turn and slowed down!")
                        dragon.brake(1)

                dragon.move(1)

                # Check if the dragon has finished the race
                if dragon.distance_traveled >= self.race_distance and dragon not in finished_dragons:
                    finished_dragons.append(dragon)
                    print(f"{dragon.name} finished the race!")

        print("\nRace finished!\nResults:")
        for index, dragon in enumerate(finished_dragons):
            print(f"{index + 1}. {dragon.name} - Distance: {dragon.distance_traveled:.2f}")

def main():
    """Main function to set up and start the race."""
    # Create dragon instances
    dragons = [
        Dragon("Firewing", speed=150, acceleration=30, maneuverability=0.8, braking_weight=5),
        Dragon("Stormclaw", speed=140, acceleration=35, maneuverability=0.7, braking_weight=6),
        Dragon("Nightshade", speed=160, acceleration=25, maneuverability=0.9, braking_weight=4),
    ]

    race_distance = 1000  # Distance of the race in arbitrary units

    # Initialize the race
    race = Race(dragons, race_distance)
    
    # Start the race
    try:
        race.start()
    except Exception as e:
        print(f"An error occurred during the race: {e}")

if __name__ == "__main__":
    main()
```
