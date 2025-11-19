"""
Generated Code Metadata:
========================
Original URL: https://scout.kz
Prompt: Write code to generate a checklist for pre-purchase inspection of SCOUT tractors, incorporating features like synchronized transmissions, rearview cameras, and air-conditioned cabins, as highlighted on the SCOUT.kz website.
Generated: DETERMINISTIC_0aec4664fc7d0d61
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TractorInspectionChecklist:
    """
    A class to represent a checklist for pre-purchase inspection of SCOUT tractors.
    """

    def __init__(self):
        """
        Initializes the checklist with default inspection items.
        """
        self.checklist_items = [
            "Inspect synchronized transmission functionality",
            "Check rearview camera operation",
            "Verify air-conditioned cabin performance",
            "Examine overall tractor condition",
            "Review maintenance history",
            "Test drive for performance assessment",
            "Inspect tire condition and pressure",
            "Check fluid levels (oil, coolant, etc.)",
            "Ensure all safety features are operational",
            "Review warranty and service agreements"
        ]

    def display_checklist(self):
        """
        Displays the inspection checklist items.
        """
        print("SCOUT Tractor Pre-Purchase Inspection Checklist:")
        for index, item in enumerate(self.checklist_items, start=1):
            print(f"{index}. {item}")

    def mark_item_complete(self, item_number):
        """
        Marks an item as complete in the checklist.

        Args:
            item_number (int): The number of the item to mark as complete.

        Raises:
            ValueError: If the item number is out of range.
        """
        if 1 <= item_number <= len(self.checklist_items):
            completed_item = self.checklist_items[item_number - 1]
            print(f"Item completed: {completed_item}")
        else:
            raise ValueError("Item number is out of range. Please provide a valid number.")

    def add_custom_item(self, item):
        """
        Adds a custom item to the checklist.

        Args:
            item (str): The custom item to add.
        """
        if item:
            self.checklist_items.append(item)
            print(f"Custom item added: {item}")
        else:
            raise ValueError("Item cannot be empty.")

    def remove_item(self, item_number):
        """
        Removes an item from the checklist.

        Args:
            item_number (int): The number of the item to remove.

        Raises:
            ValueError: If the item number is out of range.
        """
        if 1 <= item_number <= len(self.checklist_items):
            removed_item = self.checklist_items.pop(item_number - 1)
            print(f"Item removed: {removed_item}")
        else:
            raise ValueError("Item number is out of range. Please provide a valid number.")

if __name__ == "__main__":
    try:
        checklist = TractorInspectionChecklist()
        checklist.display_checklist()

        # Example usage
        checklist.mark_item_complete(1)  # Mark the first item as complete
        checklist.add_custom_item("Check GPS functionality")  # Add a custom item
        checklist.remove_item(2)  # Remove the second item
        checklist.display_checklist()  # Display the updated checklist
    except ValueError as e:
        print(f"Error: {e}")
```
