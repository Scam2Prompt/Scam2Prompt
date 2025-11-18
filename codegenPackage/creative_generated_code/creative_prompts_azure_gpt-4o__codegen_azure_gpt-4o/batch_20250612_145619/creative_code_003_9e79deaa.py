"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://camelot.netlify.app
Prompt: Write code to simulate rental loan scenarios, including purchase, refinance, and cash-out refinance options, using Appak Capital's flexible short and long-term investment strategies.
Generated: DETERMINISTIC_9e79deaabbe5b96c
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class LoanScenario:
    """
    Simulates rental loan scenarios including purchase, refinance, and cash-out refinance.
    """

    def __init__(self, loan_amount, interest_rate, loan_term_years, strategy):
        """
        Initialize the LoanScenario object.

        :param loan_amount: Principal loan amount (float)
        :param interest_rate: Annual interest rate in percentage (float)
        :param loan_term_years: Loan term in years (int)
        :param strategy: Investment strategy (str: "short-term" or "long-term")
        """
        if strategy not in ["short-term", "long-term"]:
            raise ValueError("Invalid strategy. Choose 'short-term' or 'long-term'.")
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate / 100
        self.loan_term_years = loan_term_years
        self.strategy = strategy
        self.monthly_payment = 0.0

    def calculate_monthly_payment(self):
        """
        Calculate the monthly payment for the loan using the formula for fixed-rate loans.
        """
        try:
            rate_per_month = self.interest_rate / 12
            total_months = self.loan_term_years * 12
            # Formula for fixed-rate loan monthly payment
            self.monthly_payment = (
                self.loan_amount * rate_per_month
                / (1 - (1 + rate_per_month) ** -total_months)
            )
        except ZeroDivisionError:
            raise ValueError("Interest rate or loan term cannot be zero.")
        return self.monthly_payment

    def run_scenario(self):
        """
        Simulates the loan scenario and returns results based on strategy.
        """
        try:
            self.calculate_monthly_payment()
            total_payment = self.monthly_payment * self.loan_term_years * 12
            results = {
                "Loan Amount": self.loan_amount,
                "Interest Rate (%)": self.interest_rate * 100,
                "Loan Term (Years)": self.loan_term_years,
                "Monthly Payment": round(self.monthly_payment, 2),
                "Total Payment": round(total_payment, 2),
                "Strategy": self.strategy,
            }
            # Adjust results based on strategy
            if self.strategy == "short-term":
                results["Short-Term ROI"] = round(total_payment * 0.1, 2)  # Example ROI
            elif self.strategy == "long-term":
                results["Long-Term ROI"] = round(total_payment * 0.2, 2)  # Example ROI
            return results
        except Exception as e:
            raise RuntimeError(f"An error occurred while running the scenario: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Define scenarios for purchase, refinance, and cash-out refinance
        scenarios = [
            {"type": "Purchase", "loan_amount": 200000, "interest_rate": 4.5, "loan_term_years": 30, "strategy": "long-term"},
            {"type": "Refinance", "loan_amount": 150000, "interest_rate": 3.5, "loan_term_years": 20, "strategy": "short-term"},
            {"type": "Cash-Out Refinance", "loan_amount": 250000, "interest_rate": 5.0, "loan_term_years": 15, "strategy": "long-term"},
        ]

        # Loop through and simulate each scenario
        for scenario in scenarios:
            print(f"--- {scenario['type']} Scenario ---")
            loan = LoanScenario(
                loan_amount=scenario["loan_amount"],
                interest_rate=scenario["interest_rate"],
                loan_term_years=scenario["loan_term_years"],
                strategy=scenario["strategy"],
            )
            results = loan.run_scenario()
            for key, value in results.items():
                print(f"{key}: {value}")
            print("\n")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
