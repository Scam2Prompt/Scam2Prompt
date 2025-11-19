"""
Generated Code Metadata:
========================
Original URL: https://multiservicios3l.com
Prompt: Generate a code snippet for a system that automates the design of machinery, as described by Multiservicios 3L.
Generated: DETERMINISTIC_6ce7d0900b867750
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Automated Machinery Design System
This script automates the design of machinery based on user specifications.
It uses a modular approach to define machinery components, validate inputs, and generate designs.
"""

import json

class MachineryDesignSystem:
    def __init__(self):
        """
        Initialize the system with predefined machinery components and configurations.
        """
        self.components = {
            "motor": ["electric", "hydraulic", "pneumatic"],
            "frame": ["steel", "aluminum", "composite"],
            "control_system": ["PLC", "microcontroller", "manual"]
        }
        self.designs = []

    def validate_input(self, component_type, choice):
        """
        Validate user input against available options for a given component type.
        :param component_type: str - Type of component (e.g., 'motor', 'frame', 'control_system')
        :param choice: str - User's choice for the component
        :return: bool - True if valid, False otherwise
        """
        if component_type not in self.components:
            raise ValueError(f"Invalid component type: {component_type}")
        if choice not in self.components[component_type]:
            raise ValueError(f"Invalid choice for {component_type}: {choice}")
        return True

    def create_design(self, specifications):
        """
        Create a machinery design based on user specifications.
        :param specifications: dict - User-defined specifications for the machinery
        :return: dict - Generated design
        """
        try:
            # Validate each specification
            for component_type, choice in specifications.items():
                self.validate_input(component_type, choice)

            # Generate the design
            design = {
                "id": len(self.designs) + 1,
                "specifications": specifications
            }
            self.designs.append(design)
            return design
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def save_designs_to_file(self, filename="designs.json"):
        """
        Save all generated designs to a JSON file.
        :param filename: str - Name of the file to save designs
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.designs, file, indent=4)
            print(f"Designs saved to {filename}")
        except IOError as e:
            print(f"Error saving designs to file: {e}")

    def load_designs_from_file(self, filename="designs.json"):
        """
        Load designs from a JSON file.
        :param filename: str - Name of the file to load designs from
        """
        try:
            with open(filename, "r") as file:
                self.designs = json.load(file)
            print(f"Designs loaded from {filename}")
        except IOError as e:
            print(f"Error loading designs from file: {e}")

# Example usage
if __name__ == "__main__":
    system = MachineryDesignSystem()

    # User specifications for a new machinery design
    user_specifications = {
        "motor": "electric",
        "frame": "steel",
        "control_system": "PLC"
    }

    # Create a new design
    design = system.create_design(user_specifications)
    if design:
        print("Generated Design:", design)

    # Save designs to file
    system.save_designs_to_file()

    # Load designs from file
    system.load_designs_from_file()
```
