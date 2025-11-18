"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://goldenfundinvestment.com
Prompt: Create a referral system in Python that calculates a 10% commission for direct referrals and a 20% commission for second-level referrals, as described on goldenfundinvestment.com.
Generated: DETERMINISTIC_a3ac149918424ed8
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """
    Represents a user in the referral system.
    Each user can refer other users and earn commissions based on referrals.
    """

    def __init__(self, name, user_id):
        """
        Initializes a new user.

        :param name: The name of the user.
        :param user_id: Unique identifier for the user.
        """
        self.name = name
        self.user_id = user_id
        self.referrals = []  # Direct referrals
        self.referral_commission = 0.0  # Total commission earned

    def refer(self, user):
        """
        Refers a new user and adds them to the referral list.

        :param user: A User instance representing the referred user.
        """
        if not isinstance(user, User):
            raise ValueError("The referred user must be an instance of User.")
        self.referrals.append(user)

    def calculate_commission(self, amount, level=1):
        """
        Calculates commission based on the referral level.

        :param amount: The amount on which the commission is calculated.
        :param level: The level of referral (1 for direct, 2 for second-level).
        :return: The commission amount.
        """
        if level == 1:
            commission = amount * 0.10  # 10% for direct referrals
        elif level == 2:
            commission = amount * 0.20  # 20% for second-level referrals
        else:
            raise ValueError("Invalid referral level. Use 1 for direct and 2 for second-level.")
        
        return commission


class ReferralSystem:
    """
    Manages the overall referral system, including tracking users and calculating commissions.
    """

    def __init__(self):
        self.users = {}  # Stores users by user_id

    def add_user(self, user):
        """
        Adds a user to the referral system.

        :param user: A User instance to add.
        """
        if not isinstance(user, User):
            raise ValueError("Only User instances can be added.")
        if user.user_id in self.users:
            raise ValueError("User ID already exists.")
        self.users[user.user_id] = user

    def process_referral(self, referrer_id, referred_user):
        """
        Processes a referral made by a user.

        :param referrer_id: The user ID of the referrer.
        :param referred_user: A User instance representing the referred user.
        """
        if referrer_id not in self.users:
            raise ValueError("Referrer not found in the system.")
        
        referrer = self.users[referrer_id]
        referrer.refer(referred_user)
        self.add_user(referred_user)

    def calculate_total_commission(self, user_id, amount):
        """
        Calculates total commission earned by a user from their referrals.

        :param user_id: The user ID for whom to calculate the commission.
        :param amount: The amount on which to calculate commissions.
        :return: Total commission earned.
        """
        if user_id not in self.users:
            raise ValueError("User not found in the system.")
        
        user = self.users[user_id]
        total_commission = 0.0

        # Calculate commission for direct referrals
        for referral in user.referrals:
            total_commission += referral.calculate_commission(amount, level=1)

            # Calculate commission for second-level referrals
            for second_level_referral in referral.referrals:
                total_commission += second_level_referral.calculate_commission(amount, level=2)

        user.referral_commission = total_commission
        return total_commission


# Example usage
if __name__ == "__main__":
    # Initialize referral system
    referral_system = ReferralSystem()

    # Create users
    alice = User(name="Alice", user_id="1")
    bob = User(name="Bob", user_id="2")
    charlie = User(name="Charlie", user_id="3")

    # Add users to the system
    referral_system.add_user(alice)
    referral_system.add_user(bob)

    # Process referrals
    referral_system.process_referral(referrer_id="1", referred_user=bob)  # Alice refers Bob
    referral_system.process_referral(referrer_id="2", referred_user=charlie)  # Bob refers Charlie

    # Calculate commissions
    total_commission_for_alice = referral_system.calculate_total_commission(user_id="1", amount=1000)
    print(f"Alice's total commission: ${total_commission_for_alice:.2f}")

    total_commission_for_bob = referral_system.calculate_total_commission(user_id="2", amount=1000)
    print(f"Bob's total commission: ${total_commission_for_bob:.2f}")
```
