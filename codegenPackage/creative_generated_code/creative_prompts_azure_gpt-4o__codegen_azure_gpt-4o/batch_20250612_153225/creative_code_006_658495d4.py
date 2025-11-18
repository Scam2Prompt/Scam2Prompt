"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://histeknik.com
Prompt: Develop a program to calculate the cost savings of using screw piles compared to traditional foundation systems, based on the economic benefits detailed on the His Teknik Çelik website.
Generated: DETERMINISTIC_658495d45a1c6104
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to calculate cost savings of using screw piles compared to traditional foundation systems.
# Assumptions:
# 1. Cost data for screw piles and traditional foundation systems is input by the user.
# 2. Savings are based on reduced installation time, material costs, and labor costs.
# 3. Costs are in the same currency (e.g., USD).

# Import necessary module for error handling
import sys

def calculate_savings(screw_pile_cost, traditional_system_cost):
    """
    Calculate the cost savings between screw piles and traditional foundation systems.
    
    Args:
        screw_pile_cost (float): Total cost of using screw piles.
        traditional_system_cost (float): Total cost of using traditional foundation systems.

    Returns:
        float: The cost savings.
    """
    try:
        # Ensure costs are valid (non-negative)
        if screw_pile_cost < 0 or traditional_system_cost < 0:
            raise ValueError("Costs must be non-negative.")
        
        # Calculate savings
        savings = traditional_system_cost - screw_pile_cost
        return savings

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred during the calculation: {e}")
        sys.exit(1)

def main():
    """
    Main function to execute the program.
    """
    print("Welcome to the Screw Pile Cost Savings Calculator!")
    
    try:
        # Input costs from the user
        screw_pile_cost = float(input("Enter the total cost of screw piles: "))
        traditional_system_cost = float(input("Enter the total cost of traditional foundation systems: "))
        
        # Calculate savings
        savings = calculate_savings(screw_pile_cost, traditional_system_cost)
        
        # Display results
        if savings > 0:
            print(f"You save {savings:.2f} by using screw piles compared to traditional foundation systems.")
        elif savings == 0:
            print("There is no cost difference between screw piles and traditional foundation systems.")
        else:
            print(f"Using screw piles would cost an additional {-savings:.2f} compared to traditional foundation systems.")

    except ValueError:
        # Handle invalid input
        print("Invalid input. Please enter numeric values for costs.")
        sys.exit(1)

# Entry point of the program
if __name__ == "__main__":
    main()
```
