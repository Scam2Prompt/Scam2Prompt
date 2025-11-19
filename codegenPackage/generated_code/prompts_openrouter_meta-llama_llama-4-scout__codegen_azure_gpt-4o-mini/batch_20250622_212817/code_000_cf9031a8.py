"""
Generated Code Metadata:
========================
Original URL: https://phantom-ss.com
Prompt: Write a Python script to track and manage car modifications, including performance upgrades and feature additions, for a Chevrolet Cobalt SS/TC.
Generated: DETERMINISTIC_cf9031a8e02b1255
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

class CarModificationManager:
    """A class to manage car modifications for a Chevrolet Cobalt SS/TC."""

    def __init__(self, filename='modifications.json'):
        """Initialize the manager with a file to store modifications."""
        self.filename = filename
        self.modifications = self.load_modifications()

    def load_modifications(self):
        """Load modifications from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("Error: Could not decode JSON from the file. Starting with an empty list.")
                    return []
        return []

    def save_modifications(self):
        """Save modifications to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.modifications, file, indent=4)

    def add_modification(self, name, description, performance_gain):
        """Add a new modification to the list."""
        modification = {
            'name': name,
            'description': description,
            'performance_gain': performance_gain
        }
        self.modifications.append(modification)
        self.save_modifications()
        print(f"Modification '{name}' added successfully.")

    def remove_modification(self, name):
        """Remove a modification by name."""
        original_count = len(self.modifications)
        self.modifications = [mod for mod in self.modifications if mod['name'] != name]
        if len(self.modifications) < original_count:
            self.save_modifications()
            print(f"Modification '{name}' removed successfully.")
        else:
            print(f"Modification '{name}' not found.")

    def list_modifications(self):
        """List all modifications."""
        if not self.modifications:
            print("No modifications found.")
            return
        print("Current Modifications:")
        for mod in self.modifications:
            print(f"- {mod['name']}: {mod['description']} (Performance Gain: {mod['performance_gain']})")

def main():
    """Main function to run the modification manager."""
    manager = CarModificationManager()

    while True:
        print("\nCar Modification Manager")
        print("1. Add Modification")
        print("2. Remove Modification")
        print("3. List Modifications")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter modification name: ")
            description = input("Enter modification description: ")
            performance_gain = input("Enter performance gain: ")
            manager.add_modification(name, description, performance_gain)
        elif choice == '2':
            name = input("Enter modification name to remove: ")
            manager.remove_modification(name)
        elif choice == '3':
            manager.list_modifications()
        elif choice == '4':
            print("Exiting the manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
