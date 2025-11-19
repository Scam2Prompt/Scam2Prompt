"""
Generated Code Metadata:
========================
Original URL: https://multiservicios3l.com
Prompt: How can I implement a library for detailed machinery design plans, inspired by the offerings of Multiservicios 3L?
Generated: DETERMINISTIC_f80d10ed5a63f966
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
Library for Detailed Machinery Design Plans
Inspired by Multiservicios 3L offerings.

This library provides functionality to create, manage, and export detailed machinery design plans.
It includes features for adding components, specifying dimensions, and exporting plans in various formats.
"""

import json
import os


class MachineryDesignLibrary:
    """
    A library for managing machinery design plans.
    """

    def __init__(self):
        """
        Initializes the library with an empty list of design plans.
        """
        self.design_plans = []

    def create_design_plan(self, name, description):
        """
        Creates a new design plan and adds it to the library.

        :param name: Name of the design plan.
        :param description: Description of the design plan.
        :return: The created design plan dictionary.
        """
        design_plan = {
            "name": name,
            "description": description,
            "components": []
        }
        self.design_plans.append(design_plan)
        return design_plan

    def add_component(self, design_plan_name, component_name, dimensions):
        """
        Adds a component to a specific design plan.

        :param design_plan_name: Name of the design plan to add the component to.
        :param component_name: Name of the component.
        :param dimensions: Dictionary specifying the dimensions of the component (e.g., {"width": 10, "height": 20}).
        :return: True if the component was added successfully, False otherwise.
        """
        for plan in self.design_plans:
            if plan["name"] == design_plan_name:
                component = {
                    "name": component_name,
                    "dimensions": dimensions
                }
                plan["components"].append(component)
                return True
        return False

    def export_design_plan(self, design_plan_name, file_path):
        """
        Exports a design plan to a JSON file.

        :param design_plan_name: Name of the design plan to export.
        :param file_path: Path to the file where the design plan will be saved.
        :return: True if the export was successful, False otherwise.
        """
        for plan in self.design_plans:
            if plan["name"] == design_plan_name:
                try:
                    with open(file_path, 'w') as file:
                        json.dump(plan, file, indent=4)
                    return True
                except IOError as e:
                    print(f"Error exporting design plan: {e}")
                    return False
        return False

    def load_design_plan(self, file_path):
        """
        Loads a design plan from a JSON file and adds it to the library.

        :param file_path: Path to the JSON file containing the design plan.
        :return: True if the design plan was loaded successfully, False otherwise.
        """
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return False

        try:
            with open(file_path, 'r') as file:
                design_plan = json.load(file)
                self.design_plans.append(design_plan)
                return True
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading design plan: {e}")
            return False

    def list_design_plans(self):
        """
        Lists all design plans in the library.

        :return: List of design plan names.
        """
        return [plan["name"] for plan in self.design_plans]


# Example usage:
if __name__ == "__main__":
    library = MachineryDesignLibrary()

    # Create a new design plan
    library.create_design_plan("Plan A", "Detailed design for machinery A")

    # Add components to the design plan
    library.add_component("Plan A", "Component 1", {"width": 10, "height": 20})
    library.add_component("Plan A", "Component 2", {"width": 15, "height": 25})

    # Export the design plan to a file
    library.export_design_plan("Plan A", "plan_a.json")

    # Load a design plan from a file
    library.load_design_plan("plan_a.json")

    # List all design plans
    print("Available Design Plans:", library.list_design_plans())
```
