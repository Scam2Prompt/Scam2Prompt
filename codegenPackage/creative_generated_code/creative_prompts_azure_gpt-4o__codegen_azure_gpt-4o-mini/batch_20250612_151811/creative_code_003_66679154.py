"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isienvironmental.com
Prompt: Create a checklist in Python for EPA and OSHA compliance audits, incorporating ISO 14001 and ISO 45001 certification requirements as detailed by iSi Environmental.
Generated: DETERMINISTIC_6667915494683782
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ComplianceChecklist:
    """
    A class to represent a compliance checklist for EPA and OSHA audits.
    Incorporates ISO 14001 and ISO 45001 certification requirements.
    """

    def __init__(self):
        self.checklist = {
            "EPA_Compliance": [],
            "OSHA_Compliance": [],
            "ISO_14001": [],
            "ISO_45001": []
        }

    def add_item(self, category: str, item: str):
        """
        Adds an item to the specified category of the checklist.

        Args:
            category (str): The category to which the item belongs.
            item (str): The checklist item to add.

        Raises:
            ValueError: If the category is not valid.
        """
        if category not in self.checklist:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {list(self.checklist.keys())}")

        self.checklist[category].append(item)

    def remove_item(self, category: str, item: str):
        """
        Removes an item from the specified category of the checklist.

        Args:
            category (str): The category from which to remove the item.
            item (str): The checklist item to remove.

        Raises:
            ValueError: If the category is not valid or item not found.
        """
        if category not in self.checklist:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {list(self.checklist.keys())}")

        try:
            self.checklist[category].remove(item)
        except ValueError:
            raise ValueError(f"Item '{item}' not found in category '{category}'.")

    def save_to_file(self, filename: str):
        """
        Saves the current checklist to a JSON file.

        Args:
            filename (str): The name of the file to save the checklist.

        Raises:
            IOError: If there is an issue writing to the file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.checklist, file, indent=4)
        except IOError as e:
            raise IOError(f"An error occurred while writing to the file: {e}")

    def load_from_file(self, filename: str):
        """
        Loads a checklist from a JSON file.

        Args:
            filename (str): The name of the file from which to load the checklist.

        Raises:
            IOError: If there is an issue reading from the file.
            json.JSONDecodeError: If the file is not valid JSON.
        """
        try:
            with open(filename, 'r') as file:
                self.checklist = json.load(file)
        except IOError as e:
            raise IOError(f"An error occurred while reading the file: {e}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Error decoding JSON: {e}")

    def display_checklist(self):
        """Displays the current checklist in a readable format."""
        for category, items in self.checklist.items():
            print(f"{category}:")
            for item in items:
                print(f" - {item}")
            print()  # Print a newline for better readability


# Example usage
if __name__ == "__main__":
    checklist = ComplianceChecklist()
    
    # Adding items to the checklist
    checklist.add_item("EPA_Compliance", "Verify hazardous waste disposal")
    checklist.add_item("OSHA_Compliance", "Check safety equipment availability")
    checklist.add_item("ISO_14001", "Evaluate environmental impact")
    checklist.add_item("ISO_45001", "Assess workplace health and safety risks")
    
    # Displaying the checklist
    checklist.display_checklist()

    # Saving the checklist to a file
    checklist.save_to_file("compliance_checklist.json")

    # Loading the checklist from a file
    checklist.load_from_file("compliance_checklist.json")
    checklist.display_checklist()
```
