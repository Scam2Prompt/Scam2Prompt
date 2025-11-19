"""
Generated Code Metadata:
========================
Original URL: https://lenderlibrary.ca
Prompt: "Create a documentation checklist for a mortgage application involving a chalet with 3-season usage in Canada."
Generated: DETERMINISTIC_2bfb23df2dbf75e3
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MortgageApplicationChecklist:
    """
    A class to represent a checklist for a mortgage application
    involving a chalet with 3-season usage in Canada.
    """

    def __init__(self):
        """
        Initializes the checklist with required documentation items.
        """
        self.checklist_items = [
            "Completed mortgage application form",
            "Proof of identity (e.g., driver's license, passport)",
            "Proof of income (e.g., pay stubs, tax returns)",
            "Credit report (to be obtained by lender)",
            "Property appraisal report",
            "Purchase agreement for the chalet",
            "Proof of down payment (e.g., bank statements)",
            "Insurance policy for the property",
            "Property tax statements",
            "Zoning compliance documents",
            "Environmental assessment (if applicable)",
            "Home inspection report",
            "Proof of 3-season usage (e.g., usage history, permits)",
            "Any existing mortgage statements (if applicable)",
            "Additional documentation as requested by the lender"
        ]

    def display_checklist(self):
        """
        Displays the mortgage application checklist.
        """
        print("Mortgage Application Checklist for Chalet (3-Season Usage):")
        for item in self.checklist_items:
            print(f"- {item}")

    def check_item(self, item):
        """
        Marks an item as checked in the checklist.

        Args:
            item (str): The item to check off.

        Raises:
            ValueError: If the item is not in the checklist.
        """
        if item in self.checklist_items:
            print(f"Item checked: {item}")
        else:
            raise ValueError(f"Item '{item}' not found in the checklist.")

    def add_item(self, item):
        """
        Adds a new item to the checklist.

        Args:
            item (str): The item to add.
        """
        if item not in self.checklist_items:
            self.checklist_items.append(item)
            print(f"Item added: {item}")
        else:
            print(f"Item '{item}' already exists in the checklist.")

    def remove_item(self, item):
        """
        Removes an item from the checklist.

        Args:
            item (str): The item to remove.

        Raises:
            ValueError: If the item is not in the checklist.
        """
        try:
            self.checklist_items.remove(item)
            print(f"Item removed: {item}")
        except ValueError:
            raise ValueError(f"Item '{item}' not found in the checklist.")

if __name__ == "__main__":
    # Create an instance of the checklist
    checklist = MortgageApplicationChecklist()
    
    # Display the initial checklist
    checklist.display_checklist()
    
    # Example usage of checking an item
    try:
        checklist.check_item("Proof of income (e.g., pay stubs, tax returns)")
    except ValueError as e:
        print(e)

    # Example of adding a new item
    checklist.add_item("Additional financial statements (if applicable)")

    # Example of removing an item
    try:
        checklist.remove_item("Proof of identity (e.g., driver's license, passport)")
    except ValueError as e:
        print(e)

    # Display the updated checklist
    checklist.display_checklist()
```
