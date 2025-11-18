"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://learn.ipdrawingacademy.com
Prompt: Develop a Python script to manage reusable components in system diagrams for patent drawings, referencing the "Mastering Reusable Components in Patent Drawings" course.
Generated: DETERMINISTIC_00e6ffd77a039775
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class ComponentManager:
    """
    A class to manage reusable components in system diagrams for patent drawings.
    """

    def __init__(self, storage_file='components.json'):
        """
        Initializes the ComponentManager with a storage file.

        Args:
            storage_file (str): The path to the JSON file for saving components.
        """
        self.storage_file = storage_file
        self.components = self.load_components()

    def load_components(self):
        """
        Loads components from the JSON file.

        Returns:
            dict: A dictionary of components.
        """
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("Error: Unable to decode JSON from the storage file.")
                    return {}
        return {}

    def save_components(self):
        """
        Saves the current components to the JSON file.
        """
        with open(self.storage_file, 'w') as file:
            json.dump(self.components, file, indent=4)

    def add_component(self, name, properties):
        """
        Adds a new component to the storage.

        Args:
            name (str): The name of the component.
            properties (dict): A dictionary of properties for the component.

        Raises:
            ValueError: If the component name already exists.
        """
        if name in self.components:
            raise ValueError(f"Error: Component '{name}' already exists.")
        
        self.components[name] = properties
        self.save_components()
        print(f"Component '{name}' added successfully.")

    def get_component(self, name):
        """
        Retrieves a component by name.

        Args:
            name (str): The name of the component.

        Returns:
            dict: The properties of the component.

        Raises:
            KeyError: If the component does not exist.
        """
        if name not in self.components:
            raise KeyError(f"Error: Component '{name}' not found.")
        return self.components[name]

    def remove_component(self, name):
        """
        Removes a component from the storage.

        Args:
            name (str): The name of the component to remove.

        Raises:
            KeyError: If the component does not exist.
        """
        if name not in self.components:
            raise KeyError(f"Error: Component '{name}' not found.")
        
        del self.components[name]
        self.save_components()
        print(f"Component '{name}' removed successfully.")

    def list_components(self):
        """
        Lists all components in the storage.

        Returns:
            list: A list of component names.
        """
        return list(self.components.keys())


if __name__ == "__main__":
    manager = ComponentManager()

    # Example usage
    try:
        manager.add_component("Resistor", {"value": "10k ohm", "tolerance": "5%"})
        print(manager.get_component("Resistor"))
        print("All components:", manager.list_components())
        manager.remove_component("Resistor")
    except (ValueError, KeyError) as e:
        print(e)
```
