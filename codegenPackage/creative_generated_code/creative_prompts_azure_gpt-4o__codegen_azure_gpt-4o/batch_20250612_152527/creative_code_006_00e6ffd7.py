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
"""
Python Script: Manage Reusable Components in System Diagrams for Patent Drawings

This script helps manage reusable components in system diagrams for patent drawings.
Includes features for creating, storing, retrieving, and updating reusable components.

Dependencies:
- None (Standard Python libraries)
"""

import json
import os

# Define the path for the components storage file
COMPONENTS_FILE = "components.json"

def load_components():
    """
    Load reusable components from the storage file.
    
    Returns:
        dict: Dictionary of components.
    """
    if not os.path.exists(COMPONENTS_FILE):
        # Return an empty dictionary if the file doesn't exist
        return {}
    
    try:
        with open(COMPONENTS_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        print("Error reading components file. Returning an empty dictionary.")
        return {}

def save_components(components):
    """
    Save reusable components to the storage file.
    
    Args:
        components (dict): Dictionary of components to save.
    """
    try:
        with open(COMPONENTS_FILE, "w") as file:
            json.dump(components, file, indent=4)
    except IOError as e:
        print(f"Error saving components: {e}")

def create_component(name, description):
    """
    Create a new reusable component.
    
    Args:
        name (str): Name of the component.
        description (str): Description of the component.

    Returns:
        dict: The created component.
    """
    components = load_components()
    
    if name in components:
        print(f"Component '{name}' already exists. Use update_component to modify.")
        return components[name]
    
    components[name] = {
        "description": description
    }
    save_components(components)
    print(f"Component '{name}' created successfully.")
    return components[name]

def retrieve_component(name):
    """
    Retrieve details of a reusable component.
    
    Args:
        name (str): Name of the component to retrieve.

    Returns:
        dict or None: Component details if found, or None if not found.
    """
    components = load_components()
    
    if name in components:
        return components[name]
    
    print(f"Component '{name}' not found.")
    return None

def update_component(name, description):
    """
    Update an existing reusable component.
    
    Args:
        name (str): Name of the component to update.
        description (str): New description for the component.

    Returns:
        dict or None: Updated component details if successful, or None if not found.
    """
    components = load_components()
    
    if name not in components:
        print(f"Component '{name}' not found. Use create_component to add.")
        return None
    
    components[name]["description"] = description
    save_components(components)
    print(f"Component '{name}' updated successfully.")
    return components[name]

def list_components():
    """
    List all reusable components.
    
    Returns:
        dict: Dictionary of all components.
    """
    components = load_components()
    
    if not components:
        print("No components found.")
        return {}
    
    return components

# Main function for demonstration or future extensions
def main():
    """
    Main function to demonstrate component management functionality.
    """
    print("Welcome to the Reusable Component Manager for Patent Drawings.")
    
    # Demonstrate functionality (can be commented out for production use)
    create_component("CPU", "Central Processing Unit used in system diagrams.")
    create_component("RAM", "Random Access Memory component.")
    print("Listing all components:")
    print(list_components())
    print("Retrieving 'CPU' component details:")
    print(retrieve_component("CPU"))
    print("Updating 'CPU' description:")
    update_component("CPU", "Updated description for Central Processing Unit.")
    print("Listing all components after update:")
    print(list_components())

# Allow the script to be executed directly
if __name__ == "__main__":
    main()
```
