"""
Generated Code Metadata:
========================
Original URL: https://eraengineering.co.in
Prompt: Provide a Python script for detecting and repairing leaks in underground drainage systems, inspired by ERA ENGINEERING's plumbing services.
Generated: DETERMINISTIC_13bab623588c903e
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# drainage_leak_detector.py

import numpy as np
from scipy.spatial import distance
import matplotlib.pyplot as plt

class DrainageSystem:
    def __init__(self, pipes, nodes):
        """
        Initialize the drainage system with pipes and nodes.

        Parameters:
        pipes (list): List of pipes with their start and end nodes, and flow rate.
        nodes (list): List of nodes with their coordinates.
        """
        self.pipes = pipes
        self.nodes = nodes

    def detect_leaks(self, flow_rates):
        """
        Detect leaks in the drainage system by comparing actual flow rates with expected flow rates.

        Parameters:
        flow_rates (list): List of actual flow rates at each node.

        Returns:
        list: List of nodes with potential leaks.
        """
        # Calculate expected flow rates using the continuity equation
        expected_flow_rates = self.calculate_expected_flow_rates()

        # Compare actual flow rates with expected flow rates
        leaks = []
        for i, (node, actual_flow_rate, expected_flow_rate) in enumerate(zip(self.nodes, flow_rates, expected_flow_rates)):
            if abs(actual_flow_rate - expected_flow_rate) > 0.1:  # 10% tolerance
                leaks.append(node)

        return leaks

    def calculate_expected_flow_rates(self):
        """
        Calculate expected flow rates at each node using the continuity equation.

        Returns:
        list: List of expected flow rates at each node.
        """
        # Initialize expected flow rates at each node to 0
        expected_flow_rates = [0] * len(self.nodes)

        # Iterate over pipes and update expected flow rates at each node
        for pipe in self.pipes:
            start_node_index = self.nodes.index(pipe['start_node'])
            end_node_index = self.nodes.index(pipe['end_node'])
            flow_rate = pipe['flow_rate']

            expected_flow_rates[start_node_index] += flow_rate
            expected_flow_rates[end_node_index] -= flow_rate

        return expected_flow_rates

    def repair_leak(self, leak_node, repair_flow_rate):
        """
        Repair a leak by updating the flow rate at the leak node.

        Parameters:
        leak_node (dict): Node with the leak.
        repair_flow_rate (float): Flow rate to repair the leak.
        """
        # Find the pipe connected to the leak node
        for pipe in self.pipes:
            if pipe['start_node'] == leak_node or pipe['end_node'] == leak_node:
                # Update the flow rate of the pipe
                pipe['flow_rate'] -= repair_flow_rate
                break

def main():
    # Define the drainage system
    pipes = [
        {'start_node': {'x': 0, 'y': 0}, 'end_node': {'x': 10, 'y': 0}, 'flow_rate': 10},
        {'start_node': {'x': 10, 'y': 0}, 'end_node': {'x': 20, 'y': 0}, 'flow_rate': 5},
        {'start_node': {'x': 20, 'y': 0}, 'end_node': {'x': 30, 'y': 0}, 'flow_rate': 3}
    ]
    nodes = [{'x': 0, 'y': 0}, {'x': 10, 'y': 0}, {'x': 20, 'y': 0}, {'x': 30, 'y': 0}]

    drainage_system = DrainageSystem(pipes, nodes)

    # Detect leaks
    flow_rates = [9, 11, 4, 3]  # actual flow rates at each node
    leaks = drainage_system.detect_leaks(flow_rates)

    print("Potential leaks at nodes:")
    for leak in leaks:
        print(leak)

    # Repair leak
    repair_flow_rate = 2
    drainage_system.repair_leak(leaks[0], repair_flow_rate)

    # Plot the drainage system
    node_x_coords = [node['x'] for node in nodes]
    node_y_coords = [node['y'] for node in nodes]
    plt.scatter(node_x_coords, node_y_coords)

    pipe_x_coords = []
    pipe_y_coords = []
    for pipe in pipes:
        pipe_x_coords.extend([pipe['start_node']['x'], pipe['end_node']['x'], None])
        pipe_y_coords.extend([pipe['start_node']['y'], pipe['end_node']['y'], None])
    plt.plot(pipe_x_coords, pipe_y_coords)

    plt.show()

if __name__ == "__main__":
    main()
```
