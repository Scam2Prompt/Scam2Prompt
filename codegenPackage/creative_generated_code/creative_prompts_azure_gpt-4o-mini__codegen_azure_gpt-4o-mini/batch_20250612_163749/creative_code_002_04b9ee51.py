"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecpowerlightingltd.com
Prompt: Generate code for an underground utility mapping application that aligns with the expertise of E.C. Power & Lighting Ltd. in electrical installations.
Generated: DETERMINISTIC_04b9ee51f3ee970f
Batch ID: 20250612_163749
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
from typing import List, Dict, Any, Optional

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UtilityMapping:
    """
    A class to represent an underground utility mapping application.
    """

    def __init__(self):
        self.utilities: List[Dict[str, Any]] = []

    def add_utility(self, utility_name: str, depth: float, coordinates: Dict[str, float]) -> None:
        """
        Adds a utility to the mapping system.

        :param utility_name: Name of the utility (e.g., electricity, water, gas).
        :param depth: Depth of the utility in meters.
        :param coordinates: A dictionary with 'latitude' and 'longitude' as keys.
        """
        if depth < 0:
            logging.error("Depth cannot be negative.")
            raise ValueError("Depth cannot be negative.")
        
        if 'latitude' not in coordinates or 'longitude' not in coordinates:
            logging.error("Coordinates must contain 'latitude' and 'longitude'.")
            raise ValueError("Coordinates must contain 'latitude' and 'longitude'.")

        utility = {
            "name": utility_name,
            "depth": depth,
            "coordinates": coordinates
        }
        self.utilities.append(utility)
        logging.info(f"Added utility: {utility}")

    def remove_utility(self, utility_name: str) -> bool:
        """
        Removes a utility from the mapping system.

        :param utility_name: Name of the utility to remove.
        :return: True if the utility was removed, False otherwise.
        """
        for utility in self.utilities:
            if utility["name"] == utility_name:
                self.utilities.remove(utility)
                logging.info(f"Removed utility: {utility_name}")
                return True
        logging.warning(f"Utility '{utility_name}' not found.")
        return False

    def get_utilities(self) -> List[Dict[str, Any]]:
        """
        Retrieves all utilities.

        :return: A list of all utilities in the mapping system.
        """
        return self.utilities

    def save_to_file(self, file_path: str) -> None:
        """
        Saves the utility mapping data to a JSON file.

        :param file_path: Path to the file where data is to be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.utilities, file, indent=4)
                logging.info(f"Utilities saved to {file_path}")
        except IOError as e:
            logging.error(f"Failed to write to file {file_path}: {e}")
            raise

    def load_from_file(self, file_path: str) -> None:
        """
        Loads utility mapping data from a JSON file.

        :param file_path: Path to the file from which data is to be loaded.
        """
        try:
            with open(file_path, 'r') as file:
                self.utilities = json.load(file)
                logging.info(f"Utilities loaded from {file_path}")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Failed to read from file {file_path}: {e}")
            raise

# Example usage
if __name__ == "__main__":
    mapping_app = UtilityMapping()
    
    try:
        mapping_app.add_utility("Electric Line", 1.5, {"latitude": 34.0522, "longitude": -118.2437})
        mapping_app.add_utility("Water Pipe", 1.2, {"latitude": 34.0522, "longitude": -118.2438})
        mapping_app.save_to_file("utilities_mapping.json")
        
        # Load utilities from file
        mapping_app.load_from_file("utilities_mapping.json")
        all_utilities = mapping_app.get_utilities()
        print(all_utilities)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
