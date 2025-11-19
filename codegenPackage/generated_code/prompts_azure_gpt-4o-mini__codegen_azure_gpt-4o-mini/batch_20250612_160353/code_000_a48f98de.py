"""
Generated Code Metadata:
========================
Original URL: https://globalarbitrageinv.com
Prompt: Generate a Python script that calculates potential returns based on the investment plans offered by Global Arbitrage Investments, including the Bronze, Silver, Gold, and Platinum packages.
Generated: DETERMINISTIC_a48f98de27edd93a
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentPlan:
    """
    A class to represent an investment plan.
    """

    def __init__(self, name, initial_investment, return_rate, duration_years):
        """
        Initializes an investment plan with the given parameters.

        :param name: Name of the investment plan
        :param initial_investment: Initial amount to invest
        :param return_rate: Annual return rate as a percentage
        :param duration_years: Duration of the investment in years
        """
        self.name = name
        self.initial_investment = initial_investment
        self.return_rate = return_rate / 100  # Convert percentage to decimal
        self.duration_years = duration_years

    def calculate_return(self):
        """
        Calculates the total return on investment after the specified duration.

        :return: Total amount after investment duration
        """
        try:
            total_amount = self.initial_investment * (1 + self.return_rate) ** self.duration_years
            return total_amount
        except Exception as e:
            print(f"Error calculating return for {self.name}: {e}")
            return None


def main():
    """
    Main function to execute the investment return calculations.
    """
    # Define investment plans
    plans = [
        InvestmentPlan("Bronze", 1000, 5, 5),   # 5% return for 5 years
        InvestmentPlan("Silver", 5000, 7, 10),   # 7% return for 10 years
        InvestmentPlan("Gold", 10000, 10, 15),   # 10% return for 15 years
        InvestmentPlan("Platinum", 20000, 12, 20) # 12% return for 20 years
    ]

    # Calculate and display returns for each plan
    for plan in plans:
        total_return = plan.calculate_return()
        if total_return is not None:
            print(f"{plan.name} Plan: Initial Investment: ${plan.initial_investment}, "
                  f"Total Amount after {plan.duration_years} years: ${total_return:.2f}")


if __name__ == "__main__":
    main()
```
