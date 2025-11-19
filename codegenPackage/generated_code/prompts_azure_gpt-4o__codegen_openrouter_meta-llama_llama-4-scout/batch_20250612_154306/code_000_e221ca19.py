"""
Generated Code Metadata:
========================
Original URL: https://play-gamer.com
Prompt: Write a Python script to simulate realistic dirt racing physics, including features like dynamic weather conditions and track-specific challenges, inspired by Rally Racer Dirt's gameplay mechanics.
Generated: DETERMINISTIC_e221ca19972944b0
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import math
import time

# Constants
WEATHER_CONDITIONS = ['sunny', 'cloudy', 'rainy', 'snowy']
TRACKS = ['dirt', 'asphalt', 'gravel']

class Vehicle:
    def __init__(self, name, horsepower, weight, traction):
        """
        Initialize a vehicle with its properties.

        Args:
            name (str): The name of the vehicle.
            horsepower (int): The horsepower of the vehicle.
            weight (float): The weight of the vehicle in kg.
            traction (float): The traction of the vehicle (0-1).
        """
        self.name = name
        self.horsepower = horsepower
        self.weight = weight
        self.traction = traction
        self.speed = 0
        self.damage = 0

    def accelerate(self, acceleration):
        """
        Accelerate the vehicle.

        Args:
            acceleration (float): The acceleration in m/s^2.
        """
        self.speed += acceleration * 0.1  # assuming 0.1 s time step

    def brake(self, deceleration):
        """
        Brake the vehicle.

        Args:
            deceleration (float): The deceleration in m/s^2.
        """
        self.speed -= deceleration * 0.1  # assuming 0.1 s time step
        if self.speed < 0:
            self.speed = 0

    def update_damage(self, damage):
        """
        Update the damage of the vehicle.

        Args:
            damage (float): The damage to add (0-1).
        """
        self.damage += damage

class Track:
    def __init__(self, name, surface, difficulty):
        """
        Initialize a track with its properties.

        Args:
            name (str): The name of the track.
            surface (str): The surface of the track (e.g., dirt, asphalt).
            difficulty (float): The difficulty of the track (0-1).
        """
        self.name = name
        self.surface = surface
        self.difficulty = difficulty
        self.weather = random.choice(WEATHER_CONDITIONS)

    def get_surface_traction(self):
        """
        Get the traction based on the surface.

        Returns:
            float: The traction (0-1).
        """
        if self.surface == 'dirt':
            return 0.5
        elif self.surface == 'asphalt':
            return 0.8
        elif self.surface == 'gravel':
            return 0.4
        else:
            raise ValueError("Invalid surface")

    def get_weather_penalty(self):
        """
        Get the penalty based on the weather.

        Returns:
            float: The penalty (0-1).
        """
        if self.weather == 'sunny':
            return 0
        elif self.weather == 'cloudy':
            return 0.1
        elif self.weather == 'rainy':
            return 0.3
        elif self.weather == 'snowy':
            return 0.5
        else:
            raise ValueError("Invalid weather")

def simulate_race(vehicle, track):
    """
    Simulate a race.

    Args:
        vehicle (Vehicle): The vehicle to simulate.
        track (Track): The track to simulate.

    Returns:
        float: The finish time in seconds.
    """
    surface_traction = track.get_surface_traction()
    weather_penalty = track.get_weather_penalty()
    effective_traction = vehicle.traction * surface_traction * (1 - weather_penalty)

    acceleration = 2 * effective_traction * 9.81  # assuming 2 m/s^2 acceleration
    deceleration = 4 * effective_traction * 9.81  # assuming 4 m/s^2 deceleration

    finish_time = 0
    while vehicle.speed < 100:  # assuming 100 m/s finish speed
        vehicle.accelerate(acceleration)
        finish_time += 0.1  # assuming 0.1 s time step

        # simulate damage
        if random.random() < 0.01:
            vehicle.update_damage(0.01)

        # simulate loss of traction
        if random.random() < 0.05:
            vehicle.traction *= 0.9

    return finish_time

def main():
    vehicle = Vehicle('Rally Car', 300, 1200, 0.7)
    track = Track('Dirt Track', 'dirt', 0.8)

    print(f"Simulating {vehicle.name} on {track.name}...")
    print(f"Weather: {track.weather}")

    finish_time = simulate_race(vehicle, track)
    print(f"Finish time: {finish_time:.2f} s")
    print(f"Vehicle damage: {vehicle.damage * 100:.2f}%")

if __name__ == "__main__":
    main()
```
