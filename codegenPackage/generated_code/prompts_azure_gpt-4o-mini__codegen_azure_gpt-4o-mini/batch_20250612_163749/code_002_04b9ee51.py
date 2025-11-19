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
import logging
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UtilityMapping:
    def __init__(self):
        """Initialize the UtilityMapping class with an empty utility map."""
        self.utility_map: Dict[str, List[Dict[str, Any]]] = {}

    def add_utility(self, utility_type: str, location: Dict[str, float], details: Dict[str, Any]) -> None:
        """
        Add a utility to the mapping.

        Args:
            utility_type (str): The type of utility (e.g., 'electric', 'water').
            location (Dict[str, float]): The coordinates of the utility (latitude and longitude).
            details (Dict[str, Any]): Additional details about the utility.

        Raises:
            ValueError: If the utility_type is empty or location is invalid.
        """
        if not utility_type:
            logging.error("Utility type cannot be empty.")
            raise ValueError("Utility type cannot be empty.")
        
        if not isinstance(location, dict) or 'latitude' not in location or 'longitude' not in location:
            logging.error("Invalid location provided. Must contain 'latitude' and 'longitude'.")
            raise ValueError("Invalid location provided. Must contain 'latitude' and 'longitude'.")

        utility_entry = {
            'location': location,
            'details': details
        }

        if utility_type not in self.utility_map:
            self.utility_map[utility_type] = []
        
        self.utility_map[utility_type].append(utility_entry)
        logging.info(f"Added utility: {utility_type} at {location}.")

    def get_utilities(self, utility_type: str) -> List[Dict[str, Any]]:
        """
        Retrieve utilities of a specific type.

        Args:
            utility_type (str): The type of utility to retrieve.

        Returns:
            List[Dict[str, Any]]: A list of utilities of the specified type.

        Raises:
            ValueError: If the utility_type is empty.
        """
        if not utility_type:
            logging.error("Utility type cannot be empty.")
            raise ValueError("Utility type cannot be empty.")

        utilities = self.utility_map.get(utility_type, [])
        logging.info(f"Retrieved {len(utilities)} utilities of type: {utility_type}.")
        return utilities

    def export_to_json(self, file_path: str) -> None:
        """
        Export the utility map to a JSON file.

        Args:
            file_path (str): The path to the file where the data will be saved.

        Raises:
            IOError: If there is an error writing to the file.
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(self.utility_map, json_file, indent=4)
            logging.info(f"Utility map exported to {file_path}.")
        except IOError as e:
            logging.error(f"Failed to write to file {file_path}: {e}")
            raise IOError(f"Failed to write to file {file_path}: {e}")

# Example usage
if __name__ == "__main__":
    mapping_app = UtilityMapping()
    
    # Adding utilities
    try:
        mapping_app.add_utility('electric', {'latitude': 51.5074, 'longitude': -0.1278}, {'voltage': '230V', 'status': 'active'})
        mapping_app.add_utility('water', {'latitude': 51.5074, 'longitude': -0.1279}, {'pressure': '1.5 bar', 'status': 'active'})
        
        # Retrieving utilities
        electric_utilities = mapping_app.get_utilities('electric')
        water_utilities = mapping_app.get_utilities('water')
        
        # Exporting to JSON
        mapping_app.export_to_json('utility_map.json')
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
