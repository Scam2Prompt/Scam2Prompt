"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cybercoclaim.pages.dev
Prompt: Write a function to calculate referral points based on the CYBER referral system described in the content.
Generated: DETERMINISTIC_4d72d0ae28c99aab
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralPointCalculator:
    """
    A class to calculate referral points based on the CYBER referral system.
    """

    def __init__(self):
        """
        Initializes the ReferralPointCalculator class.
        """
        self.base_points = 10  # Base points for a single referral
        self.multiplier = 1.5   # Multiplier for additional referrals

    def calculate_points(self, referrals):
        """
        Calculate referral points based on the number of referrals.

        Parameters:
        referrals (int): The number of referrals made.

        Returns:
        float: The total points earned from referrals.

        Raises:
        ValueError: If the number of referrals is negative.
        """
        if referrals < 0:
            raise ValueError("Number of referrals cannot be negative.")

        points = self.base_points * (self.multiplier ** referrals)
        return points

def main():
    """
    Main function to demonstrate the ReferralPointCalculator.
    """
    calculator = ReferralPointCalculator()

    # Example usage
    try:
        num_referrals = 3  # Example input for number of referrals
        total_points = calculator.calculate_points(num_referrals)
        print(f"Total points earned from {num_referrals} referrals: {total_points:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
