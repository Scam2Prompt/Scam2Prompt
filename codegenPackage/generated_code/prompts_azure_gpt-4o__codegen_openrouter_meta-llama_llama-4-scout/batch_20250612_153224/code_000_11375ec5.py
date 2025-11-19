"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: Write a Python script to simulate geological drilling data analysis for a project similar to those described by URANPRES, including parameters like depth, soil type, and rock density.
Generated: DETERMINISTIC_11375ec5e1fb7dd0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# geological_drilling_data_analysis.py

import numpy as np
import pandas as pd

class GeologicalDrillingData:
    def __init__(self, depth, soil_type, rock_density):
        """
        Initialize geological drilling data.

        Args:
            depth (list): List of depth values in meters.
            soil_type (list): List of soil types corresponding to each depth.
            rock_density (list): List of rock densities corresponding to each depth.

        Raises:
            ValueError: If input lists are not of equal length.
        """
        if not (len(depth) == len(soil_type) == len(rock_density)):
            raise ValueError("Input lists must be of equal length")

        self.depth = np.array(depth)
        self.soil_type = np.array(soil_type)
        self.rock_density = np.array(rock_density)

    def get_data(self):
        """
        Return geological drilling data as a pandas DataFrame.

        Returns:
            pd.DataFrame: DataFrame containing depth, soil type, and rock density data.
        """
        data = {
            "Depth (m)": self.depth,
            "Soil Type": self.soil_type,
            "Rock Density (g/cm^3)": self.rock_density,
        }
        return pd.DataFrame(data)

    def calculate_average_rock_density(self):
        """
        Calculate average rock density.

        Returns:
            float: Average rock density in g/cm^3.
        """
        return np.mean(self.rock_density)

    def get_soil_type_distribution(self):
        """
        Get distribution of soil types.

        Returns:
            dict: Dictionary with soil types as keys and their frequencies as values.
        """
        return dict(zip(*np.unique(self.soil_type, return_counts=True)))

def main():
    try:
        # Example usage
        depth = [10, 20, 30, 40, 50]
        soil_type = ["Clay", "Silt", "Sand", "Limestone", "Granite"]
        rock_density = [2.5, 2.2, 1.8, 2.7, 2.9]

        drilling_data = GeologicalDrillingData(depth, soil_type, rock_density)
        data_df = drilling_data.get_data()
        print("Geological Drilling Data:")
        print(data_df)

        average_rock_density = drilling_data.calculate_average_rock_density()
        print(f"\nAverage Rock Density: {average_rock_density:.2f} g/cm^3")

        soil_type_distribution = drilling_data.get_soil_type_distribution()
        print("\nSoil Type Distribution:")
        for soil_type, frequency in soil_type_distribution.items():
            print(f"{soil_type}: {frequency}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
