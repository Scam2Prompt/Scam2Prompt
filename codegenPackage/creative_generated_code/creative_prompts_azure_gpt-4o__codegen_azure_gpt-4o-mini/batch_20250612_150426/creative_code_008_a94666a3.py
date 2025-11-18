"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ff-exchange.at
Prompt: Create a program to calculate referral rewards based on FF.IO's structure, including reduced fees and ongoing rewards for each referred user.
Generated: DETERMINISTIC_a94666a3e35ed7f6
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralSystem:
    """
    A class to represent a referral rewards system.
    
    Attributes
    ----------
    rewards : dict
        A dictionary storing the rewards for each referred user.
    referral_fee : float
        The percentage fee reduced for each referral.
    ongoing_reward_percentage : float
        The ongoing percentage reward for users referred.
    """

    def __init__(self, referral_fee: float = 0.1, ongoing_reward_percentage: float = 0.05):
        """
        Initializes the ReferralSystem with default fee and reward percentages.
        
        Parameters
        ----------
        referral_fee : float
            The fee reduction for each referral (default is 10%).
        ongoing_reward_percentage : float
            The ongoing reward percentage for each referred user (default is 5%).
        """
        self.rewards = {}
        self.referral_fee = referral_fee
        self.ongoing_reward_percentage = ongoing_reward_percentage

    def add_referral(self, referrer: str, referred_user: str):
        """
        Adds a referred user to the referrer’s list and rewards.
        
        Parameters
        ----------
        referrer : str
            The username of the referrer.
        referred_user : str
            The username of the referred user.
        
        Raises
        ------
        ValueError
            If the referred user is the same as the referrer.
        """
        if referrer == referred_user:
            raise ValueError("A user cannot refer themselves.")

        if referrer not in self.rewards:
            self.rewards[referrer] = {
                'referred_users': [],
                'total_reward': 0
            }

        self.rewards[referrer]['referred_users'].append(referred_user)
        self.calculate_rewards(referrer)

    def calculate_rewards(self, referrer: str):
        """
        Calculates the total rewards for the referrer based on their referred users.
        
        Parameters
        ----------
        referrer : str
            The username of the referrer.
        """
        # Simulating calculation as an example (e.g., fixed fee for simplicity)
        reward_per_user = 100  # fixed reward per referred user
        total_reward = len(self.rewards[referrer]['referred_users']) * reward_per_user

        # Adding ongoing rewards based on the number of referrals
        ongoing_reward = total_reward * self.ongoing_reward_percentage

        # Update total reward with ongoing reward
        self.rewards[referrer]['total_reward'] = total_reward + ongoing_reward

    def get_rewards(self, referrer: str) -> dict:
        """
        Retrieves the rewards for a specific referrer.
        
        Parameters
        ----------
        referrer : str
            The username of the referrer.
        
        Returns
        -------
        dict
            A dictionary containing the referred users and total rewards.
        
        Raises
        ------
        KeyError
            If the referrer does not exist in the rewards system.
        """
        if referrer not in self.rewards:
            raise KeyError("Referrer does not exist.")
        
        return self.rewards[referrer]

# Example usage
if __name__ == "__main__":
    referral_system = ReferralSystem()

    try:
        referral_system.add_referral("userA", "userB")
        referral_system.add_referral("userA", "userC")
        
        rewards_userA = referral_system.get_rewards("userA")
        print(f"Rewards for userA: {rewards_userA}")
    
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except KeyError as ke:
        print(f"KeyError: {ke}")
```
