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
class ReferralProgram:
    def __init__(self):
        """
        Initializes the Referral Program with an empty referral tracking dictionary.
        """
        self.referrals = {}  # Dictionary to track referrals and rewards

    def add_referral(self, referrer, referee):
        """
        Adds a new referral to the tracking system.

        Parameters:
        referrer (str): The identifier of the person who referred another user.
        referee (str): The identifier of the newly referred user.

        Raises:
        ValueError: If the referrer and referee are the same.
        """
        if referrer == referee:
            raise ValueError("Referrer and referee cannot be the same.")
        
        if referrer not in self.referrals:
            self.referrals[referrer] = {'count': 0, 'reward': 0}

        # Increment the referral count for the referrer
        self.referrals[referrer]['count'] += 1
        self.referrals[referrer]['reward'] += self.calculate_reward()
        
        print(f"Referral added: {referrer} referred {referee}. Total referrals: {self.referrals[referrer]['count']}.")

    def calculate_reward(self):
        """
        Calculates the reward for each successful referral.

        Returns:
        int: The reward amount for a single referral.
        """
        return 10  # Fixed reward amount for simplicity

    def get_referrer_info(self, referrer):
        """
        Retrieves the referral information for a given referrer.

        Parameters:
        referrer (str): The identifier of the referrer.

        Returns:
        dict: A dictionary containing the count of referrals and total rewards.

        Raises:
        KeyError: If the referrer is not found in the tracking system.
        """
        if referrer not in self.referrals:
            raise KeyError(f"No information found for referrer: {referrer}")
        
        return self.referrals[referrer]

    def display_all_referrals(self):
        """
        Displays all referrals and their corresponding rewards.
        """
        if not self.referrals:
            print("No referrals have been made yet.")
            return
        
        print("Referrer Information:")
        for referrer, info in self.referrals.items():
            print(f"Referrer: {referrer}, Referrals Count: {info['count']}, Total Reward: ${info['reward']}")

# Example usage
if __name__ == "__main__":
    referral_program = ReferralProgram()
    
    try:
        referral_program.add_referral("user1", "user2")
        referral_program.add_referral("user1", "user3")
        referral_program.add_referral("user2", "user4")
        
        referral_program.display_all_referrals()

        # Get information for a specific referrer
        info = referral_program.get_referrer_info("user1")
        print(f"User1 Info: {info}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except KeyError as ke:
        print(f"KeyError: {ke}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
