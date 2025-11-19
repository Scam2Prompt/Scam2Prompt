"""
Generated Code Metadata:
========================
Original URL: https://kataskeui.gr
Prompt: Write Python code to calculate coordinates for a topographic diagram based on the ΕΓΣΑ ‘87 Greek Geodetic Reference System. Include validation for accurate boundary representation.
Generated: DETERMINISTIC_1569883bec2781e5
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
import numpy as np
from pyproj import CRS, Transformer

class EGSA87TopographicCalculator:
    """
    A class to calculate topographic coordinates in the ΕΓΣΑ ‘87 Greek Geodetic Reference System.
    Provides methods for coordinate transformation and boundary validation.
    """
    
    def __init__(self):
        """
        Initialize the coordinate reference systems and transformers.
        """
        # Define CRS for WGS84 (EPSG:4326) and EGSA87 (EPSG:2100)
        self.wgs84 = CRS.from_epsg(4326)
        self.egsa87 = CRS.from_epsg(2100)
        
        # Create transformers for WGS84 to EGSA87 and vice versa
        self.to_egsa87 = Transformer.from_crs(self.wgs84, self.egsa87)
        self.to_wgs84 = Transformer.from_crs(self.egsa87, self.wgs84)
        
        # Define approximate boundaries of Greece in WGS84 (lat, lon)
        self.greece_bounds = {
            'min_lat': 34.5,
            'max_lat': 42.0,
            'min_lon': 19.0,
            'max_lon': 29.0
        }
    
    def validate_bounds(self, lat, lon):
        """
        Validate if given coordinates are within approximate Greek boundaries.
        
        Args:
            lat (float): Latitude in WGS84
            lon (float): Longitude in WGS84
            
        Returns:
            bool: True if coordinates are within bounds, False otherwise
        """
        return (self.greece_bounds['min_lat'] <= lat <= self.greece_bounds['max_lat'] and
                self.greece_bounds['min_lon'] <= lon <= self.greece_bounds['max_lon'])
    
    def wgs84_to_egsa87(self, lat, lon, height=0.0):
        """
        Convert WGS84 coordinates to EGSA87.
        
        Args:
            lat (float): Latitude in WGS84
            lon (float): Longitude in WGS84
            height (float, optional): Height in meters. Defaults to 0.0.
            
        Returns:
            tuple: (easting, northing) in EGSA87
        """
        if not self.validate_bounds(lat, lon):
            raise ValueError("Coordinates are outside Greek boundaries")
        
        easting, northing = self.to_egsa87.transform(lat, lon, height)
        return easting, northing
    
    def egsa87_to_wgs84(self, easting, northing, height=0.0):
        """
        Convert EGSA87 coordinates to WGS84.
        
        Args:
            easting (float): Easting coordinate in EGSA87
            northing (float): Northing coordinate in EGSA87
            height (float, optional): Height in meters. Defaults to 0.0.
            
        Returns:
            tuple: (latitude, longitude) in WGS84
        """
        lat, lon = self.to_wgs84.transform(easting, northing, height)
        
        if not self.validate_bounds(lat, lon):
            raise ValueError("Coordinates are outside Greek boundaries")
        
        return lat, lon
    
    def calculate_topographic_diagram(self, points_wgs84):
        """
        Calculate topographic diagram coordinates in EGSA87 from WGS84 points.
        
        Args:
            points_wgs84 (list of tuples): List of (lat, lon) points in WGS84
            
        Returns:
            dict: {
                'points_egsa87': list of transformed points,
                'bounding_box': (min_easting, max_easting, min_northing, max_northing),
                'centroid': (easting, northing),
                'area': area in square meters (for closed polygons)
            }
        """
        if not points_wgs84:
            raise ValueError("No points provided")
        
        # Validate all points are within bounds
        for lat, lon in points_wgs84:
            if not self.validate_bounds(lat, lon):
                raise ValueError(f"Point ({lat}, {lon}) is outside Greek boundaries")
        
        # Transform all points to EGSA87
        points_egsa87 = [self.wgs84_to_egsa87(lat, lon) for lat, lon in points_wgs84]
        
        # Calculate bounding box
        eastings = [p[0] for p in points_egsa87]
        northings = [p[1] for p in points_egsa87]
        
        min_easting = min(eastings)
        max_easting = max(eastings)
        min_northing = min(northings)
        max_northing = max(northings)
        
        # Calculate centroid
        centroid_easting = sum(eastings) / len(eastings)
        centroid_northing = sum(northings) / len(northings)
        
        # Calculate area if it's a closed polygon (first and last point are the same)
        area = 0.0
        if len(points_egsa87) > 2 and points_egsa87[0] == points_egsa87[-1]:
            area = self._calculate_polygon_area(points_egsa87)
        
        return {
            'points_egsa87': points_egsa87,
            'bounding_box': (min_easting, max_easting, min_northing, max_northing),
            'centroid': (centroid_easting, centroid_northing),
            'area': area
        }
    
    def _calculate_polygon_area(self, points):
        """
        Calculate the area of a polygon using the shoelace formula.
        
        Args:
            points (list of tuples): List of (easting, northing) points
            
        Returns:
            float: Area in square meters
        """
        x = np.array([p[0] for p in points])
        y = np.array([p[1] for p in points])
        
        # Shoelace formula
        return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
```
