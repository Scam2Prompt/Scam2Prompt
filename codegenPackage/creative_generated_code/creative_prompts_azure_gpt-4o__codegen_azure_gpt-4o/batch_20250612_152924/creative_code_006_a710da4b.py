"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ingeostar.com
Prompt: Suggest APIs or libraries for analyzing geospatial data to ensure compliance with height and safety standards for electrical line crossings.
Generated: DETERMINISTIC_a710da4b49da5d2e
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to use geospatial libraries to analyze data 
and ensure compliance with height and safety standards for electrical line crossings.

Libraries used:
- GeoPandas for GIS data manipulation
- Shapely for geometric calculations
- Pyproj for coordinate transformations
"""

import geopandas as gpd
from shapely.geometry import LineString, Point
from pyproj import Geod

# Define constants for height and safety standards
MINIMUM_HEIGHT_THRESHOLD = 5.0  # Minimum height in meters
BUFFER_DISTANCE = 10.0         # Safety buffer distance in meters

# Function to calculate height compliance for electrical lines
def check_height_compliance(line_geometry, height_data):
    """
    Check if an electrical line meets the minimum height threshold.

    Parameters:
    line_geometry (LineString): Geometry of the electrical line.
    height_data (dict): Dictionary containing height data for each segment of the line.

    Returns:
    bool: True if compliant, False otherwise.
    """
    for segment, height in height_data.items():
        if height < MINIMUM_HEIGHT_THRESHOLD:
            return False
    return True


# Function to check safety buffer compliance
def check_safety_buffer(line_geometry, nearby_objects):
    """
    Check if an electrical line maintains a safe buffer distance from nearby objects.

    Parameters:
    line_geometry (LineString): Geometry of the electrical line.
    nearby_objects (GeoDataFrame): Geospatial data of nearby objects.

    Returns:
    bool: True if compliant, False otherwise.
    """
    geod = Geod(ellps="WGS84")  # Use WGS84 ellipsoid for distance calculation
    for _, obj in nearby_objects.iterrows():
        object_geometry = obj.geometry
        distance = geod.geometry_length(line_geometry.distance(object_geometry))
        if distance < BUFFER_DISTANCE:
            return False
    return True


# Main function to analyze geospatial data for compliance
def analyze_compliance(electrical_lines_gdf, nearby_objects_gdf, height_data):
    """
    Analyze geospatial data to ensure compliance with standards.

    Parameters:
    electrical_lines_gdf (GeoDataFrame): Geospatial data of electrical lines.
    nearby_objects_gdf (GeoDataFrame): Geospatial data of nearby objects.
    height_data (dict): Dictionary containing height data for each electrical line.

    Returns:
    list: List of non-compliant electrical lines.
    """
    non_compliant_lines = []

    for _, line in electrical_lines_gdf.iterrows():
        line_geometry = line.geometry
        line_id = line['id']

        # Check height compliance
        if not check_height_compliance(line_geometry, height_data[line_id]):
            non_compliant_lines.append((line_id, "Height Non-Compliance"))
            continue

        # Check safety buffer compliance
        if not check_safety_buffer(line_geometry, nearby_objects_gdf):
            non_compliant_lines.append((line_id, "Safety Buffer Non-Compliance"))
    
    return non_compliant_lines


# Example usage:
if __name__ == "__main__":
    try:
        # Load geospatial data (replace file paths with actual data sources)
        electrical_lines_gdf = gpd.read_file("data/electrical_lines.shp")
        nearby_objects_gdf = gpd.read_file("data/nearby_objects.shp")
        
        # Example height data (replace with actual height data)
        height_data = {
            1: [6.0, 5.5, 4.0],  # Heights for line segments (example data)
            2: [8.0, 7.0, 6.5],
        }
        
        # Analyze compliance
        non_compliant_lines = analyze_compliance(electrical_lines_gdf, nearby_objects_gdf, height_data)
        
        # Output results
        if not non_compliant_lines:
            print("All electrical lines are compliant.")
        else:
            print("Non-compliant electrical lines:")
            for line in non_compliant_lines:
                print(f"Line ID: {line[0]}, Issue: {line[1]}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
