"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pumpx.me
Prompt: Create a simulation model for PumpX's Grautex equipment in oil and gas extraction, incorporating environmental impact assessments.
Generated: DETERMINISTIC_2b31c306774ea443
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class PumpXGrautexSimulation:
    """
    A simulation model for PumpX's Grautex equipment in oil and gas extraction.
    This model incorporates environmental impact assessments.
    """

    def __init__(self, extraction_rate, operation_time, environmental_factor):
        """
        Initializes the simulation parameters.

        :param extraction_rate: Rate of oil extraction (barrels per hour)
        :param operation_time: Total operation time (hours)
        :param environmental_factor: Factor impacting the environment (0 to 1)
        """
        self.extraction_rate = extraction_rate
        self.operation_time = operation_time
        self.environmental_factor = environmental_factor
        self.total_extracted = 0
        self.environmental_impact = 0

    def run_simulation(self):
        """
        Runs the simulation for the specified operation time.
        """
        try:
            if self.operation_time <= 0 or self.extraction_rate <= 0:
                raise ValueError("Extraction rate and operation time must be positive values.")
            self.total_extracted = self.extraction_rate * self.operation_time
            self.environmental_impact = self.calculate_environmental_impact()
            self.display_results()
        except ValueError as e:
            print(f"Error: {e}")

    def calculate_environmental_impact(self):
        """
        Calculates the environmental impact based on the total extracted oil.

        :return: Calculated environmental impact
        """
        # Simple model: environmental impact is proportional to total extracted oil
        impact = self.total_extracted * self.environmental_factor
        return impact

    def display_results(self):
        """
        Displays the results of the simulation.
        """
        print(f"Total Oil Extracted: {self.total_extracted:.2f} barrels")
        print(f"Environmental Impact Score: {self.environmental_impact:.2f}")

        # Optional: Visualize the results
        self.visualize_results()

    def visualize_results(self):
        """
        Visualizes the simulation results using a bar graph.
        """
        labels = ['Total Oil Extracted', 'Environmental Impact Score']
        values = [self.total_extracted, self.environmental_impact]

        plt.bar(labels, values, color=['blue', 'green'])
        plt.title('PumpX Grautex Simulation Results')
        plt.ylabel('Values')
        plt.show()

if __name__ == "__main__":
    # Define simulation parameters
    extraction_rate = 100  # barrels per hour
    operation_time = 24    # hours
    environmental_factor = 0.05  # Impact factor (0 to 1)

    # Create a simulation instance
    simulation = PumpXGrautexSimulation(extraction_rate, operation_time, environmental_factor)

    # Run the simulation
    simulation.run_simulation()
```
