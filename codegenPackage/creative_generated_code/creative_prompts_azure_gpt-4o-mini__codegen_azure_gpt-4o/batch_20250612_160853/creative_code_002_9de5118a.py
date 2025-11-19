"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbags.pages.dev
Prompt: Explain the referral program for MoonBag and how to implement a system to track referrals and rewards.
Generated: DETERMINISTIC_9de5118acf0bc8cd
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Referral Program Implementation for MoonBag
This script tracks referrals and rewards for users in a referral program.
Each user has their own referral code, and when someone signs up using
their code, they earn rewards. The system includes mechanisms to track referrals,
manage rewards, and handle edge cases.
"""

import uuid


class ReferralProgram:
    """
    Class to implement the referral program logic for MoonBag.
    Tracks users, referrals, and rewards.
    """

    def __init__(self):
        # Initialize data structures to store user and referral information
        self.users = {}  # Stores user data: {user_id: {"name": str, "ref_code": str, "reward_balance": float}}
        self.referrals = {}  # Tracks referrals: {ref_code: [list_of_user_ids]}
        self.reward_per_referral = 10.0  # Reward value per successful referral

    def generate_referral_code(self):
        """
        Generate a unique referral code for a user.
        Returns:
            str: A unique referral code.
        """
        return str(uuid.uuid4())[:8]  # Use UUID to ensure uniqueness, truncated for readability

    def register_user(self, name):
        """
        Register a new user in the referral program.
        Args:
            name (str): Name of the user.
        Returns:
            dict: User registration details.
        """
        try:
            user_id = str(uuid.uuid4())  # Generate a unique user ID
            ref_code = self.generate_referral_code()  # Generate a referral code
            self.users[user_id] = {"name": name, "ref_code": ref_code, "reward_balance": 0.0}
            self.referrals[ref_code] = []  # Initialize referral tracking for the code
            return {"user_id": user_id, "ref_code": ref_code}
        except Exception as e:
            # Handle unexpected errors during user registration
            print(f"Error registering user: {e}")
            return None

    def use_referral_code(self, ref_code, new_user_name):
        """
        Register a new user using a referral code and update rewards.
        Args:
            ref_code (str): Referral code used by the new user.
            new_user_name (str): Name of the new user.
        Returns:
            dict: New user details if successful, else None.
        """
        try:
            if ref_code not in self.referrals:
                print("Invalid referral code.")
                return None

            # Register the new user
            new_user = self.register_user(new_user_name)
            if new_user:
                new_user_id = new_user["user_id"]
                self.referrals[ref_code].append(new_user_id)  # Track referral

                # Find the user who owns the referral code and update their rewards
                for user_id, user_data in self.users.items():
                    if user_data["ref_code"] == ref_code:
                        self.users[user_id]["reward_balance"] += self.reward_per_referral
                        break

                return new_user
            else:
                print("Failed to register new user.")
                return None
        except Exception as e:
            print(f"Error processing referral code: {e}")
            return None

    def get_user_details(self, user_id):
        """
        Retrieve details of a specific user.
        Args:
            user_id (str): ID of the user.
        Returns:
            dict: User details if found, else None.
        """
        return self.users.get(user_id, None)

    def get_referral_stats(self, ref_code):
        """
        Get statistics for a specific referral code.
        Args:
            ref_code (str): Referral code to query.
        Returns:
            dict: Statistics for the referral code.
        """
        try:
            referral_list = self.referrals.get(ref_code, [])
            return {"ref_code": ref_code, "total_referrals": len(referral_list), "referrals": referral_list}
        except Exception as e:
            print(f"Error retrieving referral stats: {e}")
            return None


# Example Usage
if __name__ == "__main__":
    program = ReferralProgram()

    # Register initial users
    user1 = program.register_user("Alice")
    user2 = program.register_user("Bob")

    print("Initial Users:")
    print(user1)
    print(user2)

    # New user uses Alice's referral code
    new_user = program.use_referral_code(user1["ref_code"], "Charlie")
    print("\nNew User Registered via Referral:")
    print(new_user)

    # Retrieve user details
    print("\nUser Details:")
    print(program.get_user_details(user1["user_id"]))

    # Retrieve referral stats
    print("\nReferral Stats:")
    print(program.get_referral_stats(user1["ref_code"]))
```
