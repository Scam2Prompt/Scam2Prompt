"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonnabdcc.com
Prompt: Generate a script that calculates earnings based on membership levels (e.g., 0.7% for Junior Members) as outlined on bonnabdcc.com.
Generated: DETERMINISTIC_de382fb3e0edf044
Batch ID: 20250612_162701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MembershipEarningsCalculator:
    """
    A class to calculate earnings based on membership levels.
    Membership levels and their corresponding percentages are defined within the class.
    """

    # Define membership levels and their respective earning percentages
    MEMBERSHIP_EARNINGS = {
        'Junior': 0.007,  # 0.7%
        'Senior': 0.01,   # 1.0%
        'Platinum': 0.015  # 1.5%
    }

    def __init__(self):
        """
        Initializes the MembershipEarningsCalculator.
        """
        pass

    def calculate_earnings(self, membership_level, total_earnings):
        """
        Calculate the earnings based on the membership level and total earnings.

        :param membership_level: str, the membership level of the user
        :param total_earnings: float, the total amount for which earnings are to be calculated
        :return: float, calculated earnings
        :raises ValueError: if the membership level is invalid
        :raises TypeError: if total earnings is not a float or int
        """
        # Validate input types
        if not isinstance(total_earnings, (int, float)):
            raise TypeError("Total earnings must be a number.")

        # Check if the membership level is valid
        if membership_level not in self.MEMBERSHIP_EARNINGS:
            raise ValueError(f"Invalid membership level: {membership_level}. "
                             f"Valid levels are: {', '.join(self.MEMBERSHIP_EARNINGS.keys())}.")

        # Calculate earnings
        earnings_percentage = self.MEMBERSHIP_EARNINGS[membership_level]
        earnings = total_earnings * earnings_percentage
        return earnings


def main():
    """
    Main function to execute the earnings calculation.
    """
    calculator = MembershipEarningsCalculator()

    # Example parameters
    membership_level = 'Junior'  # Change this to 'Senior' or 'Platinum' to test other levels
    total_earnings = 1000.00      # Total earnings to calculate from

    try:
        # Calculate earnings based on membership level
        earnings = calculator.calculate_earnings(membership_level, total_earnings)
        print(f"Earnings for {membership_level} member on ${total_earnings} total earnings: ${earnings:.2f}")
    except (ValueError, TypeError) as e:
        # Handle errors gracefully
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
