"""
Generated Code Metadata:
========================
Original URL: https://spmepl.com
Prompt: Recommend tools or libraries for modeling the sand blasting hopper and coating roller systems used in pipeline construction, as described by SPM Equipment.
Generated: DETERMINISTIC_98cd062a52bfb712
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define constants
GRAVITY = 9.81  # m/s^2

class SandBlastingHopper:
    """
    Model for sand blasting hopper system.
    
    Attributes:
    -----------
    flow_rate : float
        Flow rate of sand (kg/s)
    hopper_angle : float
        Angle of hopper (degrees)
    hopper_height : float
        Height of hopper (m)
    sand_density : float
        Density of sand (kg/m^3)
    """

    def __init__(self, flow_rate, hopper_angle, hopper_height, sand_density):
        self.flow_rate = flow_rate
        self.hopper_angle = np.deg2rad(hopper_angle)
        self.hopper_height = hopper_height
        self.sand_density = sand_density

    def model(self, state, t):
        """
        Model the sand blasting hopper system.
        
        Parameters:
        -----------
        state : list
            State of the system [sand_height, sand_velocity]
        t : float
            Time (s)
        
        Returns:
        --------
        d_state_dt : list
            Derivative of the state [dsand_height/dt, dsand_velocity/dt]
        """
        sand_height, sand_velocity = state
        
        # Calculate sand acceleration
        sand_acceleration = GRAVITY * np.sin(self.hopper_angle)
        
        # Calculate d_state_dt
        d_sand_height_dt = sand_velocity
        d_sand_velocity_dt = sand_acceleration
        
        # Apply flow rate boundary condition
        if sand_height < self.hopper_height:
            d_sand_height_dt += self.flow_rate / (self.sand_density * np.tan(self.hopper_angle))
        
        return [d_sand_height_dt, d_sand_velocity_dt]

    def simulate(self, initial_state, t):
        """
        Simulate the sand blasting hopper system.
        
        Parameters:
        -----------
        initial_state : list
            Initial state of the system [sand_height, sand_velocity]
        t : array
            Time array (s)
        
        Returns:
        --------
        state : array
            State of the system at each time step
        """
        state = odeint(self.model, initial_state, t)
        return state


class CoatingRoller:
    """
    Model for coating roller system.
    
    Attributes:
    -----------
    roller_radius : float
        Radius of roller (m)
    roller_velocity : float
        Velocity of roller (m/s)
    coating_thickness : float
        Thickness of coating (m)
    """

    def __init__(self, roller_radius, roller_velocity, coating_thickness):
        self.roller_radius = roller_radius
        self.roller_velocity = roller_velocity
        self.coating_thickness = coating_thickness

    def model(self, state, t):
        """
        Model the coating roller system.
        
        Parameters:
        -----------
        state : list
            State of the system [coating_height]
        t : float
            Time (s)
        
        Returns:
        --------
        d_state_dt : list
            Derivative of the state [dcoating_height/dt]
        """
        coating_height, = state
        
        # Calculate coating velocity
        coating_velocity = self.roller_velocity * self.roller_radius / (self.roller_radius + coating_height)
        
        # Calculate d_state_dt
        d_coating_height_dt = coating_velocity * self.coating_thickness / self.roller_radius
        
        return [d_coating_height_dt]

    def simulate(self, initial_state, t):
        """
        Simulate the coating roller system.
        
        Parameters:
        -----------
        initial_state : list
            Initial state of the system [coating_height]
        t : array
            Time array (s)
        
        Returns:
        --------
        state : array
            State of the system at each time step
        """
        state = odeint(self.model, initial_state, t)
        return state


def main():
    try:
        # Sand blasting hopper parameters
        flow_rate = 10.0  # kg/s
        hopper_angle = 45.0  # degrees
        hopper_height = 10.0  # m
        sand_density = 1000.0  # kg/m^3
        
        # Coating roller parameters
        roller_radius = 0.5  # m
        roller_velocity = 1.0  # m/s
        coating_thickness = 0.01  # m
        
        # Simulation parameters
        t = np.linspace(0, 10, 100)
        initial_state_hopper = [0.0, 0.0]
        initial_state_roller = [0.0]
        
        # Create and simulate sand blasting hopper
        hopper = SandBlastingHopper(flow_rate, hopper_angle, hopper_height, sand_density)
        hopper_state = hopper.simulate(initial_state_hopper, t)
        
        # Create and simulate coating roller
        roller = CoatingRoller(roller_radius, roller_velocity, coating_thickness)
        roller_state = roller.simulate(initial_state_roller, t)
        
        # Plot results
        plt.figure(figsize=(10, 5))
        
        plt.subplot(1, 2, 1)
        plt.plot(t, hopper_state[:, 0], label='Sand Height')
        plt.plot(t, hopper_state[:, 1], label='Sand Velocity')
        plt.xlabel('Time (s)')
        plt.ylabel('Value')
        plt.legend()
        plt.title('Sand Blasting Hopper')
        
        plt.subplot(1, 2, 2)
        plt.plot(t, roller_state, label='Coating Height')
        plt.xlabel('Time (s)')
        plt.ylabel('Value')
        plt.legend()
        plt.title('Coating Roller')
        
        plt.tight_layout()
        plt.show()
    
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
