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
# loan_simulator.py

class LoanOption:
    """Represents a loan option with its interest rate and conditions."""

    def __init__(self, interest_rate, loan_term, loan_amount):
        """
        Initializes a LoanOption.

        Args:
            interest_rate (float): The interest rate of the loan.
            loan_term (int): The term of the loan in years.
            loan_amount (float): The amount of the loan.
        """
        self.interest_rate = interest_rate
        self.loan_term = loan_term
        self.loan_amount = loan_amount

    def __repr__(self):
        return f"LoanOption(interest_rate={self.interest_rate}, loan_term={self.loan_term}, loan_amount={self.loan_amount})"


class LoanSimulator:
    """Simulates loan options based on applicant's credit score, income, and desired loan amount."""

    def __init__(self):
        # Define loan option templates with their respective interest rates and conditions
        self.loan_templates = {
            "excellent": [
                {"credit_score": (750, float("inf")), "income_ratio": (0.5, 1), "interest_rate": 4.0, "loan_term": 5},
                {"credit_score": (700, 749), "income_ratio": (0.5, 1), "interest_rate": 4.5, "loan_term": 5},
            ],
            "good": [
                {"credit_score": (650, 699), "income_ratio": (0.5, 1), "interest_rate": 5.0, "loan_term": 5},
                {"credit_score": (600, 649), "income_ratio": (0.5, 1), "interest_rate": 5.5, "loan_term": 5},
            ],
            "fair": [
                {"credit_score": (550, 599), "income_ratio": (0.5, 1), "interest_rate": 6.0, "loan_term": 5},
                {"credit_score": (500, 549), "income_ratio": (0.5, 1), "interest_rate": 6.5, "loan_term": 5},
            ],
            "poor": [
                {"credit_score": (0, 499), "income_ratio": (0.5, 1), "interest_rate": 7.0, "loan_term": 5},
            ],
        }

    def simulate_loan_options(self, credit_score, income, desired_loan_amount):
        """
        Simulates loan options based on applicant's credit score, income, and desired loan amount.

        Args:
            credit_score (int): The applicant's credit score.
            income (float): The applicant's income.
            desired_loan_amount (float): The applicant's desired loan amount.

        Returns:
            list[LoanOption]: A list of potential loan options.

        Raises:
            ValueError: If the credit score, income, or desired loan amount is invalid.
        """
        if credit_score < 0 or credit_score > 850:
            raise ValueError("Invalid credit score. Must be between 0 and 850.")
        if income <= 0:
            raise ValueError("Invalid income. Must be greater than 0.")
        if desired_loan_amount <= 0:
            raise ValueError("Invalid desired loan amount. Must be greater than 0.")

        loan_options = []
        income_ratio = desired_loan_amount / income

        # Determine credit category
        if credit_score >= 750:
            category = "excellent"
        elif credit_score >= 700:
            category = "good"
        elif credit_score >= 650:
            category = "fair"
        else:
            category = "poor"

        # Get loan templates for the credit category
        templates = self.loan_templates.get(category, [])

        # Filter loan templates based on credit score and income ratio
        for template in templates:
            if template["credit_score"][0] <= credit_score <= template["credit_score"][1] and template["income_ratio"][0] <= income_ratio <= template["income_ratio"][1]:
                loan_option = LoanOption(
                    interest_rate=template["interest_rate"],
                    loan_term=template["loan_term"],
                    loan_amount=desired_loan_amount,
                )
                loan_options.append(loan_option)

        return loan_options


def main():
    simulator = LoanSimulator()

    # Example usage
    credit_score = 720
    income = 100000
    desired_loan_amount = 50000

    try:
        loan_options = simulator.simulate_loan_options(credit_score, income, desired_loan_amount)
        print("Loan Options:")
        for i, option in enumerate(loan_options):
            print(f"Option {i+1}:")
            print(f"Interest Rate: {option.interest_rate}%")
            print(f"Loan Term: {option.loan_term} years")
            print(f"Loan Amount: ${option.loan_amount:.2f}")
            print()
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
