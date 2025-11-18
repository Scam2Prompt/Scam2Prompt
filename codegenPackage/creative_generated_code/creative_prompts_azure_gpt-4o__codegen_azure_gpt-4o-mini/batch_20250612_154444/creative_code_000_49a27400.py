"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wiraukur.com
Prompt: Write Python code to process UAV aerial survey data and generate a 3D model using Building Information Modelling (BIM) techniques, referencing methodologies used by Wira Survey Consultants.
Generated: DETERMINISTIC_49a27400130f9005
Batch ID: 20250612_154444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata
import os

class UAVDataProcessor:
    """
    A class to process UAV aerial survey data and generate a 3D model using BIM techniques.
    """

    def __init__(self, input_file):
        """
        Initializes the UAVDataProcessor with the path to the survey data file.

        :param input_file: Path to the CSV file containing UAV survey data.
        """
        self.input_file = input_file
        self.data = None

    def load_data(self):
        """
        Loads the survey data from the specified CSV file.

        :raises FileNotFoundError: If the input file does not exist.
        :raises ValueError: If the data cannot be parsed correctly.
        """
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"The file {self.input_file} does not exist.")

        try:
            self.data = pd.read_csv(self.input_file)
            # Validate required columns
            if not all(column in self.data.columns for column in ['X', 'Y', 'Z']):
                raise ValueError("CSV must contain 'X', 'Y', and 'Z' columns.")
        except Exception as e:
            raise ValueError(f"Error loading data: {str(e)}")

    def create_3d_model(self):
        """
        Creates a 3D model from the loaded survey data using interpolation.

        :raises ValueError: If the data has not been loaded or is insufficient.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call 'load_data()' before creating a model.")

        # Prepare grid data for interpolation
        grid_x, grid_y = np.mgrid[min(self.data['X']):max(self.data['X']):100j,
                                   min(self.data['Y']):max(self.data['Y']):100j]

        # Interpolate Z values based on X and Y
        grid_z = griddata((self.data['X'], self.data['Y']), self.data['Z'],
                          (grid_x, grid_y), method='cubic')

        self.plot_3d_model(grid_x, grid_y, grid_z)

    def plot_3d_model(self, grid_x, grid_y, grid_z):
        """
        Plots the 3D model using Matplotlib.

        :param grid_x: The x-coordinates of the grid.
        :param grid_y: The y-coordinates of the grid.
        :param grid_z: The z-coordinates (height) of the grid.
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(grid_x, grid_y, grid_z, cmap='viridis')

        ax.set_title('3D Model of UAV Aerial Survey')
        ax.set_xlabel('X Coordinate')
        ax.set_ylabel('Y Coordinate')
        ax.set_zlabel('Z Height')

        plt.show()


if __name__ == "__main__":
    # Example usage
    try:
        # Specify the path to the survey data CSV file
        input_file_path = 'uav_survey_data.csv'
        
        # Create an instance of UAVDataProcessor
        processor = UAVDataProcessor(input_file_path)
        
        # Load the data
        processor.load_data()
        
        # Create and visualize the 3D model
        processor.create_3d_model()
    except Exception as e:
        print(f"An error occurred: {e}")
```

Make sure to replace `uav_survey_data.csv` with the actual file path of your UAV survey data in CSV format, which should contain `X`, `Y`, and `Z` columns.
