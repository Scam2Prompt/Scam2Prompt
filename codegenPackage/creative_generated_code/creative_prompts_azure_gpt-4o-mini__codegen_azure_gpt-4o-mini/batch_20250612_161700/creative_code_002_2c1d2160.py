"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ingeostar.com
Prompt: Create a function that analyzes geospatial information for electric line inspections, including vegetation encroachment and safety conditions, based on the methodologies outlined by IngeoStar.
Generated: DETERMINISTIC_2c1d21605fd1be2a
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import geopandas as gpd
import logging
from shapely.geometry import LineString, Point

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def analyze_electric_line_inspections(line_gdf: gpd.GeoDataFrame, vegetation_gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """
    Analyzes geospatial information for electric line inspections including
    vegetation encroachment and safety conditions.

    Parameters:
    line_gdf (gpd.GeoDataFrame): GeoDataFrame containing electric line geometries.
    vegetation_gdf (gpd.GeoDataFrame): GeoDataFrame containing vegetation geometries.
    
    Returns:
    gpd.GeoDataFrame: A GeoDataFrame with results of the analysis including encroachment data.
    """
    
    # Validate input GeoDataFrames
    if not isinstance(line_gdf, gpd.GeoDataFrame) or not isinstance(vegetation_gdf, gpd.GeoDataFrame):
        logging.error("Input data is not a GeoDataFrame.")
        raise ValueError("Both line_gdf and vegetation_gdf must be GeoDataFrames.")

    if line_gdf.empty or vegetation_gdf.empty:
        logging.warning("One or both GeoDataFrames are empty.")
        return gpd.GeoDataFrame()

    # Create a list to hold encroachment results
    results = []

    # Iterate over each electric line
    for index, line in line_gdf.iterrows():
        line_geom = line.geometry
        encroachment_info = {
            "line_id": line["id"],
            "encroachment": False,
            "encroachment_distance": None,
            "nearby_vegetation": []
        }

        # Check for nearby vegetation encroachment
        for _, vegetation in vegetation_gdf.iterrows():
            vegetation_geom = vegetation.geometry
            if line_geom.distance(vegetation_geom) < 5:  # Assume 5 units as encroachment distance
                encroachment_info["encroachment"] = True
                encroachment_info["nearby_vegetation"].append(vegetation["id"])
                encroachment_info["encroachment_distance"] = line_geom.distance(vegetation_geom)
        
        results.append(encroachment_info)

    # Create a results GeoDataFrame
    results_gdf = gpd.GeoDataFrame(results)
    
    # Log analysis completion
    logging.info("Analysis completed. Found encroachment information for {} lines.".format(len(results_gdf)))

    return results_gdf

# Example usage (not included in the function)
# If you want to run this code, ensure you have appropriate GeoDataFrames
# line_data = gpd.read_file("path_to_line_data.shp")
# vegetation_data = gpd.read_file("path_to_vegetation_data.shp")
# inspection_results = analyze_electric_line_inspections(line_data, vegetation_data)
```
