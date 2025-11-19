"""
Generated Code Metadata:
========================
Original URL: https://aspiregaininvest.com
Prompt: Create a Python script to calculate affiliate rewards for a two-level partnership program, as described on AspireGain Invest's website (5% for first-level referrals and 5% for second-level referrals).
Generated: DETERMINISTIC_803db76f779b154b
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Affiliate Rewards Calculator for a Two-Level Partnership Program

Calculates rewards for first-level and second-level referrals.
"""

class AffiliateRewardsCalculator:
    """
    Calculates affiliate rewards for a two-level partnership program.

    Attributes:
        first_level_referral_rate (float): Rate for first-level referrals (default: 5%).
        second_level_referral_rate (float): Rate for second-level referrals (default: 5%).
    """

    def __init__(self, first_level_referral_rate=0.05, second_level_referral_rate=0.05):
        """
        Initializes the AffiliateRewardsCalculator.

        Args:
            first_level_referral_rate (float, optional): Rate for first-level referrals. Defaults to 0.05.
            second_level_referral_rate (float, optional): Rate for second-level referrals. Defaults to 0.05.
        """
        self.first_level_referral_rate = first_level_referral_rate
        self.second_level_referral_rate = second_level_referral_rate

    def calculate_rewards(self, investment_amount, first_level_referrals, second_level_referrals):
        """
        Calculates affiliate rewards.

        Args:
            investment_amount (float): Investment amount.
            first_level_referrals (list[float]): List of investment amounts from first-level referrals.
            second_level_referrals (list[list[float]]): List of lists of investment amounts from second-level referrals.

        Returns:
            dict: Dictionary containing total rewards, first-level rewards, and second-level rewards.
        """
        try:
            # Calculate first-level rewards
            first_level_rewards = [investment * self.first_level_referral_rate for investment in first_level_referrals]
            total_first_level_rewards = sum(first_level_rewards)

            # Calculate second-level rewards
            second_level_rewards = []
            for referrals in second_level_referrals:
                rewards = [investment * self.second_level_referral_rate for investment in referrals]
                second_level_rewards.append(sum(rewards))
            total_second_level_rewards = sum(second_level_rewards)

            # Calculate total rewards
            total_rewards = total_first_level_rewards + total_second_level_rewards

            return {
                "total_rewards": total_rewards,
                "first_level_rewards": first_level_rewards,
                "second_level_rewards": second_level_rewards,
            }

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None


def main():
    calculator = AffiliateRewardsCalculator()

    investment_amount = 1000.0
    first_level_referrals = [500.0, 750.0, 200.0]
    second_level_referrals = [
        [100.0, 200.0],
        [50.0, 75.0],
        [25.0, 50.0]
    ]

    rewards = calculator.calculate_rewards(investment_amount, first_level_referrals, second_level_referrals)

    if rewards:
        print("Rewards:")
        print(f"Total Rewards: ${rewards['total_rewards']:.2f}")
        print("First-Level Rewards:")
        for i, reward in enumerate(rewards['first_level_rewards']):
            print(f"Referral {i+1}: ${reward:.2f}")
        print("Second-Level Rewards:")
        for i, rewards_list in enumerate(rewards['second_level_rewards']):
            print(f"Referral {i+1}: ${rewards_list:.2f}")


if __name__ == "__main__":
    main()
```
