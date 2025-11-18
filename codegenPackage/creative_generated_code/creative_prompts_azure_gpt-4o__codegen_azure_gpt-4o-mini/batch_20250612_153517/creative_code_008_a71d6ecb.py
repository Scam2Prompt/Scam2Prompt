"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scapemania-0x2eca5.pages.dev
Prompt: Develop a function that validates referral transactions and updates the referral statistics, ensuring compliance with the referral program rules.
Generated: DETERMINISTIC_a71d6ecb16769e14
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralTransactionError(Exception):
    """Custom exception for invalid referral transactions."""
    pass

class ReferralProgram:
    def __init__(self):
        # Initialize referral statistics
        self.referral_counts = {}
        self.referral_rewards = {}

    def validate_transaction(self, user_id, referral_code):
        """
        Validate the referral transaction based on user ID and referral code.
        
        Parameters:
            user_id (str): The ID of the user making the referral.
            referral_code (str): The referral code being used.

        Raises:
            ReferralTransactionError: If the transaction is invalid.
        """
        if not isinstance(user_id, str) or not isinstance(referral_code, str):
            raise ReferralTransactionError("User ID and referral code must be strings.")
        
        # Check if the referral code exists in the referral counts
        if referral_code not in self.referral_counts:
            raise ReferralTransactionError(f"Referral code {referral_code} does not exist.")

        # Dummy check for the user (this could be expanded to check if the user already used the code)
        if user_id in self.referral_rewards:
            raise ReferralTransactionError("User has already used a referral code.")

    def update_referral_statistics(self, user_id, referral_code):
        """
        Update the referral statistics upon successful transaction validation.
        
        Parameters:
            user_id (str): The ID of the user making the referral.
            referral_code (str): The referral code being used.
        """
        try:
            # Validate the transaction
            self.validate_transaction(user_id, referral_code)
            
            # Update referral counts
            if referral_code in self.referral_counts:
                self.referral_counts[referral_code] += 1
            else:
                self.referral_counts[referral_code] = 1

            # Track rewards for the user
            self.referral_rewards[user_id] = referral_code
            
            print(f"Referral transaction successful for user {user_id} using code {referral_code}.")
        except ReferralTransactionError as e:
            print(f"Transaction failed: {e}")

# Example usage:
if __name__ == "__main__":
    referral_program = ReferralProgram()
    
    # Initialize some referral codes
    referral_program.referral_counts['CODE123'] = 0
    referral_program.referral_counts['CODE456'] = 0

    # Simulate a referral transaction
    referral_program.update_referral_statistics('user1', 'CODE123')
    referral_program.update_referral_statistics('user2', 'CODE123')  # should succeed
    referral_program.update_referral_statistics('user1', 'CODE456')  # should fail (already used)
    referral_program.update_referral_statistics('user3', 'CODE789')  # should fail (code does not exist)
```
