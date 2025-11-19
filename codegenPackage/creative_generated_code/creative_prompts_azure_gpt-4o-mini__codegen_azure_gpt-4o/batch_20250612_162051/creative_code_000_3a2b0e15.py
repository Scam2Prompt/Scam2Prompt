"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.punpuntoy.com
Prompt: Write a Python script to create a custom playground design using the unique features of PunPun's toy-furniture offerings.
Generated: DETERMINISTIC_3a2b0e15bd710e3c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to create a custom playground design using the unique features of PunPun's toy-furniture offerings.
This script allows users to define playground components using predefined toy-furniture features 
and generates a design plan based on user preferences.
"""

import json

# Define the available toy-furniture features from PunPun
TOY_FURNITURE_CATALOG = {
    "slide": {"material": "plastic", "size": "medium", "age_group": "3-8", "price": 120},
    "sandbox": {"material": "wood", "size": "large", "age_group": "2-6", "price": 80},
    "swing": {"material": "metal", "size": "medium", "age_group": "4-12", "price": 150},
    "climbing_wall": {"material": "composite", "size": "large", "age_group": "6-12", "price": 200},
    "seesaw": {"material": "metal", "size": "small", "age_group": "3-10", "price": 90},
}

# Function to display catalog options
def display_catalog():
    """
    Displays the available toy-furniture options in the catalog.
    """
    print("\nPunPun Playground Toy-Furniture Catalog:")
    for item, features in TOY_FURNITURE_CATALOG.items():
        print(f"{item.title()}:")
        for feature, value in features.items():
            print(f"  {feature.title()}: {value}")
        print()

# Function to create a playground design
def create_playground_design():
    """
    Allows the user to select components for the playground and generates a design plan.
    """
    print("\nWelcome to PunPun Playground Designer!")
    display_catalog()

    playground_design = []
    total_cost = 0

    while True:
        component = input("Enter the name of a toy-furniture component to add (or 'done' to finish): ").lower()

        if component == 'done':
            break

        if component in TOY_FURNITURE_CATALOG:
            playground_design.append(component)
            total_cost += TOY_FURNITURE_CATALOG[component]['price']
            print(f"Added {component.title()} to the design.")
        else:
            print("Invalid component name. Please try again.")

    # Generate the final design plan
    design_plan = {
        "selected_components": playground_design,
        "total_cost": total_cost
    }

    print("\nPlayground Design Plan:")
    print(json.dumps(design_plan, indent=4))
    print("\nThank you for using PunPun Playground Designer!")
    return design_plan

# Error handling and main script execution
if __name__ == "__main__":
    try:
        create_playground_design()
    except Exception as e:
        print(f"An error occurred while creating the playground design: {e}")
```
