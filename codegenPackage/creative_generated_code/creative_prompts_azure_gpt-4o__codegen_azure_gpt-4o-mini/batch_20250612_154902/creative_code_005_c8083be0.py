"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cotidashboard.com
Prompt: Generate a Python script to calculate rewards for a user depositing $COTI in the COTI Treasury, factoring in both Base APY and Boost APY.
Generated: DETERMINISTIC_c8083be0177c3a22
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class COTIRewardCalculator:
    """
    A class to calculate rewards for a user depositing COTI in the COTI Treasury.
    
    Attributes:
        base_apy (float): The base annual percentage yield (APY) as a percentage.
        boost_apy (float): The boost annual percentage yield (APY) as a percentage.
    """

    def __init__(self, base_apy: float, boost_apy: float):
        """
        Initializes the COTIRewardCalculator with the given APYs.

        Args:
            base_apy (float): The base APY.
            boost_apy (float): The boost APY.
        """
        self.base_apy = base_apy
        self.boost_apy = boost_apy

    def calculate_rewards(self, deposit_amount: float, time_period_years: float) -> float:
        """
        Calculates the total rewards earned from depositing COTI.

        Args:
            deposit_amount (float): The amount of COTI deposited.
            time_period_years (float): The time period in years for which the amount is deposited.

        Returns:
            float: The total rewards earned.

        Raises:
            ValueError: If deposit_amount or time_period_years is negative.
        """
        if deposit_amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        if time_period_years < 0:
            raise ValueError("Time period cannot be negative.")

        # Calculate base rewards
        base_rewards = deposit_amount * (self.base_apy / 100) * time_period_years
        
        # Calculate boost rewards (assuming boost is available for the same period)
        boost_rewards = deposit_amount * (self.boost_apy / 100) * time_period_years

        # Total rewards are the sum of base and boost rewards
        total_rewards = base_rewards + boost_rewards
        return total_rewards


def main():
    """
    Main function to run the COTI reward calculation.
    """
    try:
        # Example APY values and deposit information
        base_apy = 5.0  # Base APY
        boost_apy = 3.0  # Boost APY
        deposit_amount = 1000.0  # Amount of COTI deposited
        time_period_years = 1.0  # Duration in years

        # Create an instance of the reward calculator
        reward_calculator = COTIRewardCalculator(base_apy, boost_apy)

        # Calculate the rewards
        rewards = reward_calculator.calculate_rewards(deposit_amount, time_period_years)

        # Display the results
        print(f"Total rewards earned for depositing ${deposit_amount} COTI over {time_period_years} year(s): ${rewards:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
