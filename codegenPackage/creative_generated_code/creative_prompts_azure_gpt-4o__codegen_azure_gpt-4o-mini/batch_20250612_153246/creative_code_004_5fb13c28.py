"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spmepl.com
Prompt: Suggest libraries or frameworks for simulating the behavior of pipe lowering cradles with PU-coated slings, referencing the features highlighted by SPM Equipment.
Generated: DETERMINISTIC_5fb13c28ee171da9
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for simulation
import numpy as np
import matplotlib.pyplot as plt

class PipeLiftingSimulation:
    """
    A class to simulate the behavior of pipe lowering cradles with PU-coated slings.
    This simulation will provide a basic overview of the forces and angles involved in the process.
    """

    def __init__(self, pipe_weight, sling_length, cradle_angle):
        """
        Initializes the simulation parameters.

        :param pipe_weight: Weight of the pipe (in Newtons)
        :param sling_length: Length of the sling (in meters)
        :param cradle_angle: Angle of the cradle (in degrees)
        """
        self.pipe_weight = pipe_weight
        self.sling_length = sling_length
        self.cradle_angle = cradle_angle
        self.gravity = 9.81  # Acceleration due to gravity in m/s^2
        self.forces = []

    def calculate_forces(self):
        """
        Calculate the forces acting on the slings and the cradle.

        :return: A dictionary containing the calculated forces.
        """
        # Convert angle from degrees to radians for calculations
        angle_rad = np.radians(self.cradle_angle)

        # Calculate the vertical and horizontal components of the force
        vertical_force = self.pipe_weight * np.cos(angle_rad)
        horizontal_force = self.pipe_weight * np.sin(angle_rad)

        # Store the forces in a list
        self.forces = {
            "Vertical Force (N)": vertical_force,
            "Horizontal Force (N)": horizontal_force,
            "Total Force (N)": np.sqrt(vertical_force**2 + horizontal_force**2)
        }

        return self.forces

    def plot_forces(self):
        """
        Plot the forces acting on the pipe and cradle.

        :raises RuntimeError: If forces have not been calculated yet.
        """
        if not self.forces:
            raise RuntimeError("Forces must be calculated before plotting.")
        
        labels = self.forces.keys()
        values = self.forces.values()

        # Create a bar chart for visualizing the forces
        plt.bar(labels, values, color=['blue', 'orange', 'green'])
        plt.ylabel('Force (N)')
        plt.title('Forces Acting on Pipe Lowering Cradle')
        plt.grid(True)
        plt.show()

def main():
    """
    Main function to run the pipe lifting simulation.
    """
    try:
        # User-defined parameters
        pipe_weight = 1000  # Weight of the pipe in Newtons
        sling_length = 5.0  # Length of the sling in meters
        cradle_angle = 30   # Angle of the cradle in degrees

        # Create an instance of the simulation
        simulation = PipeLiftingSimulation(pipe_weight, sling_length, cradle_angle)

        # Calculate forces and print the results
        forces = simulation.calculate_forces()
        print("Calculated Forces:", forces)

        # Plot the forces
        simulation.plot_forces()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
