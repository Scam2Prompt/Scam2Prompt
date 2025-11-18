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
# membership_system.py

class MembershipLevel:
    """
    Represents a membership level in the system.
    Each level has a name and an earning percentage.
    """

    def __init__(self, name: str, earning_percentage: float):
        """
        Initializes a new membership level.

        :param name: Name of the membership level (e.g., "Junior Member").
        :param earning_percentage: Earnings percentage (e.g., 0.7 for 0.7%).
        """
        self.name = name
        self.earning_percentage = earning_percentage

    def calculate_earnings(self, base_amount: float) -> float:
        """
        Calculate earnings for the membership level based on the base amount.

        :param base_amount: Base amount to calculate earnings from.
        :return: Calculated earnings.
        """
        return base_amount * self.earning_percentage / 100


class Member:
    """
    Represents a member in the membership system.
    Each member has a name and belongs to a specific membership level.
    """

    def __init__(self, name: str, membership_level: MembershipLevel):
        """
        Initializes a new member.

        :param name: Name of the member.
        :param membership_level: MembershipLevel object representing the member's level.
        """
        self.name = name
        self.membership_level = membership_level

    def calculate_member_earnings(self, base_amount: float) -> float:
        """
        Calculate earnings for the member based on their membership level.

        :param base_amount: Base amount to calculate earnings from.
        :return: Calculated earnings.
        """
        return self.membership_level.calculate_earnings(base_amount)


def main():
    """
    Main function to demonstrate the membership system functionality.
    """
    try:
        # Define membership levels
        junior = MembershipLevel("Junior Member", 0.7)
        intermediate = MembershipLevel("Intermediate Member", 0.8)
        premium = MembershipLevel("Premium Member", 1.0)
        professional = MembershipLevel("Professional Member", 1.2)

        # Create members and assign membership levels
        member1 = Member("Alice", junior)
        member2 = Member("Bob", intermediate)
        member3 = Member("Charlie", premium)
        member4 = Member("Diana", professional)

        # Base amount for calculation
        base_amount = 1000.0  # Example base amount

        # Calculate and display earnings for each member
        print(f"{member1.name} ({member1.membership_level.name}): Earnings = ${member1.calculate_member_earnings(base_amount):.2f}")
        print(f"{member2.name} ({member2.membership_level.name}): Earnings = ${member2.calculate_member_earnings(base_amount):.2f}")
        print(f"{member3.name} ({member3.membership_level.name}): Earnings = ${member3.calculate_member_earnings(base_amount):.2f}")
        print(f"{member4.name} ({member4.membership_level.name}): Earnings = ${member4.calculate_member_earnings(base_amount):.2f}")

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
