"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fi-dapp-b1r6bzwwh-etherfi.vercel.app
Prompt: What are the unique features of the eETH portfolio in the context of DeFi promotions?
Generated: DETERMINISTIC_793f1a77b9422968
Batch ID: 20250612_135343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EETHPortfolio:
    """
    Class representing the eETH portfolio in the context of DeFi promotions.
    This class encapsulates the unique features of the eETH portfolio, including
    staking, yield farming, and governance participation.
    """

    def __init__(self, initial_investment: float):
        """
        Initializes the eETHPortfolio with a given initial investment.

        :param initial_investment: The initial amount invested in eETH.
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        self.balance = initial_investment
        self.staked_amount = 0
        self.yield_farmed_amount = 0
        self.governance_tokens = 0

    def stake(self, amount: float):
        """
        Stakes a specified amount of eETH in the DeFi protocol.

        :param amount: The amount of eETH to stake.
        :raises ValueError: If the amount is invalid or exceeds the available balance.
        """
        if amount <= 0:
            raise ValueError("Amount to stake must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient balance to stake the specified amount.")

        self.balance -= amount
        self.staked_amount += amount
        self.governance_tokens += amount * 0.1  # Example reward rate for governance tokens

    def yield_farm(self, amount: float):
        """
        Participates in yield farming with a specified amount of eETH.

        :param amount: The amount of eETH to yield farm.
        :raises ValueError: If the amount is invalid or exceeds the available balance.
        """
        if amount <= 0:
            raise ValueError("Amount to yield farm must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient balance to yield farm the specified amount.")

        self.balance -= amount
        self.yield_farmed_amount += amount * 1.2  # Example yield farming rate

    def withdraw(self, amount: float):
        """
        Withdraws a specified amount of eETH from the portfolio.

        :param amount: The amount of eETH to withdraw.
        :raises ValueError: If the amount is invalid or exceeds the total available (balance + staked).
        """
        if amount <= 0:
            raise ValueError("Amount to withdraw must be greater than zero.")
        if amount > (self.balance + self.staked_amount):
            raise ValueError("Insufficient balance to withdraw the specified amount.")

        if amount <= self.balance:
            self.balance -= amount
        else:
            withdraw_from_stake = amount - self.balance
            self.staked_amount -= withdraw_from_stake
            self.balance = 0

    def get_portfolio_summary(self) -> dict:
        """
        Provides a summary of the current eETH portfolio.

        :return: A dictionary containing the balance, staked amount, yield farmed amount,
                 and governance tokens.
        """
        return {
            "Balance": self.balance,
            "Staked Amount": self.staked_amount,
            "Yield Farmed Amount": self.yield_farmed_amount,
            "Governance Tokens": self.governance_tokens
        }


# Example usage
if __name__ == "__main__":
    try:
        portfolio = EETHPortfolio(initial_investment=1000.0)
        portfolio.stake(200.0)
        portfolio.yield_farm(300.0)
        print(portfolio.get_portfolio_summary())
        portfolio.withdraw(150.0)
        print(portfolio.get_portfolio_summary())
    except ValueError as e:
        print(f"Error: {e}")
```
