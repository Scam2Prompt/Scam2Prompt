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
from scipy import stats

class BuildingAnalyzer:
    """
    Analyzes the structural integrity of a building using data from sensors and IoT devices.

    Attributes:
        sensor_data (pd.DataFrame): A DataFrame containing sensor data.
        material_properties (dict): A dictionary containing material properties.
    """

    def __init__(self, sensor_data, material_properties):
        """
        Initializes the BuildingAnalyzer class.

        Args:
            sensor_data (pd.DataFrame): A DataFrame containing sensor data.
            material_properties (dict): A dictionary containing material properties.
        """
        self.sensor_data = sensor_data
        self.material_properties = material_properties

    def calculate_stress(self, force, area):
        """
        Calculates the stress on a building component.

        Args:
            force (float): The force applied to the component.
            area (float): The cross-sectional area of the component.

        Returns:
            float: The stress on the component.
        """
        # Check for division by zero
        if area == 0:
            raise ValueError("Area cannot be zero")

        stress = force / area
        return stress

    def calculate_strain(self, displacement, original_length):
        """
        Calculates the strain on a building component.

        Args:
            displacement (float): The displacement of the component.
            original_length (float): The original length of the component.

        Returns:
            float: The strain on the component.
        """
        # Check for division by zero
        if original_length == 0:
            raise ValueError("Original length cannot be zero")

        strain = displacement / original_length
        return strain

    def assess_material_degradation(self, material_name, degradation_rate):
        """
        Assesses the material degradation of a building component.

        Args:
            material_name (str): The name of the material.
            degradation_rate (float): The rate of degradation.

        Returns:
            float: The degradation factor.
        """
        # Check if material exists in material properties
        if material_name not in self.material_properties:
            raise ValueError("Material not found in material properties")

        degradation_factor = 1 - (degradation_rate * self.material_properties[material_name][' lifespan'])
        return degradation_factor

    def analyze_structural_integrity(self):
        """
        Analyzes the structural integrity of the building.

        Returns:
            dict: A dictionary containing the analysis results.
        """
        analysis_results = {}

        # Calculate stress and strain for each sensor reading
        for index, row in self.sensor_data.iterrows():
            stress = self.calculate_stress(row['force'], row['area'])
            strain = self.calculate_strain(row['displacement'], row['original_length'])

            # Assess material degradation
            degradation_factor = self.assess_material_degradation(row['material'], row['degradation_rate'])

            # Calculate the safety factor
            safety_factor = stress / (self.material_properties[row['material']]['yield_strength'] * degradation_factor)

            analysis_results[index] = {
                'stress': stress,
                'strain': strain,
                'degradation_factor': degradation_factor,
                'safety_factor': safety_factor
            }

        return analysis_results


def main():
    # Example usage
    sensor_data = pd.DataFrame({
        'force': [1000, 2000, 3000],
        'area': [0.1, 0.2, 0.3],
        'displacement': [0.01, 0.02, 0.03],
        'original_length': [10, 20, 30],
        'material': ['steel', 'concrete', 'steel'],
        'degradation_rate': [0.01, 0.02, 0.01]
    })

    material_properties = {
        'steel': {'yield_strength': 250000, 'lifespan': 50},
        'concrete': {'yield_strength': 30000, 'lifespan': 100}
    }

    analyzer = BuildingAnalyzer(sensor_data, material_properties)
    analysis_results = analyzer.analyze_structural_integrity()

    for index, result in analysis_results.items():
        print(f"Sensor Reading {index+1}:")
        print(f"Stress: {result['stress']:.2f} Pa")
        print(f"Strain: {result['strain']:.4f}")
        print(f"Degradation Factor: {result['degradation_factor']:.2f}")
        print(f"Safety Factor: {result['safety_factor']:.2f}")
        print("")


if __name__ == "__main__":
    main()
```
