"""
Generated Code Metadata:
========================
Original URL: https://starplumbingelectrical.com
Prompt: "Generate a code snippet for a simple plumbing inspection and maintenance checklist, inspired by the services provided by Certified Plumbers Graham, TX."
Generated: DETERMINISTIC_882a2ced2dfe28f9
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PlumbingInspectionChecklist:
    """
    A class to represent a plumbing inspection and maintenance checklist.
    """

    def __init__(self):
        """
        Initializes the checklist with default items.
        """
        self.checklist_items = [
            "Inspect all visible pipes for leaks",
            "Check water pressure",
            "Examine faucets for drips",
            "Test toilets for proper flushing",
            "Inspect water heater for corrosion",
            "Check drainage systems for clogs",
            "Examine sump pump operation",
            "Inspect for signs of mold or mildew",
            "Verify proper venting of plumbing fixtures",
            "Check for proper insulation on pipes"
        ]
        self.completed_items = []

    def display_checklist(self):
        """
        Displays the current checklist items.
        """
        print("Plumbing Inspection and Maintenance Checklist:")
        for index, item in enumerate(self.checklist_items, start=1):
            status = "✓" if item in self.completed_items else "✗"
            print(f"{index}. [{status}] {item}")

    def mark_item_completed(self, item_number):
        """
        Marks a checklist item as completed.

        Args:
            item_number (int): The number of the item to mark as completed.

        Raises:
            ValueError: If the item number is out of range.
        """
        if 1 <= item_number <= len(self.checklist_items):
            item = self.checklist_items[item_number - 1]
            if item not in self.completed_items:
                self.completed_items.append(item)
                print(f"Marked item {item_number} as completed.")
            else:
                print(f"Item {item_number} is already completed.")
        else:
            raise ValueError("Item number is out of range.")

    def reset_checklist(self):
        """
        Resets the checklist, marking all items as incomplete.
        """
        self.completed_items.clear()
        print("Checklist has been reset.")

def main():
    """
    Main function to run the plumbing inspection checklist.
    """
    checklist = PlumbingInspectionChecklist()
    
    while True:
        checklist.display_checklist()
        try:
            user_input = input("Enter the item number to mark as completed (or 'r' to reset, 'q' to quit): ").strip()
            if user_input.lower() == 'q':
                print("Exiting the checklist.")
                break
            elif user_input.lower() == 'r':
                checklist.reset_checklist()
            else:
                item_number = int(user_input)
                checklist.mark_item_completed(item_number)
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid item number or command.")

if __name__ == "__main__":
    main()
```
