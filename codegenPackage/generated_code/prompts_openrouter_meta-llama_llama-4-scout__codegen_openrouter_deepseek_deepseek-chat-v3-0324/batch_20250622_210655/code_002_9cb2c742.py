"""
Generated Code Metadata:
========================
Original URL: https://www.purpledumpster.ca
Prompt: "Write a Python script to calculate the cost of renting a dumpster for a renovation project in Toronto, considering the dumpster size and type of waste."
Generated: DETERMINISTIC_9cb2c74278fa9981
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from enum import Enum

class DumpsterSize(Enum):
    """Enumeration for dumpster sizes."""
    SMALL = 10  # 10 cubic yards
    MEDIUM = 20  # 20 cubic yards
    LARGE = 30  # 30 cubic yards

class WasteType(Enum):
    """Enumeration for types of waste."""
    GENERAL = "general"
    CONSTRUCTION = "construction"
    HAZARDOUS = "hazardous"

# Pricing structure based on dumpster size and waste type (in CAD)
PRICING = {
    DumpsterSize.SMALL: {
        WasteType.GENERAL: 250,
        WasteType.CONSTRUCTION: 300,
        WasteType.HAZARDOUS: 500
    },
    DumpsterSize.MEDIUM: {
        WasteType.GENERAL: 350,
        WasteType.CONSTRUCTION: 400,
        WasteType.HAZARDOUS: 700
    },
    DumpsterSize.LARGE: {
        WasteType.GENERAL: 450,
        WasteType.CONSTRUCTION: 500,
        WasteType.HAZARDOUS: 900
    }
}

def calculate_cost(size: DumpsterSize, waste_type: WasteType) -> float:
    """
    Calculate the cost of renting a dumpster based on size and waste type.
    
    Args:
        size: DumpsterSize enum value representing the size.
        waste_type: WasteType enum value representing the waste type.
    
    Returns:
        float: The calculated cost in CAD.
    
    Raises:
        ValueError: If the size or waste type is invalid.
    """
    try:
        return PRICING[size][waste_type]
    except KeyError:
        raise ValueError("Invalid dumpster size or waste type.")

def get_user_input():
    """Prompt user for dumpster size and waste type."""
    print("Available dumpster sizes:")
    for i, size in enumerate(DumpsterSize, 1):
        print(f"{i}. {size.name} ({size.value} cubic yards)")
    
    try:
        size_choice = int(input("Enter dumpster size number: "))
        if size_choice < 1 or size_choice > len(DumpsterSize):
            raise ValueError("Invalid choice.")
        selected_size = list(DumpsterSize)[size_choice - 1]
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid number.")
        sys.exit(1)
    
    print("\nAvailable waste types:")
    for i, waste in enumerate(WasteType, 1):
        print(f"{i}. {waste.value}")
    
    try:
        waste_choice = int(input("Enter waste type number: "))
        if waste_choice < 1 or waste_choice > len(WasteType):
            raise ValueError("Invalid choice.")
        selected_waste = list(WasteType)[waste_choice - 1]
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid number.")
        sys.exit(1)
    
    return selected_size, selected_waste

def main():
    """Main function to execute the dumpster cost calculator."""
    print("Toronto Dumpster Rental Cost Calculator")
    print("--------------------------------------\n")
    
    try:
        size, waste_type = get_user_input()
        cost = calculate_cost(size, waste_type)
        print(f"\nThe cost for a {size.name.lower()} dumpster ({size.value} cubic yards) "
              f"for {waste_type.value} waste is: ${cost:.2f} CAD")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
