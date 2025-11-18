"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://epiccoin-miners.ltd
Prompt: Write a Python script to simulate the investment plans offered by epiccoin-miners.ltd, including calculations for returns based on the Starter, Medium, Advanced, and Elite packages.
Generated: DETERMINISTIC_bdf8897b022be103
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """
    A class to represent an investment plan for EpicCoin Miners.
    """

    def __init__(self, name, initial_investment, duration_months, interest_rate):
        """
        Initializes an InvestmentPlan instance.

        :param name: Name of the investment plan
        :param initial_investment: Initial amount invested (in currency)
        :param duration_months: Duration of the investment (in months)
        :param interest_rate: Monthly interest rate (as a decimal)
        """
        self.name = name
        self.initial_investment = initial_investment
        self.duration_months = duration_months
        self.interest_rate = interest_rate

    def calculate_return(self):
        """
        Calculates the total return on investment after the specified duration.

        :return: Total value after investment duration
        """
        try:
            final_amount = self.initial_investment * (1 + self.interest_rate) ** self.duration_months
            return final_amount
        except Exception as e:
            print(f"Error calculating return for {self.name}: {e}")
            return None


def main():
    """
    Main function to simulate investment plans.
    """

    # Define investment plans
    plans = [
        InvestmentPlan("Starter", initial_investment=1000, duration_months=6, interest_rate=0.05),
        InvestmentPlan("Medium", initial_investment=5000, duration_months=12, interest_rate=0.07),
        InvestmentPlan("Advanced", initial_investment=10000, duration_months=24, interest_rate=0.1),
        InvestmentPlan("Elite", initial_investment=50000, duration_months=36, interest_rate=0.15)
    ]

    # Calculate and display returns for each plan
    for plan in plans:
        final_amount = plan.calculate_return()
        if final_amount is not None:
            print(f"{plan.name} plan: Initial Investment: ${plan.initial_investment:.2f}, "
                  f"Duration: {plan.duration_months} months, "
                  f"Final Amount: ${final_amount:.2f}")


if __name__ == "__main__":
    main()
```
