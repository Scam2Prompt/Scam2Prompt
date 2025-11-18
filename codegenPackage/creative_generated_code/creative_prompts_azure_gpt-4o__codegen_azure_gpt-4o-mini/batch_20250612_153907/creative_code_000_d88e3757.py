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
import os

def las_to_raster(las_file_path, raster_file_path, pixel_size=1.0):
    """
    Convert a LAS dataset into raster format.

    Parameters:
    las_file_path (str): The file path of the input LAS file.
    raster_file_path (str): The file path for the output raster file.
    pixel_size (float): The size of the pixel in the output raster.

    Raises:
    FileNotFoundError: If the LAS file does not exist.
    ValueError: If the LAS file is empty or not properly formatted.
    """
    # Check if the LAS file exists
    if not os.path.exists(las_file_path):
        raise FileNotFoundError(f"The file {las_file_path} does not exist.")

    # Read the LAS file
    with laspy.open(las_file_path) as las:
        las_data = las.read()
    
    # Ensure the LAS data is not empty
    if las_data.points.size == 0:
        raise ValueError(f"The LAS file {las_file_path} is empty or not properly formatted.")

    # Extract X, Y, and Z coordinates
    x = las_data.x
    y = las_data.y
    z = las_data.z

    # Calculate the bounds of the raster
    min_x, max_x = x.min(), x.max()
    min_y, max_y = y.min(), y.max()
    
    # Calculate the dimensions of the raster
    width = int((max_x - min_x) / pixel_size) + 1
    height = int((max_y - min_y) / pixel_size) + 1
    
    # Create an empty raster array
    raster_array = np.full((height, width), np.nan, dtype=np.float32)

    # Populate the raster array with Z values
    for xi, yi, zi in zip(x, y, z):
        col = int((xi - min_x) / pixel_size)
        row = int((max_y - yi) / pixel_size)  # Invert Y-axis for raster
    
        # Assign Z value; if there is already a value, take the maximum (or adjust as needed)
        if np.isnan(raster_array[row, col]) or raster_array[row, col] < zi:
            raster_array[row, col] = zi

    # Define the transformation for the raster
    transform = from_origin(min_x, max_y, pixel_size, pixel_size)

    # Write the raster to a file
    with rasterio.open(
        raster_file_path,
        'w',
        driver='GTiff',
        height=height,
        width=width,
        count=1,
        dtype=raster_array.dtype,
        crs='EPSG:4326',  # Change as appropriate for your data
        transform=transform,
    ) as dst:
        dst.write(raster_array, 1)

# Example usage:
# las_to_raster('input.las', 'output.tif', pixel_size=1.0)
```
