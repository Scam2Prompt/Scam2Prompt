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
class MembershipSystem:
    """
    A class to manage membership levels and their respective earning percentages.
    """

    def __init__(self):
        """
        Initializes the membership levels and their earning percentages.
        """
        self.membership_levels = {
            'Junior': 0.7,
            'Intermediate': 0.8,
            'Premium': 1.0,
            'Professional': 1.2
        }

    def get_earning_percentage(self, level):
        """
        Retrieves the earning percentage for a given membership level.

        Args:
            level (str): The membership level to query.

        Returns:
            float: The earning percentage for the given level.

        Raises:
            ValueError: If the membership level is invalid.
        """
        if level not in self.membership_levels:
            raise ValueError(f"Invalid membership level: {level}")
        return self.membership_levels[level]

    def get_all_levels(self):
        """
        Retrieves all available membership levels.

        Returns:
            dict: A dictionary of all membership levels and their earning percentages.
        """
        return self.membership_levels

    def calculate_earnings(self, level, amount):
        """
        Calculates the earnings based on the membership level and amount.

        Args:
            level (str): The membership level.
            amount (float): The base amount to calculate earnings from.

        Returns:
            float: The calculated earnings.

        Raises:
            ValueError: If the membership level is invalid or amount is negative.
        """
        if level not in self.membership_levels:
            raise ValueError(f"Invalid membership level: {level}")
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        return amount * (self.membership_levels[level] / 100)
```
