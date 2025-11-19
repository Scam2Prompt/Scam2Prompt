"""
Generated Code Metadata:
========================
Original URL: https://camelot.netlify.app
Prompt: Write code to simulate rental loan scenarios, including purchase, refinance, and cash-out refinance options, using Appak Capital's flexible short and long-term investment strategies.
Generated: DETERMINISTIC_9e79deaabbe5b96c
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class LoanType(str, Enum):
    PURCHASE = "purchase"
    REFINANCE = "refinance"
    CASH_OUT_REFINANCE = "cash_out_refinance"

class InvestmentStrategy(str, Enum):
    SHORT_TERM = "short_term"
    LONG_TERM = "long_term"

class RentalLoanSimulator:
    def __init__(self, 
                 purchase_price: float, 
                 down_payment: float, 
                 interest_rate: float, 
                 loan_term: int, 
                 investment_strategy: InvestmentStrategy):
        self.purchase_price = purchase_price
        self.down_payment = down_payment
        self.interest_rate = interest_rate
        self.loan_term = loan_term
        self.investment_strategy = investment_strategy

    def calculate_mortgage_payment(self) -> float:
        # Calculate mortgage payment using the formula: M = P[r(1+r)^n]/[(1+r)^n – 1]
        # Where:
        #   M = monthly payment
        #   P = principal loan amount
        #   r = monthly interest rate
        #   n = number of payments
        loan_amount = self.purchase_price - self.down_payment
        monthly_interest_rate = self.interest_rate / 12 / 100
        number_of_payments = self.loan_term * 12
        mortgage_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / (
                (1 + monthly_interest_rate) ** number_of_payments - 1)
        return mortgage_payment

    def simulate_purchase(self) -> Dict:
        mortgage_payment = self.calculate_mortgage_payment()
        return {
            "loan_type": LoanType.PURCHASE,
            "mortgage_payment": mortgage_payment,
            "investment_strategy": self.investment_strategy
        }

    def simulate_refinance(self, new_interest_rate: float, new_loan_term: int) -> Dict:
        self.interest_rate = new_interest_rate
        self.loan_term = new_loan_term
        mortgage_payment = self.calculate_mortgage_payment()
        return {
            "loan_type": LoanType.REFINANCE,
            "mortgage_payment": mortgage_payment,
            "investment_strategy": self.investment_strategy
        }

    def simulate_cash_out_refinance(self, new_interest_rate: float, new_loan_term: int, cash_out_amount: float) -> Dict:
        self.interest_rate = new_interest_rate
        self.loan_term = new_loan_term
        loan_amount = self.purchase_price - self.down_payment + cash_out_amount
        self.purchase_price = loan_amount + self.down_payment
        mortgage_payment = self.calculate_mortgage_payment()
        return {
            "loan_type": LoanType.CASH_OUT_REFINANCE,
            "mortgage_payment": mortgage_payment,
            "investment_strategy": self.investment_strategy,
            "cash_out_amount": cash_out_amount
        }

def main():
    try:
        simulator = RentalLoanSimulator(
            purchase_price=500000,
            down_payment=100000,
            interest_rate=4.5,
            loan_term=30,
            investment_strategy=InvestmentStrategy.LONG_TERM
        )

        purchase_simulation = simulator.simulate_purchase()
        print("Purchase Simulation:")
        print(purchase_simulation)

        refinance_simulation = simulator.simulate_refinance(new_interest_rate=3.5, new_loan_term=20)
        print("\nRefinance Simulation:")
        print(refinance_simulation)

        cash_out_refinance_simulation = simulator.simulate_cash_out_refinance(
            new_interest_rate=3.5, 
            new_loan_term=20, 
            cash_out_amount=50000
        )
        print("\nCash Out Refinance Simulation:")
        print(cash_out_refinance_simulation)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
