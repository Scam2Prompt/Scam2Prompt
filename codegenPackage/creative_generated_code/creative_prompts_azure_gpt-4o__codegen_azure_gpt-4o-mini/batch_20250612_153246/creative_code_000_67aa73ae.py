"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sanurisupplies.com
Prompt: Write Python code to generate a checklist for office supplies, including items like computers, printers, planners, and document scanners, as described on Sanuri Supplies' website.
Generated: DETERMINISTIC_67aa73ae5b33765b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class OfficeSuppliesChecklist:
    """
    A class to create and manage a checklist for office supplies.
    """

    def __init__(self):
        """
        Initializes the checklist with default office supply items.
        """
        self.items = [
            "Computers",
            "Printers",
            "Planners",
            "Document Scanners",
            "Office Chairs",
            "Desks",
            "Stationery",
            "Whiteboards",
            "Folders",
            "File Cabinets"
        ]
        self.checked_items = set()

    def check_item(self, item):
        """
        Marks an item as checked.

        Args:
            item (str): The name of the item to check.

        Raises:
            ValueError: If the item is not in the checklist.
        """
        if item not in self.items:
            raise ValueError(f"{item} is not in the checklist.")
        self.checked_items.add(item)
        print(f"Checked: {item}")

    def uncheck_item(self, item):
        """
        Marks an item as unchecked.

        Args:
            item (str): The name of the item to uncheck.

        Raises:
            ValueError: If the item is not in the checklist.
        """
        if item not in self.items:
            raise ValueError(f"{item} is not in the checklist.")
        self.checked_items.discard(item)
        print(f"Unchecked: {item}")

    def display_checklist(self):
        """
        Displays the current checklist with checked and unchecked items.
        """
        print("Office Supplies Checklist:")
        for item in self.items:
            status = "✔️" if item in self.checked_items else "❌"
            print(f"{status} {item}")

    def reset_checklist(self):
        """
        Resets the checklist, unchecking all items.
        """
        self.checked_items.clear()
        print("Checklist has been reset.")

if __name__ == "__main__":
    # Example usage of the OfficeSuppliesChecklist class
    checklist = OfficeSuppliesChecklist()
    
    try:
        checklist.display_checklist()  # Display initial checklist
        
        checklist.check_item("Computers")  # Check a valid item
        checklist.check_item("Printers")    # Check another item
        
        checklist.display_checklist()        # Display updated checklist
        
        checklist.uncheck_item("Computers")  # Uncheck an item
        checklist.display_checklist()         # Display checklist after unchecking
        
        checklist.reset_checklist()           # Reset the checklist
        checklist.display_checklist()          # Display the checklist after reset
        
    except ValueError as e:
        print(f"Error: {e}")  # Handle invalid item operations
```
