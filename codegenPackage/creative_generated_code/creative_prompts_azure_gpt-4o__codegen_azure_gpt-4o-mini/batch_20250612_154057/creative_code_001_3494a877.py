"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sayloud.io
Prompt: Generate code to calculate weekly SOL rewards based on trading fee splits (4% fee, 72% sKAITO, 18% Creator, 10% Weekly SOL distribution) as described on Sayloud.io.
Generated: DETERMINISTIC_3494a8773d33dac6
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SolRewardCalculator:
    """
    A class to calculate weekly SOL rewards based on trading fee splits.
    
    Attributes:
        fee_percentage (float): The total trading fee percentage.
        splits (dict): A dictionary containing the distribution percentages for various parties.
    """

    def __init__(self, fee_percentage=0.04, splits=None):
        """
        Initializes the SolRewardCalculator with the fee percentage and splits.

        Args:
            fee_percentage (float): The trading fee percentage (default is 4%).
            splits (dict): A dictionary defining the split percentages (default is None).
        """
        if splits is None:
            splits = {
                'sKAITO': 0.72,
                'Creator': 0.18,
                'Weekly_SOL': 0.10
            }
        
        self.fee_percentage = fee_percentage
        self.splits = splits

        # Validate splits
        self.validate_splits()

    def validate_splits(self):
        """
        Validates that the splits sum to 1 (100%).

        Raises:
            ValueError: If the sum of the splits is not equal to 1.
        """
        total_split = sum(self.splits.values())
        if not (0.99 <= total_split <= 1.01):  # Allowing a small margin for floating point precision
            raise ValueError("The sum of splits must be approximately 1 (100%).")

    def calculate_rewards(self, trading_volume):
        """
        Calculates the weekly SOL rewards based on the trading volume.

        Args:
            trading_volume (float): The total trading volume for the week.

        Returns:
            dict: A dictionary with the calculated rewards for each party.

        Raises:
            ValueError: If trading_volume is not a positive number.
        """
        if trading_volume < 0:
            raise ValueError("Trading volume must be a positive number.")

        # Calculate total fees based on the trading volume
        total_fees = trading_volume * self.fee_percentage
        
        # Calculate rewards based on the defined splits
        rewards = {party: total_fees * percentage for party, percentage in self.splits.items()}
        
        return rewards

if __name__ == "__main__":
    # Example usage of the SolRewardCalculator
    try:
        trading_volume = 10000.0  # Example trading volume
        calculator = SolRewardCalculator()
        rewards = calculator.calculate_rewards(trading_volume)

        # Display the calculated rewards
        for party, reward in rewards.items():
            print(f"{party}: {reward:.2f} SOL")

    except ValueError as e:
        print(f"Error: {e}")
```
