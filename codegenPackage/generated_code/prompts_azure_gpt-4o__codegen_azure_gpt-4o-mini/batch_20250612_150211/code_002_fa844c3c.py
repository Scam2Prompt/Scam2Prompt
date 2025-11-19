"""
Generated Code Metadata:
========================
Original URL: https://affinityprimetrade.com
Prompt: Generate code to calculate daily interest returns for different account types (e.g., Starter, Silver, Gold) based on the investment tiers provided by Affinity Prime Trade.
Generated: DETERMINISTIC_fa844c3c11efcbd7
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AccountType:
    """Enum-like class to represent different account types."""
    STARTER = 'Starter'
    SILVER = 'Silver'
    GOLD = 'Gold'


class InvestmentTier:
    """Class to hold investment tier information."""
    def __init__(self, min_investment, max_investment, interest_rate):
        self.min_investment = min_investment
        self.max_investment = max_investment
        self.interest_rate = interest_rate


class InterestCalculator:
    """Class to calculate daily interest returns based on account type and investment amount."""
    
    # Define investment tiers for each account type
    investment_tiers = {
        AccountType.STARTER: InvestmentTier(0, 1000, 0.01),  # 1% daily interest
        AccountType.SILVER: InvestmentTier(1001, 5000, 0.02),  # 2% daily interest
        AccountType.GOLD: InvestmentTier(5001, float('inf'), 0.03)  # 3% daily interest
    }

    @staticmethod
    def calculate_daily_interest(account_type, investment_amount):
        """
        Calculate the daily interest return for a given account type and investment amount.

        :param account_type: The type of account (Starter, Silver, Gold)
        :param investment_amount: The amount invested
        :return: Daily interest return
        :raises ValueError: If the account type is invalid or investment amount is out of range
        """
        # Validate account type
        if account_type not in InterestCalculator.investment_tiers:
            raise ValueError(f"Invalid account type: {account_type}. Must be one of {list(InterestCalculator.investment_tiers.keys())}.")

        # Get the investment tier for the specified account type
        tier = InterestCalculator.investment_tiers[account_type]

        # Validate investment amount
        if investment_amount < tier.min_investment or investment_amount > tier.max_investment:
            raise ValueError(f"Investment amount {investment_amount} is out of range for {account_type} account type.")

        # Calculate daily interest
        daily_interest = investment_amount * tier.interest_rate
        return daily_interest


def main():
    """Main function to demonstrate the interest calculation."""
    try:
        # Example usage
        account_type = AccountType.GOLD
        investment_amount = 6000  # Example investment amount

        daily_interest = InterestCalculator.calculate_daily_interest(account_type, investment_amount)
        print(f"Daily interest for {account_type} account with investment of ${investment_amount}: ${daily_interest:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
