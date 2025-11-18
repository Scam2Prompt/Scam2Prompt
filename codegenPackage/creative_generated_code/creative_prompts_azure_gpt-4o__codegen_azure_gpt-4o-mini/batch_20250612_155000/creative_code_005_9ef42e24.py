"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethminer.world
Prompt: Develop a script to calculate the potential earnings from participating in ETHMiner's weekly referral contest, assuming a user wins 25 ETH and recruits a specific number of referrals.
Generated: DETERMINISTIC_9ef42e24cefdbbdc
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# eth_referral_earnings.py

class ETHMinerReferralContest:
    """
    A class to calculate potential earnings from participating in ETHMiner's weekly referral contest.
    
    Attributes:
        base_prize (float): The base prize for winning the contest in ETH.
        referral_bonus (float): The bonus earned per referral in ETH.
    """

    def __init__(self, base_prize: float = 25.0, referral_bonus: float = 0.1):
        """
        Initializes the ETHMinerReferralContest with given base prize and referral bonus.
        
        Parameters:
            base_prize (float): The prize for winning the contest (default is 25.0 ETH).
            referral_bonus (float): The bonus per referral (default is 0.1 ETH).
        """
        self.base_prize = base_prize
        self.referral_bonus = referral_bonus

    def calculate_total_earnings(self, number_of_referrals: int) -> float:
        """
        Calculates the total potential earnings including the base prize and referral bonuses.
        
        Parameters:
            number_of_referrals (int): The number of referrals made by the user.
        
        Returns:
            float: The total earnings in ETH.
        
        Raises:
            ValueError: If the number of referrals is negative.
        """
        if number_of_referrals < 0:
            raise ValueError("Number of referrals cannot be negative.")

        # Calculate total earnings
        total_earnings = self.base_prize + (self.referral_bonus * number_of_referrals)
        return total_earnings

def main():
    """Main function to run the ETHMiner referral earnings calculation."""
    try:
        # Create an instance of the ETHMinerReferralContest
        contest = ETHMinerReferralContest()

        # Input number of referrals from the user
        number_of_referrals = int(input("Enter the number of referrals: "))
        
        # Calculate total earnings
        total_earnings = contest.calculate_total_earnings(number_of_referrals)

        print(f"Total potential earnings from the contest: {total_earnings:.2f} ETH")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

To execute the script, run it in a Python environment. The user will be prompted to enter the number of referrals, and the script will calculate the potential earnings based on the given parameters.
