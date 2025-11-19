"""
Generated Code Metadata:
========================
Original URL: https://lexi-con.com
Prompt: Develop a relocation checklist for individuals moving to Las Vegas, using the resources and advice provided on AndySellsVegas.com.
Generated: DETERMINISTIC_a819d9f8d694862e
Batch ID: 20250622_211401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class RelocationChecklist:
    def __init__(self):
        """Initialize the relocation checklist with default items."""
        self.checklist = {
            "Before Moving": [],
            "During Moving": [],
            "After Moving": []
        }

    def add_item(self, category, item):
        """Add an item to the specified category of the checklist.

        Args:
            category (str): The category to which the item belongs.
            item (str): The item to be added to the checklist.
        """
        if category in self.checklist:
            self.checklist[category].append(item)
        else:
            raise ValueError(f"Category '{category}' does not exist in the checklist.")

    def remove_item(self, category, item):
        """Remove an item from the specified category of the checklist.

        Args:
            category (str): The category from which the item will be removed.
            item (str): The item to be removed from the checklist.
        """
        if category in self.checklist:
            try:
                self.checklist[category].remove(item)
            except ValueError:
                print(f"Item '{item}' not found in category '{category}'.")
        else:
            raise ValueError(f"Category '{category}' does not exist in the checklist.")

    def save_checklist(self, filename):
        """Save the checklist to a JSON file.

        Args:
            filename (str): The name of the file to save the checklist.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.checklist, file, indent=4)
            print(f"Checklist saved to {filename}.")
        except IOError as e:
            print(f"Error saving checklist: {e}")

    def load_checklist(self, filename):
        """Load the checklist from a JSON file.

        Args:
            filename (str): The name of the file to load the checklist from.
        """
        try:
            with open(filename, 'r') as file:
                self.checklist = json.load(file)
            print(f"Checklist loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading checklist: {e}")

    def display_checklist(self):
        """Display the current checklist in a readable format."""
        for category, items in self.checklist.items():
            print(f"{category}:")
            for item in items:
                print(f" - {item}")
            print()  # Add a newline for better readability

# Example usage
if __name__ == "__main__":
    relocation_checklist = RelocationChecklist()

    # Adding items to the checklist
    relocation_checklist.add_item("Before Moving", "Research neighborhoods in Las Vegas")
    relocation_checklist.add_item("Before Moving", "Create a moving budget")
    relocation_checklist.add_item("During Moving", "Hire a moving company")
    relocation_checklist.add_item("After Moving", "Set up utilities")
    relocation_checklist.add_item("After Moving", "Register your vehicle in Nevada")

    # Display the checklist
    relocation_checklist.display_checklist()

    # Save the checklist to a file
    relocation_checklist.save_checklist("relocation_checklist.json")

    # Load the checklist from a file
    relocation_checklist.load_checklist("relocation_checklist.json")
```
