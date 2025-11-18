"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ingeostar.com
Prompt: Write code to verify vegetation encroachment along electrical line corridors using geospatial data and generate a compliance report.
Generated: DETERMINISTIC_c9a1d65fc181d40b
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import geopandas as gpd
from shapely.geometry import LineString, Polygon
import pandas as pd

def check_vegetation_encroachment(power_line_file, vegetation_file, buffer_distance, output_report_file):
    """
    This function checks for vegetation encroachment along electrical line corridors
    and generates a compliance report.

    Args:
        power_line_file (str): Path to the file containing power line geospatial data (e.g., GeoJSON/Shapefile).
        vegetation_file (str): Path to the file containing vegetation geospatial data (e.g., GeoJSON/Shapefile).
        buffer_distance (float): Buffer distance around the power lines to check for vegetation encroachment (in meters).
        output_report_file (str): Path to the output compliance report file (CSV format).
    """
    try:
        # Load geospatial data for power lines and vegetation
        power_lines = gpd.read_file(power_line_file)
        vegetation = gpd.read_file(vegetation_file)

        # Ensure both datasets use the same coordinate reference system (CRS)
        if power_lines.crs != vegetation.crs:
            vegetation = vegetation.to_crs(power_lines.crs)

        # Create buffer zones around power lines
        power_lines['buffer_zone'] = power_lines.geometry.buffer(buffer_distance)

        # Check for intersections between buffer zones and vegetation polygons
        encroachment_results = []
        for idx, line in power_lines.iterrows():
            buffer_zone = line['buffer_zone']
            encroaching_vegetation = vegetation[vegetation.geometry.intersects(buffer_zone)]

            # Record encroachment details
            encroachment_results.append({
                'power_line_id': line.get('id', idx),  # Use 'id' column if it exists, else index
                'num_encroachments': len(encroaching_vegetation),
                'encroachment_areas': encroaching_vegetation.geometry.area.sum()  # Total area intersecting
            })

        # Generate compliance report as a DataFrame
        compliance_report = pd.DataFrame(encroachment_results)

        # Save compliance report to file
        compliance_report.to_csv(output_report_file, index=False)
        print(f"Compliance report successfully saved to {output_report_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    power_line_file = "data/power_lines.geojson"  # Replace with your file path
    vegetation_file = "data/vegetation.geojson"  # Replace with your file path
    buffer_distance = 10.0  # Buffer distance in meters
    output_report_file = "output/compliance_report.csv"

    check_vegetation_encroachment(power_line_file, vegetation_file, buffer_distance, output_report_file)
```
