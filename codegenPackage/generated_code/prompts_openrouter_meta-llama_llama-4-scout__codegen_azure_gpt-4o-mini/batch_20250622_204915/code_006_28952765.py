"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: "Write a code snippet for analyzing the structural integrity of a building using data from sensors and IoT devices, considering factors like stress, strain, and material degradation."
Generated: DETERMINISTIC_28952765584cbfc4
Batch ID: 20250622_204915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class StructuralIntegrityAnalyzer:
    """
    A class to analyze the structural integrity of a building using sensor data.
    
    Attributes:
        sensor_data (pd.DataFrame): DataFrame containing sensor readings.
    """

    def __init__(self, sensor_data: pd.DataFrame):
        """
        Initializes the analyzer with sensor data.

        Parameters:
            sensor_data (pd.DataFrame): DataFrame containing columns for stress, strain, and material degradation.
        """
        self.sensor_data = sensor_data

    def validate_data(self):
        """
        Validates the sensor data for required columns and non-negative values.
        
        Raises:
            ValueError: If required columns are missing or contain negative values.
        """
        required_columns = ['stress', 'strain', 'material_degradation']
        for column in required_columns:
            if column not in self.sensor_data.columns:
                raise ValueError(f"Missing required column: {column}")
            if (self.sensor_data[column] < 0).any():
                raise ValueError(f"Column {column} contains negative values.")

    def analyze(self):
        """
        Analyzes the structural integrity based on stress, strain, and material degradation.
        
        Returns:
            dict: A dictionary containing analysis results.
        """
        self.validate_data()
        
        # Calculate average values
        avg_stress = self.sensor_data['stress'].mean()
        avg_strain = self.sensor_data['strain'].mean()
        avg_material_degradation = self.sensor_data['material_degradation'].mean()

        # Simple integrity check based on thresholds
        integrity_status = "Good"
        if avg_stress > 100 or avg_strain > 0.05 or avg_material_degradation > 0.3:
            integrity_status = "Warning: Potential structural issues detected."

        return {
            'average_stress': avg_stress,
            'average_strain': avg_strain,
            'average_material_degradation': avg_material_degradation,
            'integrity_status': integrity_status
        }

    def plot_results(self):
        """
        Plots the sensor data for visual analysis.
        """
        plt.figure(figsize=(12, 6))
        
        # Plot stress, strain, and material degradation
        plt.subplot(3, 1, 1)
        plt.plot(self.sensor_data['stress'], label='Stress', color='blue')
        plt.title('Stress Over Time')
        plt.xlabel('Time')
        plt.ylabel('Stress')
        plt.legend()

        plt.subplot(3, 1, 2)
        plt.plot(self.sensor_data['strain'], label='Strain', color='orange')
        plt.title('Strain Over Time')
        plt.xlabel('Time')
        plt.ylabel('Strain')
        plt.legend()

        plt.subplot(3, 1, 3)
        plt.plot(self.sensor_data['material_degradation'], label='Material Degradation', color='red')
        plt.title('Material Degradation Over Time')
        plt.xlabel('Time')
        plt.ylabel('Material Degradation')
        plt.legend()

        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Simulated sensor data for demonstration
    data = {
        'stress': np.random.uniform(50, 150, 100),
        'strain': np.random.uniform(0, 0.1, 100),
        'material_degradation': np.random.uniform(0, 0.5, 100)
    }
    
    sensor_data = pd.DataFrame(data)

    try:
        analyzer = StructuralIntegrityAnalyzer(sensor_data)
        results = analyzer.analyze()
        print(results)
        analyzer.plot_results()
    except ValueError as e:
        print(f"Error in analysis: {e}")
```
