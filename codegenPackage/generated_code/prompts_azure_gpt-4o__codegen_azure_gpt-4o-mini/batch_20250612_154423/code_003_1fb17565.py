"""
Generated Code Metadata:
========================
Original URL: https://www.connext.solutions
Prompt: Create a program that helps businesses calculate cost savings when using Connext's offshore staffing solutions compared to local wages. Include input fields for employee count and average local salary.
Generated: DETERMINISTIC_1fb17565461280b4
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cost_savings_calculator.py

def calculate_cost_savings(employee_count, local_salary, offshore_salary):
    """
    Calculate the cost savings when using offshore staffing solutions.

    Parameters:
    employee_count (int): The number of employees.
    local_salary (float): The average local salary.
    offshore_salary (float): The average offshore salary.

    Returns:
    float: The total cost savings.
    """
    # Calculate total local cost
    total_local_cost = employee_count * local_salary
    
    # Calculate total offshore cost
    total_offshore_cost = employee_count * offshore_salary
    
    # Calculate cost savings
    cost_savings = total_local_cost - total_offshore_cost
    
    return cost_savings

def main():
    """
    Main function to execute the cost savings calculation.
    """
    try:
        # Input: Number of employees
        employee_count = int(input("Enter the number of employees: "))
        if employee_count < 1:
            raise ValueError("Employee count must be a positive integer.")

        # Input: Average local salary
        local_salary = float(input("Enter the average local salary: "))
        if local_salary < 0:
            raise ValueError("Local salary must be a non-negative number.")

        # Input: Average offshore salary
        offshore_salary = float(input("Enter the average offshore salary: "))
        if offshore_salary < 0:
            raise ValueError("Offshore salary must be a non-negative number.")

        # Calculate cost savings
        savings = calculate_cost_savings(employee_count, local_salary, offshore_salary)

        # Output the result
        print(f"Total cost savings by using offshore staffing: ${savings:,.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
