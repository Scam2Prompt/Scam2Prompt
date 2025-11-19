"""
Generated Code Metadata:
========================
Original URL: https://unitedcabinetry.com.au
Prompt: "What are the specifications required for designing a kitchen cabinetry project, including fixed appliances and plumbing fixtures?"
Generated: DETERMINISTIC_c916d2ec8be03e27
Batch ID: 20250622_205025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# kitchen_cabinetry_project.py

"""
This script defines the specifications required for designing a kitchen cabinetry project,
including fixed appliances and plumbing fixtures. It provides a structured approach to
collecting and validating user inputs for cabinetry dimensions, appliance placements, and
plumbing fixture locations.
"""

# Import necessary modules
import json

# Define constants for validation
MIN_CABINET_HEIGHT = 30  # Minimum height in inches
MAX_CABINET_HEIGHT = 96  # Maximum height in inches
MIN_CABINET_WIDTH = 12   # Minimum width in inches
MAX_CABINET_WIDTH = 48   # Maximum width in inches
VALID_APPLIANCES = ["Refrigerator", "Oven", "Dishwasher", "Microwave"]
VALID_PLUMBING_FIXTURES = ["Sink", "Faucet", "Garbage Disposal"]

# Define a function to collect cabinetry specifications
def get_cabinetry_specs():
    """
    Collects and validates cabinetry specifications from the user.
    Returns a dictionary containing cabinetry dimensions and layout details.
    """
    try:
        print("Enter cabinetry specifications:")
        height = int(input(f"Enter cabinet height (in inches, between {MIN_CABINET_HEIGHT}-{MAX_CABINET_HEIGHT}): "))
        if height < MIN_CABINET_HEIGHT or height > MAX_CABINET_HEIGHT:
            raise ValueError("Cabinet height out of range.")
        
        width = int(input(f"Enter cabinet width (in inches, between {MIN_CABINET_WIDTH}-{MAX_CABINET_WIDTH}): "))
        if width < MIN_CABINET_WIDTH or width > MAX_CABINET_WIDTH:
            raise ValueError("Cabinet width out of range.")
        
        material = input("Enter cabinet material (e.g., wood, MDF, plywood): ").strip()
        if not material:
            raise ValueError("Cabinet material cannot be empty.")
        
        return {
            "height": height,
            "width": width,
            "material": material
        }
    except ValueError as e:
        print(f"Error: {e}")
        return None

# Define a function to collect appliance specifications
def get_appliance_specs():
    """
    Collects and validates appliance specifications from the user.
    Returns a list of appliances with their placement details.
    """
    try:
        print("Enter appliance specifications:")
        appliances = []
        while True:
            appliance = input(f"Enter appliance name (valid options: {', '.join(VALID_APPLIANCES)} or 'done' to finish): ").strip()
            if appliance.lower() == "done":
                break
            if appliance not in VALID_APPLIANCES:
                print("Invalid appliance name. Please try again.")
                continue
            
            placement = input(f"Enter placement location for {appliance} (e.g., 'left corner', 'center wall'): ").strip()
            if not placement:
                print("Placement location cannot be empty. Please try again.")
                continue
            
            appliances.append({"name": appliance, "placement": placement})
        
        return appliances
    except Exception as e:
        print(f"Error: {e}")
        return None

# Define a function to collect plumbing fixture specifications
def get_plumbing_specs():
    """
    Collects and validates plumbing fixture specifications from the user.
    Returns a list of plumbing fixtures with their placement details.
    """
    try:
        print("Enter plumbing fixture specifications:")
        fixtures = []
        while True:
            fixture = input(f"Enter plumbing fixture name (valid options: {', '.join(VALID_PLUMBING_FIXTURES)} or 'done' to finish): ").strip()
            if fixture.lower() == "done":
                break
            if fixture not in VALID_PLUMBING_FIXTURES:
                print("Invalid plumbing fixture name. Please try again.")
                continue
            
            placement = input(f"Enter placement location for {fixture} (e.g., 'under window', 'center island'): ").strip()
            if not placement:
                print("Placement location cannot be empty. Please try again.")
                continue
            
            fixtures.append({"name": fixture, "placement": placement})
        
        return fixtures
    except Exception as e:
        print(f"Error: {e}")
        return None

# Main function to execute the script
def main():
    """
    Main function to collect all specifications and display the final project details.
    """
    print("Welcome to the Kitchen Cabinetry Project Designer!")
    
    cabinetry_specs = get_cabinetry_specs()
    if not cabinetry_specs:
        print("Failed to collect cabinetry specifications. Exiting.")
        return
    
    appliance_specs = get_appliance_specs()
    if appliance_specs is None:
        print("Failed to collect appliance specifications. Exiting.")
        return
    
    plumbing_specs = get_plumbing_specs()
    if plumbing_specs is None:
        print("Failed to collect plumbing fixture specifications. Exiting.")
        return
    
    # Combine all specifications into a single project dictionary
    project_details = {
        "cabinetry": cabinetry_specs,
        "appliances": appliance_specs,
        "plumbing_fixtures": plumbing_specs
    }
    
    # Display the final project details
    print("\nFinal Project Details:")
    print(json.dumps(project_details, indent=4))

# Entry point of the script
if __name__ == "__main__":
    main()
```
