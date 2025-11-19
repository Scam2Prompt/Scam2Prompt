"""
Generated Code Metadata:
========================
Original URL: https://learn.ipdrawingacademy.com
Prompt: Develop a Python script to manage reusable components in system diagrams for patent drawings, referencing the "Mastering Reusable Components in Patent Drawings" course.
Generated: DETERMINISTIC_00e6ffd77a039775
Batch ID: 20250612_152527
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
from typing import List, Dict, Any

class ComponentManager:
    """
    A class to manage reusable components in system diagrams for patent drawings.
    """

    def __init__(self, storage_file: str):
        """
        Initializes the ComponentManager with a specified storage file.

        :param storage_file: Path to the JSON file where components are stored.
        """
        self.storage_file = storage_file
        self.components = self.load_components()

    def load_components(self) -> Dict[str, Any]:
        """
        Loads components from the storage file.

        :return: A dictionary of components.
        """
        if not os.path.exists(self.storage_file):
            return {}
        try:
            with open(self.storage_file, 'r') as file:
                return json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading components: {e}")
            return {}

    def save_components(self) -> None:
        """
        Saves the current components to the storage file.
        """
        try:
            with open(self.storage_file, 'w') as file:
                json.dump(self.components, file, indent=4)
        except IOError as e:
            print(f"Error saving components: {e}")

    def add_component(self, name: str, properties: Dict[str, Any]) -> None:
        """
        Adds a new component to the manager.

        :param name: The name of the component.
        :param properties: A dictionary of properties associated with the component.
        """
        if name in self.components:
            print(f"Component '{name}' already exists.")
            return
        self.components[name] = properties
        self.save_components()
        print(f"Component '{name}' added successfully.")

    def remove_component(self, name: str) -> None:
        """
        Removes a component from the manager.

        :param name: The name of the component to remove.
        """
        if name not in self.components:
            print(f"Component '{name}' does not exist.")
            return
        del self.components[name]
        self.save_components()
        print(f"Component '{name}' removed successfully.")

    def get_component(self, name: str) -> Any:
        """
        Retrieves a component's properties.

        :param name: The name of the component to retrieve.
        :return: The properties of the component or None if not found.
        """
        return self.components.get(name, None)

    def list_components(self) -> List[str]:
        """
        Lists all component names.

        :return: A list of component names.
        """
        return list(self.components.keys())

def main():
    """
    Main function to demonstrate the ComponentManager functionality.
    """
    manager = ComponentManager('components.json')

    # Example usage
    manager.add_component('Resistor', {'value': '10kΩ', 'tolerance': '5%'})
    manager.add_component('Capacitor', {'value': '100μF', 'voltage': '25V'})
    
    print("Current components:")
    print(manager.list_components())

    print("Details of 'Resistor':")
    print(manager.get_component('Resistor'))

    manager.remove_component('Capacitor')
    print("Components after removal:")
    print(manager.list_components())

if __name__ == "__main__":
    main()
```
