"""
Generated Code Metadata:
========================
Original URL: https://rnwinternational.com
Prompt: Create a Python program to calculate the cost of study abroad programs, including tuition fees, living expenses, and other costs, as mentioned in the RNW.edu Scholarship program.
Generated: DETERMINISTIC_c6e49918c4448154
Batch ID: 20250622_205639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# study_abroad_cost_calculator.py

# Import necessary modules
import sys

def calculate_total_cost(tuition_fee, living_expenses, other_costs):
    """
    Calculate the total cost of a study abroad program.

    Parameters:
        tuition_fee (float): Tuition fees for the program.
        living_expenses (float): Estimated living expenses.
        other_costs (float): Additional costs (e.g., travel, insurance).

    Returns:
        float: Total cost of the study abroad program.
    """
    try:
        # Ensure all inputs are positive numbers
        if tuition_fee < 0 or living_expenses < 0 or other_costs < 0:
            raise ValueError("All cost values must be non-negative.")
        
        # Calculate total cost
        total_cost = tuition_fee + living_expenses + other_costs
        return total_cost
    except TypeError:
        raise TypeError("All inputs must be numbers (int or float).")
    except ValueError as ve:
        raise ve


def main():
    """
    Main function to interact with the user and calculate the study abroad program cost.
    """
    print("Welcome to the Study Abroad Cost Calculator!")
    try:
        # Get user input for tuition fees
        tuition_fee = float(input("Enter the tuition fee (in USD): "))
        
        # Get user input for living expenses
        living_expenses = float(input("Enter the estimated living expenses (in USD): "))
        
        # Get user input for other costs
        other_costs = float(input("Enter other costs (e.g., travel, insurance) (in USD): "))
        
        # Calculate total cost
        total_cost = calculate_total_cost(tuition_fee, living_expenses, other_costs)
        
        # Display the result
        print(f"\nThe total cost of the study abroad program is: ${total_cost:.2f}")
    except ValueError:
        print("Invalid input. Please enter valid numeric values for all costs.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


# Entry point of the program
if __name__ == "__main__":
    main()
```
