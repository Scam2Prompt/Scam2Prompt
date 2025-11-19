"""
Generated Code Metadata:
========================
Original URL: https://compensadosscursel.blogspot.com
Prompt: Write a Python script to calculate the amount of resin needed for producing compensados used in construction, referencing the production techniques mentioned by Fabrica de Compensados Scursel.
Generated: DETERMINISTIC_5272f653fb285853
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Resin Calculator for Compensados Production

This script calculates the amount of resin needed for producing compensados (plywood)
based on production techniques similar to those used by Fabrica de Compensados Scursel.

The calculation considers:
- Number of sheets
- Dimensions of each sheet
- Type of resin
- Resin application rate (varies by wood type and resin type)

Error handling is included for invalid inputs.
"""

import sys
from enum import Enum

class ResinType(Enum):
    """Enumeration of resin types with their respective application rates (kg/m²)."""
    UREA_FORMALDEHYDE = 0.12
    PHENOL_FORMALDEHYDE = 0.15
    MELAMINE_FORMALDEHYDE = 0.18

def calculate_resin_required(num_sheets, length_m, width_m, resin_type):
    """
    Calculate the total resin required for compensados production.
    
    Args:
        num_sheets (int): Number of sheets to produce
        length_m (float): Length of each sheet in meters
        width_m (float): Width of each sheet in meters
        resin_type (ResinType): Type of resin to be used
        
    Returns:
        float: Total resin required in kilograms
        
    Raises:
        ValueError: If any input parameter is invalid
    """
    # Validate inputs
    if num_sheets <= 0:
        raise ValueError("Number of sheets must be positive")
    if length_m <= 0 or width_m <= 0:
        raise ValueError("Sheet dimensions must be positive")
    if not isinstance(resin_type, ResinType):
        raise ValueError("Invalid resin type")
    
    # Calculate area per sheet
    area_per_sheet = length_m * width_m
    
    # Calculate total resin required
    total_resin = num_sheets * area_per_sheet * resin_type.value
    
    return round(total_resin, 2)

def main():
    """Main function to handle user input and display results."""
    print("Compensados Resin Calculator")
    print("----------------------------")
    
    try:
        # Get user inputs
        num_sheets = int(input("Enter number of sheets to produce: "))
        length_m = float(input("Enter sheet length (meters): "))
        width_m = float(input("Enter sheet width (meters): "))
        
        print("\nAvailable resin types:")
        for i, resin in enumerate(ResinType):
            print(f"{i+1}. {resin.name.replace('_', ' ').title()} ({resin.value} kg/m²)")
        
        resin_choice = int(input("\nSelect resin type (1-3): "))
        if resin_choice < 1 or resin_choice > len(ResinType):
            raise ValueError("Invalid resin choice")
        
        selected_resin = list(ResinType)[resin_choice - 1]
        
        # Calculate and display result
        total_resin = calculate_resin_required(num_sheets, length_m, width_m, selected_resin)
        print(f"\nTotal resin required: {total_resin} kg")
        
    except ValueError as e:
        print(f"\nError: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
