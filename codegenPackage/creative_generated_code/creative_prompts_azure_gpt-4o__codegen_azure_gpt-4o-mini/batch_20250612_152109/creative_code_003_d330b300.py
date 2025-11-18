"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mimsr.edu.in
Prompt: Create a function in Python to parse and categorize the infrastructure details of MIMSR, including hostel accommodations, sports facilities, and library resources.
Generated: DETERMINISTIC_d330b300f96d7b9d
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, Any, List

class InfrastructureParser:
    """
    A class to parse and categorize infrastructure details for MIMSR.
    """

    def __init__(self, data: str):
        """
        Initializes the InfrastructureParser with JSON data.

        :param data: A JSON string containing infrastructure details.
        """
        self.data = self._load_data(data)

    def _load_data(self, data: str) -> Dict[str, Any]:
        """
        Loads and parses JSON data.

        :param data: A JSON string.
        :return: Parsed JSON data as a dictionary.
        :raises ValueError: If JSON data is invalid.
        """
        try:
            return json.loads(data)
        except json.JSONDecodeError as e:
            raise ValueError("Invalid JSON data provided.") from e

    def categorize_infrastructure(self) -> Dict[str, List[str]]:
        """
        Categorizes infrastructure details into hostel accommodations,
        sports facilities, and library resources.

        :return: A dictionary categorizing infrastructure details.
        """
        categorized_data = {
            "hostels": [],
            "sports_facilities": [],
            "library_resources": []
        }

        for category, items in self.data.items():
            if category == "hostels":
                categorized_data["hostels"] = items
            elif category == "sports_facilities":
                categorized_data["sports_facilities"] = items
            elif category == "library_resources":
                categorized_data["library_resources"] = items
            else:
                raise ValueError(f"Unknown category found in data: {category}")

        return categorized_data

    def display_infrastructure(self) -> None:
        """
        Prints the categorized infrastructure details.

        :raises Exception: If an error occurs during display.
        """
        try:
            categorized = self.categorize_infrastructure()
            print("Infrastructure Details:")
            for category, items in categorized.items():
                print(f"\n{category.capitalize()}:")
                if items:
                    for item in items:
                        print(f" - {item}")
                else:
                    print(" - No items found.")
        except Exception as e:
            raise Exception("Error while displaying infrastructure details.") from e

# Example usage (this would be removed in a production environment)
if __name__ == "__main__":
    json_data = '''
    {
        "hostels": ["Hostel A", "Hostel B"],
        "sports_facilities": ["Football Field", "Tennis Court"],
        "library_resources": ["Central Library", "Digital Library"]
    }
    '''
    
    try:
        parser = InfrastructureParser(json_data)
        parser.display_infrastructure()
    except Exception as e:
        print(f"An error occurred: {e}")
```
