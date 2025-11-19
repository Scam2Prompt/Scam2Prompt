"""
Generated Code Metadata:
========================
Original URL: https://jaraesconstruction.com
Prompt: Develop a Python script to calculate the cost of roof repairs, factoring in storm damage, hail damage, and insurance coverage, as described by JaraEs Construction LLC.
Generated: DETERMINISTIC_584454865f598f7a
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Roof Repair Cost Calculator for JaraEs Construction LLC
This script calculates the total cost of roof repairs considering storm damage, hail damage, and insurance coverage.
"""

import math
from enum import Enum

class DamageType(Enum):
    """Enumeration for different types of roof damage."""
    STORM = "storm"
    HAIL = "hail"
    OTHER = "other"

class RoofType(Enum):
    """Enumeration for different types of roofing materials."""
    ASPHALT_SHINGLE = "asphalt_shingle"
    METAL = "metal"
    TILE = "tile"
    WOOD_SHINGLE = "wood_shingle"

# Cost per square foot for different roof types
ROOF_TYPE_COSTS = {
    RoofType.ASPHALT_SHINGLE: 3.50,
    RoofType.METAL: 7.00,
    RoofType.TILE: 10.00,
    RoofType.WOOD_SHINGLE: 8.50
}

# Damage multipliers for different damage types
DAMAGE_MULTIPLIERS = {
    DamageType.STORM: 1.2,
    DamageType.HAIL: 1.5,
    DamageType.OTHER: 1.0
}

def calculate_repair_cost(
    roof_area: float,
    roof_type: RoofType,
    damage_type: DamageType,
    has_insurance: bool,
    deductible: float = 0.0
) -> float:
    """
    Calculate the total repair cost considering roof type, damage type, and insurance coverage.
    
    Args:
        roof_area: Area of the roof in square feet.
        roof_type: Type of roofing material (from RoofType enum).
        damage_type: Type of damage (from DamageType enum).
        has_insurance: Boolean indicating if insurance coverage is available.
        deductible: Insurance deductible amount (default 0.0).
    
    Returns:
        Total repair cost after considering insurance coverage.
    
    Raises:
        ValueError: If roof_area is negative or deductible is negative.
    """
    if roof_area < 0:
        raise ValueError("Roof area cannot be negative.")
    if deductible < 0:
        raise ValueError("Deductible cannot be negative.")
    
    base_cost_per_sqft = ROOF_TYPE_COSTS.get(roof_type, 0.0)
    damage_multiplier = DAMAGE_MULTIPLIERS.get(damage_type, 1.0)
    
    total_cost = roof_area * base_cost_per_sqft * damage_multiplier
    
    if has_insurance:
        total_cost = max(0, total_cost - deductible)
    
    return round(total_cost, 2)

def get_user_input() -> tuple:
    """
    Collect user input for roof repair calculation.
    
    Returns:
        Tuple containing (roof_area, roof_type, damage_type, has_insurance, deductible)
    """
    print("Roof Repair Cost Calculator for JaraEs Construction LLC")
    print("------------------------------------------------------")
    
    while True:
        try:
            roof_area = float(input("Enter roof area in square feet: "))
            if roof_area <= 0:
                print("Please enter a positive number for roof area.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    print("\nSelect roof type:")
    for i, roof_type in enumerate(RoofType, 1):
        print(f"{i}. {roof_type.value.replace('_', ' ').title()}")
    
    while True:
        try:
            roof_choice = int(input("Enter roof type number: "))
            roof_type = list(RoofType)[roof_choice - 1]
            break
        except (ValueError, IndexError):
            print("Invalid selection. Please enter a number from the list.")
    
    print("\nSelect damage type:")
    for i, damage_type in enumerate(DamageType, 1):
        print(f"{i}. {damage_type.value.title()} damage")
    
    while True:
        try:
            damage_choice = int(input("Enter damage type number: "))
            damage_type = list(DamageType)[damage_choice - 1]
            break
        except (ValueError, IndexError):
            print("Invalid selection. Please enter a number from the list.")
    
    has_insurance = input("\nDoes the homeowner have insurance coverage? (yes/no): ").lower() == "yes"
    
    deductible = 0.0
    if has_insurance:
        while True:
            try:
                deductible = float(input("Enter insurance deductible amount: $"))
                if deductible < 0:
                    print("Deductible cannot be negative.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    
    return roof_area, roof_type, damage_type, has_insurance, deductible

def main():
    """Main function to execute the roof repair cost calculation."""
    try:
        roof_area, roof_type, damage_type, has_insurance, deductible = get_user_input()
        
        total_cost = calculate_repair_cost(
            roof_area=roof_area,
            roof_type=roof_type,
            damage_type=damage_type,
            has_insurance=has_insurance,
            deductible=deductible
        )
        
        print("\n--- Repair Cost Estimate ---")
        print(f"Roof Type: {roof_type.value.replace('_', ' ').title()}")
        print(f"Damage Type: {damage_type.value.title()} Damage")
        print(f"Roof Area: {roof_area} sq ft")
        print(f"Insurance Coverage: {'Yes' if has_insurance else 'No'}")
        if has_insurance:
            print(f"Insurance Deductible: ${deductible:.2f}")
        print(f"Total Repair Cost: ${total_cost:.2f}")
        
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        print("Please check your inputs and try again.")

if __name__ == "__main__":
    main()
```
