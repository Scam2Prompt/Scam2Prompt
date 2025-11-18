"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capinvest.ltd
Prompt: Create a script to simulate risk minimization strategies described by CAPINVEST LTD, including diversification and balancing short-term and long-term investments.
Generated: DETERMINISTIC_c82b89114ca9bcf5
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random


class InvestmentPortfolio:
    """
    A class to represent an investment portfolio and simulate risk minimization strategies.

    Attributes:
        short_term_investments (list): Short-term investment amounts.
        long_term_investments (list): Long-term investment amounts.
        diversification_factor (float): Diversification factor to spread investments across types.
    """

    def __init__(self, diversification_factor=0.5):
        """
        Initialize an investment portfolio.

        Args:
            diversification_factor (float): Determines the ratio of investments split
                                             between short-term and long-term.
                                             Default is 0.5 (50% short-term, 50% long-term).
        """
        self.short_term_investments = []
        self.long_term_investments = []
        self.diversification_factor = diversification_factor

    def allocate_investment(self, investment_amount):
        """
        Allocate investment based on diversification factor.

        Args:
            investment_amount (float): The amount to invest.
        """
        try:
            if investment_amount <= 0:
                raise ValueError("Investment amount must be greater than zero.")

            short_term_allocation = investment_amount * self.diversification_factor
            long_term_allocation = investment_amount * (1 - self.diversification_factor)

            self.short_term_investments.append(short_term_allocation)
            self.long_term_investments.append(long_term_allocation)

            print(f"Allocated ${investment_amount:.2f}: "
                  f"${short_term_allocation:.2f} to short-term, "
                  f"${long_term_allocation:.2f} to long-term.")
        except Exception as e:
            print(f"Error allocating investment: {e}")

    def balance_portfolio(self):
        """
        Rebalance portfolio to ensure proper diversification ratio.
        """
        try:
            total_short_term = sum(self.short_term_investments)
            total_long_term = sum(self.long_term_investments)
            total_investment = total_short_term + total_long_term

            if total_investment == 0:
                raise ValueError("Portfolio is empty. No investments to balance.")

            # Calculate the target allocation based on the diversification factor
            target_short_term = total_investment * self.diversification_factor
            target_long_term = total_investment * (1 - self.diversification_factor)

            # Adjust short-term and long-term investments
            adjustment_short_term = target_short_term - total_short_term
            adjustment_long_term = target_long_term - total_long_term

            self.short_term_investments.append(adjustment_short_term)
            self.long_term_investments.append(adjustment_long_term)

            print(f"Portfolio balanced: Adjusted short-term by ${adjustment_short_term:.2f}, "
                  f"long-term by ${adjustment_long_term:.2f}.")
        except Exception as e:
            print(f"Error balancing portfolio: {e}")

    def simulate_portfolio_growth(self, years=1, short_term_growth_rate=0.05, long_term_growth_rate=0.08):
        """
        Simulate the growth of the portfolio over a given number of years.

        Args:
            years (int): The number of years for growth simulation.
            short_term_growth_rate (float): Annual growth rate for short-term investments.
            long_term_growth_rate (float): Annual growth rate for long-term investments.
        """
        try:
            if years <= 0:
                raise ValueError("Years for simulation must be greater than zero.")

            for year in range(1, years + 1):
                self.short_term_investments = [
                    investment * (1 + short_term_growth_rate) for investment in self.short_term_investments
                ]
                self.long_term_investments = [
                    investment * (1 + long_term_growth_rate) for investment in self.long_term_investments
                ]

                print(f"Year {year}: Portfolio grew by {short_term_growth_rate * 100:.2f}% (short-term) and "
                      f"{long_term_growth_rate * 100:.2f}% (long-term).")
        except Exception as e:
            print(f"Error simulating portfolio growth: {e}")

    def display_portfolio(self):
        """
        Display the current state of the portfolio.
        """
        total_short_term = sum(self.short_term_investments)
        total_long_term = sum(self.long_term_investments)
        total_value = total_short_term + total_long_term

        print("\nPortfolio Summary:")
        print("-------------------")
        print(f"Short-term Investments: ${total_short_term:.2f}")
        print(f"Long-term Investments: ${total_long_term:.2f}")
        print(f"Total Portfolio Value: ${total_value:.2f}")


# Example usage of the InvestmentPortfolio class
if __name__ == "__main__":
    # Create a portfolio with a diversification factor of 60% short-term, 40% long-term
    portfolio = InvestmentPortfolio(diversification_factor=0.6)

    # Allocate investments
    portfolio.allocate_investment(1000)
    portfolio.allocate_investment(5000)

    # Display initial portfolio
    portfolio.display_portfolio()

    # Balance the portfolio
    portfolio.balance_portfolio()

    # Simulate portfolio growth over 5 years
    portfolio.simulate_portfolio_growth(years=5)

    # Display final portfolio
    portfolio.display_portfolio()
```
