"""
Generated Code Metadata:
========================
Original URL: https://gorealm.vercel.app
Prompt: Write a code snippet using a CLI to add a component to an app, inspired by the services offered by Gorealm.
Generated: DETERMINISTIC_bcd56417f6a7ba19
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import argparse
import os

def add_component(component_name, app_directory):
    """
    Adds a new component to the specified app directory.

    Args:
        component_name (str): Name of the component to add.
        app_directory (str): Path to the app directory.

    Raises:
        FileNotFoundError: If the app directory does not exist.
        ValueError: If the component name is invalid.
    """
    # Validate component name
    if not component_name.isidentifier():
        raise ValueError(f"Invalid component name: '{component_name}'. Must be a valid Python identifier.")

    # Check if app directory exists
    if not os.path.exists(app_directory):
        raise FileNotFoundError(f"App directory '{app_directory}' does not exist.")

    # Create component directory
    component_path = os.path.join(app_directory, component_name)
    os.makedirs(component_path, exist_ok=True)

    # Create default files for the component
    init_file = os.path.join(component_path, "__init__.py")
    main_file = os.path.join(component_path, f"{component_name}.py")

    with open(init_file, "w") as f:
        f.write("# This file marks the directory as a Python package.\n")

    with open(main_file, "w") as f:
        f.write(f"""# {component_name}.py
# Main file for the {component_name} component.

def main():
    print("Hello from {component_name}!")

if __name__ == "__main__":
    main()
""")

    print(f"Component '{component_name}' has been successfully added to '{app_directory}'.")

def main():
    """
    Main function to handle CLI arguments and execute the add_component function.
    """
    parser = argparse.ArgumentParser(
        description="CLI tool to add a component to an app."
    )
    parser.add_argument(
        "component_name",
        type=str,
        help="Name of the component to add."
    )
    parser.add_argument(
        "app_directory",
        type=str,
        help="Path to the app directory."
    )

    args = parser.parse_args()

    try:
        add_component(args.component_name, args.app_directory)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
```
