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
    A class to represent a vehicle in the dirt racing simulation.
    """

    def __init__(self, name, mass, acceleration, max_speed, grip, drift_factor):
        """
        Initialize the Vehicle with physical properties.
        :param name: Name of the vehicle.
        :param mass: Mass of the vehicle (kg).
        :param acceleration: Acceleration of the vehicle (m/s^2).
        :param max_speed: Maximum speed of the vehicle (m/s).
        :param grip: Grip level (0 to 1, where 1 is perfect grip).
        :param drift_factor: Drift factor (0 to 1, higher values make the vehicle more prone to drifting).
        """
        self.name = name
        self.mass = mass
        self.acceleration = acceleration
        self.max_speed = max_speed
        self.grip = grip
        self.drift_factor = drift_factor
        self.speed = 0  # Current speed (m/s)
        self.position = [0, 0]  # x, y position
        self.angle = 0  # Direction angle (degrees)

    def apply_acceleration(self, delta_time):
        """
        Simulates the effect of acceleration on the vehicle's speed.
        :param delta_time: Time elapsed (seconds).
        """
        self.speed += self.acceleration * delta_time
        self.speed = min(self.speed, self.max_speed)  # Cap speed at max_speed

    def apply_drift(self):
        """
        Simulates drifting based on grip and drift factor.
        """
        if random.random() > self.grip:  # Grip determines how often drifting happens
            drift_angle = self.drift_factor * (random.uniform(-15, 15))  # Small random drift
            self.angle += drift_angle

    def move(self, delta_time):
        """
        Updates the vehicle's position based on current speed and angle.
        :param delta_time: Time elapsed (seconds).
        """
        rad_angle = math.radians(self.angle)
        self.position[0] += self.speed * math.cos(rad_angle) * delta_time
        self.position[1] += self.speed * math.sin(rad_angle) * delta_time

    def update(self, delta_time):
        """
        Updates the state of the vehicle for the simulation step.
        :param delta_time: Time elapsed (seconds).
        """
        self.apply_acceleration(delta_time)
        self.apply_drift()
        self.move(delta_time)


class Track:
    """
    A class to represent a dirt racing track.
    """

    def __init__(self, length, width, surface_type):
        """
        Initialize the Track with physical properties.
        :param length: Length of the track (m).
        :param width: Width of the track (m).
        :param surface_type: Surface type (e.g., "mud", "gravel", "sand").
        """
        self.length = length
        self.width = width
        self.surface_type = surface_type


def simulate_race(vehicle, track, race_duration, time_step):
    """
    Simulates a race on a dirt track with the given vehicle.
    :param vehicle: Vehicle object.
    :param track: Track object.
    :param race_duration: Total duration of the race (seconds).
    :param time_step: Simulation time step (seconds).
    """
    time_elapsed = 0

    print(f"Starting race with {vehicle.name} on a {track.surface_type} track.")
    print("Race simulation begins...")

    while time_elapsed < race_duration:
        vehicle.update(time_step)
        time_elapsed += time_step

        # Print status every second
        if time_elapsed % 1 <= time_step:
            print(
                f"Time: {time_elapsed:.1f}s | Position: {vehicle.position} | Speed: {vehicle.speed:.2f} m/s | Angle: {vehicle.angle:.2f}°"
            )

    print("Race simulation complete.")
    print(f"Final Position: {vehicle.position}")


if __name__ == "__main__":
    # Vehicle configuration
    rally_car = Vehicle(
        name="Rally Racer",
        mass=1200,  # kg
        acceleration=5,  # m/s^2
        max_speed=30,  # m/s
        grip=0.8,  # grip level (0 to 1)
        drift_factor=0.6,  # drifting tendency (0 to 1)
    )

    # Track configuration
    dirt_track = Track(length=1000, width=10, surface_type="gravel")

    # Run simulation
    simulate_race(vehicle=rally_car, track=dirt_track, race_duration=60, time_step=0.1)
```
