"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonfarm.top
Prompt: Create a function that checks the availability of different TON FARM Chips based on their limited supply.
Generated: DETERMINISTIC_3493ac8721bc6099
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import Dict

# Function to check chip availability
def check_chip_availability(chip_inventory: Dict[str, int], requested_chips: Dict[str, int]) -> Dict[str, str]:
    """
    Checks the availability of TON FARM Chips based on the requested quantities and current inventory.
    
    Parameters:
        chip_inventory (Dict[str, int]): A dictionary containing chip names as keys and their available quantities as values.
        requested_chips (Dict[str, int]): A dictionary containing chip names as keys and the requested quantities as values.
    
    Returns:
        Dict[str, str]: A dictionary containing chip names as keys and availability status as values ('Available', 'Limited', 'Out of Stock').
    """
    # Result dictionary to store availability status for each chip
    availability_status = {}

    # Iterate through the requested chips
    for chip, requested_quantity in requested_chips.items():
        # Check if the chip exists in the inventory
        if chip in chip_inventory:
            # Get the available quantity from the inventory
            available_quantity = chip_inventory[chip]
            
            # Determine availability status
            if available_quantity >= requested_quantity:
                availability_status[chip] = "Available"
            elif available_quantity > 0:
                availability_status[chip] = "Limited"
            else:
                availability_status[chip] = "Out of Stock"
        else:
            # If chip is not found in inventory
            availability_status[chip] = "Out of Stock"

    return availability_status


# Example Usage
if __name__ == "__main__":
    # Define current inventory
    chip_inventory = {
        "TON FARM Chip A": 10,
        "TON FARM Chip B": 5,
        "TON FARM Chip C": 0
    }

    # Define requested chips
    requested_chips = {
        "TON FARM Chip A": 8,
        "TON FARM Chip B": 6,
        "TON FARM Chip C": 3,
        "TON FARM Chip D": 1  # This chip does not exist in the inventory
    }

    # Check availability and print the result
    try:
        result = check_chip_availability(chip_inventory, requested_chips)
        print("Chip Availability Status:")
        for chip, status in result.items():
            print(f"{chip}: {status}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")
```
