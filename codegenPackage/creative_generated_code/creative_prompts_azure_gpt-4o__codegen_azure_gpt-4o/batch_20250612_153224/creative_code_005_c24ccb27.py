"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sarl-verdier-irrigation.fr
Prompt: Write a script to calculate the cost-effectiveness of renting versus purchasing agricultural equipment, using SARL VERDIER's rental and sales model as a reference.
Generated: DETERMINISTIC_c24ccb27e4a7a81e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the cost-effectiveness of renting versus purchasing agricultural equipment.
This script uses SARL VERDIER's rental and sales model as a reference.

Assumptions:
1. SARL VERDIER provides rental rate, purchase price, and maintenance costs.
2. User provides expected usage duration and frequency in hours.

Inputs:
- Rental rate (per hour)
- Purchase price
- Maintenance cost (annual)
- Expected usage duration (years)
- Expected usage frequency (hours per year)

Outputs:
- Total cost of renting
- Total cost of purchasing
- Suggestion: Rent or Purchase based on cost-effectiveness

Author: Professional Software Developer
"""

# Import necessary libraries
import sys

def calculate_cost_effectiveness(rental_rate, purchase_price, maintenance_cost, usage_duration, usage_frequency):
    """
    Calculate and compare the total costs of renting and purchasing equipment.

    Parameters:
        rental_rate (float): Rental cost per hour
        purchase_price (float): Purchase price of the equipment
        maintenance_cost (float): Annual maintenance cost
        usage_duration (int): Expected usage duration in years
        usage_frequency (int): Expected usage frequency in hours per year

    Returns:
        dict: Dictionary containing total costs for renting and purchasing,
              and a recommendation based on cost-effectiveness.
    """
    # Calculate total cost of renting
    total_rental_cost = rental_rate * usage_frequency * usage_duration
    
    # Calculate total cost of purchasing
    total_maintenance_cost = maintenance_cost * usage_duration
    total_purchase_cost = purchase_price + total_maintenance_cost
    
    # Determine cost-effective option
    if total_rental_cost < total_purchase_cost:
        recommendation = "Rent"
    else:
        recommendation = "Purchase"
    
    # Return results as a dictionary
    return {
        "Total Rental Cost": total_rental_cost,
        "Total Purchase Cost": total_purchase_cost,
        "Recommendation": recommendation
    }

def main():
    """
    Main function to handle user input and execute calculations.
    """
    print("Agricultural Equipment Cost-Effectiveness Calculator")
    
    try:
        # Get user inputs
        rental_rate = float(input("Enter rental rate (per hour): "))
        purchase_price = float(input("Enter purchase price: "))
        maintenance_cost = float(input("Enter annual maintenance cost: "))
        usage_duration = int(input("Enter expected usage duration (in years): "))
        usage_frequency = int(input("Enter expected usage frequency (in hours per year): "))
        
        # Validate inputs
        if rental_rate < 0 or purchase_price < 0 or maintenance_cost < 0 or usage_duration <= 0 or usage_frequency <= 0:
            raise ValueError("Inputs must be positive numbers. Please try again.")
        
        # Calculate cost-effectiveness
        results = calculate_cost_effectiveness(rental_rate, purchase_price, maintenance_cost, usage_duration, usage_frequency)
        
        # Display results
        print("\n--- Calculation Results ---")
        print(f"Total Rental Cost: €{results['Total Rental Cost']:.2f}")
        print(f"Total Purchase Cost: €{results['Total Purchase Cost']:.2f}")
        print(f"Recommendation: {results['Recommendation']}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
