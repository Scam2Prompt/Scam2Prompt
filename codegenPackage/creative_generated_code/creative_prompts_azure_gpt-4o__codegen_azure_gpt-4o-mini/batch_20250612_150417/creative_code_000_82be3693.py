"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crptominer.com
Prompt: Write Python code to simulate the profit calculation for CrptoMiner's investment plans, including Starter, Gold, Standard, and Platinum plans, based on daily returns and lifetime earnings.
Generated: DETERMINISTIC_82be36937be2f4bc
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CryptoMinerInvestment:
    """Class to simulate profit calculation for CryptoMiner investment plans."""

    def __init__(self, plan: str, initial_investment: float):
        """
        Initializes the CryptoMinerInvestment instance.

        Args:
            plan (str): The investment plan type (Starter, Gold, Standard, Platinum).
            initial_investment (float): The initial amount invested.
        
        Raises:
            ValueError: If the investment plan is not recognized.
        """
        self.plan = plan.lower()
        self.initial_investment = initial_investment
        self.daily_return_rate = self.get_daily_return_rate()
        self.lifetime_earnings = 0.0

    def get_daily_return_rate(self) -> float:
        """Returns the daily return rate based on the investment plan."""
        plans = {
            'starter': 0.01,  # 1% daily return
            'gold': 0.02,     # 2% daily return
            'standard': 0.03,  # 3% daily return
            'platinum': 0.05   # 5% daily return
        }
        if self.plan not in plans:
            raise ValueError(f"Unrecognized investment plan: {self.plan}")
        return plans[self.plan]

    def calculate_daily_profit(self) -> float:
        """Calculates the daily profit based on the initial investment and daily return rate."""
        return self.initial_investment * self.daily_return_rate

    def simulate_investment(self, days: int) -> None:
        """
        Simulates the investment over a number of days.

        Args:
            days (int): The number of days to simulate the investment.
        
        Raises:
            ValueError: If days is not a positive integer.
        """
        if not isinstance(days, int) or days <= 0:
            raise ValueError("The number of days must be a positive integer.")

        for day in range(1, days + 1):
            daily_profit = self.calculate_daily_profit()
            self.lifetime_earnings += daily_profit
            print(f"Day {day}: Daily Profit: ${daily_profit:.2f}, "
                  f"Total Earnings: ${self.lifetime_earnings:.2f}")

    def get_total_earnings(self) -> float:
        """Returns the total earnings from the investment."""
        return self.lifetime_earnings


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the investment plan and amount
        investment_plan = "Gold"
        initial_amount = 1000.0  # Initial investment amount in dollars

        # Create a CryptoMinerInvestment instance
        investor = CryptoMinerInvestment(investment_plan, initial_amount)

        # Simulate the investment for a specified number of days
        investor.simulate_investment(days=10)

        # Print the total earnings after the simulation
        total_earnings = investor.get_total_earnings()
        print(f"Total Earnings after 10 days: ${total_earnings:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
