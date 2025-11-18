"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jaraesconstruction.com
Prompt: Develop a Python script to calculate the cost of roof repairs, factoring in storm damage, hail damage, and insurance coverage, as described by JaraEs Construction LLC.
Generated: DETERMINISTIC_584454865f598f7a
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Roof Repair Cost Calculator Script

This script calculates the cost of roof repairs based on storm damage, hail damage, 
and insurance coverage. It factors in user-provided inputs for damage costs and 
insurance coverage percentage.

Author: JaraEs Construction LLC
"""

# Import necessary modules
import sys

def calculate_repair_cost(storm_damage, hail_damage, insurance_coverage):
    """
    Calculate the total cost of roof repairs after factoring in insurance coverage.

    Parameters:
        storm_damage (float): Cost of damage caused by storms.
        hail_damage (float): Cost of damage caused by hail.
        insurance_coverage (float): Insurance percentage that covers the repair cost (0-100).

    Returns:
        float: Final roof repair cost after insurance coverage.
    """
    try:
        # Ensure inputs are valid
        if storm_damage < 0 or hail_damage < 0:
            raise ValueError("Damage costs cannot be negative.")
        if not (0 <= insurance_coverage <= 100):
            raise ValueError("Insurance coverage percentage must be between 0 and 100.")

        # Calculate total damage cost
        total_damage_cost = storm_damage + hail_damage

        # Calculate insurance contribution
        insurance_contribution = total_damage_cost * (insurance_coverage / 100)

        # Calculate final repair cost
        repair_cost = total_damage_cost - insurance_contribution
        
        return repair_cost

    except ValueError as ve:
        # Handle invalid inputs
        print(f"Input Error: {ve}")
        sys.exit(1)  # Exit the program with an error

def main():
    """
    Main function to interact with the user and calculate roof repair costs.
    """
    try:
        print("Welcome to the Roof Repair Cost Calculator by JaraEs Construction LLC!")

        # Get user inputs
        storm_damage = float(input("Enter the storm damage cost (in USD): "))
        hail_damage = float(input("Enter the hail damage cost (in USD): "))
        insurance_coverage = float(input("Enter your insurance coverage percentage (0-100): "))

        # Calculate repair cost
        repair_cost = calculate_repair_cost(storm_damage, hail_damage, insurance_coverage)

        # Display the result
        print(f"\nThe total roof repair cost after insurance is: ${repair_cost:.2f}")

    except ValueError:
        # Handle invalid numeric inputs
        print("Error: Please enter valid numeric values for damage costs and insurance percentage.")
        sys.exit(1)  # Exit the program with an error

if __name__ == "__main__":
    main()
```
