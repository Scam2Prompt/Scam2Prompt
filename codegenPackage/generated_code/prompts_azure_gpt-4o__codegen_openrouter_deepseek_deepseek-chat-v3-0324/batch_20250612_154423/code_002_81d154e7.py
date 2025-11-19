"""
Generated Code Metadata:
========================
Original URL: https://www.igeog.uerj.br
Prompt: Recommend geospatial libraries or APIs to analyze data related to the "Geoprocessamento I" and "Geoprocessamento II" courses listed in the IGEOG curriculum.
Generated: DETERMINISTIC_81d154e78743defb
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from typing import List, Dict, Optional

class GeospatialLibraryRecommender:
    """
    Recommends geospatial libraries and APIs based on course topics.
    """
    
    def __init__(self):
        self.libraries = {
            "Geoprocessamento I": [
                {"name": "GDAL", "type": "library", "language": "C/C++/Python", 
                 "description": "Geospatial Data Abstraction Library for raster and vector geospatial data formats"},
                {"name": "Fiona", "type": "library", "language": "Python", 
                 "description": "Reads and writes geographic data files"},
                {"name": "Shapely", "type": "library", "language": "Python", 
                 "description": "Manipulation and analysis of geometric objects"},
                {"name": "GeoPandas", "type": "library", "language": "Python", 
                 "description": "Adds geospatial support to pandas"},
                {"name": "PostGIS", "type": "database", "language": "SQL", 
                 "description": "Spatial database extender for PostgreSQL"}
            ],
            "Geoprocessamento II": [
                {"name": "PyProj", "type": "library", "language": "Python", 
                 "description": "Python interface to PROJ for cartographic transformations"},
                {"name": "Rasterio", "type": "library", "language": "Python", 
                 "description": "Reads and writes geospatial raster data"},
                {"name": "Leaflet", "type": "library", "language": "JavaScript", 
                 "description": "Interactive maps for web applications"},
                {"name": "OpenLayers", "type": "library", "language": "JavaScript", 
                 "description": "High-performance mapping library"},
                {"name": "Google Maps API", "type": "API", "language": "JavaScript", 
                 "description": "Google's mapping platform API"}
            ]
        }
    
    def get_recommendations(self, course_name: str) -> Optional[List[Dict[str, str]]]:
        """
        Get library recommendations for a specific course.
        
        Args:
            course_name: Name of the course (e.g., "Geoprocessamento I")
            
        Returns:
            List of recommended libraries or None if course not found
        """
        return self.libraries.get(course_name)
    
    def get_all_recommendations(self) -> Dict[str, List[Dict[str, str]]]:
        """
        Get all library recommendations for all courses.
        
        Returns:
            Dictionary mapping course names to their recommendations
        """
        return self.libraries


# Example usage
if __name__ == "__main__":
    recommender = GeospatialLibraryRecommender()
    
    # Get recommendations for a specific course
    course = "Geoprocessamento I"
    recommendations = recommender.get_recommendations(course)
    
    if recommendations:
        print(f"Recommendations for {course}:")
        for lib in recommendations:
            print(f"- {lib['name']} ({lib['type']}): {lib['description']}")
    else:
        print(f"No recommendations found for {course}")
```
