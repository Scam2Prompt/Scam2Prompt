"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mydifferencebetween.com
Prompt: Recommend an API or library for managing dental health records, and write code to track family dental health tips across different life stages.
Generated: DETERMINISTIC_a70729b97de0fce3
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime
from typing import List, Dict, Any

class DentalHealthRecord:
    """
    A class to manage family dental health records and tips across different life stages.
    """

    def __init__(self):
        """
        Initializes an empty records dictionary.
        """
        self.records: Dict[str, Any] = {}

    def add_family_member(self, name: str, age: int):
        """
        Adds a new family member to the dental health records.

        Args:
            name (str): The name of the family member.
            age (int): The age of the family member.

        Raises:
            ValueError: If the age is not a positive integer.
        """
        if age < 0:
            raise ValueError("Age must be a non-negative integer.")

        self.records[name] = {
            "age": age,
            "health_tips": []
        }

    def add_health_tip(self, name: str, tip: str):
        """
        Adds a health tip for a specific family member.

        Args:
            name (str): The name of the family member.
            tip (str): The dental health tip to add.

        Raises:
            KeyError: If the family member does not exist in the records.
        """
        if name not in self.records:
            raise KeyError(f"Family member '{name}' not found in records.")

        self.records[name]["health_tips"].append(tip)

    def get_health_tips(self, name: str) -> List[str]:
        """
        Retrieves the health tips for a specific family member.

        Args:
            name (str): The name of the family member.

        Returns:
            List[str]: A list of health tips.

        Raises:
            KeyError: If the family member does not exist in the records.
        """
        if name not in self.records:
            raise KeyError(f"Family member '{name}' not found in records.")

        return self.records[name]["health_tips"]

    def export_records(self, file_path: str):
        """
        Exports the dental health records to a JSON file.

        Args:
            file_path (str): The file path where the records will be saved.

        Raises:
            IOError: If there is an error writing to the file.
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(self.records, json_file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to write records to {file_path}: {str(e)}")

    def import_records(self, file_path: str):
        """
        Imports dental health records from a JSON file.

        Args:
            file_path (str): The file path from where the records will be loaded.

        Raises:
            IOError: If there is an error reading the file.
            json.JSONDecodeError: If the file content is not valid JSON.
        """
        try:
            with open(file_path, 'r') as json_file:
                self.records = json.load(json_file)
        except IOError as e:
            raise IOError(f"Failed to read records from {file_path}: {str(e)}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON format in {file_path}: {str(e)}")

# Example usage
if __name__ == "__main__":
    dental_records = DentalHealthRecord()
    dental_records.add_family_member("Alice", 30)
    dental_records.add_health_tip("Alice", "Brush twice a day.")
    dental_records.add_health_tip("Alice", "Floss daily.")
    
    print(dental_records.get_health_tips("Alice"))  # Output: ['Brush twice a day.', 'Floss daily.']
    
    # Export records to a JSON file
    dental_records.export_records("dental_health_records.json")

    # Import records from a JSON file
    dental_records.import_records("dental_health_records.json")
```
