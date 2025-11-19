"""
Generated Code Metadata:
========================
Original URL: https://bonanzavc.com
Prompt: Write code to implement a membership system with multiple earning levels (e.g., Junior Member, Intermediate Member, Premium Member, Professional Member) using Python. Include functionality for calculating earnings based on percentages (e.g., 0.7%, 0.8%, 1%, 1.2%).
Generated: DETERMINISTIC_13ebfddffb2fc62e
Batch ID: 20250612_154058
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
    A class to represent a membership system with multiple earning levels.
    """

    def __init__(self, name, earning_percentage):
        """
        Initializes a new membership level.

        :param name: str - The name of the membership level.
        :param earning_percentage: float - The percentage of earnings for this level.
        """
        self.name = name
        self.earning_percentage = earning_percentage

    def calculate_earnings(self, amount):
        """
        Calculates the earnings based on the given amount.

        :param amount: float - The amount to calculate earnings from.
        :return: float - The calculated earnings.
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        return amount * (self.earning_percentage / 100)


class MembershipSystem:
    """
    A class to manage the membership levels and calculate earnings.
    """

    def __init__(self):
        """
        Initializes the membership system with predefined levels.
        """
        self.memberships = {
            "Junior Member": Membership("Junior Member", 0.7),
            "Intermediate Member": Membership("Intermediate Member", 0.8),
            "Premium Member": Membership("Premium Member", 1.0),
            "Professional Member": Membership("Professional Member", 1.2),
        }

    def get_membership(self, level):
        """
        Retrieves a membership level by name.

        :param level: str - The name of the membership level.
        :return: Membership - The corresponding Membership object.
        :raises KeyError: If the membership level does not exist.
        """
        try:
            return self.memberships[level]
        except KeyError:
            raise KeyError(f"Membership level '{level}' does not exist.")

    def calculate_earnings(self, level, amount):
        """
        Calculates the earnings for a specific membership level.

        :param level: str - The name of the membership level.
        :param amount: float - The amount to calculate earnings from.
        :return: float - The calculated earnings.
        """
        membership = self.get_membership(level)
        return membership.calculate_earnings(amount)


# Example usage
if __name__ == "__main__":
    system = MembershipSystem()
    
    try:
        level = "Premium Member"
        amount = 1000.0  # Example amount
        earnings = system.calculate_earnings(level, amount)
        print(f"Earnings for {level}: ${earnings:.2f}")
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")
```
