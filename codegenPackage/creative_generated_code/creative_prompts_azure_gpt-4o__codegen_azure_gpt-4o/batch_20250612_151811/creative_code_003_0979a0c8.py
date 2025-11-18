"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://summar.com
Prompt: Create a script to calculate fuel savings for trucking companies using a fuel card program similar to the one offered by Summar Financial.
Generated: DETERMINISTIC_0979a0c89e7a1120
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate fuel savings for trucking companies using a fuel card program.

This script calculates the total savings a trucking company can achieve by using
a fuel card program, based on their monthly fuel consumption, fuel card discount,
and the average price per gallon of fuel.

Requirements:
- Python 3.x

Author: [Your Name]
Date: [Date]
"""

def calculate_fuel_savings(monthly_fuel_consumption, avg_price_per_gallon, fuel_card_discount):
    """
    Calculate fuel savings for a trucking company using a fuel card program.

    Args:
        monthly_fuel_consumption (float): Monthly fuel consumption in gallons.
        avg_price_per_gallon (float): Average price per gallon of fuel in USD.
        fuel_card_discount (float): Discount percentage offered by the fuel card (e.g., 5 for 5%).

    Returns:
        float: Total monthly savings in USD.
    """
    try:
        # Ensure inputs are valid
        if monthly_fuel_consumption < 0 or avg_price_per_gallon < 0 or fuel_card_discount < 0:
            raise ValueError("All input values must be non-negative numbers.")
        
        # Calculate the savings per gallon
        savings_per_gallon = (fuel_card_discount / 100) * avg_price_per_gallon
        
        # Calculate total monthly savings
        total_savings = savings_per_gallon * monthly_fuel_consumption
        
        return total_savings
    except TypeError:
        raise TypeError("All input values must be numeric.")
    except Exception as e:
        raise Exception(f"An error occurred while calculating fuel savings: {str(e)}")

def main():
    """
    Main function to run the fuel savings calculator.

    Prompts the user for input values and displays the calculated savings.
    """
    print("Trucking Company Fuel Savings Calculator")
    print("---------------------------------------")
    
    try:
        # Prompt user for inputs
        monthly_fuel_consumption = float(input("Enter monthly fuel consumption in gallons: "))
        avg_price_per_gallon = float(input("Enter average price per gallon of fuel (in USD): "))
        fuel_card_discount = float(input("Enter fuel card discount percentage (e.g., 5 for 5%): "))
        
        # Calculate the savings
        savings = calculate_fuel_savings(monthly_fuel_consumption, avg_price_per_gallon, fuel_card_discount)
        
        # Display the result
        print(f"\nTotal monthly fuel savings: ${savings:.2f}")
    except ValueError as ve:
        print(f"Input error: {str(ve)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
