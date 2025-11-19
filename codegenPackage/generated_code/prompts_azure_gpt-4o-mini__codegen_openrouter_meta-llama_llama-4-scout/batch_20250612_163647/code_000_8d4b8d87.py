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
import numpy as np

class Vehicle:
    def __init__(self, mass, power, gear_ratios, tire_friction_coefficient, suspension_stiffness, suspension_damping):
        """
        Initialize the vehicle properties.

        Args:
            mass (float): Vehicle mass in kg.
            power (float): Vehicle power in horsepower.
            gear_ratios (list): List of gear ratios.
            tire_friction_coefficient (float): Tire friction coefficient.
            suspension_stiffness (float): Suspension stiffness in N/m.
            suspension_damping (float): Suspension damping in Ns/m.
        """
        self.mass = mass
        self.power = power
        self.gear_ratios = gear_ratios
        self.tire_friction_coefficient = tire_friction_coefficient
        self.suspension_stiffness = suspension_stiffness
        self.suspension_damping = suspension_damping
        self.velocity = 0  # initial velocity in m/s
        self.acceleration = 0  # initial acceleration in m/s^2
        self.gear = 1  # initial gear
        self.rpm = 0  # initial engine RPM

    def update(self, delta_time, terrain_friction_coefficient):
        """
        Update the vehicle state.

        Args:
            delta_time (float): Time step in seconds.
            terrain_friction_coefficient (float): Terrain friction coefficient.
        """
        # calculate the traction force
        traction_force = self.tire_friction_coefficient * terrain_friction_coefficient * self.mass * 9.81

        # calculate the engine torque
        engine_torque = self.power * 745.7 / (self.rpm + 1e-6)  # convert horsepower to Nm

        # calculate the wheel torque
        wheel_torque = engine_torque * self.gear_ratios[self.gear - 1]

        # calculate the wheel angular velocity
        wheel_angular_velocity = self.velocity / 0.35  # assume a wheel radius of 0.35m

        # calculate the acceleration
        self.acceleration = (wheel_torque * self.gear_ratios[self.gear - 1] / 0.35 - traction_force) / self.mass

        # update the velocity
        self.velocity += self.acceleration * delta_time

        # update the RPM
        self.rpm = wheel_angular_velocity * 60 / (2 * math.pi)

        # update the gear
        if self.rpm > 5000 and self.gear < len(self.gear_ratios):
            self.gear += 1
        elif self.rpm < 2000 and self.gear > 1:
            self.gear -= 1

    def get_state(self):
        """
        Get the vehicle state.

        Returns:
            dict: Vehicle state.
        """
        return {
            'velocity': self.velocity,
            'acceleration': self.acceleration,
            'gear': self.gear,
            'rpm': self.rpm
        }


class Suspension:
    def __init__(self, stiffness, damping):
        """
        Initialize the suspension properties.

        Args:
            stiffness (float): Suspension stiffness in N/m.
            damping (float): Suspension damping in Ns/m.
        """
        self.stiffness = stiffness
        self.damping = damping
        self.displacement = 0  # initial displacement in m
        self.velocity = 0  # initial velocity in m/s

    def update(self, delta_time, force):
        """
        Update the suspension state.

        Args:
            delta_time (float): Time step in seconds.
            force (float): Force applied to the suspension in N.
        """
        # calculate the acceleration
        acceleration = (force - self.stiffness * self.displacement - self.damping * self.velocity) / 1000  # assume a mass of 1000kg

        # update the velocity and displacement
        self.velocity += acceleration * delta_time
        self.displacement += self.velocity * delta_time

    def get_state(self):
        """
        Get the suspension state.

        Returns:
            dict: Suspension state.
        """
        return {
            'displacement': self.displacement,
            'velocity': self.velocity
        }


class Terrain:
    def __init__(self, friction_coefficient):
        """
        Initialize the terrain properties.

        Args:
            friction_coefficient (float): Terrain friction coefficient.
        """
        self.friction_coefficient = friction_coefficient

    def get_friction_coefficient(self):
        """
        Get the terrain friction coefficient.

        Returns:
            float: Terrain friction coefficient.
        """
        return self.friction_coefficient


def main():
    # create a vehicle
    vehicle = Vehicle(
        mass=1500,
        power=300,
        gear_ratios=[4.5, 2.5, 1.7, 1.2, 0.9],
        tire_friction_coefficient=0.8,
        suspension_stiffness=10000,
        suspension_damping=5000
    )

    # create a suspension
    suspension = Suspension(
        stiffness=10000,
        damping=5000
    )

    # create a terrain
    terrain = Terrain(
        friction_coefficient=0.6
    )

    # simulate the vehicle
    delta_time = 0.01
    time = 0
    while time < 100:
        vehicle.update(delta_time, terrain.get_friction_coefficient())
        suspension.update(delta_time, vehicle.get_state()['acceleration'] * vehicle.mass)
        print(f'Time: {time:.2f}, Velocity: {vehicle.get_state()["velocity"]:.2f}, Gear: {vehicle.get_state()["gear"]}, RPM: {vehicle.get_state()["rpm"]:.2f}, Displacement: {suspension.get_state()["displacement"]:.2f}')
        time += delta_time


if __name__ == '__main__':
    main()
```
