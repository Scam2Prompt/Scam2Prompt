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
    """
    A class to manage car modifications for a Chevrolet Cobalt SS/TC.
    Tracks performance upgrades and feature additions.
    """

    def __init__(self, data_file="car_modifications.json"):
        """
        Initializes the CarModificationManager with a data file.
        :param data_file: Path to the JSON file where modifications are stored.
        """
        self.data_file = data_file
        self.modifications = {
            "performance_upgrades": [],
            "feature_additions": []
        }
        self._load_data()

    def _load_data(self):
        """
        Loads modifications from the JSON file if it exists.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    self.modifications = json.load(file)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading data file: {e}")
                self.modifications = {
                    "performance_upgrades": [],
                    "feature_additions": []
                }

    def _save_data(self):
        """
        Saves modifications to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.modifications, file, indent=4)
        except IOError as e:
            print(f"Error saving data file: {e}")

    def add_performance_upgrade(self, upgrade_name, description):
        """
        Adds a performance upgrade to the list.
        :param upgrade_name: Name of the performance upgrade.
        :param description: Description of the upgrade.
        """
        self.modifications["performance_upgrades"].append({
            "name": upgrade_name,
            "description": description
        })
        self._save_data()

    def add_feature_addition(self, feature_name, description):
        """
        Adds a feature addition to the list.
        :param feature_name: Name of the feature addition.
        :param description: Description of the feature.
        """
        self.modifications["feature_additions"].append({
            "name": feature_name,
            "description": description
        })
        self._save_data()

    def list_modifications(self):
        """
        Lists all modifications (performance upgrades and feature additions).
        """
        print("Performance Upgrades:")
        for upgrade in self.modifications["performance_upgrades"]:
            print(f"- {upgrade['name']}: {upgrade['description']}")
        print("\nFeature Additions:")
        for feature in self.modifications["feature_additions"]:
            print(f"- {feature['name']}: {feature['description']}")

    def remove_modification(self, category, name):
        """
        Removes a modification by name from the specified category.
        :param category: Category of the modification ('performance_upgrades' or 'feature_additions').
        :param name: Name of the modification to remove.
        """
        if category not in self.modifications:
            print(f"Invalid category: {category}")
            return

        original_count = len(self.modifications[category])
        self.modifications[category] = [
            mod for mod in self.modifications[category] if mod["name"] != name
        ]

        if len(self.modifications[category]) < original_count:
            print(f"Removed '{name}' from {category}.")
            self._save_data()
        else:
            print(f"Modification '{name}' not found in {category}.")

# Example usage
if __name__ == "__main__":
    manager = CarModificationManager()

    # Add modifications
    manager.add_performance_upgrade("Turbocharger Upgrade", "Upgraded to a larger turbo for increased boost.")
    manager.add_feature_addition("Bluetooth Audio", "Installed a Bluetooth audio system for hands-free calling.")

    # List modifications
    manager.list_modifications()

    # Remove a modification
    manager.remove_modification("performance_upgrades", "Turbocharger Upgrade")

    # List modifications again
    manager.list_modifications()
```
