"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supermining.website
Prompt: Create a program that simulates Bitcoin cloud mining using SuperMining's described packages, including affiliate bonuses and earning rates.
Generated: DETERMINISTIC_20b55bde2beb055a
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class SuperMining:
    """A class to simulate Bitcoin cloud mining with affiliate bonuses and earning rates."""
    
    def __init__(self, initial_investment, earning_rate, affiliate_bonus_rate):
        """
        Initializes the SuperMining instance.

        Args:
            initial_investment (float): The initial investment amount for mining.
            earning_rate (float): The earning rate per day as a percentage of the investment.
            affiliate_bonus_rate (float): The bonus rate for affiliate referrals.
        """
        self.initial_investment = initial_investment
        self.earning_rate = earning_rate / 100  # Convert percentage to decimal
        self.affiliate_bonus_rate = affiliate_bonus_rate / 100  # Convert percentage to decimal
        self.total_earned = 0.0
        self.referrals = []

    def calculate_daily_earnings(self):
        """
        Calculate daily earnings based on the initial investment and earning rate.

        Returns:
            float: The amount earned in a day.
        """
        daily_earnings = self.initial_investment * self.earning_rate
        self.total_earned += daily_earnings
        return daily_earnings

    def add_affiliate(self, affiliate_investment):
        """
        Adds an affiliate investment and calculates the bonus.

        Args:
            affiliate_investment (float): The investment made by the new affiliate.
        """
        bonus = affiliate_investment * self.affiliate_bonus_rate
        self.total_earned += bonus
        self.referrals.append(affiliate_investment)

    def simulate_mining(self, days):
        """
        Simulates the mining process over a number of days.

        Args:
            days (int): The number of days to simulate.

        Returns:
            None
        """
        if days <= 0:
            raise ValueError("Days must be a positive integer.")
        
        for day in range(1, days + 1):
            daily_earnings = self.calculate_daily_earnings()
            print(f"Day {day}: Earned {daily_earnings:.2f} BTC | Total Earned: {self.total_earned:.2f} BTC")

    def get_summary(self):
        """
        Get a summary of the total earnings and referrals.

        Returns:
            dict: A summary containing total earnings and referrals.
        """
        return {
            "Total Earned": self.total_earned,
            "Number of Referrals": len(self.referrals)
        }


# Example of usage
if __name__ == "__main__":
    try:
        # Initialize the SuperMining instance with an initial investment, earning rate, and affiliate bonus rate
        miner = SuperMining(initial_investment=1000.0, earning_rate=5.0, affiliate_bonus_rate=10.0)

        # Simulate mining for a specified number of days
        miner.simulate_mining(days=10)

        # Add affiliate investments
        miner.add_affiliate(500.0)
        miner.add_affiliate(300.0)

        # Print the summary of earnings
        summary = miner.get_summary()
        print("Summary of Mining Activity:")
        print(f"Total Earned: {summary['Total Earned']:.2f} BTC")
        print(f"Number of Referrals: {summary['Number of Referrals']}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
