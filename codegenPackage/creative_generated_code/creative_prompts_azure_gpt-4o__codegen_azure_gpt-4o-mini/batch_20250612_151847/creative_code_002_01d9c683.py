"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skytrustasset.com
Prompt: Generate code to simulate the referral program described on Sky Trust ltd's website, including tracking registrations and calculating referral bonuses for three levels.
Generated: DETERMINISTIC_01d9c683c2a75000
Batch ID: 20250612_151847
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
    Class representing a user in the referral program.
    """

    def __init__(self, user_id, name):
        """
        Initialize a new user with a unique ID and a name.

        Parameters:
        - user_id: Unique identifier for the user.
        - name: The name of the user.
        """
        self.user_id = user_id
        self.name = name
        self.referrals = []  # List to keep track of referrals
        self.bonus = 0.0     # Bonus accumulated from referrals


class ReferralProgram:
    """
    Class to manage the referral program.
    """

    def __init__(self):
        """
        Initializes an empty referral program with no registered users.
        """
        self.users = {}

    def register_user(self, user_id, name, referrer_id=None):
        """
        Registers a new user in the referral program.

        Parameters:
        - user_id: Unique identifier for the user.
        - name: The name of the user.
        - referrer_id: The user ID of the referrer (optional).
        
        Returns:
        - str: Confirmation message or error message.
        """
        if user_id in self.users:
            return f"Error: User with ID {user_id} already exists."

        # Create new user
        new_user = User(user_id, name)
        self.users[user_id] = new_user

        # Handle referral
        if referrer_id and referrer_id in self.users:
            self.track_referral(referrer_id, new_user)
            
        return f"User {name} registered successfully."

    def track_referral(self, referrer_id, new_user):
        """
        Tracks a new referral for a referrer.

        Parameters:
        - referrer_id: The user ID of the referrer.
        - new_user: The new user being referred.
        """
        referrer = self.users[referrer_id]
        referrer.referrals.append(new_user)

        # Calculate bonuses for the referrer and their upline
        self.calculate_bonus(referrer)

    def calculate_bonus(self, referrer):
        """
        Calculates bonuses for the referrer and up to two levels of upline.

        Parameters:
        - referrer: The user who referred the new user.
        """
        # Bonus structure
        level_bonuses = [10.0, 5.0, 2.0]  # Bonuses for each level

        # Reward referrer
        referrer.bonus += level_bonuses[0]

        # Reward up to 2 levels of uplines
        for level in range(1, 3):
            if hasattr(referrer, 'referrer_id') and referrer.referrer_id in self.users:
                referrer = self.users[referrer.referrer_id]
                referrer.bonus += level_bonuses[level]

    def get_user_info(self, user_id):
        """
        Retrieves information about a user.

        Parameters:
        - user_id: Unique identifier for the user.

        Returns:
        - dict: User information including bonuses and referrals or error message.
        """
        user = self.users.get(user_id)

        if user:
            return {
                "user_id": user.user_id,
                "name": user.name,
                "bonus": user.bonus,
                "referrals": [ref.user_id for ref in user.referrals],
            }
        else:
            return {"error": f"User with ID {user_id} not found."}


# Example usage
if __name__ == "__main__":
    program = ReferralProgram()
    
    # Register users
    print(program.register_user("U001", "Alice"))
    print(program.register_user("U002", "Bob", referrer_id="U001"))
    print(program.register_user("U003", "Charlie", referrer_id="U002"))
    
    # Get user info
    print(program.get_user_info("U001"))
    print(program.get_user_info("U002"))
    print(program.get_user_info("U003"))
```
