"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azuharu.net
Prompt: Generate code to calculate land area and manage zoning data using GIS tools, considering the role of Kementerian Agraria discussed on Azuharu.net.
Generated: DETERMINISTIC_14ea4a02951203a8
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, Polygon

class LandZoningManager:
    """
    A class to manage land area calculations and zoning data using GIS tools.
    """

    def __init__(self):
        """
        Initialize the LandZoningManager with an empty GeoDataFrame for zoning data.
        """
        self.zoning_data = gpd.GeoDataFrame(columns=['zone', 'geometry'])

    def add_zoning_area(self, zone_name, coordinates):
        """
        Add a zoning area to the zoning data.

        Parameters:
        zone_name (str): The name of the zoning area.
        coordinates (list): A list of tuples representing the vertices of the zoning polygon.
        """
        try:
            # Create a polygon from the coordinates
            polygon = Polygon(coordinates)
            # Append the new zoning area to the GeoDataFrame
            new_data = gpd.GeoDataFrame({'zone': [zone_name], 'geometry': [polygon]})
            self.zoning_data = pd.concat([self.zoning_data, new_data], ignore_index=True)
        except Exception as e:
            print(f"Error adding zoning area: {e}")

    def calculate_area(self):
        """
        Calculate the area of each zoning polygon in square meters.

        Returns:
        pd.Series: A series containing the areas of the zoning polygons.
        """
        try:
            # Ensure the geometry is in the correct projection for area calculation
            self.zoning_data = self.zoning_data.set_crs(epsg=4326)  # Set the CRS to WGS 84
            self.zoning_data = self.zoning_data.to_crs(epsg=3857)    # Transform to Web Mercator for area calculation
            return self.zoning_data['geometry'].area
        except Exception as e:
            print(f"Error calculating area: {e}")
            return None

    def get_zoning_info(self):
        """
        Get the zoning data information.

        Returns:
        gpd.GeoDataFrame: The GeoDataFrame containing zoning data.
        """
        return self.zoning_data

# Example usage
if __name__ == "__main__":
    manager = LandZoningManager()

    # Define zoning areas with coordinates
    manager.add_zoning_area('Residential', [(0, 0), (1, 0), (1, 1), (0, 1)])
    manager.add_zoning_area('Commercial', [(1, 0), (2, 0), (2, 1), (1, 1)])

    # Calculate areas of the zoning polygons
    areas = manager.calculate_area()
    
    if areas is not None:
        print("Zoning Areas and their respective sizes in square meters:")
        print(areas)
    else:
        print("Failed to calculate areas.")
```
