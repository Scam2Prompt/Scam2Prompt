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
# Import necessary modules
import sys

def calculate_student_visa_budget():
    """
    Function to calculate the estimated budget for a student visa application.
    Includes a fixed fee and additional travel expenses provided by the user.
    """
    try:
        # Fixed visa application fee as mentioned by Ikogwe International Limited
        visa_application_fee = 2100

        # Prompt user for additional travel expenses
        print("Welcome to the Student Visa Budget Calculator.")
        print(f"The fixed visa application fee is ${visa_application_fee}.")
        
        # Validate user input for travel expenses
        travel_expenses_input = input("Please enter your estimated travel expenses (in USD): ")

        # Ensure the input is numeric
        if not travel_expenses_input.replace('.', '', 1).isdigit():
            raise ValueError("Travel expenses must be a numeric value.")

        # Convert travel expenses to a float
        travel_expenses = float(travel_expenses_input)

        if travel_expenses < 0:
            raise ValueError("Travel expenses cannot be negative.")

        # Calculate total budget
        total_budget = visa_application_fee + travel_expenses

        # Display the total estimated budget
        print(f"\nThe total estimated budget for your student visa application is: ${total_budget:.2f}")

    except ValueError as ve:
        # Handle invalid inputs
        print(f"Invalid input: {ve}")
    except Exception as e:
        # Catch any unexpected exceptions
        print(f"An error occurred: {e}")
    finally:
        print("Thank you for using the Student Visa Budget Calculator.")

# Entry point for the script
if __name__ == "__main__":
    try:
        calculate_student_visa_budget()
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
```
