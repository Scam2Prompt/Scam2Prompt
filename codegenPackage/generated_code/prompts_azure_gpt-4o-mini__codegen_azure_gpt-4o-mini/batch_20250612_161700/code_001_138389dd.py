"""
Generated Code Metadata:
========================
Original URL: https://ingeostar.com
Prompt: Write a code snippet that utilizes remote sensing data to create high-resolution 3D terrain models, similar to the services offered by IngeoStar.
Generated: DETERMINISTIC_138389dd74b2bc68
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import rasterio
from rasterio.transform import from_origin
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class TerrainModel:
    def __init__(self, elevation_data_path):
        """
        Initializes the TerrainModel with the path to the elevation data.

        :param elevation_data_path: Path to the elevation data file (GeoTIFF format).
        """
        self.elevation_data_path = elevation_data_path
        self.elevation_data = None
        self.transform = None

    def load_elevation_data(self):
        """
        Loads elevation data from a GeoTIFF file and stores it in a numpy array.
        """
        try:
            with rasterio.open(self.elevation_data_path) as src:
                self.elevation_data = src.read(1)  # Read the first band
                self.transform = src.transform
        except Exception as e:
            print(f"Error loading elevation data: {e}")
            raise

    def create_3d_model(self):
        """
        Creates a 3D terrain model from the elevation data.
        """
        if self.elevation_data is None:
            raise ValueError("Elevation data not loaded. Call load_elevation_data() first.")

        # Generate grid coordinates
        rows, cols = self.elevation_data.shape
        x = np.arange(cols)
        y = np.arange(rows)
        x, y = np.meshgrid(x, y)

        # Transform grid coordinates to geographic coordinates
        x_geo, y_geo = from_origin(self.transform.c, self.transform.f, self.transform.a, self.transform.e)
        x_geo = x_geo + x * self.transform.a
        y_geo = y_geo + y * self.transform.e

        # Create a 3D plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x_geo, y_geo, self.elevation_data, cmap='terrain')

        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')
        ax.set_zlabel('Elevation (m)')
        ax.set_title('3D Terrain Model')

        plt.show()

if __name__ == "__main__":
    # Example usage
    try:
        terrain_model = TerrainModel('path/to/elevation_data.tif')
        terrain_model.load_elevation_data()
        terrain_model.create_3d_model()
    except Exception as e:
        print(f"An error occurred: {e}")
```

Make sure to replace `'path/to/elevation_data.tif'` with the actual path to your elevation data file in GeoTIFF format.
