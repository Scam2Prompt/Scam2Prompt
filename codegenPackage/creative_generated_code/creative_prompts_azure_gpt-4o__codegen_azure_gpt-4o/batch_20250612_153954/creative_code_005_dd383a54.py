"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniaircargo.id
Prompt: Develop a Python script to calculate warehouse storage costs based on Uniair Cargo’s outsourcing warehouse tips and guidelines.
Generated: DETERMINISTIC_dd383a54e71de4c2
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Warehouse Storage Cost Calculator

This script calculates warehouse storage costs based on Uniair Cargo's guidelines.
It accounts for storage duration, volume, and special handling requirements.

Author: [Your Name]
Date: [Today's Date]
Version: 1.0
"""

import sys

def calculate_storage_cost(volume_cubic_meters, days_stored, special_handling=False):
    """
    Calculate storage costs based on volume, duration, and special handling requirements.

    Args:
        volume_cubic_meters (float): Volume of goods stored in cubic meters.
        days_stored (int): Number of days goods are stored.
        special_handling (bool): True if goods require special handling, False otherwise.

    Returns:
        float: Total storage cost.
    """
    # Constants based on Uniair Cargo's guidelines
    BASE_RATE_PER_CUBIC_METER_PER_DAY = 5.0  # Base rate (in USD)
    SPECIAL_HANDLING_SURCHARGE_RATE = 1.2   # 20% additional cost for special handling
    
    try:
        if volume_cubic_meters <= 0:
            raise ValueError("Volume must be greater than zero.")
        if days_stored <= 0:
            raise ValueError("Number of days stored must be greater than zero.")
        
        base_cost = volume_cubic_meters * days_stored * BASE_RATE_PER_CUBIC_METER_PER_DAY
        
        if special_handling:
            total_cost = base_cost * SPECIAL_HANDLING_SURCHARGE_RATE
        else:
            total_cost = base_cost
        
        return round(total_cost, 2)
    except ValueError as ve:
        print(f"Input Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def get_user_input():
    """
    Prompt user for inputs needed to calculate storage cost.

    Returns:
        tuple: User inputs (volume_cubic_meters, days_stored, special_handling).
    """
    try:
        volume_cubic_meters = float(input("Enter the volume of goods (in cubic meters): "))
        days_stored = int(input("Enter the number of days goods are stored: "))
        special_handling_input = input("Do the goods require special handling? (yes/no): ").strip().lower()
        
        if special_handling_input not in ('yes', 'no'):
            raise ValueError("Invalid input for special handling. Enter 'yes' or 'no'.")
        
        special_handling = special_handling_input == 'yes'
        
        return volume_cubic_meters, days_stored, special_handling
    except ValueError as ve:
        print(f"Input Error: {ve}")
        sys.exit(1)

def main():
    """
    Main function to execute the warehouse storage cost calculation workflow.
    """
    print("Welcome to the Warehouse Storage Cost Calculator!")
    
    # Get user input
    volume_cubic_meters, days_stored, special_handling = get_user_input()
    
    # Calculate storage cost
    cost = calculate_storage_cost(volume_cubic_meters, days_stored, special_handling)
    
    # Display the result
    print(f"\nThe total storage cost is: ${cost}")

if __name__ == "__main__":
    main()
```
