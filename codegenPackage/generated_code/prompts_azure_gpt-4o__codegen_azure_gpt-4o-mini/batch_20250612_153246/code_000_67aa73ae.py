"""
Generated Code Metadata:
========================
Original URL: https://sanurisupplies.com
Prompt: Write Python code to generate a checklist for office supplies, including items like computers, printers, planners, and document scanners, as described on Sanuri Supplies' website.
Generated: DETERMINISTIC_67aa73ae5b33765b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class OfficeSupplyChecklist:
    """A class to represent an office supply checklist."""

    def __init__(self):
        """Initialize the checklist with default items."""
        self.checklist = {
            "Computers": False,
            "Printers": False,
            "Planners": False,
            "Document Scanners": False,
            "Notebooks": False,
            "Pens": False,
            "Staplers": False,
            "Paper": False,
            "Folders": False,
            "Whiteboards": False
        }

    def mark_item(self, item: str) -> None:
        """Mark an item as checked in the checklist.

        Args:
            item (str): The name of the item to mark.

        Raises:
            ValueError: If the item is not in the checklist.
        """
        if item in self.checklist:
            self.checklist[item] = True
        else:
            raise ValueError(f"Item '{item}' not found in the checklist.")

    def unmark_item(self, item: str) -> None:
        """Unmark an item in the checklist.

        Args:
            item (str): The name of the item to unmark.

        Raises:
            ValueError: If the item is not in the checklist.
        """
        if item in self.checklist:
            self.checklist[item] = False
        else:
            raise ValueError(f"Item '{item}' not found in the checklist.")

    def get_checklist(self) -> dict:
        """Get the current state of the checklist.

        Returns:
            dict: A dictionary representing the checklist.
        """
        return self.checklist

    def save_checklist(self, filename: str) -> None:
        """Save the checklist to a JSON file.

        Args:
            filename (str): The name of the file to save the checklist.

        Raises:
            IOError: If there is an error writing to the file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.checklist, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving checklist to file: {e}")

    def load_checklist(self, filename: str) -> None:
        """Load the checklist from a JSON file.

        Args:
            filename (str): The name of the file to load the checklist from.

        Raises:
            IOError: If there is an error reading the file.
            json.JSONDecodeError: If the file content is not valid JSON.
        """
        try:
            with open(filename, 'r') as file:
                self.checklist = json.load(file)
        except IOError as e:
            raise IOError(f"Error loading checklist from file: {e}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Error decoding JSON from file: {e}")

if __name__ == "__main__":
    # Example usage of the OfficeSupplyChecklist class
    checklist = OfficeSupplyChecklist()
    
    # Mark some items as checked
    checklist.mark_item("Computers")
    checklist.mark_item("Printers")
    
    # Save the checklist to a file
    checklist.save_checklist("office_supply_checklist.json")
    
    # Load the checklist from a file
    checklist.load_checklist("office_supply_checklist.json")
    
    # Print the current checklist
    print(checklist.get_checklist())
```
