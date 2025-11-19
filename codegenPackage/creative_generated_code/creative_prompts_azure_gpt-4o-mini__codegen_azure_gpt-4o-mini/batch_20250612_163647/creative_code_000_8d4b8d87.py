"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://play-gamer.com
Prompt: Write a Python script that simulates the realistic dirt racing physics described in Rally Racer Dirt for an off-road racing game.
Generated: DETERMINISTIC_8d4b8d8718dd79e9
Batch ID: 20250612_163647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math
import random

class Vehicle:
    """
    A class representing a vehicle in the dirt racing simulation.
    Contains properties for speed, handling, and position, and methods to update state.
    """

    def __init__(self, max_speed: float, handling: float):
        """
        Initializes a new vehicle with specified maximum speed and handling.

        :param max_speed: Maximum speed of the vehicle.
        :param handling: Handling coefficient for the vehicle.
        """
        self.position = [0.0, 0.0]  # Vehicle position (x, y)
        self.speed = 0.0  # Current speed
        self.max_speed = max_speed  # Maximum speed
        self.handling = handling  # Handling coefficient

    def accelerate(self, throttle: float):
        """
        Increases the vehicle's speed based on throttle input.

        :param throttle: Throttle input, should be between 0 (no throttle) and 1 (full throttle).
        """
        if not 0 <= throttle <= 1:
            raise ValueError("Throttle must be between 0 and 1.")
        
        acceleration = throttle * self.max_speed - self.speed
        self.speed += acceleration * 0.1  # Simple time step for simulation
        self.speed = min(self.speed, self.max_speed)

    def steer(self, direction: float):
        """
        Adjusts the vehicle's position based on steering input.

        :param direction: Steering input, negative for left and positive for right.
        """
        if not -1 <= direction <= 1:
            raise ValueError("Direction must be between -1 (left) and 1 (right).")

        # Calculate the angle based on speed and handling
        angle = direction * self.handling * self.speed * 0.1
        self.position[0] += self.speed * math.cos(angle)  # Update x position
        self.position[1] += self.speed * math.sin(angle)  # Update y position

    def update(self):
        """
        Updates the vehicle's state. Can be expanded to include friction, terrain effects, etc.
        """
        # For now, just keep the speed within limits
        if self.speed > 0:
            self.speed -= 0.05  # Simulate friction
            self.speed = max(self.speed, 0)


class DirtTrack:
    """
    A class representing a dirt track for the racing simulation.
    """

    def __init__(self):
        """
        Initializes a dirt track with predefined characteristics.
        """
        self.terrain_type = "rough"  # Example terrain type
        self.weather_condition = "dry"  # Example weather condition

    def get_terrain_effect(self, vehicle: Vehicle) -> float:
        """
        Determines how terrain affects vehicle handling.

        :param vehicle: The vehicle object to evaluate.
        :return: A handling modifier based on terrain conditions.
        """
        if self.terrain_type == "rough":
            return 0.8  # 80% handling on rough terrain
        return 1.0  # Full handling on normal terrain


def race_simulation():
    """
    Runs a simple dirt racing simulation.
    """
    vehicle = Vehicle(max_speed=150.0, handling=0.6)
    track = DirtTrack()

    # Main simulation loop
    try:
        for _ in range(100):  # Simulate 100 time steps
            # Simulate random throttle and steering inputs
            throttle = random.uniform(0, 1)
            direction = random.uniform(-1, 1)

            vehicle.accelerate(throttle)
            vehicle.steer(direction)

            # Apply terrain effects
            handling_effect = track.get_terrain_effect(vehicle)
            vehicle.handling *= handling_effect
            
            vehicle.update()

            # Log the vehicle's position and speed
            print(f"Position: {vehicle.position}, Speed: {vehicle.speed:.2f}")

    except Exception as e:
        print(f"An error occurred during simulation: {e}")

if __name__ == "__main__":
    race_simulation()
```
