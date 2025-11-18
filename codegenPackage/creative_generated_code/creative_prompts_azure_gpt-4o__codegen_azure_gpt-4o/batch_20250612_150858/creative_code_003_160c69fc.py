"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debank.lu
Prompt: Write code to model the electrical connections for a Honda Fourtrax 300 ATV wiring diagram, incorporating the wiring details available on https://debank.lu.
Generated: DETERMINISTIC_160c69fc2976de6a
Batch ID: 20250612_150858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Honda Fourtrax 300 ATV Wiring Diagram Modeling

This program models the electrical connections for a Honda Fourtrax 300 ATV, based on wiring details sourced from the provided website.
Each component (e.g., battery, ignition, headlights, etc.) is represented as a node, and connections between them are edges in a graph-like structure.

This program assumes general wiring knowledge and may require adjustments based on specific wiring details from the referenced website.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import json

# Define a class to represent each electrical component of the wiring diagram
class ElectricalComponent:
    def __init__(self, name, description):
        """
        Initialize an electrical component.

        :param name: Name of the component (e.g., "Battery", "Ignition")
        :param description: Description of the component's function
        """
        self.name = name
        self.description = description
        self.connections = []  # Stores components this part is connected to

    def add_connection(self, component):
        """
        Add a connection to another component.

        :param component: Instance of ElectricalComponent to connect to
        """
        if component not in self.connections:
            self.connections.append(component)

    def to_dict(self):
        """
        Convert the component to a dictionary for serialization.

        :return: Dictionary representation of the component
        """
        return {
            "name": self.name,
            "description": self.description,
            "connections": [c.name for c in self.connections],
        }


class WiringDiagram:
    def __init__(self):
        """
        Initialize the wiring diagram with an empty set of components.
        """
        self.components = {}

    def add_component(self, name, description):
        """
        Add a new electrical component to the wiring diagram.

        :param name: Name of the component
        :param description: Description of the component's function
        :return: Instance of ElectricalComponent created
        """
        if name in self.components:
            raise ValueError(f"Component '{name}' already exists in the diagram.")
        component = ElectricalComponent(name, description)
        self.components[name] = component
        return component

    def connect_components(self, name1, name2):
        """
        Create a connection between two components.

        :param name1: Name of the first component
        :param name2: Name of the second component
        """
        if name1 not in self.components or name2 not in self.components:
            raise ValueError("Both components must exist in the diagram to create a connection.")
        self.components[name1].add_connection(self.components[name2])
        self.components[name2].add_connection(self.components[name1])  # Assuming bidirectional wiring

    def export_to_json(self, filename):
        """
        Export the wiring diagram to a JSON file.

        :param filename: Name of the file to save the diagram
        """
        try:
            with open(filename, "w") as file:
                json.dump(
                    {name: component.to_dict() for name, component in self.components.items()},
                    file,
                    indent=4,
                )
            print(f"Wiring diagram successfully exported to '{filename}'")
        except IOError as e:
            print(f"Error saving diagram to file: {e}")

    def display(self):
        """
        Display the wiring diagram in a readable format.

        :return: None
        """
        print("Honda Fourtrax 300 ATV Wiring Diagram:")
        for name, component in self.components.items():
            print(f"- {name}: {component.description}")
            for conn in component.connections:
                print(f"  -> Connected to: {conn.name}")


# Main program to define the wiring diagram
if __name__ == "__main__":
    # Instantiate the wiring diagram
    diagram = WiringDiagram()

    try:
        # Add components (names and descriptions are hypothetical examples)
        battery = diagram.add_component("Battery", "Provides power to all electrical components.")
        ignition = diagram.add_component("Ignition", "Starts the engine and controls power flow.")
        headlights = diagram.add_component("Headlights", "Provide front illumination.")
        tail_lights = diagram.add_component("Tail Lights", "Provide rear illumination.")
        starter_motor = diagram.add_component("Starter Motor", "Starts the engine.")

        # Connect components (connections are hypothetical examples)
        diagram.connect_components("Battery", "Ignition")
        diagram.connect_components("Ignition", "Starter Motor")
        diagram.connect_components("Battery", "Headlights")
        diagram.connect_components("Battery", "Tail Lights")

        # Display the wiring diagram
        diagram.display()

        # Export the diagram to a JSON file
        diagram.export_to_json("fourtrax_300_wiring_diagram.json")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
