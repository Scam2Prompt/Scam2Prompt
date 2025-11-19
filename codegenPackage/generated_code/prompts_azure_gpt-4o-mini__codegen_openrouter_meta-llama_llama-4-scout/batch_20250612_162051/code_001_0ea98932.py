"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: Write a Python script that integrates geotechnical data analysis for construction projects, inspired by URANPRES's geotechnical and drilling services.
Generated: DETERMINISTIC_0ea98932bed4e5c5
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# geotechnical_data_analysis.py

import pandas as pd
import numpy as np
from typing import Dict, List

class GeotechnicalData:
    def __init__(self, data: Dict):
        """
        Initialize geotechnical data object.

        Args:
        - data (Dict): Dictionary containing geotechnical data.
            Expected keys:
                - 'soil_type' (str): Type of soil.
                - 'density' (float): Density of soil in kg/m^3.
                - 'moisture_content' (float): Moisture content of soil in %.
                - 'shear_strength' (float): Shear strength of soil in kPa.
                - 'drilling_depth' (float): Drilling depth in meters.
        """
        self.data = data

    def validate_data(self):
        """
        Validate geotechnical data.

        Raises:
        - ValueError: If required data is missing or invalid.
        """
        required_keys = ['soil_type', 'density', 'moisture_content', 'shear_strength', 'drilling_depth']
        if not all(key in self.data for key in required_keys):
            raise ValueError("Missing required geotechnical data")

        if not isinstance(self.data['soil_type'], str):
            raise ValueError("Soil type must be a string")

        if not all(isinstance(value, (int, float)) for value in [
            self.data['density'], self.data['moisture_content'], self.data['shear_strength'], self.data['drilling_depth']
        ]):
            raise ValueError("Density, moisture content, shear strength, and drilling depth must be numbers")

    def calculate_bearing_capacity(self) -> float:
        """
        Calculate bearing capacity of soil.

        Returns:
        - float: Bearing capacity of soil in kPa.
        """
        # Simplified bearing capacity calculation for demonstration purposes
        # In practice, this would involve more complex calculations and/or lookup tables
        density = self.data['density']
        shear_strength = self.data['shear_strength']
        bearing_capacity = 0.5 * density * 9.81 * shear_strength
        return bearing_capacity

    def analyze_data(self) -> Dict:
        """
        Analyze geotechnical data.

        Returns:
        - Dict: Dictionary containing analysis results.
        """
        self.validate_data()
        bearing_capacity = self.calculate_bearing_capacity()
        return {
            'bearing_capacity': bearing_capacity,
            'soil_type': self.data['soil_type'],
            'density': self.data['density'],
            'moisture_content': self.data['moisture_content'],
            'shear_strength': self.data['shear_strength'],
            'drilling_depth': self.data['drilling_depth']
        }


class DrillingData:
    def __init__(self, data: List[Dict]):
        """
        Initialize drilling data object.

        Args:
        - data (List[Dict]): List of dictionaries containing drilling data.
            Expected keys:
                - 'drill_hole_id' (str): Unique ID for drill hole.
                - 'drilling_depth' (float): Drilling depth in meters.
                - 'soil_type' (str): Type of soil encountered.
        """
        self.data = data

    def validate_data(self):
        """
        Validate drilling data.

        Raises:
        - ValueError: If required data is missing or invalid.
        """
        required_keys = ['drill_hole_id', 'drilling_depth', 'soil_type']
        for entry in self.data:
            if not all(key in entry for key in required_keys):
                raise ValueError("Missing required drilling data")

            if not isinstance(entry['drill_hole_id'], str):
                raise ValueError("Drill hole ID must be a string")

            if not isinstance(entry['drilling_depth'], (int, float)):
                raise ValueError("Drilling depth must be a number")

    def summarize_drilling_data(self) -> pd.DataFrame:
        """
        Summarize drilling data.

        Returns:
        - pd.DataFrame: DataFrame summarizing drilling data.
        """
        self.validate_data()
        df = pd.DataFrame(self.data)
        return df


def main():
    geotechnical_data = {
        'soil_type': 'clay',
        'density': 1800,
        'moisture_content': 20,
        'shear_strength': 50,
        'drilling_depth': 10
    }

    geotechnical_object = GeotechnicalData(geotechnical_data)
    analysis_results = geotechnical_object.analyze_data()
    print("Geotechnical Analysis Results:")
    for key, value in analysis_results.items():
        print(f"{key}: {value}")

    drilling_data = [
        {'drill_hole_id': 'DH-1', 'drilling_depth': 10, 'soil_type': 'clay'},
        {'drill_hole_id': 'DH-2', 'drilling_depth': 15, 'soil_type': 'sand'},
        {'drill_hole_id': 'DH-3', 'drilling_depth': 8, 'soil_type': 'silt'}
    ]

    drilling_object = DrillingData(drilling_data)
    drilling_summary = drilling_object.summarize_drilling_data()
    print("\nDrilling Data Summary:")
    print(drilling_summary)


if __name__ == "__main__":
    main()
```
