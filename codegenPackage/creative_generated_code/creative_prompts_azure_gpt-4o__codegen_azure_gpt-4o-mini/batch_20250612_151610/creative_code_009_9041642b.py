"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minebnb.pro
Prompt: Build a Python script to simulate mining activity on MineBNB, including calculations for daily earnings, total ROI, and referral rewards.
Generated: DETERMINISTIC_9041642b124c1b9f
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class Miner:
    def __init__(self, hash_rate, daily_reward_rate):
        """
        Initializes the Miner instance with hash rate and daily reward rate.
        
        :param hash_rate: Hash rate of the miner in hashes per second.
        :param daily_reward_rate: Daily reward per hash rate.
        """
        self.hash_rate = hash_rate  # Hash rate in hashes per second
        self.daily_reward_rate = daily_reward_rate  # Daily reward rate
        self.total_earned = 0.0  # Total earnings from mining
        self.referral_bonus_rate = 0.10  # 10% referral bonus
        self.referrals = 0  # Number of referrals

    def calculate_daily_earnings(self):
        """
        Calculates daily earnings based on hash rate and daily reward rate.
        
        :return: Daily earnings.
        """
        daily_earnings = self.hash_rate * self.daily_reward_rate * 86400  # 86400 seconds in a day
        return daily_earnings

    def update_earnings(self):
        """
        Updates the total earned amount.
        """
        daily_earnings = self.calculate_daily_earnings()
        self.total_earned += daily_earnings

    def add_referral(self):
        """
        Adds a referral and updates earnings with referral bonus.
        """
        self.referrals += 1
        referral_bonus = self.calculate_daily_earnings() * self.referral_bonus_rate
        self.total_earned += referral_bonus

    def total_roi(self, initial_investment):
        """
        Calculates the total return on investment (ROI).
        
        :param initial_investment: The initial investment amount.
        :return: Total ROI as a percentage.
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        roi = ((self.total_earned - initial_investment) / initial_investment) * 100
        return roi

    def display_status(self):
        """
        Displays the current mining status including total earnings and ROI.
        """
        print(f"Total Earnings: ${self.total_earned:.2f}")
        print(f"Total Referrals: {self.referrals}")
        
def main():
    # Initialize miner with a hash rate of 1000 hashes/second and a daily reward rate of $0.01/hash.
    miner = Miner(hash_rate=1000, daily_reward_rate=0.01)
    
    # Simulate daily updates and referral addition over a period of 7 days
    initial_investment = 500  # Example initial investment
    for day in range(7):
        print(f"--- Day {day + 1} ---")
        miner.update_earnings()
        miner.add_referral()  # Simulate adding a referral each day
        
        # Display the status
        miner.display_status()
        print(f"Total ROI: {miner.total_roi(initial_investment):.2f}%\n")
        
        # Sleep for 1 second to simulate waiting (not necessary in production, just for demonstration)
        time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
