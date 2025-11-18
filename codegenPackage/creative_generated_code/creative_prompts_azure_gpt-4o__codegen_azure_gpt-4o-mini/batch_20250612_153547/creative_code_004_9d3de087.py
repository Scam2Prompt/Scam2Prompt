"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earnm-rectify-presale-url.pages.dev
Prompt: Generate code to calculate APY rewards in a DeFi system, referencing EARN'M's Initial Merge Offering (IMO) with up to 250% APY.
Generated: DETERMINISTIC_9d3de0873ac63d20
Batch ID: 20250612_153547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DeFiRewardsCalculator:
    """
    A class to calculate the Annual Percentage Yield (APY) rewards
    for users participating in a decentralized finance (DeFi) system.
    Specifically designed to reference EARN'M's Initial Merge Offering (IMO)
    with a maximum APY of 250%.
    """

    def __init__(self, principal: float, apy: float, time_period_years: float):
        """
        Initializes the rewards calculator with the principal amount,
        APY and the time period in years.

        :param principal: The initial amount of cryptocurrency invested.
        :param apy: The annual percentage yield expressed as a decimal (e.g., 0.25 for 25%).
        :param time_period_years: The time period in years for which the rewards are calculated.
        """
        if principal < 0:
            raise ValueError("Principal amount must be non-negative.")
        if not (0 <= apy <= 2.5):
            raise ValueError("APY must be between 0 and 250% (0 to 2.5).")
        if time_period_years < 0:
            raise ValueError("Time period must be non-negative.")

        self.principal = principal
        self.apy = apy
        self.time_period_years = time_period_years

    def calculate_total_rewards(self) -> float:
        """
        Calculates the total rewards earned after the specified time period.

        :return: Total amount including principal and earned rewards.
        """
        total_amount = self.principal * (1 + self.apy) ** self.time_period_years
        return total_amount

    def calculate_rewards(self) -> float:
        """
        Calculates the total rewards earned (excluding principal) after
        the specified time period.

        :return: Total rewards earned.
        """
        total_rewards = self.calculate_total_rewards() - self.principal
        return total_rewards

    def display_rewards(self):
        """
        Displays the summary of the rewards calculation.
        """
        try:
            total_rewards = self.calculate_rewards()
            total_amount = self.calculate_total_rewards()
            print(f"Principal Amount: ${self.principal:.2f}")
            print(f"APY: {self.apy * 100:.2f}%")
            print(f"Time Period: {self.time_period_years} years")
            print(f"Total Rewards Earned: ${total_rewards:.2f}")
            print(f"Total Amount after {self.time_period_years} years: ${total_amount:.2f}")
        except Exception as e:
            print(f"Error calculating rewards: {e}")


if __name__ == "__main__":
    # Example Usage
    try:
        # Initialize the calculator with a principal of $1000, 
        # an APY of 250% (2.5), and a time period of 1 year.
        calculator = DeFiRewardsCalculator(principal=1000.0, apy=2.5, time_period_years=1)
        
        # Display the rewards
        calculator.display_rewards()
    except Exception as e:
        print(f"Initialization error: {e}")
```
