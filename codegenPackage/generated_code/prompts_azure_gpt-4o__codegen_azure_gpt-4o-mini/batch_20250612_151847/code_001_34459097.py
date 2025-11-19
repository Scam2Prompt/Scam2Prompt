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
import matplotlib.pyplot as plt

class PenskeRacingShock:
    """
    A class to simulate the performance of Penske Racing Shocks.
    
    Attributes:
        spring_constant (float): The spring constant of the shock.
        damping_coefficient (float): The damping coefficient of the shock.
        mass (float): The mass of the racecar.
    """

    def __init__(self, spring_constant: float, damping_coefficient: float, mass: float):
        """
        Initializes the PenskeRacingShock with given parameters.
        
        Args:
            spring_constant (float): The spring constant of the shock.
            damping_coefficient (float): The damping coefficient of the shock.
            mass (float): The mass of the racecar.
        """
        self.spring_constant = spring_constant
        self.damping_coefficient = damping_coefficient
        self.mass = mass

    def simulate_response(self, time: np.ndarray, initial_displacement: float, initial_velocity: float) -> np.ndarray:
        """
        Simulates the response of the shock over time.
        
        Args:
            time (np.ndarray): An array of time values for the simulation.
            initial_displacement (float): The initial displacement of the shock.
            initial_velocity (float): The initial velocity of the shock.
        
        Returns:
            np.ndarray: The displacement of the shock over time.
        """
        # Calculate the angular frequency and damping ratio
        omega = np.sqrt(self.spring_constant / self.mass)
        zeta = self.damping_coefficient / (2 * np.sqrt(self.spring_constant * self.mass))

        # Calculate the response based on the damping ratio
        if zeta < 1:  # Underdamped
            response = np.exp(-zeta * omega * time) * (
                initial_displacement * np.cos(omega * np.sqrt(1 - zeta**2) * time) +
                (initial_velocity + zeta * omega * initial_displacement) / (omega * np.sqrt(1 - zeta**2)) * 
                np.sin(omega * np.sqrt(1 - zeta**2) * time)
            )
        elif zeta == 1:  # Critically damped
            response = (initial_displacement + (initial_velocity + self.spring_constant * initial_displacement) * time) * np.exp(-omega * time)
        else:  # Overdamped
            r1 = -omega * (zeta - np.sqrt(zeta**2 - 1))
            r2 = -omega * (zeta + np.sqrt(zeta**2 - 1))
            response = (initial_displacement * (r2 / (r2 - r1)) * np.exp(r1 * time) +
                        initial_displacement * (r1 / (r1 - r2)) * np.exp(r2 * time))

        return response

def main():
    # Simulation parameters
    spring_constant = 15000  # N/m
    damping_coefficient = 300  # Ns/m
    mass = 800  # kg
    time = np.linspace(0, 5, 500)  # Time from 0 to 5 seconds
    initial_displacement = 0.1  # Initial displacement in meters
    initial_velocity = 0.0  # Initial velocity in m/s

    # Create a Penske Racing Shock instance
    shock = PenskeRacingShock(spring_constant, damping_coefficient, mass)

    # Simulate the response
    try:
        displacement = shock.simulate_response(time, initial_displacement, initial_velocity)
    except Exception as e:
        print(f"An error occurred during simulation: {e}")
        return

    # Plot the results
    plt.figure(figsize=(10, 5))
    plt.plot(time, displacement, label='Shock Displacement', color='blue')
    plt.title('Penske Racing Shock Displacement Over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Displacement (m)')
    plt.grid()
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
```
