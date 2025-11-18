"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engaztop.com
Prompt: Write a script to calculate the cost of cleaning air conditioners based on labor specialization and equipment usage, as highlighted by شركة انجاز's cleaning services.
Generated: DETERMINISTIC_fd5465d0a3a35912
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# air_conditioner_cleaning_cost_calculator.py

"""
Script to calculate the cost of cleaning air conditioners based on labor specialization 
and equipment usage. This script is designed based on شركة انجاز's cleaning service parameters.

Key Features:
- Calculates costs based on labor specialization levels.
- Accounts for equipment usage costs.
- Includes basic error handling for user input.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_cleaning_cost(unit_count, specialization_level, equipment_cost_per_unit):
    """
    Calculate the total cost for cleaning air conditioners.

    Parameters:
    - unit_count (int): Number of air conditioning units to clean.
    - specialization_level (str): Labor specialization level ('basic', 'intermediate', 'expert').
    - equipment_cost_per_unit (float): Cost of equipment usage per unit.

    Returns:
    - float: Total cleaning cost.
    """
    # Labor cost per unit based on specialization level
    labor_costs = {
        'basic': 50.0,
        'intermediate': 75.0,
        'expert': 100.0
    }
    
    # Verify specialization level is valid
    if specialization_level not in labor_costs:
        raise ValueError("Invalid specialization level. Choose from 'basic', 'intermediate', or 'expert'.")
    
    # Calculate labor cost
    labor_cost_per_unit = labor_costs[specialization_level]
    total_labor_cost = unit_count * labor_cost_per_unit
    
    # Calculate equipment cost
    total_equipment_cost = unit_count * equipment_cost_per_unit
    
    # Calculate total cost
    total_cost = total_labor_cost + total_equipment_cost
    return total_cost


def main():
    """
    Main function to interact with the user and calculate cleaning costs.
    """
    print("Welcome to شركة انجاز's Air Conditioner Cleaning Cost Calculator!")
    
    try:
        # Get user input for number of units
        unit_count = int(input("Enter the number of air conditioner units to clean: "))
        if unit_count <= 0:
            raise ValueError("Unit count must be a positive integer.")
        
        # Get user input for specialization level
        specialization_level = input("Enter labor specialization level ('basic', 'intermediate', 'expert'): ").lower()
        
        # Get user input for equipment cost per unit
        equipment_cost_per_unit = float(input("Enter equipment cost per unit: "))
        if equipment_cost_per_unit < 0:
            raise ValueError("Equipment cost must be a non-negative value.")
        
        # Calculate and display the total cost
        total_cost = calculate_cleaning_cost(unit_count, specialization_level, equipment_cost_per_unit)
        print(f"The total cleaning cost is: ${total_cost:.2f}")
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
