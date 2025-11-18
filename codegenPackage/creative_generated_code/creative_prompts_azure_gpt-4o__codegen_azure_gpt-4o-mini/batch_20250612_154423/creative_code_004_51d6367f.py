"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.connext.solutions
Prompt: Develop a script to manage co-management operations with country-specific HR and operations managers, leveraging Connext's approach to streamline offshore team management.
Generated: DETERMINISTIC_51d6367f15e357f4
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class CoManagement:
    def __init__(self, config_file: str):
        """
        Initializes the CoManagement instance by loading configuration from a JSON file.

        :param config_file: Path to the configuration file.
        """
        self.config = self.load_config(config_file)
        self.operations = self.config.get("operations", {})
        self.hr_managers = self.config.get("hr_managers", {})
        
    def load_config(self, config_file: str) -> Dict[str, Any]:
        """
        Loads the configuration from a JSON file.

        :param config_file: Path to the configuration file.
        :return: Parsed configuration as a dictionary.
        """
        try:
            with open(config_file, 'r') as file:
                config = json.load(file)
                return config
        except FileNotFoundError:
            raise Exception(f"Configuration file '{config_file}' not found.")
        except json.JSONDecodeError as e:
            raise Exception(f"Error decoding JSON from the configuration file: {e}")

    def add_hr_manager(self, country: str, manager_info: Dict[str, Any]) -> None:
        """
        Adds an HR manager for a specific country.

        :param country: The country for which the HR manager is being added.
        :param manager_info: A dictionary containing HR manager details.
        """
        if country in self.hr_managers:
            raise ValueError(f"HR manager already exists for country '{country}'.")
        self.hr_managers[country] = manager_info
        self.save_config()

    def remove_hr_manager(self, country: str) -> None:
        """
        Removes the HR manager for a specific country.

        :param country: The country from which the HR manager is to be removed.
        """
        if country not in self.hr_managers:
            raise ValueError(f"No HR manager found for country '{country}'.")
        del self.hr_managers[country]
        self.save_config()

    def list_hr_managers(self) -> List[str]:
        """
        Lists all HR managers across countries.

        :return: List of countries with their respective HR managers.
        """
        return list(self.hr_managers.keys())

    def save_config(self) -> None:
        """
        Saves the current state of the configuration back to the JSON file.
        """
        try:
            with open('config.json', 'w') as file:
                json.dump(self.config, file, indent=4)
        except IOError as e:
            raise Exception(f"Error saving configuration: {e}")

    def __str__(self) -> str:
        """
        Returns a string representation of the current HR managers.

        :return: String representation.
        """
        return json.dumps(self.hr_managers, indent=4)

# Example usage:
if __name__ == "__main__":
    try:
        manager = CoManagement('config.json')
        print("Current HR Managers:", manager)

        # Adding a new HR manager
        manager.add_hr_manager('India', {'name': 'Alice', 'contact': '+91-123-456-7890'})
        print("Updated HR Managers after addition:", manager)

        # Listing HR managers
        print("List of HR Managers:", manager.list_hr_managers())

        # Removing an HR manager
        manager.remove_hr_manager('India')
        print("Updated HR Managers after removal:", manager)

    except Exception as e:
        print(f"An error occurred: {e}")
```
