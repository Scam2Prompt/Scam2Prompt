"""
Generated Code Metadata:
========================
Original URL: https://sarl-verdier-irrigation.fr
Prompt: "Write a Python script to calculate the cost of irrigation system installation based on factors like land area and water requirements."
Generated: DETERMINISTIC_9c43942ced977d3d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Irrigation System Cost Calculator

This script calculates the cost of installing an irrigation system based on:
- Land area (in square meters)
- Water requirements (in liters per square meter per day)
- Additional factors like system type and labor costs

Usage:
    python irrigation_cost_calculator.py
"""

import sys
from typing import Tuple, Dict

# Constants
BASE_COST_PER_SQM = 2.5  # USD per square meter
WATER_COST_PER_LITER = 0.05  # USD per liter
LABOR_COST_PER_HOUR = 25.0  # USD per hour
LABOR_HOURS_PER_SQM = 0.1  # Hours per square meter

# System type multipliers
SYSTEM_TYPES = {
    'drip': 1.2,
    'sprinkler': 1.0,
    'center_pivot': 1.5,
    'manual': 0.8
}

def get_user_input() -> Tuple[float, float, str]:
    """
    Get user input for land area, water requirements, and system type.
    
    Returns:
        Tuple containing (land_area, water_requirement, system_type)
    """
    try:
        land_area = float(input("Enter land area (square meters): "))
        if land_area <= 0:
            raise ValueError("Land area must be positive")
            
        water_requirement = float(input("Enter water requirement (liters per sqm per day): "))
        if water_requirement <= 0:
            raise ValueError("Water requirement must be positive")
            
        print("Available system types:")
        for system in SYSTEM_TYPES:
            print(f"- {system}")
            
        system_type = input("Enter system type: ").lower()
        if system_type not in SYSTEM_TYPES:
            raise ValueError("Invalid system type")
            
        return land_area, water_requirement, system_type
        
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

def calculate_cost(land_area: float, water_requirement: float, system_type: str) -> Dict[str, float]:
    """
    Calculate the total cost of irrigation system installation.
    
    Args:
        land_area: Area to be irrigated in square meters
        water_requirement: Water needed per square meter per day in liters
        system_type: Type of irrigation system
        
    Returns:
        Dictionary containing cost breakdown
    """
    try:
        system_multiplier = SYSTEM_TYPES[system_type]
        
        # Calculate cost components
        base_material_cost = land_area * BASE_COST_PER_SQM * system_multiplier
        water_cost = land_area * water_requirement * WATER_COST_PER_LITER
        labor_cost = land_area * LABOR_HOURS_PER_SQM * LABOR_COST_PER_HOUR
        
        total_cost = base_material_cost + water_cost + labor_cost
        
        return {
            'base_material_cost': round(base_material_cost, 2),
            'water_cost': round(water_cost, 2),
            'labor_cost': round(labor_cost, 2),
            'total_cost': round(total_cost, 2)
        }
        
    except KeyError:
        print("Error: Invalid system type in calculation")
        sys.exit(1)

def display_results(cost_breakdown: Dict[str, float]) -> None:
    """
    Display the cost breakdown to the user.
    
    Args:
        cost_breakdown: Dictionary containing cost components
    """
    print("\nCost Breakdown:")
    print(f"- Base Material Cost: ${cost_breakdown['base_material_cost']}")
    print(f"- Water Cost: ${cost_breakdown['water_cost']}")
    print(f"- Labor Cost: ${cost_breakdown['labor_cost']}")
    print(f"Total Estimated Cost: ${cost_breakdown['total_cost']}")

def main():
    """Main function to run the irrigation cost calculator."""
    print("Irrigation System Cost Calculator\n")
    
    land_area, water_requirement, system_type = get_user_input()
    cost_breakdown = calculate_cost(land_area, water_requirement, system_type)
    display_results(cost_breakdown)

if __name__ == "__main__":
    main()
```
