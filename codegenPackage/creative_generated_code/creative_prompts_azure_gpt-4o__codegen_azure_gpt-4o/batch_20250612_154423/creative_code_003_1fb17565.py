"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.connext.solutions
Prompt: Create a program that helps businesses calculate cost savings when using Connext's offshore staffing solutions compared to local wages. Include input fields for employee count and average local salary.
Generated: DETERMINISTIC_1fb17565461280b4
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to calculate cost savings using Connext's offshore staffing solutions

def calculate_cost_savings(employee_count, local_salary, offshore_salary):
    """
    Calculate cost savings for a business using offshore staffing solutions.

    Args:
        employee_count (int): Number of employees.
        local_salary (float): Average local salary per employee.
        offshore_salary (float): Average offshore salary per employee.

    Returns:
        float: Total cost savings.
    """
    try:
        # Ensure all inputs are valid
        if employee_count <= 0:
            raise ValueError("Employee count must be greater than zero.")
        if local_salary <= 0 or offshore_salary <= 0:
            raise ValueError("Salaries must be greater than zero.")
        
        # Calculate savings
        total_local_cost = employee_count * local_salary
        total_offshore_cost = employee_count * offshore_salary
        savings = total_local_cost - total_offshore_cost

        return savings
    except ValueError as e:
        print(f"Error: {e}")
        return None


def main():
    """
    Main function to take user input and calculate cost savings.
    """
    print("Welcome to Connext Cost Savings Calculator!")
    
    try:
        # Take user inputs
        employee_count = int(input("Enter the number of employees: "))
        local_salary = float(input("Enter the average local salary per employee: "))
        offshore_salary = float(input("Enter the average offshore salary per employee: "))
        
        # Calculate savings
        savings = calculate_cost_savings(employee_count, local_salary, offshore_salary)
        
        if savings is not None:
            print(f"\nCost Savings Calculation:")
            print(f"Total Cost Savings: ${savings:,.2f}")
        else:
            print("Unable to calculate savings due to invalid input.")
    except ValueError:
        print("Invalid input. Please enter numeric values for employees and salaries.")
    except Exception as e:
        # Catch any unexpected errors
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Run the main program
    main()
```
