"""
Generated Code Metadata:
========================
Original URL: https://ecpowerlightingltd.com
Prompt: Generate code for an underground utility mapping application that aligns with the expertise of E.C. Power & Lighting Ltd. in electrical installations.
Generated: DETERMINISTIC_04b9ee51f3ee970f
Batch ID: 20250612_163749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import uuid
from typing import Dict, List, Optional
from datetime import datetime
from enum import Enum

class UtilityType(Enum):
    """Enum representing different types of underground utilities."""
    ELECTRICAL = "ELECTRICAL"
    WATER = "WATER"
    GAS = "GAS"
    FIBER_OPTIC = "FIBER_OPTIC"
    SEWER = "SEWER"

class UtilityLine:
    """Class representing an underground utility line."""
    
    def __init__(
        self,
        utility_type: UtilityType,
        depth: float,
        start_point: Dict[str, float],
        end_point: Dict[str, float],
        voltage: Optional[float] = None,
        owner: Optional[str] = None,
        installation_date: Optional[str] = None
    ):
        """
        Initialize a UtilityLine instance.
        
        Args:
            utility_type: Type of utility (ELECTRICAL, WATER, etc.)
            depth: Depth of the utility line in meters
            start_point: Dictionary with 'x' and 'y' coordinates of the start point
            end_point: Dictionary with 'x' and 'y' coordinates of the end point
            voltage: Voltage for electrical lines (optional)
            owner: Owner of the utility line (optional)
            installation_date: Date of installation in YYYY-MM-DD format (optional)
        """
        self.id = str(uuid.uuid4())
        self.utility_type = utility_type
        self.depth = depth
        self.start_point = start_point
        self.end_point = end_point
        self.voltage = voltage
        self.owner = owner or "Unknown"
        self.installation_date = installation_date or datetime.now().strftime("%Y-%m-%d")
        
        self.validate()
    
    def validate(self):
        """Validate the utility line data."""
        if self.depth <= 0:
            raise ValueError("Depth must be greater than 0")
        
        if not all(key in self.start_point for key in ('x', 'y')):
            raise ValueError("Start point must contain 'x' and 'y' coordinates")
            
        if not all(key in self.end_point for key in ('x', 'y')):
            raise ValueError("End point must contain 'x' and 'y' coordinates")
        
        if self.utility_type == UtilityType.ELECTRICAL and self.voltage is None:
            raise ValueError("Voltage must be specified for electrical lines")

class UtilityMap:
    """Class representing a collection of underground utility lines."""
    
    def __init__(self):
        """Initialize an empty UtilityMap."""
        self.lines: List[UtilityLine] = []
    
    def add_line(self, line: UtilityLine) -> None:
        """Add a utility line to the map."""
        self.lines.append(line)
    
    def remove_line(self, line_id: str) -> bool:
        """
        Remove a utility line by its ID.
        
        Returns:
            bool: True if line was found and removed, False otherwise
        """
        for i, line in enumerate(self.lines):
            if line.id == line_id:
                self.lines.pop(i)
                return True
        return False
    
    def find_lines_by_type(self, utility_type: UtilityType) -> List[UtilityLine]:
        """Find all utility lines of a specific type."""
        return [line for line in self.lines if line.utility_type == utility_type]
    
    def find_lines_near_point(self, point: Dict[str, float], radius: float) -> List[UtilityLine]:
        """
        Find utility lines within a certain radius of a point.
        
        Args:
            point: Dictionary with 'x' and 'y' coordinates
            radius: Search radius in meters
            
        Returns:
            List of UtilityLine objects within the radius
        """
        if not all(key in point for key in ('x', 'y')):
            raise ValueError("Point must contain 'x' and 'y' coordinates")
            
        return [
            line for line in self.lines
            if self._distance_to_line(point, line) <= radius
        ]
    
    def _distance_to_line(self, point: Dict[str, float], line: UtilityLine) -> float:
        """Calculate minimum distance from point to a line segment."""
        # Simplified distance calculation (for demonstration)
        # In production, use proper geometric calculations
        start_x, start_y = line.start_point['x'], line.start_point['y']
        end_x, end_y = line.end_point['x'], line.end_point['y']
        point_x, point_y = point['x'], point['y']
        
        # Calculate distance to line segment (simplified)
        dx = end_x - start_x
        dy = end_y - start_y
        length_squared = dx*dx + dy*dy
        
        if length_squared == 0:
            # Line is actually a point
            return ((point_x - start_x)**2 + (point_y - start_y)**2)**0.5
        
        t = max(0, min(1, ((point_x - start_x) * dx + (point_y - start_y) * dy) / length_squared))
        projection_x = start_x + t * dx
        projection_y = start_y + t * dy
        
        return ((point_x - projection_x)**2 + (point_y - projection_y)**2)**0.5
    
    def to_geojson(self) -> Dict:
        """Convert the utility map to GeoJSON format."""
        features = []
        for line in self.lines:
            feature = {
                "type": "Feature",
                "properties": {
                    "id": line.id,
                    "utility_type": line.utility_type.value,
                    "depth": line.depth,
                    "voltage": line.voltage,
                    "owner": line.owner,
                    "installation_date": line.installation_date
                },
                "geometry": {
                    "type": "LineString",
                    "coordinates": [
                        [line.start_point['x'], line.start_point['y']],
                        [line.end_point['x'], line.end_point['y']]
                    ]
                }
            }
            features.append(feature)
        
        return {
            "type": "FeatureCollection",
            "features": features
        }
    
    def save_to_file(self, filename: str) -> None:
        """Save the utility map to a GeoJSON file."""
        with open(filename, 'w') as f:
            json.dump(self.to_geojson(), f, indent=2)
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'UtilityMap':
        """Load a utility map from a GeoJSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        utility_map = cls()
        for feature in data['features']:
            props = feature['properties']
            coords = feature['geometry']['coordinates']
            
            line = UtilityLine(
                utility_type=UtilityType(props['utility_type']),
                depth=props['depth'],
                start_point={'x': coords[0][0], 'y': coords[0][1]},
                end_point={'x': coords[1][0], 'y': coords[1][1]},
                voltage=props.get('voltage'),
                owner=props.get('owner'),
                installation_date=props.get('installation_date')
            )
            line.id = props['id']  # Preserve original ID
            utility_map.add_line(line)
        
        return utility_map

# Example usage
if __name__ == "__main__":
    try:
        # Create a new utility map
        utility_map = UtilityMap()
        
        # Add some electrical lines (specific to E.C. Power & Lighting Ltd.)
        electrical_line1 = UtilityLine(
            utility_type=UtilityType.ELECTRICAL,
            depth=1.2,
            start_point={'x': -73.9876, 'y': 40.7484},
            end_point={'x': -73.9865, 'y': 40.7478},
            voltage=480,
            owner="E.C. Power & Lighting Ltd.",
            installation_date="2022-05-15"
        )
        
        electrical_line2 = UtilityLine(
            utility_type=UtilityType.ELECTRICAL,
            depth=1.5,
            start_point={'x': -73.9850, 'y': 40.7490},
            end_point={'x': -73.9842, 'y': 40.7485},
            voltage=208,
            owner="E.C. Power & Lighting Ltd."
        )
        
        utility_map.add_line(electrical_line1)
        utility_map.add_line(electrical_line2)
        
        # Add a water line (for demonstration)
        water_line = UtilityLine(
            utility_type=UtilityType.WATER,
            depth=2.0,
            start_point={'x': -73.9860, 'y': 40.7470},
            end_point={'x': -73.9850, 'y': 40.7465},
            owner="City Water Dept."
        )
        utility_map.add_line(water_line)
        
        # Save to file
        utility_map.save_to_file("utility_map.geojson")
        
        # Find all electrical lines
        electrical_lines = utility_map.find_lines_by_type
