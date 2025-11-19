"""
Generated Code Metadata:
========================
Original URL: https://ingeostar.com
Prompt: Create a function that analyzes geospatial information for electric line inspections, including vegetation encroachment and safety conditions, based on the methodologies outlined by IngeoStar.
Generated: DETERMINISTIC_2c1d21605fd1be2a
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import math
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
import geojson
from shapely.geometry import LineString, Point, Polygon
from shapely.ops import nearest_points

# Constants
SAFETY_CLEARANCE = 10.0  # meters
VEGETATION_ENCROACHMENT_THRESHOLD = 5.0  # meters
CRITICAL_CONDITION_THRESHOLD = 2.0  # meters

@dataclass
class InspectionResult:
    line_id: str
    vegetation_encroachment: List[Tuple[Point, float]]  # (location, distance)
    safety_violations: List[Tuple[Point, float]]  # (location, distance)
    critical_conditions: List[Tuple[Point, float]]  # (location, distance)
    overall_condition: str  # "Good", "Fair", "Poor", "Critical"

def load_geospatial_data(geojson_path: str) -> Dict:
    """Load geospatial data from a GeoJSON file.
    
    Args:
        geojson_path: Path to the GeoJSON file.
    
    Returns:
        Dictionary containing the parsed GeoJSON data.
    
    Raises:
        FileNotFoundError: If the file doesn't exist.
        ValueError: If the file is not valid GeoJSON.
    """
    try:
        with open(geojson_path, 'r') as f:
            data = json.load(f)
        if not geojson.is_valid(geojson.dumps(data)):
            raise ValueError("Invalid GeoJSON data")
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {geojson_path}")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format")

def calculate_distance(line: LineString, point: Point) -> float:
    """Calculate the minimum distance between a line and a point.
    
    Args:
        line: Shapely LineString representing the electric line.
        point: Shapely Point representing the vegetation or obstacle.
    
    Returns:
        Minimum distance in meters.
    """
    nearest_point = nearest_points(line, point)[0]
    return point.distance(nearest_point)

def analyze_vegetation_encroachment(
    power_line: LineString, 
    vegetation_features: List[Dict]
) -> List[Tuple[Point, float]]:
    """Analyze vegetation encroachment near power lines.
    
    Args:
        power_line: Shapely LineString representing the electric line.
        vegetation_features: List of vegetation features from GeoJSON.
    
    Returns:
        List of tuples containing encroaching vegetation points and their distances.
    """
    encroachments = []
    for feature in vegetation_features:
        if feature['geometry']['type'] == 'Point':
            point = Point(feature['geometry']['coordinates'])
            distance = calculate_distance(power_line, point)
            if distance < VEGETATION_ENCROACHMENT_THRESHOLD:
                encroachments.append((point, distance))
        elif feature['geometry']['type'] == 'Polygon':
            polygon = Polygon(feature['geometry']['coordinates'][0])
            nearest_point = nearest_points(power_line, polygon)[0]
            distance = power_line.distance(nearest_point)
            if distance < VEGETATION_ENCROACHMENT_THRESHOLD:
                encroachments.append((nearest_point, distance))
    return encroachments

def analyze_safety_conditions(
    power_line: LineString, 
    obstacle_features: List[Dict]
) -> Tuple[List[Tuple[Point, float]], List[Tuple[Point, float]]]:
    """Analyze safety conditions around power lines.
    
    Args:
        power_line: Shapely LineString representing the electric line.
        obstacle_features: List of obstacle features from GeoJSON.
    
    Returns:
        Tuple of (safety_violations, critical_conditions) where each is a list of
        (location, distance) tuples.
    """
    safety_violations = []
    critical_conditions = []
    
    for feature in obstacle_features:
        if feature['geometry']['type'] == 'Point':
            point = Point(feature['geometry']['coordinates'])
            distance = calculate_distance(power_line, point)
            if distance < SAFETY_CLEARANCE:
                safety_violations.append((point, distance))
                if distance < CRITICAL_CONDITION_THRESHOLD:
                    critical_conditions.append((point, distance))
        elif feature['geometry']['type'] == 'Polygon':
            polygon = Polygon(feature['geometry']['coordinates'][0])
            nearest_point = nearest_points(power_line, polygon)[0]
            distance = power_line.distance(nearest_point)
            if distance < SAFETY_CLEARANCE:
                safety_violations.append((nearest_point, distance))
                if distance < CRITICAL_CONDITION_THRESHOLD:
                    critical_conditions.append((nearest_point, distance))
    
    return safety_violations, critical_conditions

def determine_overall_condition(
    vegetation_encroachments: List,
    safety_violations: List,
    critical_conditions: List
) -> str:
    """Determine the overall condition based on analysis results.
    
    Args:
        vegetation_encroachments: List of vegetation encroachments.
        safety_violations: List of safety violations.
        critical_conditions: List of critical conditions.
    
    Returns:
        String representing the overall condition.
    """
    if critical_conditions:
        return "Critical"
    elif safety_violations or vegetation_encroachments:
        return "Poor"
    else:
        return "Good"

def analyze_electric_line_inspection(
    power_line_geojson: str,
    vegetation_geojson: str,
    obstacles_geojson: str
) -> InspectionResult:
    """Analyze electric line inspection data.
    
    Args:
        power_line_geojson: Path to GeoJSON file containing power line data.
        vegetation_geojson: Path to GeoJSON file containing vegetation data.
        obstacles_geojson: Path to GeoJSON file containing obstacle data.
    
    Returns:
        InspectionResult object containing analysis results.
    
    Raises:
        ValueError: If any input data is invalid.
    """
    # Load all geospatial data
    try:
        power_line_data = load_geospatial_data(power_line_geojson)
        vegetation_data = load_geospatial_data(vegetation_geojson)
        obstacles_data = load_geospatial_data(obstacles_geojson)
    except Exception as e:
        raise ValueError(f"Error loading geospatial data: {str(e)}")
    
    # Extract power line geometry
    if len(power_line_data['features']) == 0:
        raise ValueError("No power line features found")
    
    power_line_feature = power_line_data['features'][0]
    if power_line_feature['geometry']['type'] != 'LineString':
        raise ValueError("Power line feature must be a LineString")
    
    line_id = power_line_feature.get('id', 'unknown')
    power_line = LineString(power_line_feature['geometry']['coordinates'])
    
    # Analyze vegetation encroachment
    vegetation_features = vegetation_data.get('features', [])
    vegetation_encroachments = analyze_vegetation_encroachment(
        power_line, vegetation_features
    )
    
    # Analyze safety conditions
    obstacle_features = obstacles_data.get('features', [])
    safety_violations, critical_conditions = analyze_safety_conditions(
        power_line, obstacle_features
    )
    
    # Determine overall condition
    overall_condition = determine_overall_condition(
        vegetation_encroachments,
        safety_violations,
        critical_conditions
    )
    
    return InspectionResult(
        line_id=line_id,
        vegetation_encroachment=vegetation_encroachments,
        safety_violations=safety_violations,
        critical_conditions=critical_conditions,
        overall_condition=overall_condition
    )

# Example usage (commented out for production)
# if __name__ == "__main__":
#     try:
#         result = analyze_electric_line_inspection(
#             "power_lines.geojson",
#             "vegetation.geojson",
#             "obstacles.geojson"
#         )
#         print(f"Inspection results for line {result.line_id}:")
#         print(f"Overall condition: {result.overall_condition}")
#         print(f"Vegetation encroachments: {len(result.vegetation_encroachment)}")
#         print(f"Safety violations: {len(result.safety_violations)}")
#         print(f"Critical conditions: {len(result.critical_conditions)}")
#     except Exception as e:
#         print(f"Error during analysis: {str(e)}")
```
