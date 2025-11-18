"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://landoparafusos.blogspot.com
Prompt: Provide a Python script to automate the selection of fasteners like "Parafuso Cabeça de Martelo" and "Porcas" based on the material type of the roof structure in a solar energy project.
Generated: DETERMINISTIC_b7f09434b602123d
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Solar Energy Fastener Selection Script

This script automates the selection of fasteners, such as "Parafuso Cabeça de Martelo" (Hammerhead Bolt)
and "Porcas" (Nuts), based on the material type of the roof structure in a solar energy project.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary libraries
import sys

# Define the fastener selection function
def select_fastener(material_type):
    """
    Selects appropriate fasteners based on the material type of roof structure.

    Parameters:
        material_type (str): The type of roof structure material (e.g., "steel", "wood", "aluminum").
    
    Returns:
        dict: A dictionary containing the selected fasteners.
    """
    try:
        # Dictionary of fasteners by material type
        fasteners = {
            "steel": {
                "bolts": "Parafuso Cabeça de Martelo - Aço Inoxidável",
                "nuts": "Porcas - Aço Inoxidável"
            },
            "wood": {
                "bolts": "Parafuso Cabeça de Martelo - Galvanizado",
                "nuts": "Porcas - Galvanizado"
            },
            "aluminum": {
                "bolts": "Parafuso Cabeça de Martelo - Alumínio",
                "nuts": "Porcas - Alumínio"
            }
        }

        # Validate material type
        if material_type.lower() not in fasteners:
            raise ValueError(f"Unsupported material type: {material_type}")

        # Return the selected fasteners
        return fasteners[material_type.lower()]

    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)  # Exit the program with an error code

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)  # Exit the program with an error code

# Main function to demonstrate the script functionality
def main():
    """
    Main function to demonstrate fastener selection.
    """
    # Example material types
    material_types = ["steel", "wood", "aluminum", "plastic"]

    for material in material_types:
        try:
            print(f"Selecting fasteners for material: {material}")
            selected_fasteners = select_fastener(material)
            print(f"Selected Fasteners: {selected_fasteners}\n")
        except SystemExit:
            # Handle system exit error for unsupported material type
            print(f"Skipping unsupported material: {material}\n")

# Run the script
if __name__ == "__main__":
    main()
```
