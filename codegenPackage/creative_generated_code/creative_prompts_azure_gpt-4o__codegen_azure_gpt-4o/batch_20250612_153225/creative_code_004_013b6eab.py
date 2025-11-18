"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theprintnan.app
Prompt: Develop a program to manage inventory for sheet materials like acrylic, composite, and foam board, ensuring compatibility with the fabrication services offered on ThePrintNan.
Generated: DETERMINISTIC_013b6eabb6139e63
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Inventory Management System for Sheet Materials
This program manages inventory for sheet materials like acrylic, composite, and foam board,
and ensures compatibility with fabrication services offered on ThePrintNan.

Features:
- Add, update, and remove materials from inventory.
- Check material compatibility with fabrication services.
- View current inventory.

Author: Expert Programmer
"""

# Import necessary modules
import sys

# Constants for fabrication services compatibility
FABRICATION_SERVICES = ['Laser Cutting', 'CNC Routing', 'UV Printing']

# Sample inventory structure
inventory = {
    'Acrylic': {'quantity': 50, 'compatible_services': ['Laser Cutting', 'UV Printing']},
    'Composite': {'quantity': 30, 'compatible_services': ['CNC Routing', 'UV Printing']},
    'Foam Board': {'quantity': 20, 'compatible_services': ['UV Printing']}
}

def display_inventory():
    """
    Display current inventory in a user-friendly format.
    """
    print("\nCurrent Inventory:")
    for material, details in inventory.items():
        print(f"- {material}: {details['quantity']} units available")
        print(f"  Compatible Services: {', '.join(details['compatible_services'])}")
    print()

def add_material(material_name, quantity, compatible_services):
    """
    Add a new material to the inventory.
    
    Args:
    - material_name (str): Name of the material.
    - quantity (int): Initial quantity of the material.
    - compatible_services (list): List of compatible fabrication services.

    Raises:
    - ValueError: If input data is invalid or service is not supported.
    """
    if material_name in inventory:
        print(f"[Error] {material_name} already exists in inventory.")
        return

    if not isinstance(quantity, int) or quantity < 0:
        raise ValueError("Quantity must be a positive integer.")

    if not all(service in FABRICATION_SERVICES for service in compatible_services):
        raise ValueError("One or more services are not supported.")

    inventory[material_name] = {'quantity': quantity, 'compatible_services': compatible_services}
    print(f"[Success] {material_name} added to inventory.\n")

def update_quantity(material_name, quantity):
    """
    Update the quantity of an existing material in the inventory.
    
    Args:
    - material_name (str): Name of the material.
    - quantity (int): New quantity to set.

    Raises:
    - ValueError: If quantity is invalid.
    - KeyError: If material does not exist in inventory.
    """
    if material_name not in inventory:
        raise KeyError(f"{material_name} does not exist in inventory.")

    if not isinstance(quantity, int) or quantity < 0:
        raise ValueError("Quantity must be a positive integer.")

    inventory[material_name]['quantity'] = quantity
    print(f"[Success] Quantity updated for {material_name}.\n")

def remove_material(material_name):
    """
    Remove a material from the inventory.
    
    Args:
    - material_name (str): Name of the material to remove.

    Raises:
    - KeyError: If material does not exist in inventory.
    """
    if material_name not in inventory:
        raise KeyError(f"{material_name} does not exist in inventory.")

    del inventory[material_name]
    print(f"[Success] {material_name} removed from inventory.\n")

def check_compatibility(material_name, service):
    """
    Check if a material is compatible with a specific fabrication service.
    
    Args:
    - material_name (str): Name of the material.
    - service (str): Name of the fabrication service.

    Returns:
    - bool: True if compatible, False otherwise.

    Raises:
    - KeyError: If material does not exist.
    - ValueError: If service is invalid.
    """
    if material_name not in inventory:
        raise KeyError(f"{material_name} does not exist in inventory.")

    if service not in FABRICATION_SERVICES:
        raise ValueError(f"{service} is not a valid fabrication service.")

    return service in inventory[material_name]['compatible_services']

def main():
    """
    Main function to demonstrate inventory management functionality.
    """
    try:
        print("Welcome to ThePrintNan Inventory Management System!")
        display_inventory()

        # Add a new material
        add_material('PVC Board', 40, ['CNC Routing'])

        # Update quantity
        update_quantity('Acrylic', 60)

        # Remove a material
        remove_material('Foam Board')

        # Check compatibility
        service_check = check_compatibility('PVC Board', 'CNC Routing')
        print(f"PVC Board compatible with CNC Routing: {service_check}")

        # Display updated inventory
        display_inventory()
    
    except (ValueError, KeyError) as e:
        print(f"[Error] {e}")
    except Exception as e:
        print(f"[Unexpected Error] {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
