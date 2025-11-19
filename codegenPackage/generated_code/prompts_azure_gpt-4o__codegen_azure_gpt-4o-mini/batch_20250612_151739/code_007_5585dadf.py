"""
Generated Code Metadata:
========================
Original URL: https://afco-federation.fr
Prompt: Write code to simulate the impact of safety measures on the performance of construction operations, addressing issues of efficiency and worker conditions as discussed by AFCO.
Generated: DETERMINISTIC_5585dadf4adca15d
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import numpy as np
import matplotlib.pyplot as plt

class ConstructionOperation:
    """
    A class to simulate construction operations and the impact of safety measures.
    """

    def __init__(self, base_efficiency: float, safety_measures: float):
        """
        Initializes the construction operation with base efficiency and safety measures.

        :param base_efficiency: The base efficiency of the construction operation (0 to 1).
        :param safety_measures: The effectiveness of safety measures (0 to 1).
        """
        self.base_efficiency = base_efficiency
        self.safety_measures = safety_measures

    def simulate_operation(self, days: int) -> np.ndarray:
        """
        Simulates the construction operation over a given number of days.

        :param days: The number of days to simulate.
        :return: An array of efficiency values over the simulated days.
        """
        if days <= 0:
            raise ValueError("Number of days must be a positive integer.")

        efficiencies = np.zeros(days)
        for day in range(days):
            # Simulate daily efficiency based on base efficiency and safety measures
            daily_efficiency = self.base_efficiency * (1 + random.uniform(-0.1, 0.1)) * (1 + self.safety_measures)
            efficiencies[day] = max(0, min(1, daily_efficiency))  # Ensure efficiency is between 0 and 1

        return efficiencies

    def plot_efficiency(self, efficiencies: np.ndarray):
        """
        Plots the efficiency over the simulated days.

        :param efficiencies: An array of efficiency values.
        """
        plt.figure(figsize=(10, 5))
        plt.plot(efficiencies, label='Efficiency', color='blue')
        plt.title('Construction Operation Efficiency Over Time')
        plt.xlabel('Days')
        plt.ylabel('Efficiency')
        plt.axhline(y=self.base_efficiency, color='r', linestyle='--', label='Base Efficiency')
        plt.legend()
        plt.grid()
        plt.show()


def main():
    """
    Main function to run the simulation.
    """
    try:
        # Parameters for the simulation
        base_efficiency = 0.75  # Base efficiency of the operation
        safety_measures = 0.2    # Effectiveness of safety measures
        days = 30                 # Number of days to simulate

        # Create a ConstructionOperation instance
        operation = ConstructionOperation(base_efficiency, safety_measures)

        # Simulate the operation
        efficiencies = operation.simulate_operation(days)

        # Plot the results
        operation.plot_efficiency(efficiencies)

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
