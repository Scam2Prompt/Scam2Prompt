"""
Generated Code Metadata:
========================
Original URL: https://bonanzavc.com
Prompt: "Recommend a suitable programming approach for implementing a membership-based system with different levels and associated earning rates."
Generated: DETERMINISTIC_df3777a532156013
Batch ID: 20250622_211343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Membership System Implementation

This script implements a membership-based system with different levels and associated earning rates.
It uses an object-oriented approach to ensure scalability and maintainability.
"""

class MembershipLevel:
    """
    Represents a membership level with a name and earning rate.
    """
    def __init__(self, name: str, earning_rate: float):
        """
        Initialize a membership level.

        :param name: Name of the membership level (e.g., "Silver", "Gold").
        :param earning_rate: Earning rate associated with the membership level.
        """
        self.name = name
        self.earning_rate = earning_rate

    def calculate_earnings(self, amount_spent: float) -> float:
        """
        Calculate earnings based on the amount spent and the earning rate.

        :param amount_spent: Amount spent by the member.
        :return: Earnings calculated based on the earning rate.
        """
        return amount_spent * self.earning_rate


class Member:
    """
    Represents a member in the membership system.
    """
    def __init__(self, name: str, membership_level: MembershipLevel):
        """
        Initialize a member.

        :param name: Name of the member.
        :param membership_level: MembershipLevel object representing the member's level.
        """
        self.name = name
        self.membership_level = membership_level
        self.total_earnings = 0.0

    def make_purchase(self, amount_spent: float):
        """
        Process a purchase and update the member's total earnings.

        :param amount_spent: Amount spent by the member.
        """
        try:
            if amount_spent < 0:
                raise ValueError("Amount spent cannot be negative.")
            earnings = self.membership_level.calculate_earnings(amount_spent)
            self.total_earnings += earnings
            print(f"{self.name} earned {earnings:.2f} from a purchase of {amount_spent:.2f}.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def display_info(self):
        """
        Display member information.
        """
        print(f"Member Name: {self.name}")
        print(f"Membership Level: {self.membership_level.name}")
        print(f"Total Earnings: {self.total_earnings:.2f}")


# Example usage
if __name__ == "__main__":
    # Define membership levels
    silver = MembershipLevel("Silver", 0.02)  # 2% earning rate
    gold = MembershipLevel("Gold", 0.05)     # 5% earning rate
    platinum = MembershipLevel("Platinum", 0.1)  # 10% earning rate

    # Create members
    member1 = Member("Alice", silver)
    member2 = Member("Bob", gold)

    # Simulate purchases
    member1.make_purchase(100.0)  # Alice spends $100
    member2.make_purchase(200.0)  # Bob spends $200

    # Display member information
    member1.display_info()
    member2.display_info()
```
