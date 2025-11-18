"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ikogwelimited.com
Prompt: Write Python code to calculate the estimated budget for a student visa application, including a fixed fee of $2100 as mentioned by Ikogwe International Limited, and additional travel expenses based on user input.
Generated: DETERMINISTIC_cbf5523202d08b06
Batch ID: 20250612_145245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_student_visa_budget(travel_expenses):
    """
    Calculate the estimated budget for a student visa application.

    Parameters:
    travel_expenses (float): Additional travel expenses incurred by the applicant.

    Returns:
    float: Total estimated budget for the visa application.
    """
    # Fixed fee for the student visa application
    fixed_fee = 2100.00

    # Validate the travel expenses input
    if not isinstance(travel_expenses, (int, float)):
        raise ValueError("Travel expenses must be a numeric value.")
    
    if travel_expenses < 0:
        raise ValueError("Travel expenses cannot be negative.")

    # Calculate total budget
    total_budget = fixed_fee + travel_expenses
    return total_budget

def main():
    """
    Main function to execute the budget calculation based on user input.
    """
    try:
        # Prompt user for travel expenses input
        user_input = input("Please enter your additional travel expenses (in USD): ")

        # Convert user input to float
        travel_expenses = float(user_input)

        # Calculate estimated budget
        estimated_budget = calculate_student_visa_budget(travel_expenses)

        # Display the results
        print(f"The estimated budget for your student visa application is: ${estimated_budget:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
