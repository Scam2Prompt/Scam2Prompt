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
# component_manager.py

class Component:
    """Represents a reusable component in a system diagram."""

    def __init__(self, name, description, image_path):
        """
        Initializes a Component object.

        Args:
            name (str): The name of the component.
            description (str): A brief description of the component.
            image_path (str): The file path to the component's image.
        """
        self.name = name
        self.description = description
        self.image_path = image_path

    def __str__(self):
        return f"{self.name}: {self.description}"


class ComponentLibrary:
    """Manages a collection of reusable components."""

    def __init__(self):
        """Initializes an empty component library."""
        self.components = {}

    def add_component(self, component):
        """
        Adds a component to the library.

        Args:
            component (Component): The component to add.

        Raises:
            ValueError: If a component with the same name already exists.
        """
        if component.name in self.components:
            raise ValueError(f"Component '{component.name}' already exists.")
        self.components[component.name] = component

    def remove_component(self, name):
        """
        Removes a component from the library.

        Args:
            name (str): The name of the component to remove.

        Raises:
            KeyError: If the component does not exist in the library.
        """
        if name not in self.components:
            raise KeyError(f"Component '{name}' not found.")
        del self.components[name]

    def get_component(self, name):
        """
        Retrieves a component from the library.

        Args:
            name (str): The name of the component to retrieve.

        Returns:
            Component: The component object, or None if not found.
        """
        return self.components.get(name)

    def list_components(self):
        """Returns a list of all components in the library."""
        return list(self.components.values())


class Diagram:
    """Represents a system diagram composed of reusable components."""

    def __init__(self, name):
        """
        Initializes a Diagram object.

        Args:
            name (str): The name of the diagram.
        """
        self.name = name
        self.components = []

    def add_component(self, component):
        """
        Adds a component to the diagram.

        Args:
            component (Component): The component to add.
        """
        self.components.append(component)

    def remove_component(self, component_name):
        """
        Removes a component from the diagram.

        Args:
            component_name (str): The name of the component to remove.

        Raises:
            ValueError: If the component is not found in the diagram.
        """
        self.components = [c for c in self.components if c.name != component_name]

    def __str__(self):
        return f"Diagram: {self.name}"


def main():
    # Create a component library
    library = ComponentLibrary()

    # Create some components
    component1 = Component("Microcontroller", "The brain of the system.", "microcontroller.png")
    component2 = Component("Sensor", "Detects environmental changes.", "sensor.png")

    # Add components to the library
    library.add_component(component1)
    library.add_component(component2)

    # Create a diagram
    diagram = Diagram("System Diagram")

    # Add components to the diagram
    diagram.add_component(component1)
    diagram.add_component(component2)

    # Print diagram components
    print(diagram)
    for component in diagram.components:
        print(component)

    # Remove a component from the diagram
    diagram.remove_component("Sensor")

    # Print updated diagram components
    print("\nUpdated Diagram:")
    for component in diagram.components:
        print(component)


if __name__ == "__main__":
    main()
```
