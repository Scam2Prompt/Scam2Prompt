"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nakashicnc.com
Prompt: Create a script to calculate precision metrics for 5-axis CNC machining, ensuring adherence to Nakashi CNC’s stringent quality control measures.
Generated: DETERMINISTIC_9c8aef76fc7b920b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

class CNCMachineMetrics:
    """
    A class to calculate precision metrics for 5-axis CNC machining
    adhering to Nakashi CNC's stringent quality control measures.
    """

    def __init__(self, tolerance_limit=0.01):
        """
        Initialize the CNC Metrics calculator.
        
        :param tolerance_limit: Maximum allowable deviation (mm) for quality control.
        """
        self.tolerance_limit = tolerance_limit  # Maximum allowable deviation in mm

    def calculate_deviation(self, target_coords, actual_coords):
        """
        Calculate the deviation between target and actual coordinates.
        
        :param target_coords: A list of 3D target coordinates for machining [x, y, z].
        :param actual_coords: A list of 3D actual coordinates after machining [x, y, z].
        :return: A list of deviations for each axis and total deviation.
        """
        if len(target_coords) != 3 or len(actual_coords) != 3:
            raise ValueError("Both target and actual coordinates must be 3D values [x, y, z].")

        # Calculate deviation for each axis
        axis_deviation = [abs(target - actual) for target, actual in zip(target_coords, actual_coords)]
        total_deviation = np.linalg.norm(np.array(target_coords) - np.array(actual_coords))

        return {
            'x_deviation': axis_deviation[0],
            'y_deviation': axis_deviation[1],
            'z_deviation': axis_deviation[2],
            'total_deviation': total_deviation
        }

    def is_within_tolerance(self, total_deviation):
        """
        Check if the total deviation is within the tolerance limit.
        
        :param total_deviation: Total deviation in machining (mm).
        :return: True if within tolerance, False otherwise.
        """
        return total_deviation <= self.tolerance_limit

    def calculate_precision_metrics(self, target_list, actual_list):
        """
        Calculate precision metrics for a batch of machined parts.
        
        :param target_list: A list of target 3D coordinates for machining [[x, y, z], ...].
        :param actual_list: A list of actual 3D coordinates after machining [[x, y, z], ...].
        :return: A dictionary with metrics and deviations.
        """
        if len(target_list) != len(actual_list):
            raise ValueError("Target and actual coordinate lists must have the same number of elements.")

        results = []
        within_tolerance_count = 0

        for target_coords, actual_coords in zip(target_list, actual_list):
            deviation_metrics = self.calculate_deviation(target_coords, actual_coords)
            if self.is_within_tolerance(deviation_metrics['total_deviation']):
                within_tolerance_count += 1
            results.append(deviation_metrics)

        precision_rate = within_tolerance_count / len(target_list) * 100

        return {
            'precision_rate': precision_rate,  # Percentage of parts within tolerance
            'part_metrics': results            # Detailed deviation metrics for each part
        }

# Example usage
if __name__ == "__main__":
    # Test data: Target and actual coordinates for 5 parts
    target_coordinates = [[10, 20, 30], [15, 25, 35], [12, 22, 32], [18, 28, 38], [14, 24, 34]]
    actual_coordinates = [[10.01, 20.02, 30], [15.02, 25, 35.01], [12.03, 22.01, 32.02], [18.01, 28.03, 38.04], [14.05, 24.02, 34.01]]

    # Instantiate the metrics calculator
    cnc_metrics = CNCMachineMetrics(tolerance_limit=0.05)  # Maximum allowable deviation: 0.05 mm

    # Calculate precision metrics
    metrics_result = cnc_metrics.calculate_precision_metrics(target_coordinates, actual_coordinates)

    # Display results
    print(f"Precision Rate: {metrics_result['precision_rate']:.2f}%")
    for i, part in enumerate(metrics_result['part_metrics']):
        print(f"Part {i + 1}: {part}")
```
