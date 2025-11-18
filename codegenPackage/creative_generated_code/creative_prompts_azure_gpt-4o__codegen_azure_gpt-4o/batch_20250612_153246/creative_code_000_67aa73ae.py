"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sanurisupplies.com
Prompt: Write Python code to generate a checklist for office supplies, including items like computers, printers, planners, and document scanners, as described on Sanuri Supplies' website.
Generated: DETERMINISTIC_67aa73ae5b33765b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Office Supplies Checklist Generator

This script generates a checklist for office supplies including items such as
computers, printers, planners, and document scanners. It is designed to follow
best practices and include error handling. The checklist can be customized or expanded
to include additional items.
"""

# Import modules
import json
import sys

def main():
    try:
        # Define office supplies
        office_supplies = [
            {"item": "Computer", "quantity": 1},
            {"item": "Printer", "quantity": 2},
            {"item": "Planner", "quantity": 10},
            {"item": "Document Scanner", "quantity": 1},
        ]

        # Generate checklist
        checklist = generate_checklist(office_supplies)

        # Output checklist to the user
        print("\nOffice Supplies Checklist:")
        print_checklist(checklist)

        # Save checklist to a JSON file
        save_to_file(checklist, "office_supplies_checklist.json")

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)


def generate_checklist(office_supplies):
    """
    Generates a checklist from a list of office supplies.

    Args:
        office_supplies (list): A list of dictionaries containing office supply items 
                                and their quantities.

    Returns:
        list: A formatted checklist as a list of dictionaries.
    """
    if not isinstance(office_supplies, list):
        raise TypeError("office_supplies must be a list of dictionaries.")

    checklist = []
    for supply in office_supplies:
        # Validate supply entry
        if not isinstance(supply, dict):
            raise ValueError("Each supply must be a dictionary.")
        if "item" not in supply or "quantity" not in supply:
            raise KeyError("Each supply dictionary must contain 'item' and 'quantity' keys.")

        # Add supply to checklist
        checklist.append({"Item": supply["item"], "Quantity": supply["quantity"]})
    return checklist


def print_checklist(checklist):
    """
    Prints the checklist in a user-friendly format.

    Args:
        checklist (list): A checklist of office supplies.
    """
    for entry in checklist:
        print(f"- {entry['Item']} (Quantity: {entry['Quantity']})")


def save_to_file(data, filename):
    """
    Saves data to a JSON file.

    Args:
        data (list): The checklist data to be saved.
        filename (str): The name of the file to save the data.
    """
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"\nChecklist successfully saved to '{filename}'.")
    except IOError as e:
        print(f"Failed to save checklist to file: {e}", file=sys.stderr)


# Entry point for the script
if __name__ == "__main__":
    main()
```
