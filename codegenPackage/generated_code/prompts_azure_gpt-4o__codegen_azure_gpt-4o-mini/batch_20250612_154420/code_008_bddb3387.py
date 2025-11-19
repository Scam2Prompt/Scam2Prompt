"""
Generated Code Metadata:
========================
Original URL: https://sistemabox.com.br
Prompt: Create a checklist for setting up IT infrastructure for small businesses, including ERP systems, professional WiFi, and Ethernet networks, as offered by Sistemabox.
Generated: DETERMINISTIC_bddb3387c1f64179
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ITInfrastructureChecklist:
    """
    A class to represent a checklist for setting up IT infrastructure for small businesses.
    This includes ERP systems, professional WiFi, and Ethernet networks.
    """

    def __init__(self):
        """
        Initializes the checklist with default items.
        """
        self.checklist_items = {
            "ERP System": False,
            "Professional WiFi": False,
            "Ethernet Network": False,
            "Firewall Setup": False,
            "Data Backup Solutions": False,
            "User Access Control": False,
            "Network Security Protocols": False,
            "Hardware Inventory": False,
            "Software Licensing": False,
            "IT Support Plan": False
        }

    def mark_item_complete(self, item):
        """
        Marks a checklist item as complete.

        Args:
            item (str): The name of the checklist item to mark as complete.

        Raises:
            ValueError: If the item is not found in the checklist.
        """
        if item in self.checklist_items:
            self.checklist_items[item] = True
        else:
            raise ValueError(f"Item '{item}' not found in the checklist.")

    def get_checklist(self):
        """
        Returns the current state of the checklist.

        Returns:
            dict: A dictionary representing the checklist items and their completion status.
        """
        return self.checklist_items

    def display_checklist(self):
        """
        Displays the checklist in a user-friendly format.
        """
        print("IT Infrastructure Setup Checklist:")
        for item, completed in self.checklist_items.items():
            status = "✔️" if completed else "❌"
            print(f"{status} {item}")

    def reset_checklist(self):
        """
        Resets the checklist to its initial state.
        """
        for item in self.checklist_items:
            self.checklist_items[item] = False

# Example usage
if __name__ == "__main__":
    try:
        checklist = ITInfrastructureChecklist()
        checklist.display_checklist()

        # Mark some items as complete
        checklist.mark_item_complete("ERP System")
        checklist.mark_item_complete("Professional WiFi")

        # Display updated checklist
        checklist.display_checklist()

    except ValueError as e:
        print(f"Error: {e}")
```
