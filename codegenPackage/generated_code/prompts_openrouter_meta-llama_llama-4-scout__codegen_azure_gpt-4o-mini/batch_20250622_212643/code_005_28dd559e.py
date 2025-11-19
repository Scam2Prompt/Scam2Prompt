"""
Generated Code Metadata:
========================
Original URL: https://tonstake.gitbook.io
Prompt: Design a referral program for a staking service, inspired by the TON Stake App's program, including rewards structures and terms of use.
Generated: DETERMINISTIC_28dd559eba14eca6
Batch ID: 20250622_212643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ReferralProgram:
    """
    A class to represent a referral program for a staking service.
    
    Attributes
    ----------
    referrer_rewards : dict
        A dictionary to store rewards for each referrer.
    referred_users : dict
        A dictionary to store referred users and their referrers.
    total_rewards : float
        Total rewards distributed in the program.
    """

    def __init__(self):
        """Initializes the ReferralProgram with empty records."""
        self.referrer_rewards = {}
        self.referred_users = {}
        self.total_rewards = 0.0

    def add_referral(self, referrer: str, referred: str) -> None:
        """
        Adds a referral to the program.
        
        Parameters
        ----------
        referrer : str
            The username of the referrer.
        referred : str
            The username of the referred user.
        
        Raises
        ------
        ValueError
            If the referred user is already registered.
        """
        if referred in self.referred_users:
            raise ValueError(f"User {referred} has already been referred.")
        
        self.referred_users[referred] = referrer
        self.referrer_rewards[referrer] = self.referrer_rewards.get(referrer, 0) + 10.0  # Reward for referral
        self.total_rewards += 10.0

    def get_referrer_rewards(self, referrer: str) -> float:
        """
        Retrieves the total rewards for a given referrer.
        
        Parameters
        ----------
        referrer : str
            The username of the referrer.
        
        Returns
        -------
        float
            The total rewards for the referrer.
        """
        return self.referrer_rewards.get(referrer, 0.0)

    def get_total_rewards(self) -> float:
        """
        Retrieves the total rewards distributed in the program.
        
        Returns
        -------
        float
            The total rewards distributed.
        """
        return self.total_rewards

    def display_referral_summary(self) -> None:
        """
        Displays a summary of the referral program including referrer rewards and total rewards.
        """
        print("Referral Program Summary:")
        print("--------------------------")
        for referrer, rewards in self.referrer_rewards.items():
            print(f"Referrer: {referrer}, Rewards: {rewards}")
        print(f"Total Rewards Distributed: {self.total_rewards}")


# Example usage
if __name__ == "__main__":
    referral_program = ReferralProgram()
    
    try:
        referral_program.add_referral("Alice", "Bob")
        referral_program.add_referral("Alice", "Charlie")
        referral_program.add_referral("Bob", "David")
        
        # Attempting to refer an already referred user
        referral_program.add_referral("Alice", "Bob")  # This should raise an error
        
    except ValueError as e:
        print(f"Error: {e}")

    # Displaying the summary of the referral program
    referral_program.display_referral_summary()
```
