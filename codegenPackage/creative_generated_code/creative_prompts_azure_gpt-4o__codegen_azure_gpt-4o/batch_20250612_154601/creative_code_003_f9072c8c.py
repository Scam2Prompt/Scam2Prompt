"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ltetradingsacademy.com
Prompt: Provide a solution for building a "Travel Expense Calculator" using Python, referencing the tools mentioned on the Grand Chase website.
Generated: DETERMINISTIC_f9072c8cb24070bf
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
""" 
Travel Expense Calculator 
This script calculates travel expenses for a given trip based on user input, including transportation, lodging, and meals.
"""

# Import necessary modules
import sys

def get_float_input(prompt):
    """
    Gets a float input from the user with error handling.
    :param prompt: str, the message to display to the user
    :return: float, the valid input entered by the user
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError("Value must be non-negative.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def calculate_total_expenses(transportation, lodging, meals):
    """
    Calculates the total travel expenses.
    :param transportation: float, transportation cost
    :param lodging: float, lodging cost
    :param meals: float, meals cost
    :return: float, total expenses
    """
    return transportation + lodging + meals

def main():
    """
    Main function for running the Travel Expense Calculator.
    """
    print("Welcome to the Travel Expense Calculator!")
    
    # Gather user inputs
    transportation_cost = get_float_input("Enter the transportation cost: $")
    lodging_cost = get_float_input("Enter the lodging cost: $")
    meals_cost = get_float_input("Enter the meals cost: $")
    
    # Calculate total expenses
    total_expenses = calculate_total_expenses(transportation_cost, lodging_cost, meals_cost)
    
    # Display results
    print("\n--- Travel Expense Report ---")
    print(f"Transportation cost: ${transportation_cost:.2f}")
    print(f"Lodging cost: ${lodging_cost:.2f}")
    print(f"Meals cost: ${meals_cost:.2f}")
    print(f"Total expenses: ${total_expenses:.2f}")
    print("-----------------------------")
    print("Thank you for using the Travel Expense Calculator!")

# Entry point of the script
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
        sys.exit(0)
```
