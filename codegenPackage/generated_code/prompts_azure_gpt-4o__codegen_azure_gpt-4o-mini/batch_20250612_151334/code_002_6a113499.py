"""
Generated Code Metadata:
========================
Original URL: https://ecpowerlightingltd.com
Prompt: Generate code to design an underground utility mapping system, inspired by E.C. Power & Lighting Ltd.'s specialization in underground utilities.
Generated: DETERMINISTIC_6a1134998bad3a08
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UtilityMappingSystem:
    def __init__(self):
        """Initialize the utility mapping system with an empty map."""
        self.utility_map: Dict[str, List[Dict[str, Any]]] = {}

    def add_utility(self, utility_type: str, location: Dict[str, float], details: Dict[str, Any]) -> None:
        """
        Add a utility to the mapping system.

        :param utility_type: Type of the utility (e.g., 'water', 'electricity', 'gas').
        :param location: A dictionary containing 'latitude' and 'longitude'.
        :param details: Additional details about the utility (e.g., 'depth', 'material').
        """
        if utility_type not in self.utility_map:
            self.utility_map[utility_type] = []
        
        utility_entry = {
            'location': location,
            'details': details
        }
        self.utility_map[utility_type].append(utility_entry)
        logging.info(f"Added utility: {utility_type} at {location} with details {details}")

    def remove_utility(self, utility_type: str, location: Dict[str, float]) -> bool:
        """
        Remove a utility from the mapping system.

        :param utility_type: Type of the utility to remove.
        :param location: The location of the utility to remove.
        :return: True if the utility was removed, False otherwise.
        """
        if utility_type in self.utility_map:
            for entry in self.utility_map[utility_type]:
                if entry['location'] == location:
                    self.utility_map[utility_type].remove(entry)
                    logging.info(f"Removed utility: {utility_type} at {location}")
                    return True
        logging.warning(f"Utility not found: {utility_type} at {location}")
        return False

    def get_utilities(self, utility_type: str) -> List[Dict[str, Any]]:
        """
        Retrieve all utilities of a specific type.

        :param utility_type: Type of the utility to retrieve.
        :return: A list of utilities of the specified type.
        """
        return self.utility_map.get(utility_type, [])

    def export_map(self, file_path: str) -> None:
        """
        Export the utility map to a JSON file.

        :param file_path: The path to the file where the map will be saved.
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(self.utility_map, json_file, indent=4)
            logging.info(f"Utility map exported to {file_path}")
        except IOError as e:
            logging.error(f"Failed to export utility map: {e}")

    def import_map(self, file_path: str) -> None:
        """
        Import a utility map from a JSON file.

        :param file_path: The path to the file from which the map will be loaded.
        """
        try:
            with open(file_path, 'r') as json_file:
                self.utility_map = json.load(json_file)
            logging.info(f"Utility map imported from {file_path}")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Failed to import utility map: {e}")

# Example usage
if __name__ == "__main__":
    system = UtilityMappingSystem()
    system.add_utility('water', {'latitude': 51.5074, 'longitude': -0.1278}, {'depth': 1.5, 'material': 'PVC'})
    system.add_utility('electricity', {'latitude': 51.5074, 'longitude': -0.1279}, {'depth': 0.8, 'material': 'Copper'})
    system.export_map('utility_map.json')
    system.import_map('utility_map.json')
    print(system.get_utilities('water'))
```
