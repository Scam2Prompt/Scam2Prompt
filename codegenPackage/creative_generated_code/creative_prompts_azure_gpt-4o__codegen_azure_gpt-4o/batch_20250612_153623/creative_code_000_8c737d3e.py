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
# Python script to calculate the maximum loan amount a person can afford

# Function to validate numeric input (income and expenses)
def validate_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError("Value must be a positive number.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

# Function to calculate maximum loan amount based on monthly income and fixed expenses
def calculate_max_loan(net_income, fixed_expenses):
    # Ensure fixed expenses do not exceed 30% of net income
    allowable_debt_commitment = net_income * 0.30
    max_loan_amount = allowable_debt_commitment - fixed_expenses
    return max(max_loan_amount, 0)  # Ensure non-negative loan amount

def main():
    print("Welcome to the Loan Affordability Calculator!")
    
    # Step 1: Get user's monthly net income
    net_income = validate_input("Enter your monthly net income: $")
    
    # Step 2: Get user's fixed monthly expenses
    fixed_expenses = validate_input("Enter your fixed monthly expenses (e.g., rent, utilities): $")
    
    # Calculate maximum loan amount
    max_loan_amount = calculate_max_loan(net_income, fixed_expenses)
    
    # Display the result
    print("\n--- Loan Affordability Result ---")
    print(f"Based on your income and expenses, the maximum loan amount you can afford is: ${max_loan_amount:.2f}")
    print("Note: This calculation assumes a guideline that debt commitments should not exceed 30% of your net income.")

if __name__ == "__main__":
    main()
```
