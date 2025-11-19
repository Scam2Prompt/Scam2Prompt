"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jieyasoft.com
Prompt: Write a Python script that simulates the commission calculation for a matrix-based direct selling model, similar to the one provided by Jieya Software.
Generated: DETERMINISTIC_7dd9317321c2430f
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python script to simulate commission calculation for a matrix-based direct selling model.

Key Features:
- Simulates a multi-level marketing (MLM) commission structure.
- Matrix-based model with levels and commissions.
- Includes error handling for invalid inputs.
- Designed to be clean, efficient, and production-ready.
"""

# Constants
MAX_LEVELS = 5  # Maximum levels in the matrix
COMMISSION_PERCENTAGES = [10, 5, 3, 2, 1]  # Commission percentages per level

class Member:
    """
    Represents a member in the MLM structure.
    Attributes:
        name (str): Name of the member.
        sales (float): Total sales made by the member.
        referrals (list): List of direct referrals (Member objects).
    """
    def __init__(self, name, sales=0):
        self.name = name
        self.sales = sales
        self.referrals = []

    def add_referral(self, referral):
        """
        Adds a direct referral to the member's referral list.
        Args:
            referral (Member): Referral to be added.
        """
        if not isinstance(referral, Member):
            raise ValueError("Referral must be an instance of Member.")
        self.referrals.append(referral)


def calculate_commission(member, level=1):
    """
    Recursively calculates the total commission earned for a member.
    Args:
        member (Member): Member whose commission is being calculated.
        level (int): Current matrix level (defaults to 1).
    Returns:
        float: Total commission earned by the member.
    """
    if level > MAX_LEVELS or not member.referrals:
        # Base case: End recursion if max levels reached or no referrals exist.
        return 0

    total_commission = 0

    for referral in member.referrals:
        # Calculate commission based on the referral's sales and current level percentage.
        level_commission = referral.sales * (COMMISSION_PERCENTAGES[level - 1] / 100)
        total_commission += level_commission

        # Recursively calculate commissions for the next level.
        total_commission += calculate_commission(referral, level + 1)

    return total_commission


def main():
    """
    Main function to simulate the MLM commission calculation.
    """
    try:
        # Create members and build the referral matrix
        alice = Member("Alice", sales=1000)
        bob = Member("Bob", sales=800)
        carol = Member("Carol", sales=500)
        dave = Member("Dave", sales=300)
        eve = Member("Eve", sales=200)

        # Build the referral structure
        alice.add_referral(bob)
        alice.add_referral(carol)
        bob.add_referral(dave)
        bob.add_referral(eve)

        # Calculate commission for Alice
        alice_commission = calculate_commission(alice)
        print(f"Total commission earned by {alice.name}: ${alice_commission:.2f}")

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
