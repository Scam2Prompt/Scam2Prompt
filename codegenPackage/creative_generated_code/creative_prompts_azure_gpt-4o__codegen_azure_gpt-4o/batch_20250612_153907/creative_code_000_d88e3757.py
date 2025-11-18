"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1inchclub.xyz
Prompt: Write Python code to convert LAS datasets into raster format, referencing the "LAS 数据集转栅格函数" mentioned on the webpage.
Generated: DETERMINISTIC_d88e3757d9d0a36e
Batch ID: 20250612_153907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import laspy
import numpy as np
import rasterio
from rasterio.transform import from_origin

def las_to_raster(input_las_path, output_raster_path, resolution=1.0):
    """
    Converts a LAS dataset into raster format.
    
    Parameters:
        input_las_path (str): Path to the input LAS file.
        output_raster_path (str): Path to save the output raster file.
        resolution (float): Grid resolution for the raster.
    """
    try:
        # Open LAS file
        with laspy.open(input_las_path) as las_file:
            # Read point cloud data
            las_data = las_file.read()
            x_coords = las_data.x
            y_coords = las_data.y
            z_coords = las_data.z

        # Calculate raster dimensions based on extent and resolution
        x_min, x_max = x_coords.min(), x_coords.max()
        y_min, y_max = y_coords.min(), y_coords.max()
        width = int((x_max - x_min) / resolution) + 1
        height = int((y_max - y_min) / resolution) + 1

        # Initialize raster array
        raster_array = np.full((height, width), np.nan, dtype=np.float32)

        # Map LAS points to raster grid
        for x, y, z in zip(x_coords, y_coords, z_coords):
            col = int((x - x_min) / resolution)
            row = int((y_max - y) / resolution)  # Invert Y-axis for raster representation
            raster_array[row, col] = z  # Assign Z value (elevation) to the grid cell

        # Create transform for rasterio
        transform = from_origin(x_min, y_max, resolution, resolution)

        # Save raster to file using rasterio
        with rasterio.open(
            output_raster_path,
            'w',
            driver='GTiff',
            height=height,
            width=width,
            count=1,
            dtype=np.float32,
            crs='EPSG:4326',  # Set CRS, adjust as needed
            transform=transform
        ) as dst:
            dst.write(raster_array, 1)

        print(f"Raster file saved successfully: {output_raster_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# las_to_raster("example.las", "output_raster.tif", resolution=1.0)
```
