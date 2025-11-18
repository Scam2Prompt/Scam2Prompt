"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonanzavc.com
Prompt: Write code to implement a membership system with multiple earning levels (e.g., Junior Member, Intermediate Member, Premium Member, Professional Member) using Python. Include functionality for calculating earnings based on percentages (e.g., 0.7%, 0.8%, 1%, 1.2%).
Generated: DETERMINISTIC_13ebfddffb2fc62e
Batch ID: 20250612_154058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MembershipLevel:
    """
    Enum-like class to represent different membership levels and their respective earning percentages.
    """
    JUNIOR_MEMBER = 0.007  # 0.7%
    INTERMEDIATE_MEMBER = 0.008  # 0.8%
    PREMIUM_MEMBER = 0.01  # 1%
    PROFESSIONAL_MEMBER = 0.012  # 1.2%

    @staticmethod
    def get_earning_percentage(level):
        """
        Retrieve the earning percentage based on membership level.

        Args:
            level (str): The membership level.

        Returns:
            float: The earning percentage corresponding to the membership level.
        """
        levels = {
            "Junior Member": MembershipLevel.JUNIOR_MEMBER,
            "Intermediate Member": MembershipLevel.INTERMEDIATE_MEMBER,
            "Premium Member": MembershipLevel.PREMIUM_MEMBER,
            "Professional Member": MembershipLevel.PROFESSIONAL_MEMBER,
        }
        return levels.get(level, None)


class Member:
    """
    Represents a member in the membership system.

    Attributes:
        name (str): The name of the member.
        level (str): The membership level of the member.
    """

    def __init__(self, name, level):
        """
        Initializes a new member with the given name and level.

        Args:
            name (str): The name of the member.
            level (str): The membership level of the member.

        Raises:
            ValueError: If the membership level is invalid.
        """
        self.name = name
        self.level = level
        if MembershipLevel.get_earning_percentage(level) is None:
            raise ValueError(f"Invalid membership level: {level}")

    def calculate_earnings(self, amount):
        """
        Calculate the earnings for the member based on a given amount.

        Args:
            amount (float): The amount to calculate earnings from.

        Returns:
            float: The calculated earnings based on the member's level.
        """
        percentage = MembershipLevel.get_earning_percentage(self.level)
        if percentage is None:
            raise ValueError(f"Invalid membership level: {self.level}")
        return amount * percentage


def main():
    """
    Main function to demonstrate the membership system.
    """
    try:
        # Create members with different membership levels
        members = [
            Member("Alice", "Junior Member"),
            Member("Bob", "Intermediate Member"),
            Member("Charlie", "Premium Member"),
            Member("David", "Professional Member"),
        ]

        # Amount to calculate earnings from
        amount = 10000  # Example amount

        # Calculate and display earnings for each member
        for member in members:
            earnings = member.calculate_earnings(amount)
            print(f"{member.name} ({member.level}): Earnings = ${earnings:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
