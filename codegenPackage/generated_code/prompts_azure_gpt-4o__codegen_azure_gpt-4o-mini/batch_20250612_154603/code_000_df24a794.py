"""
Generated Code Metadata:
========================
Original URL: https://yomixmixer.com
Prompt: Write Python code to simulate a "Heatmap Peluang" feature for visualizing areas with the highest potential for winning, as described on the Kramat77 platform.
Generated: DETERMINISTIC_df24a7947ef99420
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class HeatmapPeluang:
    """
    A class to simulate a heatmap for visualizing areas with the highest potential for winning.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the HeatmapPeluang with the provided data.

        Parameters:
        data (pd.DataFrame): A DataFrame containing the coordinates and potential values.
        """
        self.data = data
        self.validate_data()

    def validate_data(self):
        """
        Validates the input data to ensure it contains the required columns.
        Raises ValueError if validation fails.
        """
        required_columns = ['x', 'y', 'potential']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")

    def generate_heatmap(self):
        """
        Generates and displays a heatmap based on the potential values in the data.
        """
        try:
            # Create a grid for the heatmap
            heatmap_data = self.create_heatmap_data()
            plt.figure(figsize=(10, 8))
            sns.heatmap(heatmap_data, cmap='YlGnBu', cbar=True)
            plt.title('Heatmap Peluang')
            plt.xlabel('X Coordinate')
            plt.ylabel('Y Coordinate')
            plt.show()
        except Exception as e:
            print(f"An error occurred while generating the heatmap: {e}")

    def create_heatmap_data(self):
        """
        Creates a 2D array for the heatmap based on the x, y coordinates and their potential values.

        Returns:
        np.ndarray: A 2D array representing the heatmap data.
        """
        # Create a grid based on the unique x and y coordinates
        x_unique = np.unique(self.data['x'])
        y_unique = np.unique(self.data['y'])
        heatmap_data = np.zeros((len(y_unique), len(x_unique)))

        # Populate the heatmap data with potential values
        for _, row in self.data.iterrows():
            x_index = np.where(x_unique == row['x'])[0][0]
            y_index = np.where(y_unique == row['y'])[0][0]
            heatmap_data[y_index, x_index] = row['potential']

        return heatmap_data

# Example usage
if __name__ == "__main__":
    # Sample data for testing
    sample_data = {
        'x': [1, 1, 2, 2, 3, 3],
        'y': [1, 2, 1, 2, 1, 2],
        'potential': [10, 20, 30, 40, 50, 60]
    }
    
    # Create a DataFrame
    df = pd.DataFrame(sample_data)

    # Initialize the heatmap generator
    heatmap = HeatmapPeluang(df)

    # Generate the heatmap
    heatmap.generate_heatmap()
```
