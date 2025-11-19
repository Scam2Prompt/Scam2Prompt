"""
Generated Code Metadata:
========================
Original URL: https://ingeostar.com
Prompt: Generate a 3D model using MDT/DSM/MDV data obtained from Operaciones RPA sensores remotos for a mining project.
Generated: DETERMINISTIC_26f45f45c71dedb9
Batch ID: 20250622_210443
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
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from scipy.interpolate import griddata
import rasterio
from rasterio.plot import show
import os

class MiningTerrainModel:
    """
    Class for creating 3D models from MDT/DSM/MDV data for mining projects.
    """
    
    def __init__(self, data_path=None):
        """
        Initialize the terrain model with optional data path.
        
        Args:
            data_path (str): Path to the input data file (CSV or GeoTIFF)
        """
        self.data_path = data_path
        self.raw_data = None
        self.x = None
        self.y = None
        self.z = None
        self.grid_x = None
        self.grid_y = None
        self.grid_z = None
        
    def load_csv_data(self, x_col='x', y_col='y', z_col='z'):
        """
        Load terrain data from CSV file.
        
        Args:
            x_col (str): Column name for x coordinates
            y_col (str): Column name for y coordinates
            z_col (str): Column name for z coordinates (elevation)
        """
        try:
            df = pd.read_csv(self.data_path)
            self.raw_data = df
            self.x = df[x_col].values
            self.y = df[y_col].values
            self.z = df[z_col].values
        except Exception as e:
            raise ValueError(f"Error loading CSV data: {str(e)}")
    
    def load_geotiff_data(self):
        """
        Load terrain data from GeoTIFF file.
        """
        try:
            with rasterio.open(self.data_path) as src:
                self.z = src.read(1)
                # Create grid coordinates
                rows, cols = self.z.shape
                x, y = np.meshgrid(np.arange(cols), np.arange(rows))
                self.x, self.y = x.flatten(), y.flatten()
                self.z = self.z.flatten()
                # Transform to real coordinates if available
                if src.transform:
                    self.x, self.y = src.transform * (self.x, self.y)
        except Exception as e:
            raise ValueError(f"Error loading GeoTIFF data: {str(e)}")
    
    def interpolate_grid(self, grid_resolution=100):
        """
        Interpolate scattered data points to a regular grid.
        
        Args:
            grid_resolution (int): Number of grid points in each dimension
        """
        try:
            # Create grid
            self.grid_x = np.linspace(min(self.x), max(self.x), grid_resolution)
            self.grid_y = np.linspace(min(self.y), max(self.y), grid_resolution)
            self.grid_x, self.grid_y = np.meshgrid(self.grid_x, self.grid_y)
            
            # Interpolate using linear method
            self.grid_z = griddata(
                (self.x, self.y), 
                self.z, 
                (self.grid_x, self.grid_y), 
                method='linear'
            )
        except Exception as e:
            raise ValueError(f"Error during interpolation: {str(e)}")
    
    def plot_3d_model(self, title="Mining Terrain Model", cmap='terrain'):
        """
        Create and display a 3D plot of the terrain model.
        
        Args:
            title (str): Plot title
            cmap (str): Color map for the surface
        """
        try:
            fig = plt.figure(figsize=(12, 8))
            ax = fig.add_subplot(111, projection='3d')
            
            # Create surface plot
            surf = ax.plot_surface(
                self.grid_x, 
                self.grid_y, 
                self.grid_z, 
                cmap=cmap,
                linewidth=0,
                antialiased=True
            )
            
            # Add color bar
            fig.colorbar(surf, shrink=0.5, aspect=5, label='Elevation (m)')
            
            # Set labels and title
            ax.set_xlabel('X Coordinate')
            ax.set_ylabel('Y Coordinate')
            ax.set_zlabel('Elevation')
            ax.set_title(title)
            
            plt.tight_layout()
            plt.show()
        except Exception as e:
            raise ValueError(f"Error creating 3D plot: {str(e)}")
    
    def export_to_geotiff(self, output_path):
        """
        Export the interpolated grid to a GeoTIFF file.
        
        Args:
            output_path (str): Path to save the output GeoTIFF
        """
        try:
            # Create a simple transform for the output
            transform = rasterio.transform.from_origin(
                self.grid_x.min(), 
                self.grid_y.max(), 
                (self.grid_x.max() - self.grid_x.min()) / self.grid_z.shape[1],
                (self.grid_y.max() - self.grid_y.min()) / self.grid_z.shape[0]
            )
            
            # Write to GeoTIFF
            with rasterio.open(
                output_path,
                'w',
                driver='GTiff',
                height=self.grid_z.shape[0],
                width=self.grid_z.shape[1],
                count=1,
                dtype=self.grid_z.dtype,
                crs='+proj=latlong',
                transform=transform,
            ) as dst:
                dst.write(self.grid_z, 1)
        except Exception as e:
            raise ValueError(f"Error exporting to GeoTIFF: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Initialize with sample data path
    model = MiningTerrainModel("sample_data.csv")
    
    try:
        # Load and process data
        model.load_csv_data()
        model.interpolate_grid()
        
        # Visualize
        model.plot_3d_model()
        
        # Export
        model.export_to_geotiff("output_terrain.tif")
        
    except Exception as e:
        print(f"Error processing terrain model: {str(e)}")
```
