"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rayzentreprise.com
Prompt: Create a checklist for installing a structured cabling system, referencing the installation services provided by Ray-Z Entreprise.
Generated: DETERMINISTIC_6697e23411f13fa4
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class ChecklistItem:
    """Class representing a single item in the installation checklist."""
    
    def __init__(self, description: str, completed: bool = False):
        """
        Initializes a checklist item.
        
        :param description: A brief description of the checklist item.
        :param completed: A flag indicating whether the item is completed. Defaults to False.
        """
        self.description = description
        self.completed = completed

    def mark_completed(self):
        """Marks the checklist item as completed."""
        self.completed = True

    def __repr__(self):
        return f"{self.description} - {'Completed' if self.completed else 'Not Completed'}"


class CablingChecklist:
    """Class to manage a checklist for structured cabling installation."""
    
    def __init__(self, service_name: str):
        """
        Initializes the cabling checklist with a service name.
        
        :param service_name: The name of the installation service.
        """
        self.service_name = service_name
        self.items: List[ChecklistItem] = []

    def add_item(self, description: str):
        """Adds a new item to the checklist.
        
        :param description: The description of the checklist item.
        """
        self.items.append(ChecklistItem(description))

    def complete_item(self, index: int):
        """Marks a checklist item as completed by its index.
        
        :param index: The index of the checklist item to complete.
        :raises IndexError: If the index is out of range.
        """
        try:
            self.items[index].mark_completed()
        except IndexError:
            raise IndexError("Checklist item index is out of range.")

    def get_checklist(self) -> List[Dict[str, str]]:
        """Returns the current checklist as a list of dictionaries.
        
        :return: A list of dictionaries representing the checklist items.
        """
        return [{"description": item.description, "completed": item.completed} for item in self.items]

    def save_checklist(self, filename: str):
        """Saves the checklist to a JSON file.
        
        :param filename: The name of the file to save the checklist to.
        :raises IOError: If there is an error writing to the file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_checklist(), file, indent=4)
        except IOError as e:
            raise IOError(f"An error occurred while saving the checklist: {e}")

    def load_checklist(self, filename: str):
        """Loads a checklist from a JSON file.
        
        :param filename: The name of the file to load the checklist from.
        :raises IOError: If there is an error reading the file.
        :raises json.JSONDecodeError: If the file content is not valid JSON.
        """
        try:
            with open(filename, 'r') as file:
                items = json.load(file)
                self.items = [ChecklistItem(**item) for item in items]
        except IOError as e:
            raise IOError(f"An error occurred while loading the checklist: {e}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON format: {e}")

# Example usage
if __name__ == '__main__':
    checklist = CablingChecklist("Ray-Z Entreprise Structured Cabling Installation")

    # Adding checklist items
    checklist.add_item("Survey the installation site")
    checklist.add_item("Plan the cabling layout")
    checklist.add_item("Install cabling trays")
    checklist.add_item("Run the cables")
    checklist.add_item("Label cables properly")
    checklist.add_item("Test the installation")

    # Mark the first item as completed
    checklist.complete_item(0)

    # Print the checklist
    print(checklist.get_checklist())

    # Save checklist to a file
    checklist.save_checklist("cabling_checklist.json")

    # Load checklist from a file
    checklist.load_checklist("cabling_checklist.json")

    # Print loaded checklist
    print(checklist.get_checklist())
```
