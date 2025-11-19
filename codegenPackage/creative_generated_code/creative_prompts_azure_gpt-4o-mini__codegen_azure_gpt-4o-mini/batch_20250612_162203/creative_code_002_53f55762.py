"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gemcaster.vercel.app
Prompt: Write a function that calculates potential earnings for a cast creator on Gemcaster based on the minting fees and rewards structure.
Generated: DETERMINISTIC_53f55762729b4bb2
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GemcasterEarningsCalculator:
    """
    A class to calculate potential earnings for a cast creator on Gemcaster.
    """

    def __init__(self, minting_fee: float, reward_percentage: float):
        """
        Initializes the calculator with minting fee and reward percentage.

        :param minting_fee: The fee charged for minting (in currency units).
        :param reward_percentage: The percentage of the minting fee that is given as a reward (0 to 100).
        """
        if minting_fee < 0:
            raise ValueError("Minting fee must be a non-negative value.")
        if not (0 <= reward_percentage <= 100):
            raise ValueError("Reward percentage must be between 0 and 100.")

        self.minting_fee = minting_fee
        self.reward_percentage = reward_percentage / 100  # Convert percentage to decimal

    def calculate_earnings(self, number_of_mints: int) -> float:
        """
        Calculates the total earnings based on the number of mints.

        :param number_of_mints: The total number of mints.
        :return: Total potential earnings.
        """
        if number_of_mints < 0:
            raise ValueError("Number of mints must be a non-negative integer.")

        total_earnings = number_of_mints * self.minting_fee * self.reward_percentage
        return total_earnings

    def report(self, number_of_mints: int) -> str:
        """
        Generates a report of the potential earnings.

        :param number_of_mints: The total number of mints.
        :return: A formatted string report of potential earnings.
        """
        try:
            earnings = self.calculate_earnings(number_of_mints)
            return f"With {number_of_mints} mints, your potential earnings are: ${earnings:.2f}"
        except ValueError as e:
            return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    try:
        minting_fee = 0.05  # Example minting fee in currency units
        reward_percentage = 10  # Example reward percentage
        number_of_mints = 100  # Example number of mints

        calculator = GemcasterEarningsCalculator(minting_fee, reward_percentage)
        report = calculator.report(number_of_mints)
        print(report)
    except Exception as e:
        print(f"An error occurred: {e}")
```
