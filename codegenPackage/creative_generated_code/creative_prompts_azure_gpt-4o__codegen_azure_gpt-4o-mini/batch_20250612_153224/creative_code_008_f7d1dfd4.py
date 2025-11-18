"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geeks-on-repair.com
Prompt: Write a program to track repair service areas and locations, referencing the multiple office locations listed by Geeks On Repair.
Generated: DETERMINISTIC_f7d1dfd43ced64fd
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RepairServiceTracker:
    def __init__(self):
        """Initialize the service tracker with an empty list of locations."""
        self.locations: List[Dict[str, Any]] = []

    def load_locations(self, file_path: str) -> None:
        """
        Load office locations from a JSON file.

        Args:
            file_path (str): The path to the JSON file containing location data.

        Raises:
            FileNotFoundError: If the specified file does not exist.
            json.JSONDecodeError: If the file content is not valid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                self.locations = json.load(file)
                logging.info(f"Loaded {len(self.locations)} locations from {file_path}")
        except FileNotFoundError:
            logging.error(f"File not found: {file_path}")
            raise
        except json.JSONDecodeError:
            logging.error(f"Invalid JSON format in file: {file_path}")
            raise

    def get_service_areas(self) -> List[str]:
        """
        Retrieve a list of unique service areas.

        Returns:
            List[str]: A list of unique service areas.
        """
        service_areas = {location['service_area'] for location in self.locations}
        return list(service_areas)

    def add_location(self, location: Dict[str, Any]) -> None:
        """
        Add a new location to the tracker.

        Args:
            location (Dict[str, Any]): A dictionary representing the location.

        Raises:
            ValueError: If the location does not contain required fields.
        """
        if 'name' not in location or 'service_area' not in location:
            raise ValueError("Location must contain 'name' and 'service_area' fields")
        self.locations.append(location)
        logging.info(f"Added new location: {location['name']} in service area: {location['service_area']}")

    def save_locations(self, file_path: str) -> None:
        """
        Save the current list of locations to a JSON file.

        Args:
            file_path (str): The path to the JSON file where locations will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.locations, file, indent=4)
                logging.info(f"Saved {len(self.locations)} locations to {file_path}")
        except IOError as e:
            logging.error(f"Error saving file: {file_path}, {e}")
            raise

if __name__ == "__main__":
    tracker = RepairServiceTracker()
    
    # Example usage:
    try:
        # Load locations from a file
        tracker.load_locations('office_locations.json')
        
        # Print unique service areas
        service_areas = tracker.get_service_areas()
        print("Unique Service Areas:", service_areas)

        # Add a new location
        new_location = {
            "name": "New Office",
            "service_area": "Downtown"
        }
        tracker.add_location(new_location)
        
        # Save updated locations to a file
        tracker.save_locations('updated_office_locations.json')
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```

Make sure to create a `office_locations.json` file with valid JSON data before running this code. The expected format for the JSON file may look like this:

```json
[
    {
        "name": "Office 1",
        "service_area": "Area 1"
    },
    {
        "name": "Office 2",
        "service_area": "Area 2"
    }
]
```
