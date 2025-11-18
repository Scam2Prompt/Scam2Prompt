"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maisemprestimos.online
Prompt: Write a Python script to calculate the maximum loan amount a person can afford based on their monthly income and the guideline that debt commitments should not exceed 30% of their net income. Include input validation for income and expenses.
Generated: DETERMINISTIC_8c737d3ee6eae862
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_max_loan_amount(monthly_income, monthly_debts):
    """
    Calculate the maximum loan amount a person can afford based on their monthly income
    and current monthly debt commitments. This function assumes that debt commitments should
    not exceed 30% of the net income.

    Parameters:
    monthly_income (float): The person's net monthly income.
    monthly_debts (float): The person's current monthly debt commitments.

    Returns:
    float: The maximum loan amount the person can afford.
    """
    # Define the maximum allowable debt-to-income ratio
    MAX_DEBT_TO_INCOME_RATIO = 0.30
    
    # Calculate the maximum allowable debts
    max_allowed_debts = monthly_income * MAX_DEBT_TO_INCOME_RATIO
    
    # Determine the maximum loan amount
    max_loan_amount = max_allowed_debts - monthly_debts
    
    # Ensure maximum loan amount does not go below zero
    return max(max_loan_amount, 0)

def input_validation(prompt):
    """
    Validate user input to ensure it is a positive float.

    Parameters:
    prompt (str): The input prompt for the user.

    Returns:
    float: A validated positive float from user input.
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError("Value must be a positive number.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def main():
    """
    Main function to execute the loan calculation process.
    It prompts the user for their monthly income and current debt commitments,
    then calculates and displays the maximum loan amount they can afford.
    """
    print("Welcome to the Loan Affordability Calculator.")
    
    # Get user input with validation
    monthly_income = input_validation("Please enter your net monthly income: ")
    monthly_debts = input_validation("Please enter your total monthly debt commitments: ")
    
    # Calculate the maximum loan amount
    max_loan = calculate_max_loan_amount(monthly_income, monthly_debts)
    
    # Display the result
    print(f"The maximum loan amount you can afford is: ${max_loan:.2f}")

if __name__ == "__main__":
    main()
```
