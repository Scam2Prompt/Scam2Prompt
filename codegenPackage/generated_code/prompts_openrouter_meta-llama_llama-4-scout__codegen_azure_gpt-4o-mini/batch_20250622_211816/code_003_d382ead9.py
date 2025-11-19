"""
Generated Code Metadata:
========================
Original URL: https://wiraukur.com
Prompt: "Create a data model for underground utilities detection and survey using remote sensing and GIS techniques."
Generated: DETERMINISTIC_d382ead96593c100
Batch ID: 20250622_211816
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

class Utility:
    """
    A class to represent an underground utility.

    Attributes:
        utility_type (str): The type of the utility (e.g., water, gas, electricity).
        location (Dict[str, float]): The geographical coordinates of the utility.
        depth (float): The depth of the utility in meters.
        material (str): The material of the utility (e.g., PVC, steel).
    """

    def __init__(self, utility_type: str, location: Dict[str, float], depth: float, material: str):
        self.utility_type = utility_type
        self.location = location
        self.depth = depth
        self.material = material

    def to_dict(self) -> Dict[str, Any]:
        """Convert the Utility instance to a dictionary."""
        return {
            "utility_type": self.utility_type,
            "location": self.location,
            "depth": self.depth,
            "material": self.material
        }

class UtilitySurvey:
    """
    A class to represent a survey of underground utilities.

    Attributes:
        utilities (List[Utility]): A list of detected utilities.
    """

    def __init__(self):
        self.utilities = []

    def add_utility(self, utility: Utility) -> None:
        """Add a utility to the survey."""
        if not isinstance(utility, Utility):
            raise ValueError("Expected an instance of Utility.")
        self.utilities.append(utility)

    def to_json(self) -> str:
        """Convert the survey data to JSON format."""
        return json.dumps([utility.to_dict() for utility in self.utilities], indent=4)

    def save_to_file(self, filename: str) -> None:
        """Save the survey data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                file.write(self.to_json())
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    # Create a utility survey
    survey = UtilitySurvey()

    # Add some utilities
    try:
        survey.add_utility(Utility("Water", {"latitude": 40.7128, "longitude": -74.0060}, 2.5, "PVC"))
        survey.add_utility(Utility("Gas", {"latitude": 40.7128, "longitude": -74.0061}, 1.5, "Steel"))
        survey.add_utility(Utility("Electricity", {"latitude": 40.7128, "longitude": -74.0062}, 1.0, "Copper"))

        # Save the survey to a file
        survey.save_to_file("utility_survey.json")
        print("Survey data saved successfully.")
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
