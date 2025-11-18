"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kigaliinstitute.rw
Prompt: Write a script for managing scholarships and financial aid programs for an online brokerage education platform, inspired by Kigali Institute's scholarship initiatives.
Generated: DETERMINISTIC_12ece3f94fe24da8
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class ScholarshipManager:
    def __init__(self, data_file: str):
        """
        Initializes the ScholarshipManager with a given data file.
        
        :param data_file: Path to the JSON file containing scholarship data.
        """
        self.data_file = data_file
        self.scholarships = self.load_scholarships()

    def load_scholarships(self) -> List[Dict[str, Any]]:
        """
        Loads scholarship data from the JSON file.
        
        :return: A list of scholarships.
        """
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
            return []
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON from the file.")
            return []

    def save_scholarships(self):
        """
        Saves the current scholarships to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.scholarships, file, indent=4)
        except IOError as e:
            print(f"Error saving scholarships to file: {e}")

    def add_scholarship(self, scholarship: Dict[str, Any]):
        """
        Adds a new scholarship to the list and saves it to the file.
        
        :param scholarship: A dictionary containing scholarship details.
        """
        self.scholarships.append(scholarship)
        self.save_scholarships()

    def find_scholarships(self, criteria: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Finds scholarships that match the given criteria.
        
        :param criteria: A dictionary of criteria to filter scholarships.
        :return: A list of scholarships that match the criteria.
        """
        matched_scholarships = []
        for scholarship in self.scholarships:
            if all(scholarship.get(key) == value for key, value in criteria.items()):
                matched_scholarships.append(scholarship)
        return matched_scholarships

    def __str__(self):
        """
        Returns a string representation of all scholarships.
        
        :return: A string listing all scholarships.
        """
        return json.dumps(self.scholarships, indent=4)

# Example usage
if __name__ == "__main__":
    manager = ScholarshipManager('scholarships.json')
    
    # Adding a new scholarship
    new_scholarship = {
        "name": "Kigali Institute Scholarship",
        "amount": 1000,
        "eligibility": "Students enrolled in online brokerage programs",
        "deadline": "2024-06-30"
    }
    manager.add_scholarship(new_scholarship)

    # Finding scholarships based on eligibility
    criteria = {"eligibility": "Students enrolled in online brokerage programs"}
    available_scholarships = manager.find_scholarships(criteria)
    print("Available Scholarships:")
    print(json.dumps(available_scholarships, indent=4))
```
