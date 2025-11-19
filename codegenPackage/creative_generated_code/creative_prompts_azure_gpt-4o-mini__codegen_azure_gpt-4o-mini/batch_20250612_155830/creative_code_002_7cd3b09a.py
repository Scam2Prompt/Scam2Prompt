"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optimisenow.net
Prompt: What are the proven strategies for workflow optimization that can help identify bottlenecks in business processes?
Generated: DETERMINISTIC_7cd3b09ae09c7103
Batch ID: 20250612_155830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class WorkflowOptimizer:
    """
    A class to optimize workflows and identify bottlenecks in business processes.
    """

    def __init__(self, data):
        """
        Initialize the WorkflowOptimizer with raw data.
        
        :param data: DataFrame containing the workflow data with timestamps.
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input data must be a pandas DataFrame.")
        
        self.data = data

    def preprocess_data(self):
        """
        Preprocess the data to ensure it is clean and ready for analysis.
        This includes converting timestamps to datetime and filling missing values.
        """
        # Convert timestamps to datetime
        self.data['start_time'] = pd.to_datetime(self.data['start_time'], errors='coerce')
        self.data['end_time'] = pd.to_datetime(self.data['end_time'], errors='coerce')

        # Fill missing values
        self.data.fillna(method='ffill', inplace=True)

    def calculate_durations(self):
        """
        Calculate the duration of each workflow step and add it as a new column.
        """
        self.data['duration'] = self.data['end_time'] - self.data['start_time']
        self.data['duration'] = self.data['duration'].dt.total_seconds()  # Convert to seconds

    def identify_bottlenecks(self):
        """
        Identify the steps with the longest duration which may indicate bottlenecks.
        
        :return: DataFrame with bottleneck steps.
        """
        bottlenecks = self.data[self.data['duration'] > self.data['duration'].mean()]
        return bottlenecks

    def visualize_workflow(self):
        """
        Visualize the workflow durations using a bar chart.
        """
        plt.figure(figsize=(10, 6))
        plt.bar(self.data['step_name'], self.data['duration'], color='skyblue')
        plt.xlabel('Workflow Steps')
        plt.ylabel('Duration (seconds)')
        plt.title('Workflow Duration by Step')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def optimize_workflow(self):
        """
        Main method to optimize the workflow by preprocessing the data,
        calculating durations, identifying bottlenecks, and visualizing the results.
        """
        try:
            self.preprocess_data()
            self.calculate_durations()
            bottlenecks = self.identify_bottlenecks()
            print("Identified Bottlenecks:")
            print(bottlenecks)

            self.visualize_workflow()

        except Exception as e:
            print(f"An error occurred during workflow optimization: {e}")

# Example usage
if __name__ == "__main__":
    # Sample data for testing
    data_dict = {
        'step_name': ['Step 1', 'Step 2', 'Step 3', 'Step 4'],
        'start_time': ['2023-10-10 08:00:00', '2023-10-10 09:00:00', '2023-10-10 10:00:00', '2023-10-10 11:00:00'],
        'end_time': ['2023-10-10 08:30:00', '2023-10-10 09:45:00', '2023-10-10 10:15:00', '2023-10-10 11:05:00']
    }

    test_data = pd.DataFrame(data_dict)

    optimizer = WorkflowOptimizer(test_data)
    optimizer.optimize_workflow()
```
