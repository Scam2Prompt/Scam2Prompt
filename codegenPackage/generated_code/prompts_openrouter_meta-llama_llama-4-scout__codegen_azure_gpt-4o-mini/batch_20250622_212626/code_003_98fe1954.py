"""
Generated Code Metadata:
========================
Original URL: https://stlink.vip
Prompt: "Given the total fees of 15,160.04 LINK, write a code snippet to calculate the net rewards earned from staking LINK tokens using stakelink's protocol."
Generated: DETERMINISTIC_98fe1954b01a4af2
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class StakingCalculator:
    """
    A class to calculate net rewards earned from staking LINK tokens.
    """

    def __init__(self, total_fees: float, staking_percentage: float):
        """
        Initializes the StakingCalculator with total fees and staking percentage.

        :param total_fees: Total fees in LINK tokens (float).
        :param staking_percentage: Percentage of fees that are rewarded (float).
        """
        self.total_fees = total_fees
        self.staking_percentage = staking_percentage

    def calculate_net_rewards(self) -> float:
        """
        Calculates the net rewards earned from staking.

        :return: Net rewards in LINK tokens (float).
        """
        if self.staking_percentage < 0 or self.staking_percentage > 100:
            raise ValueError("Staking percentage must be between 0 and 100.")

        # Calculate net rewards based on the staking percentage
        net_rewards = (self.total_fees * self.staking_percentage) / 100
        return net_rewards


def main():
    """
    Main function to execute the staking rewards calculation.
    """
    try:
        total_fees = 15160.04  # Total fees in LINK
        staking_percentage = 10  # Example staking percentage

        # Create an instance of StakingCalculator
        calculator = StakingCalculator(total_fees, staking_percentage)

        # Calculate net rewards
        net_rewards = calculator.calculate_net_rewards()

        # Output the result
        print(f"Net rewards earned from staking: {net_rewards:.2f} LINK")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
