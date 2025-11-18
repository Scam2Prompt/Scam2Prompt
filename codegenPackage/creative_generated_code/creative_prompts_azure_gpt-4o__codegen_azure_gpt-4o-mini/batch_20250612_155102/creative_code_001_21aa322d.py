"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://playful-abstractt.nfts2.me
Prompt: Create a function that calculates referral earnings based on the number of NFT mints completed through a referral link, following the Abstractt Chain's reward structure.
Generated: DETERMINISTIC_21aa322d6f64f458
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralEarningsCalculator:
    """
    A class to calculate referral earnings based on the number of NFT mints completed
    through a referral link following the Abstractt Chain's reward structure.
    """

    def __init__(self, base_reward_per_mint: float, bonus_threshold: int, bonus_amount: float):
        """
        Initializes the ReferralEarningsCalculator with the necessary parameters.

        :param base_reward_per_mint: The base reward for each NFT mint.
        :param bonus_threshold: The number of mints required to qualify for a bonus.
        :param bonus_amount: The additional bonus earned for reaching the bonus threshold.
        """
        self.base_reward_per_mint = base_reward_per_mint
        self.bonus_threshold = bonus_threshold
        self.bonus_amount = bonus_amount

    def calculate_earnings(self, number_of_mints: int) -> float:
        """
        Calculates the total referral earnings based on the number of mints.

        :param number_of_mints: The total number of NFT mints through the referral link.
        :return: The total earnings as a float.
        :raises ValueError: If the number_of_mints is negative.
        """
        if number_of_mints < 0:
            raise ValueError("The number of mints cannot be negative.")

        # Calculate base earnings from the number of mints
        base_earnings = number_of_mints * self.base_reward_per_mint

        # Check if the number of mints qualifies for a bonus
        bonus_earnings = self.bonus_amount if number_of_mints >= self.bonus_threshold else 0

        # Total earnings is the sum of base earnings and any bonus earnings
        total_earnings = base_earnings + bonus_earnings

        return total_earnings


def main():
    # Example usage of the ReferralEarningsCalculator
    try:
        # Set parameters for the earnings calculator
        base_reward_per_mint = 0.01  # Example: $0.01 per mint
        bonus_threshold = 100  # Example: Bonus for 100 or more mints
        bonus_amount = 5.0  # Example: $5 bonus

        # Create the earnings calculator instance
        calculator = ReferralEarningsCalculator(base_reward_per_mint, bonus_threshold, bonus_amount)

        # Calculate earnings for a specific number of mints
        number_of_mints = 120  # Example input
        total_earnings = calculator.calculate_earnings(number_of_mints)

        print(f"Total earnings from {number_of_mints} mints: ${total_earnings:.2f}")

    except ValueError as e:
        print(f"Error calculating earnings: {e}")


if __name__ == "__main__":
    main()
```
