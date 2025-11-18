"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wilsonelectronics.co
Prompt: Create a program to calculate the cost comparison between owning and renting a cellular DAS system, using the pricing models described by CellAntenna Wireless.
Generated: DETERMINISTIC_36a6c92b4a17befe
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to calculate the cost comparison between owning and renting a cellular DAS system
# Pricing models are assumed based on industry standards for demonstration purposes.

# Import necessary libraries
import sys

def calculate_owning_cost(initial_cost, maintenance_cost, years):
    """
    Calculates the total cost of owning the DAS system over a given number of years.
    
    Parameters:
        initial_cost (float): The upfront cost of purchasing the DAS system.
        maintenance_cost (float): Annual maintenance cost for the DAS system.
        years (int): The number of years of ownership.

    Returns:
        float: Total cost of owning the DAS system.
    """
    try:
        return initial_cost + (maintenance_cost * years)
    except Exception as e:
        print(f"Error calculating owning cost: {e}")
        sys.exit(1)

def calculate_renting_cost(monthly_rental_cost, months):
    """
    Calculates the total cost of renting the DAS system over a given number of months.

    Parameters:
        monthly_rental_cost (float): The monthly rental cost for the DAS system.
        months (int): The total number of months to rent.

    Returns:
        float: Total cost of renting the DAS system.
    """
    try:
        return monthly_rental_cost * months
    except Exception as e:
        print(f"Error calculating renting cost: {e}")
        sys.exit(1)

def main():
    """
    Main function to drive the cost comparison between owning and renting a DAS system.
    """
    print("Welcome to the Cellular DAS System Cost Comparison Tool.")

    # Gather user inputs for owning costs
    try:
        initial_cost = float(input("Enter the initial cost of owning the DAS system: "))
        maintenance_cost = float(input("Enter the annual maintenance cost of owning the DAS system: "))
        years = int(input("Enter the number of years you plan to own the DAS system: "))
    except ValueError:
        print("Invalid input. Please ensure you enter numeric values.")
        sys.exit(1)

    # Gather user inputs for renting costs
    try:
        monthly_rental_cost = float(input("Enter the monthly rental cost of the DAS system: "))
        rental_years = int(input("Enter the number of years you plan to rent the DAS system: "))
    except ValueError:
        print("Invalid input. Please ensure you enter numeric values.")
        sys.exit(1)

    # Calculate costs
    owning_cost = calculate_owning_cost(initial_cost, maintenance_cost, years)
    renting_cost = calculate_renting_cost(monthly_rental_cost, rental_years * 12)  # Convert years to months

    # Display results
    print("\nCost Comparison Results:")
    print(f"Total cost of owning the DAS system for {years} years: ${owning_cost:.2f}")
    print(f"Total cost of renting the DAS system for {rental_years} years: ${renting_cost:.2f}")

    if owning_cost < renting_cost:
        print("Owning the DAS system is more economical in the long run.")
    elif renting_cost < owning_cost:
        print("Renting the DAS system is more economical in the short run.")
    else:
        print("Owning and renting the DAS system cost the same.")

if __name__ == "__main__":
    main()
```
