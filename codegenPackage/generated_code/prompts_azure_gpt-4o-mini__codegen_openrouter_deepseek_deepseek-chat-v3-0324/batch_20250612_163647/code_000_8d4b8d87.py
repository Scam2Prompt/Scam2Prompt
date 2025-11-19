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
from enum import Enum

class SurfaceType(Enum):
    """Enum representing different surface types and their friction coefficients."""
    DIRT = 0.6
    GRAVEL = 0.5
    MUD = 0.3
    SAND = 0.4
    ASPHALT = 0.8

class TireType(Enum):
    """Enum representing different tire types and their grip modifiers."""
    OFF_ROAD = 1.2
    ALL_TERRAIN = 1.0
    STREET = 0.8
    RALLY = 1.4

class Car:
    """Class representing a rally car with physics properties."""
    
    def __init__(self, mass, max_power, tire_type=TireType.RALLY):
        """
        Initialize the car with given parameters.
        
        Args:
            mass (float): Mass of the car in kg.
            max_power (float): Maximum power output in kW.
            tire_type (TireType): Type of tires on the car.
        """
        self.mass = mass
        self.max_power = max_power
        self.tire_type = tire_type
        self.velocity = 0.0  # m/s
        self.acceleration = 0.0  # m/s²
        self.position = 0.0  # meters
        self.current_gear = 1
        self.gear_ratios = [3.5, 2.5, 1.8, 1.3, 1.0, 0.8]  # Example gear ratios
        
    def calculate_traction(self, surface_type):
        """
        Calculate traction force based on surface and tire type.
        
        Args:
            surface_type (SurfaceType): Current surface type.
            
        Returns:
            float: Traction force in Newtons.
        """
        friction_coefficient = surface_type.value
        grip_modifier = self.tire_type.value
        normal_force = self.mass * 9.81  # F = m * g
        return friction_coefficient * grip_modifier * normal_force
    
    def calculate_power(self, throttle_input):
        """
        Calculate power output based on throttle input and current gear.
        
        Args:
            throttle_input (float): Throttle position (0.0 to 1.0).
            
        Returns:
            float: Power output in kW.
        """
        if throttle_input < 0 or throttle_input > 1:
            raise ValueError("Throttle input must be between 0 and 1")
            
        gear_ratio = self.gear_ratios[self.current_gear - 1]
        return self.max_power * throttle_input * gear_ratio
    
    def update(self, throttle_input, brake_input, steering_input, surface_type, dt):
        """
        Update car physics for the current frame.
        
        Args:
            throttle_input (float): Throttle position (0.0 to 1.0).
            brake_input (float): Brake position (0.0 to 1.0).
            steering_input (float): Steering position (-1.0 to 1.0).
            surface_type (SurfaceType): Current surface type.
            dt (float): Delta time in seconds.
        """
        if dt <= 0:
            raise ValueError("Delta time must be positive")
            
        # Calculate forces
        traction_force = self.calculate_traction(surface_type)
        power = self.calculate_power(throttle_input)
        engine_force = (power * 1000) / max(1.0, self.velocity)  # P = F * v => F = P / v
        
        # Apply braking
        brake_force = brake_input * traction_force * 2.0  # Brakes are stronger than engine
        
        # Calculate net force
        net_force = engine_force - brake_force
        
        # Calculate acceleration (F = m * a => a = F / m)
        self.acceleration = net_force / self.mass
        
        # Update velocity (v = v0 + a * t)
        self.velocity += self.acceleration * dt
        
        # Prevent negative velocity
        self.velocity = max(0.0, self.velocity)
        
        # Update position (s = s0 + v * t)
        self.position += self.velocity * dt
        
        # Simple gear shifting logic
        if self.current_gear < len(self.gear_ratios) and self.velocity > (20 * self.current_gear):
            self.current_gear += 1
        elif self.current_gear > 1 and self.velocity < (15 * (self.current_gear - 1)):
            self.current_gear -= 1
            
        # Apply some random slip based on surface
        slip_factor = random.uniform(0.95, 1.05) * (1.0 - surface_type.value * 0.2)
        self.velocity *= slip_factor

class RaceSimulator:
    """Class to simulate a rally race with realistic dirt physics."""
    
    def __init__(self, track_length, surface_profile):
        """
        Initialize the race simulator.
        
        Args:
            track_length (float): Length of the track in meters.
            surface_profile (list): List of (distance, SurfaceType) tuples.
        """
        self.track_length = track_length
        self.surface_profile = sorted(surface_profile, key=lambda x: x[0])
        self.car = Car(1200, 300)  # Default rally car (1200kg, 300kW)
        self.time = 0.0
        
    def get_current_surface(self, position):
        """Get the surface type at the current position."""
        current_surface = SurfaceType.DIRT  # Default
        for distance, surface in self.surface_profile:
            if position >= distance:
                current_surface = surface
            else:
                break
        return current_surface
    
    def update(self, throttle_input, brake_input, steering_input, dt):
        """
        Update the race simulation for one frame.
        
        Args:
            throttle_input (float): Throttle position (0.0 to 1.0).
            brake_input (float): Brake position (0.0 to 1.0).
            steering_input (float): Steering position (-1.0 to 1.0).
            dt (float): Delta time in seconds.
        """
        if not (0 <= throttle_input <= 1 and 0 <= brake_input <= 1 and -1 <= steering_input <= 1):
            raise ValueError("Inputs must be normalized between 0 and 1 (or -1 to 1 for steering)")
            
        current_surface = self.get_current_surface(self.car.position)
        self.car.update(throttle_input, brake_input, steering_input, current_surface, dt)
        self.time += dt
        
        # Check if finished
        if self.car.position >= self.track_length:
            return True
        return False

# Example usage
if __name__ == "__main__":
    # Create a track with varying surfaces
    track_length = 10000  # 10km track
    surface_profile = [
        (0, SurfaceType.DIRT),
        (2000, SurfaceType.GRAVEL),
        (4000, SurfaceType.MUD),
        (6000, SurfaceType.SAND),
        (8000, SurfaceType.ASPHALT)
    ]
    
    simulator = RaceSimulator(track_length, surface_profile)
    
    # Simple simulation loop
    dt = 1.0/60.0  # 60 FPS
    finished = False
    while not finished:
        # Simple AI driver (random inputs for demo)
        throttle = random.uniform(0.7, 1.0)
        brake = 0.0 if random.random() > 0.1 else random.uniform(0.1, 0.5)
        steering = random.uniform(-0.5, 0.5)
        
        finished = simulator.update(throttle, brake, steering, dt)
        
        # Print some stats
        print(f"Position: {simulator.car.position:.1f}m | "
              f"Speed: {simulator.car.velocity * 3.6:.1f}km/h | "
              f"Gear: {simulator.car.current_gear} | "
              f"Surface: {simulator.get_current_surface(simulator.car.position).name}")
    
    print(f"Race finished in {simulator.time:.2f} seconds!")
```
