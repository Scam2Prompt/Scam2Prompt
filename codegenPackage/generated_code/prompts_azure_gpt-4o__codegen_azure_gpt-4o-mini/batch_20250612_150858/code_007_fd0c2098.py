"""
Generated Code Metadata:
========================
Original URL: https://vansoltravel.com
Prompt: Write a program to extract and categorize Vansol Travel's tour packages by activity type, such as adventure tours or pilgrimage tours.
Generated: DETERMINISTIC_fd0c20986427203c
Batch ID: 20250612_150858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class TourPackage:
    """Class to represent a tour package."""
    
    def __init__(self, name: str, activity_type: str, price: float):
        self.name = name
        self.activity_type = activity_type
        self.price = price

    def to_dict(self) -> Dict[str, Any]:
        """Convert the TourPackage instance to a dictionary."""
        return {
            "name": self.name,
            "activity_type": self.activity_type,
            "price": self.price
        }

class TourCategorizer:
    """Class to categorize tour packages by activity type."""
    
    def __init__(self):
        self.packages: List[TourPackage] = []

    def add_package(self, package: TourPackage):
        """Add a tour package to the list."""
        self.packages.append(package)

    def categorize_packages(self) -> Dict[str, List[Dict[str, Any]]]:
        """Categorize tour packages by activity type."""
        categorized = {}
        for package in self.packages:
            if package.activity_type not in categorized:
                categorized[package.activity_type] = []
            categorized[package.activity_type].append(package.to_dict())
        return categorized

    def load_packages_from_json(self, json_data: str):
        """Load tour packages from a JSON string."""
        try:
            data = json.loads(json_data)
            for item in data:
                package = TourPackage(
                    name=item['name'],
                    activity_type=item['activity_type'],
                    price=item['price']
                )
                self.add_package(package)
        except (json.JSONDecodeError, KeyError, TypeError) as e:
            print(f"Error loading packages: {e}")

    def save_categorized_packages_to_json(self, categorized_packages: Dict[str, List[Dict[str, Any]]], file_path: str):
        """Save categorized packages to a JSON file."""
        try:
            with open(file_path, 'w') as json_file:
                json.dump(categorized_packages, json_file, indent=4)
        except IOError as e:
            print(f"Error saving categorized packages to file: {e}")

def main():
    """Main function to execute the program."""
    # Sample JSON data representing tour packages
    json_data = '''
    [
        {"name": "Mountain Adventure", "activity_type": "Adventure", "price": 299.99},
        {"name": "Spiritual Journey", "activity_type": "Pilgrimage", "price": 199.99},
        {"name": "Desert Safari", "activity_type": "Adventure", "price": 399.99},
        {"name": "Temple Tour", "activity_type": "Pilgrimage", "price": 149.99}
    ]
    '''

    # Create an instance of TourCategorizer
    categorizer = TourCategorizer()
    
    # Load packages from JSON data
    categorizer.load_packages_from_json(json_data)
    
    # Categorize the packages
    categorized_packages = categorizer.categorize_packages()
    
    # Save categorized packages to a JSON file
    categorizer.save_categorized_packages_to_json(categorized_packages, 'categorized_tour_packages.json')

if __name__ == "__main__":
    main()
```
