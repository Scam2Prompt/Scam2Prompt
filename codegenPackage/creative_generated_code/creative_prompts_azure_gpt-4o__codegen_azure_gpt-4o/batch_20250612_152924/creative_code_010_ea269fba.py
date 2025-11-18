"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rapidresponder.net
Prompt: Generate a Python script that calculates recovery success rates based on Rapid Responder's metrics, such as time frame and cost-effectiveness.
Generated: DETERMINISTIC_ea269fbaa53f5bda
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import json
from typing import List, Dict, Tuple

# Define a class to encapsulate recovery data processing
class RapidResponderMetrics:
    def __init__(self, data: List[Dict[str, float]]):
        """
        Initialize with a list of dictionaries containing recovery metrics.
        
        :param data: List of recovery metrics in the form of dictionaries.
                     Each dictionary should contain:
                     - 'time_frame': Recovery time in hours.
                     - 'cost_effectiveness': Cost effectiveness ratio (0-1).
                     - 'success_rate': Predefined success rate (0-1).
        """
        self.data = data

    def calculate_average_success_rate(self) -> float:
        """
        Calculate the average success rate across all data points.

        :return: Average success rate as a float.
        """
        if not self.data:
            raise ValueError("No data provided for metrics calculation.")
        
        total_success_rate = sum(entry['success_rate'] for entry in self.data)
        return total_success_rate / len(self.data)

    def calculate_weighted_success_rate(self) -> float:
        """
        Calculate a weighted success rate based on both time frame and cost effectiveness.

        :return: Weighted success rate as a float.
        """
        if not self.data:
            raise ValueError("No data provided for metrics calculation.")
        
        total_weighted_success = 0
        total_weight = 0
        
        for entry in self.data:
            weight = entry['time_frame'] * entry['cost_effectiveness']
            total_weighted_success += entry['success_rate'] * weight
            total_weight += weight
        
        if total_weight == 0:
            raise ValueError("Total weight is zero, cannot calculate weighted success rate.")
        
        return total_weighted_success / total_weight

# Define a function to load recovery data from a JSON file
def load_recovery_data(file_path: str) -> List[Dict[str, float]]:
    """
    Load recovery data from a JSON file.
    
    :param file_path: Path to the JSON file containing recovery metrics.
    :return: List of recovery metrics as dictionaries.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Validate the structure of the data
        for entry in data:
            if not all(key in entry for key in ['time_frame', 'cost_effectiveness', 'success_rate']):
                raise ValueError("Invalid data format. Each entry must contain 'time_frame', 'cost_effectiveness', and 'success_rate'.")
        
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} was not found.")
    except json.JSONDecodeError:
        raise ValueError("Failed to decode JSON. Ensure the file contains valid JSON.")

# Main function to execute the script
def main():
    """
    Main function to calculate and display recovery success rates.
    """
    # File path to the JSON data file
    file_path = 'recovery_data.json'
    
    try:
        # Load data from the file
        recovery_data = load_recovery_data(file_path)
        
        # Instantiate the metrics class
        metrics = RapidResponderMetrics(recovery_data)
        
        # Calculate metrics
        average_success_rate = metrics.calculate_average_success_rate()
        weighted_success_rate = metrics.calculate_weighted_success_rate()
        
        # Display the results
        print(f"Average Success Rate: {average_success_rate:.2f}")
        print(f"Weighted Success Rate: {weighted_success_rate:.2f}")
    except Exception as e:
        # Handle errors gracefully
        print(f"Error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
