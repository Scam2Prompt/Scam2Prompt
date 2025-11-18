"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mbdfinancials-mg.pages.dev
Prompt: Write code to implement an affiliate ambassador program for the MBD platform, including user registration, tracking referrals, and calculating rewards.
Generated: DETERMINISTIC_4c4fb35611910a60
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# affiliate_program.py

class AffiliateAmbassador:
    """
    A class to represent an affiliate ambassador in the MBD platform.
    """

    def __init__(self, ambassador_id, name, email):
        """
        Initializes the Ambassador with an ID, name, and email.
        
        :param ambassador_id: Unique identifier for the ambassador
        :param name: Name of the ambassador
        :param email: Email address of the ambassador
        """
        self.ambassador_id = ambassador_id
        self.name = name
        self.email = email
        self.referrals = []

    def add_referral(self, referral):
        """
        Add a referral to the ambassador's list of referrals.
        
        :param referral: Referral object to add
        """
        self.referrals.append(referral)

    def calculate_rewards(self):
        """
        Calculates the total rewards based on the number of referrals.
        
        :return: Total rewards earned by this ambassador
        """
        total_rewards = sum(referral.reward for referral in self.referrals)
        return total_rewards


class Referral:
    """
    A class to represent a referral made by an ambassador.
    """

    def __init__(self, referral_id, ambassador_id, reward):
        """
        Initializes the Referral with an ID, ambassador ID, and reward.
        
        :param referral_id: Unique identifier for the referral
        :param ambassador_id: ID of the ambassador who made the referral
        :param reward: Reward for this referral
        """
        self.referral_id = referral_id
        self.ambassador_id = ambassador_id
        self.reward = reward


class AffiliateProgram:
    """
    A class to manage the affiliate ambassador program.
    """

    def __init__(self):
        """
        Initializes the affiliate program with a list of ambassadors.
        """
        self.ambassadors = {}

    def register_ambassador(self, ambassador_id, name, email):
        """
        Registers a new ambassador in the program.
        
        :param ambassador_id: Unique identifier for the ambassador
        :param name: Name of the ambassador
        :param email: Email address of the ambassador
        :return: None
        """
        if ambassador_id in self.ambassadors:
            raise ValueError("Ambassador ID already exists.")
        
        self.ambassadors[ambassador_id] = AffiliateAmbassador(ambassador_id, name, email)

    def track_referral(self, ambassador_id, referral_id, reward):
        """
        Tracks a new referral made by an ambassador.
        
        :param ambassador_id: ID of the ambassador making the referral
        :param referral_id: Unique identifier for the referral
        :param reward: Reward for this referral
        :return: None
        """
        if ambassador_id not in self.ambassadors:
            raise ValueError("Ambassador not found.")
        
        referral = Referral(referral_id, ambassador_id, reward)
        self.ambassadors[ambassador_id].add_referral(referral)

    def calculate_rewards(self, ambassador_id):
        """
        Calculates the total rewards for a specific ambassador.
        
        :param ambassador_id: ID of the ambassador
        :return: Total rewards earned by the ambassador
        """
        if ambassador_id not in self.ambassadors:
            raise ValueError("Ambassador not found.")

        return self.ambassadors[ambassador_id].calculate_rewards()


# Example Usage
if __name__ == "__main__":
    program = AffiliateProgram()

    # Register ambassadors
    program.register_ambassador(1, "Alice Johnson", "alice@example.com")
    program.register_ambassador(2, "Bob Smith", "bob@example.com")

    # Track referrals
    program.track_referral(1, 101, 50)  # Alice refers a new user and earns $50
    program.track_referral(1, 102, 30)  # Alice refers another user and earns $30
    program.track_referral(2, 103, 40)  # Bob refers a user and earns $40

    # Calculate rewards
    alice_rewards = program.calculate_rewards(1)
    bob_rewards = program.calculate_rewards(2)

    print(f"Alice's Total Rewards: ${alice_rewards}")  # Output: Alice's Total Rewards: $80
    print(f"Bob's Total Rewards: ${bob_rewards}")      # Output: Bob's Total Rewards: $40
```
