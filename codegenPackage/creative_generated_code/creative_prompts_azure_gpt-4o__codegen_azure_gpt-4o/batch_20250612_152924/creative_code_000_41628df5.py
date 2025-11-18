"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ingeostar.com
Prompt: Write Python code to process georeferenced images captured by RPA drones for terrain modeling in 3D, using tools or libraries for geospatial analysis.
Generated: DETERMINISTIC_41628df5c16f489b
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import os
import numpy as np
import rasterio
from rasterio.plot import show
from rasterio.warp import calculate_default_transform, reproject, Resampling
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def process_georeferenced_images(image_folder, output_terrain_file, crs_target="EPSG:4326"):
    """
    Processes georeferenced images captured by RPA drones for terrain modeling in 3D.
    
    Args:
        image_folder (str): Path to the folder containing georeferenced images.
        output_terrain_file (str): Path to save the generated terrain model.
        crs_target (str): Target CRS for reprojecting georeferenced images. Defaults to "EPSG:4326".
        
    Returns:
        None
    """
    # Validate input folder
    if not os.path.isdir(image_folder):
        raise FileNotFoundError(f"Image folder not found: {image_folder}")
    
    # Initialize list to store georeferenced data points
    geo_points = []
    
    # Process each georeferenced image in the folder
    for image_file in os.listdir(image_folder):
        file_path = os.path.join(image_folder, image_file)
        if not rasterio.can_open(file_path):
            print(f"Skipping non-image file: {file_path}")
            continue
        
        try:
            # Open the georeferenced image
            with rasterio.open(file_path) as src:
                # Reproject image to target CRS
                transform, width, height = calculate_default_transform(
                    src.crs, crs_target, src.width, src.height, *src.bounds
                )
                kwargs = src.meta.copy()
                kwargs.update({
                    'crs': crs_target,
                    'transform': transform,
                    'width': width,
                    'height': height
                })
                
                # Create a new dataset in memory with reprojected data
                with rasterio.MemoryFile() as memfile:
                    with memfile.open(**kwargs) as dst:
                        for i in range(1, src.count + 1):
                            reproject(
                                source=rasterio.band(src, i),
                                destination=rasterio.band(dst, i),
                                src_transform=src.transform,
                                src_crs=src.crs,
                                dst_transform=transform,
                                dst_crs=crs_target,
                                resampling=Resampling.nearest
                            )
                        
                        # Extract pixel values and corresponding coordinates
                        for x in range(dst.width):
                            for y in range(dst.height):
                                value = dst.read(1)[y, x]
                                if np.isfinite(value):  # Check for valid pixel values
                                    geo_x, geo_y = rasterio.transform.xy(transform, y, x, offset="center")
                                    geo_points.append((geo_x, geo_y, value))
        except Exception as e:
            print(f"Error processing image {file_path}: {e}")
    
    # Convert collected data points into numpy array for terrain generation
    if not geo_points:
        raise ValueError("No valid georeferenced data points found.")
    
    geo_points = np.array(geo_points)
    
    # Interpolate terrain data onto a regular grid
    grid_x, grid_y = np.meshgrid(
        np.linspace(np.min(geo_points[:, 0]), np.max(geo_points[:, 0]), 500),
        np.linspace(np.min(geo_points[:, 1]), np.max(geo_points[:, 1]), 500)
    )
    grid_z = griddata(
        points=geo_points[:, :2], values=geo_points[:, 2],
        xi=(grid_x, grid_y), method='cubic'
    )
    
    # Save the generated terrain model as a numpy file
    np.save(output_terrain_file, grid_z)
    print(f"Terrain model saved to {output_terrain_file}")
    
    # Plot the terrain in 3D
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(grid_x, grid_y, grid_z, cmap='terrain', edgecolor='none')
    ax.set_title("3D Terrain Model")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.set_zlabel("Elevation")
    plt.show()


# Example usage:
# process_georeferenced_images("path/to/images", "output_terrain.npy")
```
