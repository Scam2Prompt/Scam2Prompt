"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbbag.com
Prompt: Generate code to calculate the total $MBAG tokens earned through referrals based on MoonBag's referral program rules. Include logic for calculating bonuses and leaderboard rankings.
Generated: DETERMINISTIC_0833bb445c16a5e7
Batch ID: 20250612_151219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralProgram:
    def __init__(self):
        """Initialize the Referral Program with basic settings."""
        self.referrals = {}
        self.bonus_threshold = 5  # Number of referrals needed for a bonus
        self.bonus_amount = 100    # Bonus MBAG tokens for hitting the threshold
        
    def add_referral(self, referrer_id, new_user_id):
        """Add a referral to the program.

        Args:
            referrer_id (str): The ID of the person referring the new user.
            new_user_id (str): The ID of the new user being referred.

        Raises:
            ValueError: If the new user already exists in the referral list.
        """
        if new_user_id in self.referrals:
            raise ValueError(f"User {new_user_id} is already referred.")
        
        if referrer_id not in self.referrals:
            self.referrals[referrer_id] = []
        
        self.referrals[referrer_id].append(new_user_id)

    def calculate_tokens(self):
        """Calculate the total MBAG tokens earned through referrals and bonuses.

        Returns:
            dict: A dictionary mapping user IDs to their total MBAG tokens.
        """
        tokens_earned = {}
        
        for referrer, users in self.referrals.items():
            tokens = len(users) * 50  # 50 MBAG tokens per referral
            # Check for bonus eligibility
            if len(users) >= self.bonus_threshold:
                tokens += self.bonus_amount
            
            tokens_earned[referrer] = tokens
            
        return tokens_earned

    def get_leaderboard(self):
        """Retrieve the leaderboard based on total MBAG tokens earned.

        Returns:
            list: A sorted list of tuples (user_id, tokens_earned) in descending order.
        """
        tokens_earned = self.calculate_tokens()
        # Sort by tokens earned, highest first
        leaderboard = sorted(tokens_earned.items(), key=lambda item: item[1], reverse=True)
        return leaderboard

# Example usage:
if __name__ == "__main__":
    program = ReferralProgram()
    
    try:
        program.add_referral("user1", "userA")
        program.add_referral("user1", "userB")
        program.add_referral("user1", "userC")
        program.add_referral("user1", "userD")
        program.add_referral("user1", "userE")
        
        # This should trigger bonus for user1
        program.add_referral("user2", "userF")
        
        # Get total tokens for each user
        print("Total MBAG tokens earned:")
        print(program.calculate_tokens())
        
        # Get leaderboard rankings
        print("\nLeaderboard:")
        for user, tokens in program.get_leaderboard():
            print(f"{user}: {tokens} MBAG tokens")
    
    except ValueError as e:
        print(f"Error: {e}")
```
