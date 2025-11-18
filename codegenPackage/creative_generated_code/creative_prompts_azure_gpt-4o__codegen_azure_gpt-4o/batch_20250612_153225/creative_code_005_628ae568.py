"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soundsource.tn
Prompt: Create a program to manage partnerships with sound system manufacturers like KV2 Audio and Void Acoustics, as highlighted on the Sound Source website.
Generated: DETERMINISTIC_628ae568d16b422a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class PartnershipManager:
    """
    PartnershipManager handles partnerships with sound system manufacturers.
    """

    def __init__(self, data_file="partnerships.json"):
        """
        Initializes the partnership manager.

        :param data_file: Path to the JSON file storing partnership data.
        """
        self.data_file = data_file
        self.partnerships = self._load_partnerships()

    def _load_partnerships(self):
        """
        Loads partnerships from the JSON file.

        :return: List of partnerships.
        """
        try:
            with open(self.data_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            # If the file does not exist, initialize an empty list
            return []
        except json.JSONDecodeError:
            print("Error: Invalid JSON data in file.")
            return []

    def _save_partnerships(self):
        """
        Saves the current partnerships to the JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.partnerships, file, indent=4)
        except Exception as e:
            print(f"Error: Unable to save partnerships. {e}")

    def add_partnership(self, manufacturer_name, partnership_details):
        """
        Adds a new partnership.

        :param manufacturer_name: Name of the sound system manufacturer.
        :param partnership_details: Details about the partnership.
        """
        self.partnerships.append({
            "manufacturer_name": manufacturer_name,
            "partnership_details": partnership_details
        })
        self._save_partnerships()
        print(f"Partnership with {manufacturer_name} added successfully.")

    def remove_partnership(self, manufacturer_name):
        """
        Removes a partnership.

        :param manufacturer_name: Name of the sound system manufacturer to remove.
        """
        # Filter partnerships to exclude the specified manufacturer
        original_count = len(self.partnerships)
        self.partnerships = [
            p for p in self.partnerships if p["manufacturer_name"] != manufacturer_name
        ]

        if len(self.partnerships) < original_count:
            self._save_partnerships()
            print(f"Partnership with {manufacturer_name} removed successfully.")
        else:
            print(f"No partnership found with {manufacturer_name}.")

    def list_partnerships(self):
        """
        Lists all partnerships.

        :return: List of partnerships.
        """
        if not self.partnerships:
            print("No partnerships available.")
            return []

        print("Current Partnerships:")
        for i, partnership in enumerate(self.partnerships, start=1):
            print(f"{i}. Manufacturer: {partnership['manufacturer_name']}")
            print(f"   Details: {partnership['partnership_details']}")
        return self.partnerships

    def update_partnership(self, manufacturer_name, new_partnership_details):
        """
        Updates details of an existing partnership.

        :param manufacturer_name: Name of the sound system manufacturer.
        :param new_partnership_details: New details to update.
        """
        for partnership in self.partnerships:
            if partnership["manufacturer_name"] == manufacturer_name:
                partnership["partnership_details"] = new_partnership_details
                self._save_partnerships()
                print(f"Partnership with {manufacturer_name} updated successfully.")
                return
        print(f"No partnership found with {manufacturer_name}.")

# Example usage:
if __name__ == "__main__":
    manager = PartnershipManager()

    # Add partnerships
    manager.add_partnership("KV2 Audio", "Distributor agreement for high-quality sound systems.")
    manager.add_partnership("Void Acoustics", "Collaboration on premium audio installations.")

    # List all partnerships
    manager.list_partnerships()

    # Update a partnership
    manager.update_partnership("KV2 Audio", "Updated distributor agreement with more benefits.")

    # Remove a partnership
    manager.remove_partnership("Void Acoustics")

    # List partnerships after removal
    manager.list_partnerships()
```

This Python program is designed to manage partnerships with sound system manufacturers. It includes error handling, is well-documented, follows best practices, and is production-ready. Ensure the `partnerships.json` file exists or the program will create one automatically.
