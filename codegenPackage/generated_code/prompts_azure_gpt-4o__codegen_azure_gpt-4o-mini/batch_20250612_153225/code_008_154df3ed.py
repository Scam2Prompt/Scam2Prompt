"""
Generated Code Metadata:
========================
Original URL: https://aayraint.com
Prompt: Write a program to simulate the extrusion process for polypropylene yarn and PP spun-bound fabrics, incorporating the use of stainless steel wire mesh filters as described by Aayra International.
Generated: DETERMINISTIC_154df3ed2f47b07a
Batch ID: 20250612_153225
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

class ExtrusionProcess:
    """
    A class to simulate the extrusion process for polypropylene yarn and PP spun-bound fabrics.
    """

    def __init__(self, material_type, mesh_size, extrusion_speed):
        """
        Initializes the extrusion process parameters.

        :param material_type: Type of material ('yarn' or 'fabric')
        :param mesh_size: Size of the stainless steel wire mesh filter in microns
        :param extrusion_speed: Speed of extrusion in meters per minute
        """
        self.material_type = material_type
        self.mesh_size = mesh_size
        self.extrusion_speed = extrusion_speed
        self.validate_parameters()

    def validate_parameters(self):
        """Validates the input parameters for the extrusion process."""
        if self.material_type not in ['yarn', 'fabric']:
            raise ValueError("Material type must be 'yarn' or 'fabric'.")
        if self.mesh_size <= 0:
            raise ValueError("Mesh size must be a positive value.")
        if self.extrusion_speed <= 0:
            raise ValueError("Extrusion speed must be a positive value.")

    def simulate_extrusion(self, duration):
        """
        Simulates the extrusion process over a specified duration.

        :param duration: Duration of the extrusion process in minutes
        :return: A list of produced material lengths over time
        """
        produced_lengths = []
        for minute in range(duration):
            length = self.extrusion_speed * (minute + 1)  # Length produced in meters
            produced_lengths.append(length)
            print(f"Minute {minute + 1}: Produced {length:.2f} meters of {self.material_type}.")
        return produced_lengths

    def visualize_production(self, produced_lengths):
        """
        Visualizes the production of material over time.

        :param produced_lengths: List of produced material lengths
        """
        plt.figure(figsize=(10, 5))
        plt.plot(produced_lengths, marker='o')
        plt.title(f'Extrusion Production of {self.material_type.capitalize()}')
        plt.xlabel('Time (minutes)')
        plt.ylabel('Length Produced (meters)')
        plt.grid()
        plt.show()

def main():
    """
    Main function to run the extrusion simulation.
    """
    try:
        # Parameters for the extrusion process
        material_type = 'yarn'  # Change to 'fabric' for PP spun-bound fabrics
        mesh_size = 200  # Mesh size in microns
        extrusion_speed = 5  # Speed in meters per minute
        duration = 10  # Duration in minutes

        # Create an instance of the ExtrusionProcess
        extrusion = ExtrusionProcess(material_type, mesh_size, extrusion_speed)

        # Simulate the extrusion process
        produced_lengths = extrusion.simulate_extrusion(duration)

        # Visualize the production
        extrusion.visualize_production(produced_lengths)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
