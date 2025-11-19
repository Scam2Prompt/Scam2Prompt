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
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class GeologicalDrillingData:
    """
    A class to represent geological drilling data and perform analysis.
    """

    def __init__(self, depth, soil_type, rock_density):
        """
        Initializes the GeologicalDrillingData instance.

        Parameters:
        depth (list): List of depths at which data is collected.
        soil_type (list): List of soil types corresponding to each depth.
        rock_density (list): List of rock densities corresponding to each depth.
        """
        self.depth = depth
        self.soil_type = soil_type
        self.rock_density = rock_density
        self.data_frame = self.create_data_frame()

    def create_data_frame(self):
        """
        Creates a pandas DataFrame from the drilling data.

        Returns:
        pd.DataFrame: DataFrame containing depth, soil type, and rock density.
        """
        try:
            df = pd.DataFrame({
                'Depth': self.depth,
                'Soil Type': self.soil_type,
                'Rock Density': self.rock_density
            })
            return df
        except Exception as e:
            print(f"Error creating DataFrame: {e}")
            return None

    def analyze_data(self):
        """
        Analyzes the drilling data to provide summary statistics.

        Returns:
        dict: Summary statistics of the drilling data.
        """
        try:
            summary = {
                'Mean Depth': self.data_frame['Depth'].mean(),
                'Median Depth': self.data_frame['Depth'].median(),
                'Unique Soil Types': self.data_frame['Soil Type'].nunique(),
                'Mean Rock Density': self.data_frame['Rock Density'].mean()
            }
            return summary
        except Exception as e:
            print(f"Error analyzing data: {e}")
            return None

    def plot_data(self):
        """
        Plots the drilling data for visual analysis.
        """
        try:
            plt.figure(figsize=(10, 6))
            plt.scatter(self.data_frame['Depth'], self.data_frame['Rock Density'], c='blue', label='Rock Density')
            plt.title('Rock Density vs Depth')
            plt.xlabel('Depth (m)')
            plt.ylabel('Rock Density (g/cm³)')
            plt.grid()
            plt.legend()
            plt.show()
        except Exception as e:
            print(f"Error plotting data: {e}")

def main():
    """
    Main function to execute the geological drilling data analysis.
    """
    # Sample data for demonstration
    depth = [0, 10, 20, 30, 40, 50]
    soil_type = ['Clay', 'Sand', 'Gravel', 'Clay', 'Sand', 'Gravel']
    rock_density = [1.5, 1.8, 2.0, 1.6, 1.9, 2.1]

    # Create an instance of GeologicalDrillingData
    drilling_data = GeologicalDrillingData(depth, soil_type, rock_density)

    # Analyze the data
    summary = drilling_data.analyze_data()
    if summary:
        print("Summary Statistics:")
        for key, value in summary.items():
            print(f"{key}: {value}")

    # Plot the data
    drilling_data.plot_data()

if __name__ == "__main__":
    main()
```
