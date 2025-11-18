"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-join.pages.dev
Prompt: Write a script in Python to calculate the proportional airdrop distribution based on the amount of XAVA staked during a sale, as described in the Dexalot Airdrop section.
Generated: DETERMINISTIC_dba63a6ca2adf64b
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AirdropDistribution:
    def __init__(self, total_airdrop: float, total_staked: float):
        """
        Initialize the AirdropDistribution class.

        :param total_airdrop: The total amount of tokens to be airdropped.
        :param total_staked: The total amount of XAVA staked by all participants.
        """
        if total_airdrop < 0 or total_staked < 0:
            raise ValueError("Total airdrop and total staked must be non-negative values.")
        
        self.total_airdrop = total_airdrop
        self.total_staked = total_staked

    def calculate_distribution(self, user_staked: float) -> float:
        """
        Calculate the amount of airdrop a user is entitled to based on their staked amount.

        :param user_staked: The amount of XAVA staked by the user.
        :return: The amount of airdrop the user will receive.
        """
        if user_staked < 0:
            raise ValueError("User staked amount must be a non-negative value.")
        
        if self.total_staked == 0:
            return 0.0  # No staked amount means no distribution is possible.

        # Calculate airdrop amount for the user based on their stake proportion
        user_share = user_staked / self.total_staked
        airdrop_for_user = user_share * self.total_airdrop
        
        return airdrop_for_user

def main():
    try:
        # Example values for total airdrop and total staked
        total_airdrop_amount = 10000.0  # Total tokens to be airdropped
        total_staked_amount = 50000.0    # Total XAVA staked by all participants

        airdrop_distribution = AirdropDistribution(total_airdrop_amount, total_staked_amount)
        
        # Example user stake
        user_stake = 1000.0  # Amount of XAVA staked by the user
        
        # Calculate distribution for the user
        user_airdrop = airdrop_distribution.calculate_distribution(user_stake)
        
        print(f"The user is entitled to receive {user_airdrop:.2f} tokens from the airdrop.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
