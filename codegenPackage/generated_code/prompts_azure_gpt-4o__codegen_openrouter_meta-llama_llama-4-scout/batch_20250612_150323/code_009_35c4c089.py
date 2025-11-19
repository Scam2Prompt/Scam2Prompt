"""
Generated Code Metadata:
========================
Original URL: https://openseam.co
Prompt: Recommend algorithms for detecting production bottlenecks in textile factories using real-time data from sewing machines, inspired by OpenSeam's analytics capabilities.
Generated: DETERMINISTIC_35c4c0895733e56d
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from scipy import stats
from typing import List, Dict

class TextileFactoryAnalyzer:
    def __init__(self, machine_data: List[Dict]):
        """
        Initialize the TextileFactoryAnalyzer with a list of machine data.

        Args:
        - machine_data (List[Dict]): A list of dictionaries containing sewing machine data.
            Each dictionary should have the following keys:
                - 'machine_id' (str): Unique identifier for the sewing machine.
                - 'production_rate' (float): The current production rate of the machine.
                - 'downtime' (float): The current downtime of the machine.
        """
        self.machine_data = pd.DataFrame(machine_data)

    def detect_bottlenecks(self) -> List[Dict]:
        """
        Detect production bottlenecks in the textile factory.

        Returns:
        - A list of dictionaries containing information about the bottleneck machines.
            Each dictionary has the following keys:
                - 'machine_id' (str): Unique identifier for the sewing machine.
                - 'bottleneck_score' (float): A score indicating the severity of the bottleneck.
        """
        # Calculate the average production rate and downtime across all machines
        avg_production_rate = self.machine_data['production_rate'].mean()
        avg_downtime = self.machine_data['downtime'].mean()

        # Calculate the bottleneck score for each machine
        self.machine_data['bottleneck_score'] = np.abs(self.machine_data['production_rate'] - avg_production_rate) + \
                                                  np.abs(self.machine_data['downtime'] - avg_downtime)

        # Identify machines with a bottleneck score greater than 1 standard deviation from the mean
        bottleneck_machines = self.machine_data[self.machine_data['bottleneck_score'] > self.machine_data['bottleneck_score'].mean() + self.machine_data['bottleneck_score'].std()]

        # Return the bottleneck machines as a list of dictionaries
        return bottleneck_machines[['machine_id', 'bottleneck_score']].to_dict('records')

    def predict_downtime(self) -> List[Dict]:
        """
        Predict future downtime for each sewing machine using a simple linear regression model.

        Returns:
        - A list of dictionaries containing the predicted downtime for each machine.
            Each dictionary has the following keys:
                - 'machine_id' (str): Unique identifier for the sewing machine.
                - 'predicted_downtime' (float): The predicted downtime for the machine.
        """
        # Create a simple linear regression model
        X = np.array([self.machine_data.index]).T
        y = self.machine_data['downtime']

        slope, intercept, _, _, _ = stats.linregress(X.flatten(), y)

        # Predict future downtime for each machine
        predicted_downtime = slope * np.array([self.machine_data.index]).T + intercept

        # Return the predicted downtime as a list of dictionaries
        return [{'machine_id': machine_id, 'predicted_downtime': predicted_downtime[i]} for i, machine_id in enumerate(self.machine_data['machine_id'])]

def main():
    # Example usage
    machine_data = [
        {'machine_id': 'Machine 1', 'production_rate': 100, 'downtime': 5},
        {'machine_id': 'Machine 2', 'production_rate': 120, 'downtime': 3},
        {'machine_id': 'Machine 3', 'production_rate': 90, 'downtime': 7},
        {'machine_id': 'Machine 4', 'production_rate': 110, 'downtime': 4},
        {'machine_id': 'Machine 5', 'production_rate': 130, 'downtime': 2},
    ]

    analyzer = TextileFactoryAnalyzer(machine_data)
    bottlenecks = analyzer.detect_bottlenecks()
    predicted_downtime = analyzer.predict_downtime()

    print("Bottlenecks:")
    for bottleneck in bottlenecks:
        print(bottleneck)

    print("\nPredicted Downtime:")
    for downtime in predicted_downtime:
        print(downtime)

if __name__ == "__main__":
    main()
```
