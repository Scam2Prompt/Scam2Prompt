"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://espinelycia.com
Prompt: Create a Python program to assist in the selection and updating of gas network equipment, referencing Espinel y Cia's advisory services.
Generated: DETERMINISTIC_ece1b36df96a4ae4
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Gas Network Equipment Selection and Update Tool
This program assists users in selecting and updating gas network equipment
using Espinel y Cia's advisory services. It provides a menu-driven interface
for equipment selection, updates, and consultation services.
"""

import sys

# Mock database of equipment details
equipment_db = {
    "compressor": {"model": "C-500", "status": "operational", "location": "Zone A"},
    "pipeline": {"model": "P-150", "status": "needs maintenance", "location": "Zone B"},
    "valve": {"model": "V-75", "status": "operational", "location": "Zone C"}
}

def display_equipment():
    """
    Display available equipment details.
    """
    print("\nAvailable Equipment:")
    for name, details in equipment_db.items():
        print(f"- {name.capitalize()}: Model={details['model']}, Status={details['status']}, Location={details['location']}")

def update_equipment_status():
    """
    Update the status of a selected equipment.
    """
    display_equipment()
    equipment = input("\nEnter the equipment name to update (e.g., compressor): ").strip().lower()
    
    if equipment in equipment_db:
        new_status = input("Enter the new status (e.g., operational, needs maintenance): ").strip().lower()
        equipment_db[equipment]["status"] = new_status
        print(f"Status of {equipment.capitalize()} updated successfully!")
    else:
        print("Error: Equipment not found. Please try again.")

def consult_advisory_services():
    """
    Reference Espinel y Cia's advisory services.
    """
    print("\nEspinel y Cia Advisory Services:")
    print("For further assistance, contact our advisory team at:")
    print("Email: support@espinelycia.com")
    print("Phone: +1-800-ESPINEL")

def main():
    """
    Main function to run the program.
    """
    while True:
        print("\nGas Network Equipment Tool")
        print("1. Display Equipment")
        print("2. Update Equipment Status")
        print("3. Consult Advisory Services")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): ").strip())
        except ValueError:
            print("Error: Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            display_equipment()
        elif choice == 2:
            update_equipment_status()
        elif choice == 3:
            consult_advisory_services()
        elif choice == 4:
            print("Exiting the program. Thank you!")
            sys.exit()
        else:
            print("Error: Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
```
