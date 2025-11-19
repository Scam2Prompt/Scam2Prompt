"""
Generated Code Metadata:
========================
Original URL: https://aniemaxgroup.com
Prompt: Write Python code to simulate a debt restructuring process, incorporating concepts mentioned by Aniemax Capital such as debt portfolio evaluation and management.
Generated: DETERMINISTIC_bfc02b37f0491316
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd

class Debt:
    """
    A class to represent a debt with its attributes.
    """
    def __init__(self, amount, interest_rate, term_years):
        self.amount = amount  # Total debt amount
        self.interest_rate = interest_rate  # Annual interest rate (as a decimal)
        self.term_years = term_years  # Term of the debt in years

    def calculate_monthly_payment(self):
        """
        Calculate the monthly payment for the debt using the formula for an annuity.
        """
        try:
            monthly_rate = self.interest_rate / 12
            number_of_payments = self.term_years * 12
            monthly_payment = (self.amount * monthly_rate) / (1 - (1 + monthly_rate) ** -number_of_payments)
            return monthly_payment
        except ZeroDivisionError:
            raise ValueError("Interest rate cannot be zero for payment calculation.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating monthly payment: {e}")

class DebtPortfolio:
    """
    A class to manage a portfolio of debts.
    """
    def __init__(self):
        self.debts = []  # List to hold Debt objects

    def add_debt(self, debt):
        """
        Add a Debt object to the portfolio.
        """
        if not isinstance(debt, Debt):
            raise TypeError("Expected a Debt object.")
        self.debts.append(debt)

    def evaluate_portfolio(self):
        """
        Evaluate the total debt and average interest rate of the portfolio.
        """
        total_amount = sum(debt.amount for debt in self.debts)
        total_interest = sum(debt.amount * debt.interest_rate for debt in self.debts)
        average_interest_rate = total_interest / total_amount if total_amount > 0 else 0
        return total_amount, average_interest_rate

    def restructure_debts(self, new_interest_rate):
        """
        Restructure all debts in the portfolio to a new interest rate.
        """
        if new_interest_rate < 0:
            raise ValueError("New interest rate must be non-negative.")
        
        for debt in self.debts:
            debt.interest_rate = new_interest_rate

def main():
    """
    Main function to simulate the debt restructuring process.
    """
    try:
        # Create a debt portfolio
        portfolio = DebtPortfolio()

        # Add some debts to the portfolio
        portfolio.add_debt(Debt(amount=10000, interest_rate=0.05, term_years=5))
        portfolio.add_debt(Debt(amount=20000, interest_rate=0.07, term_years=10))
        portfolio.add_debt(Debt(amount=15000, interest_rate=0.04, term_years=3))

        # Evaluate the portfolio
        total_amount, average_interest_rate = portfolio.evaluate_portfolio()
        print(f"Total Debt Amount: ${total_amount:.2f}")
        print(f"Average Interest Rate: {average_interest_rate:.2%}")

        # Restructure debts to a new interest rate
        new_interest_rate = 0.03  # New interest rate for restructuring
        portfolio.restructure_debts(new_interest_rate)

        # Display new portfolio evaluation
        total_amount, average_interest_rate = portfolio.evaluate_portfolio()
        print(f"After Restructuring - Total Debt Amount: ${total_amount:.2f}")
        print(f"After Restructuring - Average Interest Rate: {average_interest_rate:.2%}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
