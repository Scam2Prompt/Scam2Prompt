"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.eu
Prompt: Write Python code to generate a list of FSC-certified materials for a cleaning product inventory system, referencing PDC Brush's focus on sustainability.
Generated: DETERMINISTIC_d3fdfe5bb7272f44
Batch ID: 20250612_150602
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.pdcbrush.com/materials": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import json
import requests
from typing import List, Dict

class MaterialInventory:
    """
    A class to represent a material inventory for cleaning products focused on FSC certification.
    """

    def __init__(self, api_url: str):
        """
        Initializes the MaterialInventory with the given API URL.

        Args:
            api_url (str): The URL of the API endpoint to fetch material data.
        """
        self.api_url = api_url
        self.materials = []

    def fetch_materials(self) -> None:
        """
        Fetches the materials from the designated API and populates the materials list.
        Raises exceptions for HTTP errors and JSON decoding errors.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses
            self.materials = response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
        except json.JSONDecodeError as json_err:
            print(f"JSON decoding error: {json_err}")

    def filter_fsc_certified(self) -> List[Dict]:
        """
        Filters the materials to return only those that are FSC certified.

        Returns:
            List[Dict]: A list of dictionaries containing FSC certified materials.
        """
        if not self.materials:
            print("No materials available to filter.")
            return []

        fsc_certified_materials = [
            material for material in self.materials if material.get('fsc_certified', False)
        ]
        return fsc_certified_materials

    def display_materials(self, materials: List[Dict]) -> None:
        """
        Displays the materials in a readable format.

        Args:
            materials (List[Dict]): The list of materials to display.
        """
        if not materials:
            print("No FSC certified materials found.")
            return
        
        print("FSC Certified Materials:")
        for material in materials:
            print(f"- {material.get('name')} (ID: {material.get('id')})")

def main():
    """
    The main function to run the material inventory process.
    """
    # URL for the materials API (replace with the actual URL)
    api_url = "https://api.pdcbrush.com/materials"
    
    inventory = MaterialInventory(api_url)
    inventory.fetch_materials()
    fsc_materials = inventory.filter_fsc_certified()
    inventory.display_materials(fsc_materials)

if __name__ == "__main__":
    main()
```
