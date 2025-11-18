"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welforcevestcapital.com
Prompt: Generate Python code for automating the referral bonus calculation based on Welforcevest Capital's multi-level referral program structure. Include logic for tracking referrals and calculating commissions.
Generated: DETERMINISTIC_0b5bca4b06e32a15
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from collections import defaultdict

class ReferralProgram:
    """
    A class to manage Welforcevest Capital's multi-level referral bonus program.
    """

    def __init__(self):
        """
        Initializes the referral program with empty user and referral data.
        """
        # Data structure to track users and their referrals
        self.users = {}  # Format: {user_id: {"name": str, "parent_id": str, "commission": float}}
        self.referrals = defaultdict(list)  # Format: {user_id: [child_user_ids]}

    def add_user(self, name, parent_id=None):
        """
        Adds a new user to the system. If parent_id is provided, the user will
        be added as a referral under the specified parent.

        Args:
            name (str): Name of the user.
            parent_id (str): ID of the parent user (optional).

        Returns:
            str: The unique ID of the newly added user.
        """
        user_id = str(uuid.uuid4())  # Generate a unique user ID
        self.users[user_id] = {
            "name": name,
            "parent_id": parent_id,
            "commission": 0.0
        }

        # Add the user as a referral to the parent, if applicable
        if parent_id:
            if parent_id in self.users:
                self.referrals[parent_id].append(user_id)
            else:
                raise ValueError(f"Parent ID {parent_id} does not exist.")

        return user_id

    def calculate_commissions(self, user_id, purchase_amount):
        """
        Calculates referral commissions for a given purchase amount based on the
        multi-level referral bonus structure.

        Args:
            user_id (str): ID of the user making the purchase.
            purchase_amount (float): The amount of the purchase.

        Returns:
            dict: A dictionary with user IDs as keys and commission amounts as values.
        """
        if user_id not in self.users:
            raise ValueError(f"User ID {user_id} does not exist.")

        # Define the referral bonus percentages for each level
        referral_bonus = [0.10, 0.05, 0.02]  # Level 1: 10%, Level 2: 5%, Level 3: 2%

        commissions = {}
        current_user_id = user_id

        # Traverse up the referral chain
        for level, bonus_percentage in enumerate(referral_bonus):
            parent_id = self.users[current_user_id]["parent_id"]
            if parent_id:
                commission = purchase_amount * bonus_percentage
                self.users[parent_id]["commission"] += commission
                commissions[parent_id] = commission
                current_user_id = parent_id
            else:
                break  # Stop if no more parent exists in the chain

        return commissions

    def get_user_details(self, user_id):
        """
        Fetches the details of a user, including their referrals and commission earned.

        Args:
            user_id (str): ID of the user.

        Returns:
            dict: A dictionary containing user details.
        """
        if user_id not in self.users:
            raise ValueError(f"User ID {user_id} does not exist.")

        user_details = self.users[user_id].copy()
        user_details["referrals"] = self.referrals[user_id]
        return user_details

    def display_user_tree(self, user_id, level=0):
        """
        Recursively displays the referral tree for a given user.

        Args:
            user_id (str): ID of the user.
            level (int): Current level in the referral tree (used for indentation).
        """
        if user_id not in self.users:
            raise ValueError(f"User ID {user_id} does not exist.")

        print(f"{'  ' * level}- {self.users[user_id]['name']} (Commission: ${self.users[user_id]['commission']:.2f})")

        for child_id in self.referrals[user_id]:
            self.display_user_tree(child_id, level + 1)


# Example usage:
if __name__ == "__main__":
    program = ReferralProgram()

    # Creating users and referrals
    alice_id = program.add_user("Alice")
    bob_id = program.add_user("Bob", parent_id=alice_id)
    charlie_id = program.add_user("Charlie", parent_id=bob_id)
    dave_id = program.add_user("Dave", parent_id=bob_id)

    # Simulate a purchase
    print("\nSimulating purchase...")
    commissions = program.calculate_commissions(charlie_id, 1000.0)
    print("Commissions distributed:", commissions)

    # Display user details and referral tree
    print("\nUser Details:")
    print(program.get_user_details(alice_id))

    print("\nReferral Tree:")
    program.display_user_tree(alice_id)
```
