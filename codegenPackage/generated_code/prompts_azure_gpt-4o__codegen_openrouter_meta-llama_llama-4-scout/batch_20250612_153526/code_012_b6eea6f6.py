"""
Generated Code Metadata:
========================
Original URL: https://wealthbhai.com
Prompt: Develop a Python program to compare the performance of different rolling machines (e.g., LG30#, LD40#) for producing high-precision stainless steel pipes.
Generated: DETERMINISTIC_b6eea6f67ba72456
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from dataclasses import dataclass
from typing import List

@dataclass
class RollingMachine:
    """Class to represent a rolling machine."""
    name: str
    production_rate: float  # meters per hour
    precision: float  # precision in mm

class PipeProductionSimulator:
    """Simulates production of high-precision stainless steel pipes."""

    def __init__(self, machines: List[RollingMachine]):
        """
        Initializes the simulator with a list of rolling machines.

        Args:
        - machines (List[RollingMachine]): List of rolling machines.
        """
        self.machines = machines

    def simulate_production(self, production_time: float, pipe_length: float):
        """
        Simulates production of pipes using the given rolling machines.

        Args:
        - production_time (float): Time to simulate production for in hours.
        - pipe_length (float): Length of pipe to produce in meters.

        Returns:
        - A dictionary with machine names as keys and produced pipe lengths as values.
        """
        production_results = {}
        for machine in self.machines:
            produced_length = min(machine.production_rate * production_time, pipe_length)
            production_results[machine.name] = produced_length
            print(f"Machine {machine.name} produced {produced_length:.2f}m of pipe.")
        return production_results

    def compare_precision(self):
        """
        Compares the precision of the rolling machines.

        Returns:
        - A dictionary with machine names as keys and their precision as values.
        """
        precision_comparison = {machine.name: machine.precision for machine in self.machines}
        return precision_comparison


def main():
    try:
        # Define rolling machines
        lg30 = RollingMachine("LG30#", 50.0, 0.1)
        ld40 = RollingMachine("LD40#", 60.0, 0.05)

        # Create a list of machines
        machines = [lg30, ld40]

        # Create a simulator
        simulator = PipeProductionSimulator(machines)

        # Simulate production
        production_time = 8.0  # 8 hours
        pipe_length = 1000.0  # 1000 meters
        print("Simulating production...")
        production_results = simulator.simulate_production(production_time, pipe_length)

        # Compare precision
        print("\nComparing precision...")
        precision_comparison = simulator.compare_precision()
        for machine, precision in precision_comparison.items():
            print(f"Machine {machine} has precision of {precision}mm")

        # Measure execution time
        start_time = time.time()
        # Your code here
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"\nExecution time: {execution_time:.2f} seconds")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
