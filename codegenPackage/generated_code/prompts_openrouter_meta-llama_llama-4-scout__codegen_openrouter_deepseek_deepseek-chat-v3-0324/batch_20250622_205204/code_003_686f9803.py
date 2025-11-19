"""
Generated Code Metadata:
========================
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: "Compare the features and prices of different types of glass doors, including sliding, pivot, and hinged doors, for an office renovation project."
Generated: DETERMINISTIC_686f9803e6b2c994
Batch ID: 20250622_205204
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class GlassDoor:
    """Represents a glass door with its features and pricing."""
    door_type: str
    material: str
    thickness_mm: float
    height_mm: float
    width_mm: float
    price: float
    features: List[str]
    energy_efficient: bool
    soundproof: bool
    lead_time_days: int

class GlassDoorComparator:
    """Compares different types of glass doors based on features and prices."""
    
    def __init__(self):
        self.doors: List[GlassDoor] = []
    
    def add_door(self, door: GlassDoor) -> None:
        """Add a door to the comparison list."""
        self.doors.append(door)
    
    def load_from_json(self, file_path: str) -> None:
        """Load door data from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                for item in data:
                    self.add_door(GlassDoor(**item))
        except FileNotFoundError:
            print(f"Error: File {file_path} not found.")
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in {file_path}.")
        except Exception as e:
            print(f"Error loading data: {str(e)}")
    
    def compare_by_price(self) -> List[GlassDoor]:
        """Return doors sorted by price (ascending)."""
        return sorted(self.doors, key=lambda x: x.price)
    
    def compare_by_feature(self, feature: str) -> List[GlassDoor]:
        """Return doors that have the specified feature."""
        return [door for door in self.doors if feature in door.features]
    
    def filter_by_type(self, door_type: str) -> List[GlassDoor]:
        """Filter doors by type."""
        return [door for door in self.doors if door.door_type.lower() == door_type.lower()]
    
    def get_summary(self) -> Dict[str, Dict[str, float]]:
        """Get summary statistics for all doors."""
        summary = {}
        for door in self.doors:
            if door.door_type not in summary:
                summary[door.door_type] = {
                    'min_price': door.price,
                    'max_price': door.price,
                    'avg_price': door.price,
                    'count': 1
                }
            else:
                summary[door.door_type]['min_price'] = min(summary[door.door_type]['min_price'], door.price)
                summary[door.door_type]['max_price'] = max(summary[door.door_type]['max_price'], door.price)
                summary[door.door_type]['avg_price'] = (
                    (summary[door.door_type]['avg_price'] * summary[door.door_type]['count'] + door.price) / 
                    (summary[door.door_type]['count'] + 1)
                )
                summary[door.door_type]['count'] += 1
        return summary
    
    def generate_report(self) -> str:
        """Generate a comparison report in JSON format."""
        report = {
            'doors': [door.__dict__ for door in self.doors],
            'summary': self.get_summary()
        }
        return json.dumps(report, indent=2)

# Example usage
if __name__ == "__main__":
    comparator = GlassDoorComparator()
    
    # Sample data (in production, this would come from a database or file)
    sample_doors = [
        {
            "door_type": "sliding",
            "material": "tempered glass",
            "thickness_mm": 10.0,
            "height_mm": 2100.0,
            "width_mm": 900.0,
            "price": 1200.0,
            "features": ["space-saving", "modern look"],
            "energy_efficient": True,
            "soundproof": False,
            "lead_time_days": 14
        },
        {
            "door_type": "pivot",
            "material": "laminated glass",
            "thickness_mm": 12.0,
            "height_mm": 2200.0,
            "width_mm": 1000.0,
            "price": 1800.0,
            "features": ["360-degree rotation", "modern look"],
            "energy_efficient": True,
            "soundproof": True,
            "lead_time_days": 21
        },
        {
            "door_type": "hinged",
            "material": "tempered glass",
            "thickness_mm": 8.0,
            "height_mm": 2100.0,
            "width_mm": 800.0,
            "price": 950.0,
            "features": ["traditional look", "easy installation"],
            "energy_efficient": False,
            "soundproof": False,
            "lead_time_days": 7
        }
    ]
    
    # Add sample doors
    for door_data in sample_doors:
        comparator.add_door(GlassDoor(**door_data))
    
    # Generate and print report
    print(comparator.generate_report())
```
