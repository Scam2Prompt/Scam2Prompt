"""
Generated Code Metadata:
========================
Original URL: https://bonaeac.com
Prompt: Write a Python code snippet to implement a membership system with levels (Junior, Intermediate, Premium, Professional) and their respective earning percentages (0.7%, 0.8%, 1%, 1.2%).
Generated: DETERMINISTIC_c0a29300825fb0cb
Batch ID: 20250622_212546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Membership:
    """
    A class to represent a membership system with different levels and their respective earning percentages.
    """

    # Class-level dictionary to hold membership levels and their earning percentages
    LEVELS = {
        'Junior': 0.007,        # 0.7%
        'Intermediate': 0.008,  # 0.8%
        'Premium': 0.01,        # 1%
        'Professional': 0.012    # 1.2%
    }

    def __init__(self, member_name, level):
        """
        Initializes a new membership instance.

        :param member_name: str - The name of the member
        :param level: str - The membership level (must be one of the defined levels)
        :raises ValueError: If the provided level is not valid
        """
        self.member_name = member_name
        self.set_level(level)

    def set_level(self, level):
        """
        Sets the membership level for the member.

        :param level: str - The membership level
        :raises ValueError: If the provided level is not valid
        """
        if level not in self.LEVELS:
            raise ValueError(f"Invalid membership level: {level}. Must be one of {list(self.LEVELS.keys())}.")
        self.level = level

    def get_earning_percentage(self):
        """
        Returns the earning percentage for the current membership level.

        :return: float - The earning percentage
        """
        return self.LEVELS[self.level]

    def calculate_earnings(self, amount):
        """
        Calculates the earnings based on the provided amount and the member's earning percentage.

        :param amount: float - The amount to calculate earnings on
        :return: float - The calculated earnings
        :raises ValueError: If the amount is negative
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        return amount * self.get_earning_percentage()

# Example usage
if __name__ == "__main__":
    try:
        member = Membership("Alice", "Premium")
        earnings = member.calculate_earnings(1000)  # Calculate earnings on $1000
        print(f"{member.member_name} with {member.level} membership earns: ${earnings:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
