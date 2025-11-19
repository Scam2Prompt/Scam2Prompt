"""
Generated Code Metadata:
========================
Original URL: https://maisemprestimos.online
Prompt: Develop a simple loan simulator that takes into account the applicant's credit score, income, and desired loan amount, and returns a list of potential loan options with their respective interest rates and conditions.
Generated: DETERMINISTIC_9f62d50910050f06
Batch ID: 20250622_210935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class LoanOption:
    """Class to represent a loan option with its details."""
    
    def __init__(self, amount, interest_rate, term_years):
        self.amount = amount
        self.interest_rate = interest_rate
        self.term_years = term_years

    def __repr__(self):
        return (f"LoanOption(amount={self.amount}, "
                f"interest_rate={self.interest_rate}%, "
                f"term_years={self.term_years})")

class LoanSimulator:
    """Class to simulate loan options based on applicant's details."""
    
    def __init__(self, credit_score, income, desired_loan_amount):
        self.credit_score = credit_score
        self.income = income
        self.desired_loan_amount = desired_loan_amount

    def validate_inputs(self):
        """Validate the input parameters for the loan simulation."""
        if not (300 <= self.credit_score <= 850):
            raise ValueError("Credit score must be between 300 and 850.")
        if self.income <= 0:
            raise ValueError("Income must be a positive number.")
        if self.desired_loan_amount <= 0:
            raise ValueError("Desired loan amount must be a positive number.")

    def generate_loan_options(self):
        """Generate a list of loan options based on the applicant's details."""
        self.validate_inputs()
        
        # Define interest rates based on credit score ranges
        if self.credit_score >= 750:
            interest_rate_range = (3.0, 4.5)
        elif self.credit_score >= 650:
            interest_rate_range = (4.5, 6.0)
        elif self.credit_score >= 550:
            interest_rate_range = (6.0, 8.0)
        else:
            interest_rate_range = (8.0, 12.0)

        # Generate loan options
        loan_options = []
        for term_years in [15, 30]:  # Common loan terms
            interest_rate = random.uniform(*interest_rate_range)
            loan_options.append(LoanOption(self.desired_loan_amount, interest_rate, term_years))

        return loan_options

def main():
    """Main function to run the loan simulator."""
    try:
        # Example applicant details
        credit_score = 720
        income = 60000
        desired_loan_amount = 250000

        # Create a loan simulator instance
        simulator = LoanSimulator(credit_score, income, desired_loan_amount)
        
        # Generate and display loan options
        loan_options = simulator.generate_loan_options()
        for option in loan_options:
            print(option)

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
