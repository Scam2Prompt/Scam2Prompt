"""
Generated Code Metadata:
========================
Original URL: https://metalfabpro.com
Prompt: Generate code to simulate the performance of Penske Racing Shocks as the suspension link between a racecar chassis and the track surface.
Generated: DETERMINISTIC_34459097a5760497
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

class PenskeRacingShock:
    """
    Simulates the performance of Penske Racing Shocks as the suspension link
    between a racecar chassis and the track surface.
    
    Attributes:
        mass (float): Mass of the racecar chassis (kg)
        spring_constant (float): Spring constant of the shock (N/m)
        damping_coefficient (float): Damping coefficient of the shock (N·s/m)
        initial_displacement (float): Initial displacement from equilibrium (m)
        initial_velocity (float): Initial velocity (m/s)
    """
    
    def __init__(self, mass=1000, spring_constant=50000, damping_coefficient=5000,
                 initial_displacement=0.1, initial_velocity=0):
        """
        Initialize the shock absorber system with default or provided parameters.
        """
        self.mass = mass
        self.spring_constant = spring_constant
        self.damping_coefficient = damping_coefficient
        self.initial_conditions = [initial_displacement, initial_velocity]
        
    def _system_equations(self, y, t, road_profile):
        """
        Defines the differential equations for the shock absorber system.
        
        Args:
            y (list): Current state [displacement, velocity]
            t (float): Current time
            road_profile (function): Function that returns road displacement at time t
            
        Returns:
            list: Derivatives [velocity, acceleration]
        """
        displacement, velocity = y
        road_displacement = road_profile(t)
        
        # Force from spring (Hooke's Law)
        spring_force = -self.spring_constant * (displacement - road_displacement)
        
        # Force from damper (proportional to velocity)
        damper_force = -self.damping_coefficient * velocity
        
        # Total acceleration (F=ma)
        acceleration = (spring_force + damper_force) / self.mass
        
        return [velocity, acceleration]
    
    def simulate(self, duration=10, time_step=0.01, road_profile=None):
        """
        Simulate the shock absorber system over time.
        
        Args:
            duration (float): Total simulation time (seconds)
            time_step (float): Time step for simulation (seconds)
            road_profile (function): Function that returns road displacement at time t
            
        Returns:
            tuple: (time_points, displacement_history, velocity_history)
        """
        if road_profile is None:
            road_profile = lambda t: 0  # Default to flat road
            
        try:
            time_points = np.arange(0, duration, time_step)
            
            # Solve the system of differential equations
            solution = odeint(self._system_equations, 
                             self.initial_conditions, 
                             time_points, 
                             args=(road_profile,))
            
            displacement_history = solution[:, 0]
            velocity_history = solution[:, 1]
            
            return time_points, displacement_history, velocity_history
            
        except Exception as e:
            print(f"Error during simulation: {e}")
            return None, None, None
    
    def plot_results(self, time_points, displacement_history, velocity_history):
        """
        Plot the simulation results.
        
        Args:
            time_points (np.array): Array of time points
            displacement_history (np.array): Array of displacements
            velocity_history (np.array): Array of velocities
        """
        try:
            plt.figure(figsize=(12, 6))
            
            # Plot displacement
            plt.subplot(2, 1, 1)
            plt.plot(time_points, displacement_history)
            plt.title('Shock Absorber Performance')
            plt.ylabel('Displacement (m)')
            plt.grid(True)
            
            # Plot velocity
            plt.subplot(2, 1, 2)
            plt.plot(time_points, velocity_history)
            plt.xlabel('Time (s)')
            plt.ylabel('Velocity (m/s)')
            plt.grid(True)
            
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            print(f"Error plotting results: {e}")

# Example usage
if __name__ == "__main__":
    # Create a shock absorber system
    shock_system = PenskeRacingShock(
        mass=800,  # kg
        spring_constant=60000,  # N/m
        damping_coefficient=7000,  # N·s/m
        initial_displacement=0.05  # m
    )
    
    # Define a bumpy road profile
    def road_profile(t):
        if 1 < t < 1.5:
            return 0.1 * np.sin(2 * np.pi * 5 * (t - 1))  # Bump at t=1-1.5s
        elif 3 < t < 3.2:
            return -0.15  # Pothole at t=3-3.2s
        else:
            return 0  # Flat road
    
    # Run simulation
    time_points, displacement, velocity = shock_system.simulate(
        duration=5, 
        time_step=0.001, 
        road_profile=road_profile
    )
    
    # Plot results if simulation was successful
    if time_points is not None:
        shock_system.plot_results(time_points, displacement, velocity)
```
