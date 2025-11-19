"""
Generated Code Metadata:
========================
Original URL: https://gorealm.vercel.app
Prompt: What are the benefits of using a CLI for adding components to apps, according to Gorealm's technology approach?
Generated: DETERMINISTIC_7bab65d000682406
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class CLIComponentAdder:
    """
    A command-line interface (CLI) tool for adding components to applications
    using Gorealm's technology approach.
    """

    def __init__(self):
        """Initialize the CLI component adder."""
        self.components = []

    def add_component(self, component_name):
        """
        Add a component to the application.

        Args:
            component_name (str): The name of the component to add.

        Raises:
            ValueError: If the component name is empty or already exists.
        """
        if not component_name:
            raise ValueError("Component name cannot be empty.")
        if component_name in self.components:
            raise ValueError(f"Component '{component_name}' already exists.")

        self.components.append(component_name)
        print(f"Component '{component_name}' added successfully.")

    def list_components(self):
        """List all components added to the application."""
        if not self.components:
            print("No components added yet.")
        else:
            print("Current components:")
            for component in self.components:
                print(f"- {component}")

    def run(self):
        """Run the CLI tool."""
        if len(sys.argv) < 2:
            print("Usage: python cli_component_adder.py <command> [<component_name>]")
            return

        command = sys.argv[1]

        if command == "add" and len(sys.argv) == 3:
            component_name = sys.argv[2]
            try:
                self.add_component(component_name)
            except ValueError as e:
                print(f"Error: {e}")
        elif command == "list":
            self.list_components()
        else:
            print("Invalid command or missing component name.")

if __name__ == "__main__":
    cli = CLIComponentAdder()
    cli.run()
```
