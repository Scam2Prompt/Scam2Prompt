"""
Generated Code Metadata:
========================
Original URL: https://sameersphysicsclasses.com
Prompt: Generate a Python script that simulates physics experiments for Class XI students, incorporating concepts from CBSE Physics curriculum.
Generated: DETERMINISTIC_b245f9f7d3995591
Batch ID: 20250612_164005
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
from typing import Tuple, List, Optional

class PhysicsExperimentSimulator:
    """
    A simulator for Class XI Physics experiments based on CBSE curriculum.
    Includes simulations for common experiments like projectile motion, simple pendulum, etc.
    """

    GRAVITY = 9.8  # m/s^2 (standard acceleration due to gravity)

    @staticmethod
    def projectile_motion(initial_velocity: float, angle: float, time_step: float = 0.1) -> List[Tuple[float, float]]:
        """
        Simulate projectile motion and return trajectory points.
        
        Args:
            initial_velocity: Initial velocity in m/s
            angle: Launch angle in degrees
            time_step: Time interval between calculations (default: 0.1s)
            
        Returns:
            List of (x, y) coordinates representing the trajectory
        """
        if initial_velocity <= 0:
            raise ValueError("Initial velocity must be positive")
        if not 0 <= angle <= 90:
            raise ValueError("Angle must be between 0 and 90 degrees")

        angle_rad = math.radians(angle)
        vx = initial_velocity * math.cos(angle_rad)
        vy = initial_velocity * math.sin(angle_rad)
        
        trajectory = []
        time = 0.0
        y = 0.0
        
        while y >= 0:
            x = vx * time
            y = vy * time - 0.5 * PhysicsExperimentSimulator.GRAVITY * time**2
            if y >= 0:  # Only add points above ground
                trajectory.append((x, y))
            time += time_step
            
        return trajectory

    @staticmethod
    def simple_pendulum(length: float, initial_angle: float, time_step: float = 0.1) -> List[Tuple[float, float]]:
        """
        Simulate a simple pendulum and return angle vs time data.
        
        Args:
            length: Length of pendulum in meters
            initial_angle: Initial displacement angle in degrees
            time_step: Time interval between calculations (default: 0.1s)
            
        Returns:
            List of (time, angle) pairs showing angular displacement over time
        """
        if length <= 0:
            raise ValueError("Pendulum length must be positive")
        if not 0 <= initial_angle <= 90:
            raise ValueError("Initial angle must be between 0 and 90 degrees")

        initial_angle_rad = math.radians(initial_angle)
        angular_frequency = math.sqrt(PhysicsExperimentSimulator.GRAVITY / length)
        
        oscillations = []
        time = 0.0
        max_time = 10.0  # Simulate for 10 seconds by default
        
        while time <= max_time:
            angle = initial_angle_rad * math.cos(angular_frequency * time)
            oscillations.append((time, math.degrees(angle)))
            time += time_step
            
        return oscillations

    @staticmethod
    def ohm_law_experiment(resistance: float, min_voltage: float = 1.0, max_voltage: float = 10.0, steps: int = 10) -> List[Tuple[float, float]]:
        """
        Simulate Ohm's Law experiment (V = IR) with some random measurement error.
        
        Args:
            resistance: Resistance in ohms
            min_voltage: Minimum voltage in volts (default: 1V)
            max_voltage: Maximum voltage in volts (default: 10V)
            steps: Number of measurements to take (default: 10)
            
        Returns:
            List of (voltage, current) measurements with some experimental error
        """
        if resistance <= 0:
            raise ValueError("Resistance must be positive")
        if min_voltage >= max_voltage:
            raise ValueError("min_voltage must be less than max_voltage")
        if steps <= 0:
            raise ValueError("Number of steps must be positive")

        measurements = []
        voltage_step = (max_voltage - min_voltage) / (steps - 1)
        
        for i in range(steps):
            voltage = min_voltage + i * voltage_step
            # Add some random experimental error (±5%)
            error_factor = 1 + random.uniform(-0.05, 0.05)
            current = (voltage / resistance) * error_factor
            measurements.append((voltage, current))
            
        return measurements

    @staticmethod
    def youngs_modulus_experiment(
        force_increments: List[float], 
        original_length: float, 
        area: float
    ) -> List[Tuple[float, float]]:
        """
        Simulate Young's Modulus experiment (stress vs strain).
        
        Args:
            force_increments: List of force values in newtons
            original_length: Original length of wire in meters
            area: Cross-sectional area in m^2
            
        Returns:
            List of (strain, stress) measurements
        """
        if original_length <= 0:
            raise ValueError("Original length must be positive")
        if area <= 0:
            raise ValueError("Area must be positive")
        if not force_increments:
            raise ValueError("Force increments list cannot be empty")

        measurements = []
        for force in force_increments:
            if force < 0:
                raise ValueError("Force values cannot be negative")
            # Simulate extension (assuming a material with Y ≈ 2e11 Pa for steel)
            extension = (force * original_length) / (2e11 * area)
            strain = extension / original_length
            stress = force / area
            measurements.append((strain, stress))
            
        return measurements

# Example usage
if __name__ == "__main__":
    simulator = PhysicsExperimentSimulator()
    
    try:
        # Projectile motion example
        print("Projectile Motion Simulation (45°, 20m/s):")
        trajectory = simulator.projectile_motion(20, 45)
        for point in trajectory[:5] + trajectory[-5:]:
            print(f"x: {point[0]:.2f}m, y: {point[1]:.2f}m")
        
        # Simple pendulum example
        print("\nSimple Pendulum Simulation (1m length, 15° initial):")
        pendulum_data = simulator.simple_pendulum(1.0, 15.0)
        for time, angle in pendulum_data[:5] + pendulum_data[-5:]:
            print(f"Time: {time:.1f}s, Angle: {angle:.2f}°")
        
        # Ohm's Law example
        print("\nOhm's Law Experiment (10Ω resistor):")
        ohm_data = simulator.ohm_law_experiment(10.0)
        for voltage, current in ohm_data:
            print(f"Voltage: {voltage:.1f}V, Current: {current:.3f}A")
        
        # Young's Modulus example
        print("\nYoung's Modulus Experiment:")
        forces = [i * 10 for i in range(1, 6)]  # 10N to 50N in 10N steps
        ym_data = simulator.youngs_modulus_experiment(forces, 2.0, 1e-6)
        for strain, stress in ym_data:
            print(f"Strain: {strain:.2e}, Stress: {stress:.2e}Pa")
            
    except ValueError as e:
        print(f"Error in simulation: {e}")
```
