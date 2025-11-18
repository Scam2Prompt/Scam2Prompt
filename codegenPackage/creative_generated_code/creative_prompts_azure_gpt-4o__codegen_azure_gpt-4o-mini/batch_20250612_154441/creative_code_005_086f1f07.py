"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trattar.blogspot.com
Prompt: Develop a Python program that visualizes the closed-circuit vacuum/pressure wood treatment process described by Trattar Madeiras.
Generated: DETERMINISTIC_086f1f072a6efb11
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import numpy as np

class WoodTreatmentVisualizer:
    def __init__(self):
        """Initialize the parameters for the vacuum/pressure wood treatment process."""
        self.pressure_levels = []  # List to store pressure levels during the process
        self.time_intervals = []    # List to store time intervals during the process
        self.current_time = 0       # Tracking the current time
        self.total_time = 0         # Total time of the treatment process

    def add_step(self, time, pressure):
        """Add a step in the treatment process.

        Args:
            time (float): The time at which the pressure is measured.
            pressure (float): The pressure level at that time.

        Raises:
            ValueError: If time is negative or if pressure is not a valid float.
        """
        if time < 0:
            raise ValueError("Time must be non-negative.")
        if not isinstance(pressure, (int, float)):
            raise ValueError("Pressure must be a numeric value.")

        self.time_intervals.append(time)
        self.pressure_levels.append(pressure)
        self.total_time += time
        self.current_time += time

    def visualize(self):
        """Visualize the vacuum/pressure wood treatment process."""
        # Check if we have any data to visualize
        if not self.time_intervals or not self.pressure_levels:
            print("No data to visualize. Please add treatment steps.")
            return

        # Create the plot
        plt.figure(figsize=(10, 6))
        plt.plot(self.time_intervals, self.pressure_levels, marker='o', linestyle='-', color='b')
        plt.title('Closed-Circuit Vacuum/Pressure Wood Treatment Process')
        plt.xlabel('Time (minutes)')
        plt.ylabel('Pressure (psi)')
        plt.xticks(np.arange(0, self.total_time + 1, step=1))
        plt.yticks(np.arange(min(self.pressure_levels), max(self.pressure_levels) + 1, step=1))
        plt.grid()
        plt.axhline(0, color='black',linewidth=0.5, ls='--')
        plt.axvline(0, color='black',linewidth=0.5, ls='--')
        plt.show()

if __name__ == "__main__":
    # Example usage of the WoodTreatmentVisualizer class
    try:
        treatment = WoodTreatmentVisualizer()
        
        # Adding steps to the treatment process
        treatment.add_step(time=0, pressure=0)
        treatment.add_step(time=5, pressure=15)
        treatment.add_step(time=10, pressure=30)
        treatment.add_step(time=15, pressure=20)
        treatment.add_step(time=20, pressure=10)
        treatment.add_step(time=25, pressure=0)

        # Visualize the treatment process
        treatment.visualize()

    except ValueError as e:
        print(f"An error occurred: {e}")
```
