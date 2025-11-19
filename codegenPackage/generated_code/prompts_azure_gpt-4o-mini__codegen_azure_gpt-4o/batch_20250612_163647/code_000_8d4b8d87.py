"""
Generated Code Metadata:
========================
Original URL: https://play-gamer.com
Prompt: Write a Python script that simulates the realistic dirt racing physics described in Rally Racer Dirt for an off-road racing game.
Generated: DETERMINISTIC_8d4b8d8718dd79e9
Batch ID: 20250612_163647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
import random

class Car:
    """
    Represents a car in the dirt racing simulation.
    """
    def __init__(self, name, max_speed, acceleration, handling, grip):
        """
        Initialize the car with its attributes.

        :param name: Name of the car
        :param max_speed: Maximum speed of the car (km/h)
        :param acceleration: Acceleration rate (m/s^2)
        :param handling: Handling factor (higher is better)
        :param grip: Grip factor (higher is better)
        """
        self.name = name
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.handling = handling
        self.grip = grip
        self.speed = 0  # Current speed (km/h)
        self.position = 0  # Current position on the track (meters)
        self.angle = 0  # Current angle of the car (degrees)

    def accelerate(self, delta_time):
        """
        Simulates acceleration of the car.

        :param delta_time: Time elapsed (seconds)
        """
        self.speed += self.acceleration * delta_time
        self.speed = min(self.speed, self.max_speed)  # Cap speed at max_speed

    def decelerate(self, delta_time):
        """
        Simulates deceleration of the car.

        :param delta_time: Time elapsed (seconds)
        """
        self.speed -= self.acceleration * delta_time * 0.5  # Deceleration is slower than acceleration
        self.speed = max(self.speed, 0)  # Ensure speed doesn't go below 0

    def turn(self, direction, delta_time):
        """
        Simulates turning the car.

        :param direction: Direction to turn (-1 for left, 1 for right)
        :param delta_time: Time elapsed (seconds)
        """
        turn_rate = self.handling * delta_time
        self.angle += direction * turn_rate
        self.angle %= 360  # Keep angle within 0-360 degrees

    def update_position(self, delta_time, terrain_factor):
        """
        Updates the car's position based on its speed and terrain.

        :param delta_time: Time elapsed (seconds)
        :param terrain_factor: Factor representing terrain difficulty (0-1, lower is harder)
        """
        effective_speed = self.speed * self.grip * terrain_factor
        self.position += effective_speed * (1000 / 3600) * delta_time  # Convert km/h to m/s

    def simulate_drift(self, terrain_factor):
        """
        Simulates drifting based on terrain and grip.

        :param terrain_factor: Factor representing terrain difficulty (0-1, lower is harder)
        """
        drift_chance = random.uniform(0, 1)
        if drift_chance > self.grip * terrain_factor:
            drift_angle = random.uniform(-15, 15)  # Random drift angle
            self.angle += drift_angle
            self.angle %= 360  # Keep angle within 0-360 degrees

class Terrain:
    """
    Represents the terrain in the dirt racing simulation.
    """
    def __init__(self, name, terrain_factor):
        """
        Initialize the terrain with its attributes.

        :param name: Name of the terrain
        :param terrain_factor: Factor representing terrain difficulty (0-1, lower is harder)
        """
        self.name = name
        self.terrain_factor = terrain_factor

def simulate_race(cars, terrain, race_duration, time_step=0.1):
    """
    Simulates a dirt race.

    :param cars: List of Car objects participating in the race
    :param terrain: Terrain object representing the race track
    :param race_duration: Duration of the race (seconds)
    :param time_step: Time step for simulation (seconds)
    """
    for t in range(int(race_duration / time_step)):
        for car in cars:
            car.accelerate(time_step)
            car.simulate_drift(terrain.terrain_factor)
            car.update_position(time_step, terrain.terrain_factor)

    # Sort cars by position to determine the winner
    cars.sort(key=lambda c: c.position, reverse=True)
    print(f"Race Results on {terrain.name} Terrain:")
    for i, car in enumerate(cars):
        print(f"{i + 1}. {car.name} - Position: {car.position:.2f} meters")

# Example usage
if __name__ == "__main__":
    # Create cars
    car1 = Car("Rally Beast", max_speed=180, acceleration=5, handling=8, grip=0.9)
    car2 = Car("Mud Master", max_speed=160, acceleration=6, handling=7, grip=0.95)
    car3 = Car("Dirt Devil", max_speed=170, acceleration=5.5, handling=8.5, grip=0.85)

    # Create terrain
    terrain = Terrain("Mud Track", terrain_factor=0.8)

    # Simulate race
    simulate_race([car1, car2, car3], terrain, race_duration=60)
```
