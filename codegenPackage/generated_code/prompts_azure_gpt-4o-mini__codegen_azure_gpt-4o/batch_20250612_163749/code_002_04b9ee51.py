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
from typing import List, Dict, Union

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("utility_mapping.log"), logging.StreamHandler()],
)

class UndergroundUtilityMapping:
    """
    A class to represent an underground utility mapping application.
    This application is designed to map underground utilities such as electrical installations.
    """

    def __init__(self):
        """
        Initialize the mapping application with an empty dataset.
        """
        self.utility_data: List[Dict[str, Union[str, float]]] = []

    def add_utility(self, name: str, type: str, coordinates: Dict[str, float], depth: float) -> None:
        """
        Add a new utility to the mapping dataset.

        :param name: Name of the utility (e.g., "Main Power Line").
        :param type: Type of utility (e.g., "Electrical").
        :param coordinates: A dictionary containing latitude and longitude of the utility.
        :param depth: Depth of the utility underground in meters.
        """
        try:
            if not isinstance(name, str) or not isinstance(type, str):
                raise ValueError("Name and type must be strings.")
            if not isinstance(coordinates, dict) or "latitude" not in coordinates or "longitude" not in coordinates:
                raise ValueError("Coordinates must be a dictionary with 'latitude' and 'longitude' keys.")
            if not isinstance(depth, (int, float)) or depth < 0:
                raise ValueError("Depth must be a positive number.")

            utility = {
                "name": name,
                "type": type,
                "coordinates": coordinates,
                "depth": depth,
            }
            self.utility_data.append(utility)
            logging.info(f"Utility '{name}' added successfully.")
        except Exception as e:
            logging.error(f"Error adding utility: {e}")

    def get_utilities(self) -> List[Dict[str, Union[str, float]]]:
        """
        Retrieve the list of all mapped utilities.

        :return: A list of dictionaries representing the mapped utilities.
        """
        return self.utility_data

    def save_to_file(self, filename: str) -> None:
        """
        Save the utility mapping data to a JSON file.

        :param filename: Name of the file to save the data.
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.utility_data, file, indent=4)
            logging.info(f"Utility data saved to file '{filename}'.")
        except Exception as e:
            logging.error(f"Error saving utility data to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """
        Load utility mapping data from a JSON file.

        :param filename: Name of the file to load the data from.
        """
        try:
            with open(filename, "r") as file:
                self.utility_data = json.load(file)
            logging.info(f"Utility data loaded from file '{filename}'.")
        except FileNotFoundError:
            logging.error(f"File '{filename}' not found.")
        except json.JSONDecodeError:
            logging.error(f"Error decoding JSON from file '{filename}'.")
        except Exception as e:
            logging.error(f"Error loading utility data: {e}")


# Example usage
if __name__ == "__main__":
    # Create an instance of the mapping application
    mapping_app = UndergroundUtilityMapping()

    # Add some utilities
    mapping_app.add_utility(
        name="Main Power Line",
        type="Electrical",
        coordinates={"latitude": 51.5074, "longitude": -0.1278},
        depth=2.5,
    )
    mapping_app.add_utility(
        name="Backup Generator Line",
        type="Electrical",
        coordinates={"latitude": 51.5094, "longitude": -0.1188},
        depth=1.8,
    )

    # Save utilities to a file
    mapping_app.save_to_file("utilities.json")

    # Load utilities from a file
    mapping_app.load_from_file("utilities.json")

    # Print all utilities
    print(mapping_app.get_utilities())
```
