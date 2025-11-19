"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marinendtbd.com
Prompt: Create a checklist for conducting NDT inspections on marine vessels, inspired by the quality service principles of Marine NDT & Engineering Works.
Generated: DETERMINISTIC_32b5da6f229cb91b
Batch ID: 20250612_162813
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

class NDTInspectionChecklist:
    """
    A class to represent a checklist for conducting Non-Destructive Testing (NDT) inspections on marine vessels.
    """

    def __init__(self):
        """
        Initializes the checklist with default inspection items and an empty list for completed items.
        """
        self.checklist_items = [
            "Visual Inspection",
            "Ultrasonic Testing (UT)",
            "Magnetic Particle Testing (MT)",
            "Radiographic Testing (RT)",
            "Liquid Penetrant Testing (PT)",
            "Thickness Measurement",
            "Documentation Review",
            "Safety Equipment Check"
        ]
        self.completed_items = []

    def mark_item_complete(self, item):
        """
        Marks a checklist item as complete.

        Parameters:
        item (str): The checklist item to mark as complete.

        Raises:
        ValueError: If the item is not in the checklist.
        """
        if item not in self.checklist_items:
            raise ValueError(f"Item '{item}' not found in checklist.")
        
        if item not in self.completed_items:
            self.completed_items.append(item)
        else:
            print(f"Item '{item}' is already marked as complete.")

    def get_checklist_status(self):
        """
        Returns a summary of the checklist status including completed and pending items.

        Returns:
        dict: A dictionary containing the status of checklist items.
        """
        return {
            "total_items": len(self.checklist_items),
            "completed_items": len(self.completed_items),
            "pending_items": len(self.checklist_items) - len(self.completed_items),
            "completed": self.completed_items,
            "pending": [item for item in self.checklist_items if item not in self.completed_items]
        }

    def export_checklist(self, filename):
        """
        Exports the current checklist status to a JSON file.

        Parameters:
        filename (str): The name of the file to export to.

        Raises:
        IOError: If there is an error writing to the file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_checklist_status(), file, indent=4)
            print(f"Checklist exported successfully to {filename}.")
        except IOError as e:
            print(f"Error writing to file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    inspection_checklist = NDTInspectionChecklist()

    # Marking some items as complete
    try:
        inspection_checklist.mark_item_complete("Visual Inspection")
        inspection_checklist.mark_item_complete("Ultrasonic Testing (UT)")
    except ValueError as e:
        print(e)

    # Get checklist status
    status = inspection_checklist.get_checklist_status()
    print("Checklist Status:", status)

    # Export the checklist to a file
    inspection_checklist.export_checklist(f"ndt_inspection_checklist_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
```
