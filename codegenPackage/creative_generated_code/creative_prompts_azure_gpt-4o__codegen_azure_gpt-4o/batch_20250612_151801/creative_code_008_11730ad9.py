"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://billionalr.com
Prompt: Write code to implement a promotional event system where users can claim bonuses like "Depo 25 Bonus 25" based on deposit amounts and membership status.
Generated: DETERMINISTIC_11730ad95b0fb72b
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class PromotionalEventSystem:
    """
    A system to manage promotional events where users can claim bonuses based on deposit amounts 
    and membership status.
    """
    def __init__(self):
        # Define promotional rules
        self.promotions = {
            "Depo 25 Bonus 25": {
                "deposit_amount": 25,
                "bonus_amount": 25,
                "membership_required": False
            }
        }
        # Store user information
        self.users = {}

    def register_user(self, user_id, is_member=False):
        """
        Registers a user in the system.

        :param user_id: Unique identifier for the user
        :param is_member: Boolean indicating if the user is a member
        """
        if user_id in self.users:
            raise ValueError(f"User with ID {user_id} is already registered.")
        
        self.users[user_id] = {
            "is_member": is_member,
            "balance": 0,
            "claimed_promotions": []
        }

    def deposit(self, user_id, amount):
        """
        Processes a deposit for the user.

        :param user_id: Unique identifier for the user
        :param amount: Deposit amount
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} is not registered.")

        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")

        self.users[user_id]["balance"] += amount

    def claim_bonus(self, user_id, promotion_name):
        """
        Allows a user to claim a promotional bonus.

        :param user_id: Unique identifier for the user
        :param promotion_name: Name of the promotion to claim
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} is not registered.")

        if promotion_name not in self.promotions:
            raise ValueError(f"Promotion '{promotion_name}' does not exist.")
        
        promotion = self.promotions[promotion_name]
        user = self.users[user_id]

        # Check if user has already claimed the promotion
        if promotion_name in user["claimed_promotions"]:
            raise ValueError(f"Promotion '{promotion_name}' has already been claimed by user {user_id}.")

        # Check membership requirement
        if promotion["membership_required"] and not user["is_member"]:
            raise ValueError(f"Promotion '{promotion_name}' requires membership.")

        # Check deposit requirement
        if user["balance"] < promotion["deposit_amount"]:
            raise ValueError(f"Insufficient balance to claim promotion '{promotion_name}'.")

        # Apply the bonus
        user["balance"] += promotion["bonus_amount"]
        user["claimed_promotions"].append(promotion_name)

    def get_user_info(self, user_id):
        """
        Retrieves the user's information.

        :param user_id: Unique identifier for the user
        :return: Dictionary containing user information
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} is not registered.")

        return self.users[user_id]


# Example usage
if __name__ == "__main__":
    try:
        system = PromotionalEventSystem()

        # Register users
        system.register_user("user123", is_member=True)
        system.register_user("user456", is_member=False)

        # Deposit money
        system.deposit("user123", 50)
        system.deposit("user456", 25)

        # Claim bonuses
        system.claim_bonus("user123", "Depo 25 Bonus 25")
        system.claim_bonus("user456", "Depo 25 Bonus 25")

        # Print user info
        print(system.get_user_info("user123"))
        print(system.get_user_info("user456"))

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
