"""
Generated Code Metadata:
========================
Original URL: https://phantom-ss.com
Prompt: Write Python code to model and visualize the performance of Brembo brakes and EDC rotors in a racing simulation, inspired by the Phantom SS build.
Generated: DETERMINISTIC_0979c384c0b22852
Batch ID: 20250612_154115
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

class BrakePerformance:
    """
    A class to model the performance of Brembo brakes and EDC rotors in a racing simulation.
    """

    def __init__(self, brake_force, rotor_diameter, weight):
        """
        Initializes the BrakePerformance class with brake specifications.

        Parameters:
        - brake_force (float): The maximum braking force in Newtons.
        - rotor_diameter (float): The diameter of the rotor in meters.
        - weight (float): The weight of the vehicle in kilograms.
        """
        self.brake_force = brake_force
        self.rotor_diameter = rotor_diameter
        self.weight = weight

    def calculate_braking_distance(self, speed):
        """
        Calculates the braking distance based on the current speed.

        Parameters:
        - speed (float): The speed of the vehicle in meters per second.

        Returns:
        - float: The calculated braking distance in meters.
        """
        if speed < 0:
            raise ValueError("Speed must be a non-negative value.")
        
        # Using the formula: d = v^2 / (2 * a)
        # where a = F / m (acceleration)
        acceleration = self.brake_force / self.weight
        braking_distance = (speed ** 2) / (2 * acceleration)
        return braking_distance

    def simulate_braking(self, speeds):
        """
        Simulates the braking performance over a range of speeds.

        Parameters:
        - speeds (list): A list of speeds in meters per second.

        Returns:
        - list: A list of braking distances corresponding to the input speeds.
        """
        distances = []
        for speed in speeds:
            try:
                distance = self.calculate_braking_distance(speed)
                distances.append(distance)
            except ValueError as e:
                print(f"Error calculating distance for speed {speed}: {e}")
                distances.append(float('inf'))  # Append infinity for invalid speeds
        return distances

    def visualize_performance(self, speeds, distances):
        """
        Visualizes the braking performance using a line plot.

        Parameters:
        - speeds (list): A list of speeds in meters per second.
        - distances (list): A list of braking distances in meters.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(speeds, distances, marker='o', linestyle='-', color='b')
        plt.title('Braking Performance of Brembo Brakes and EDC Rotors')
        plt.xlabel('Speed (m/s)')
        plt.ylabel('Braking Distance (m)')
        plt.grid()
        plt.xlim(0, max(speeds) + 10)
        plt.ylim(0, max(distances) + 10)
        plt.axhline(0, color='black', lw=0.5, ls='--')
        plt.axvline(0, color='black', lw=0.5, ls='--')
        plt.show()

def main():
    """
    Main function to run the braking performance simulation and visualization.
    """
    # Define brake specifications
    brake_force = 5000  # in Newtons
    rotor_diameter = 0.35  # in meters
    weight = 1200  # in kilograms

    # Create a BrakePerformance instance
    brake_performance = BrakePerformance(brake_force, rotor_diameter, weight)

    # Define a range of speeds to simulate (0 to 100 m/s)
    speeds = np.linspace(0, 100, num=50)

    # Simulate braking distances
    distances = brake_performance.simulate_braking(speeds)

    # Visualize the performance
    brake_performance.visualize_performance(speeds, distances)

if __name__ == "__main__":
    main()
```
