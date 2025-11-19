"""
Generated Code Metadata:
========================
Original URL: https://eagle-tex.cn
Prompt: Write a program in Python to parse and organize fabric data from Shaoxing Eagles Textile Co., Ltd., grouping items like "French Terry," "Hacci," and "Two Face Waffle Cloth" into categories.
Generated: DETERMINISTIC_d5d98ca629857ee7
Batch ID: 20250612_154413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class FabricParser:
    """
    A class to parse and organize fabric data from Shaoxing Eagles Textile Co., Ltd.
    Groups items into categories based on predefined rules.
    """

    def __init__(self):
        """
        Initialize the FabricParser with predefined fabric categories.
        """
        self.categories = {
            "French Terry": [],
            "Hacci": [],
            "Two Face Waffle Cloth": [],
            "Other": []
        }

    def parse_fabric_data(self, fabric_data: List[Dict[str, str]]) -> Dict[str, List[Dict[str, str]]]:
        """
        Parse fabric data and organize items into categories.

        Args:
            fabric_data: A list of dictionaries containing fabric items with their attributes.

        Returns:
            A dictionary with fabric items grouped by categories.
        """
        if not isinstance(fabric_data, list):
            raise ValueError("Input fabric_data must be a list of dictionaries.")

        organized_data = {category: [] for category in self.categories}

        for item in fabric_data:
            if not isinstance(item, dict):
                raise ValueError("Each item in fabric_data must be a dictionary.")

            category = self._determine_category(item.get("name", ""))
            organized_data[category].append(item)

        return organized_data

    def _determine_category(self, fabric_name: str) -> str:
        """
        Determine the category of a fabric based on its name.

        Args:
            fabric_name: The name of the fabric.

        Returns:
            The category the fabric belongs to.
        """
        fabric_name = fabric_name.lower()

        if "french terry" in fabric_name:
            return "French Terry"
        elif "hacci" in fabric_name:
            return "Hacci"
        elif "two face waffle cloth" in fabric_name:
            return "Two Face Waffle Cloth"
        else:
            return "Other"

    def save_to_json(self, organized_data: Dict[str, List[Dict[str, str]]], file_path: str) -> None:
        """
        Save the organized fabric data to a JSON file.

        Args:
            organized_data: The organized fabric data.
            file_path: The path to the JSON file to save the data.
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(organized_data, json_file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save data to JSON file: {e}")

# Example usage
if __name__ == "__main__":
    # Sample fabric data (replace with actual data from Shaoxing Eagles Textile Co., Ltd.)
    sample_data = [
        {"name": "French Terry Cotton Blend", "code": "FT001", "weight": "200gsm"},
        {"name": "Hacci Sweater Fabric", "code": "HC001", "weight": "180gsm"},
        {"name": "Two Face Waffle Cloth", "code": "WF001", "weight": "250gsm"},
        {"name": "Polyester Twill", "code": "PT001", "weight": "150gsm"}
    ]

    try:
        parser = FabricParser()
        organized_data = parser.parse_fabric_data(sample_data)
        parser.save_to_json(organized_data, "organized_fabrics.json")
        print("Fabric data parsed and saved successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
