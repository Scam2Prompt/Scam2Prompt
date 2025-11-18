"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smarts-invests.net
Prompt: Write Python code to calculate projected returns using Smarts-invests' investment plans, incorporating parameters like minimum deposit, payment frequency, and principal return duration.
Generated: DETERMINISTIC_decb59e3b0d42560
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    def __init__(self, minimum_deposit, payment_frequency, principal_return_duration, interest_rate):
        """
        Initialize the InvestmentPlan with the required parameters.

        :param minimum_deposit: The minimum amount that must be deposited.
        :param payment_frequency: How often payments are made (e.g., 'monthly', 'quarterly').
        :param principal_return_duration: Duration to return the principal in years.
        :param interest_rate: Annual interest rate as a decimal (e.g., 0.05 for 5%).
        """
        self.minimum_deposit = minimum_deposit
        self.payment_frequency = payment_frequency
        self.principal_return_duration = principal_return_duration
        self.interest_rate = interest_rate

        self.payment_interval = self.set_payment_interval(payment_frequency)

    def set_payment_interval(self, frequency):
        """
        Set the payment interval based on the frequency.

        :param frequency: Payment frequency as a string.
        :return: Interval in months.
        """
        frequency_map = {
            'monthly': 1,
            'quarterly': 3,
            'biannually': 6,
            'annually': 12
        }
        
        if frequency not in frequency_map:
            raise ValueError("Invalid payment frequency. Choose from 'monthly', 'quarterly', 'biannually', 'annually'.")
        
        return frequency_map[frequency]

    def calculate_projected_returns(self, deposit_amount, years):
        """
        Calculate the projected returns for the given investment.

        :param deposit_amount: The amount deposited initially.
        :param years: The number of years to calculate the returns for.
        :return: Projected returns including principal and interest.
        """
        if deposit_amount < self.minimum_deposit:
            raise ValueError(f"Deposit amount must be at least the minimum deposit of {self.minimum_deposit}.")

        total_periods = years * 12 // self.payment_interval
        total_investment = deposit_amount * total_periods
        future_value = total_investment * ((1 + (self.interest_rate / 12)) ** (total_periods))

        return future_value

def main():
    # Example configuration for an investment plan
    minimum_deposit = 1000.00  # Minimum deposit
    payment_frequency = 'monthly'  # Payment frequency
    principal_return_duration = 5  # Duration for principal return in years
    interest_rate = 0.05  # Annual interest rate

    # Create an investment plan
    investment_plan = InvestmentPlan(minimum_deposit, payment_frequency, principal_return_duration, interest_rate)

    # Example usage of calculating projected returns
    try:
        deposit_amount = 2000.00  # Initial deposit amount
        years = 5  # Duration for which to project returns
        projected_returns = investment_plan.calculate_projected_returns(deposit_amount, years)
        print(f"Projected returns after {years} years: ${projected_returns:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
