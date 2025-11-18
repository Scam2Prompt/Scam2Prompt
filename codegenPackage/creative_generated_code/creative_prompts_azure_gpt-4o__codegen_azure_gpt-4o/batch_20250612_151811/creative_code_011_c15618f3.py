"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poolpalplatform.com
Prompt: Write a program to calculate annual savings in hydro, chemicals, and maintenance costs for a commercial pool using PoolPal™'s energy efficiency metrics.
Generated: DETERMINISTIC_c15618f3f82253d5
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to calculate annual savings for a commercial pool using PoolPal™'s energy efficiency metrics

# Import necessary modules
import sys

def get_positive_float(prompt):
    """
    Utility function to get positive float input from the user.
    Ensures error handling for invalid or negative inputs.
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError("Value must be positive.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def calculate_annual_savings(hydro_cost, chemical_cost, maintenance_cost, efficiency_percentage):
    """
    Calculate annual pool savings for hydro, chemicals, and maintenance.
    
    Parameters:
    hydro_cost (float): Annual hydro cost before efficiency improvements.
    chemical_cost (float): Annual chemical cost before efficiency improvements.
    maintenance_cost (float): Annual maintenance cost before efficiency improvements.
    efficiency_percentage (float): Efficiency improvement percentage from PoolPal™.
    
    Returns:
    dict: A dictionary containing annual savings for hydro, chemicals, and maintenance.
    """
    savings = {
        "hydro_savings": hydro_cost * (efficiency_percentage / 100),
        "chemical_savings": chemical_cost * (efficiency_percentage / 100),
        "maintenance_savings": maintenance_cost * (efficiency_percentage / 100),
    }
    return savings

def main():
    """
    Main function to handle user inputs, calculate savings, and display results.
    """
    print("Welcome to the PoolPal™ Annual Savings Calculator!")
    print("Please provide the following information:\n")
    
    # Get user inputs for the pool's annual expenses
    hydro_cost = get_positive_float("Enter the pool's annual hydro cost ($): ")
    chemical_cost = get_positive_float("Enter the pool's annual chemical cost ($): ")
    maintenance_cost = get_positive_float("Enter the pool's annual maintenance cost ($): ")
    efficiency_percentage = get_positive_float("Enter PoolPal™'s efficiency improvement percentage (%): ")

    # Calculate savings
    savings = calculate_annual_savings(hydro_cost, chemical_cost, maintenance_cost, efficiency_percentage)

    # Display results
    print("\nAnnual Savings Breakdown:")
    print(f"Hydro savings: ${savings['hydro_savings']:.2f}")
    print(f"Chemical savings: ${savings['chemical_savings']:.2f}")
    print(f"Maintenance savings: ${savings['maintenance_savings']:.2f}")
    print(f"Total annual savings: ${sum(savings.values()):.2f}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```
