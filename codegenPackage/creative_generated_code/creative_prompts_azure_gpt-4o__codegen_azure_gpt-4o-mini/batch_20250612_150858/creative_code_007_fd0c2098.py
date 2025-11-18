"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vansoltravel.com
Prompt: Write a program to extract and categorize Vansol Travel's tour packages by activity type, such as adventure tours or pilgrimage tours.
Generated: DETERMINISTIC_fd0c20986427203c
Batch ID: 20250612_150858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class TourPackage:
    """Class to represent a tour package with its details."""
    def __init__(self, name: str, activity_type: str, price: float):
        self.name = name
        self.activity_type = activity_type
        self.price = price

    def to_dict(self) -> Dict[str, Any]:
        """Convert the TourPackage instance to a dictionary."""
        return {
            'name': self.name,
            'activity_type': self.activity_type,
            'price': self.price
        }

class TourPackageManager:
    """Class to manage tour packages and categorize them by activity type."""
    def __init__(self):
        self.packages: List[TourPackage] = []

    def load_packages_from_json(self, json_data: str) -> None:
        """Load tour packages from a JSON string."""
        try:
            data = json.loads(json_data)
            for item in data:
                package = TourPackage(
                    name=item.get('name', ''),
                    activity_type=item.get('activity_type', ''),
                    price=float(item.get('price', 0.0))
                )
                self.packages.append(package)
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Error loading packages: {e}")

    def categorize_packages(self) -> Dict[str, List[Dict[str, Any]]]:
        """Categorize packages by activity type."""
        categorized = {}
        for package in self.packages:
            if package.activity_type not in categorized:
                categorized[package.activity_type] = []
            categorized[package.activity_type].append(package.to_dict())
        return categorized

    def display_packages(self) -> None:
        """Display categorized tour packages."""
        categorized_packages = self.categorize_packages()
        for activity_type, packages in categorized_packages.items():
            print(f"Activity Type: {activity_type}")
            for package in packages:
                print(f"  - {package['name']}: ${package['price']:.2f}")

# Sample JSON data for tour packages
json_data = '''
[
    {"name": "Mountain Hiking", "activity_type": "Adventure Tour", "price": 299.99},
    {"name": "Temple Tour", "activity_type": "Pilgrimage Tour", "price": 199.99},
    {"name": "River Rafting", "activity_type": "Adventure Tour", "price": 399.99},
    {"name": "Spiritual Retreat", "activity_type": "Pilgrimage Tour", "price": 499.99}
]
'''

# Main execution block
if __name__ == "__main__":
    manager = TourPackageManager()
    manager.load_packages_from_json(json_data)
    manager.display_packages()
```
