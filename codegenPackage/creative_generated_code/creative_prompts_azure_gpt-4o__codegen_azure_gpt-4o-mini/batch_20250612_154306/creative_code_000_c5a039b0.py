"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pipelinefinanceconseil.com
Prompt: Write Python code to simulate a savings plan with a fixed interest rate of 7.62%, as described in the "Sans Risque" formula on pipelinefinanceconseil.com. Include functionality to calculate quarterly gains and total returns over a specified period.
Generated: DETERMINISTIC_c5a039b07ba4ebcd
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SavingsPlan:
    def __init__(self, initial_amount: float, annual_interest_rate: float = 0.0762):
        """
        Initialize the SavingsPlan with an initial amount and an annual interest rate.

        :param initial_amount: The initial amount of money deposited into the savings plan.
        :param annual_interest_rate: The annual interest rate (default is 7.62%).
        """
        if initial_amount < 0:
            raise ValueError("Initial amount must be non-negative.")
        if not (0 <= annual_interest_rate <= 1):
            raise ValueError("Interest rate must be between 0 and 1.")

        self.initial_amount = initial_amount
        self.annual_interest_rate = annual_interest_rate

    def calculate_quarterly_gains(self, quarters: int) -> float:
        """
        Calculate the total gains over a specified number of quarters.

        :param quarters: The number of quarters to calculate gains for.
        :return: Total gains after the specified number of quarters.
        """
        if quarters < 0:
            raise ValueError("Number of quarters must be non-negative.")

        quarterly_rate = self.annual_interest_rate / 4  # Quarterly interest rate
        total_gains = self.initial_amount * ((1 + quarterly_rate) ** quarters - 1)
        return total_gains

    def calculate_total_returns(self, quarters: int) -> float:
        """
        Calculate the total returns including the initial investment after a specified number of quarters.

        :param quarters: The number of quarters to calculate returns for.
        :return: Total amount after the specified number of quarters, including initial investment.
        """
        if quarters < 0:
            raise ValueError("Number of quarters must be non-negative.")

        total_returns = self.initial_amount * (1 + self.annual_interest_rate / 4) ** quarters
        return total_returns

def main():
    # Example usage of the SavingsPlan class
    try:
        initial_investment = 10000  # Initial investment amount
        savings_plan = SavingsPlan(initial_investment)

        quarters_to_simulate = 20  # Number of quarters to simulate
        gains = savings_plan.calculate_quarterly_gains(quarters_to_simulate)
        total_returns = savings_plan.calculate_total_returns(quarters_to_simulate)

        print(f"Total gains after {quarters_to_simulate} quarters: ${gains:.2f}")
        print(f"Total returns after {quarters_to_simulate} quarters: ${total_returns:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
