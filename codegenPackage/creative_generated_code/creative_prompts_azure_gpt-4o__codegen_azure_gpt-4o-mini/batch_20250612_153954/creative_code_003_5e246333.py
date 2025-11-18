"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-stacks.com
Prompt: Create a function that checks eligibility for staking on Illuvium based on user input and the staking criteria outlined on the Illuvium website.
Generated: DETERMINISTIC_5e2463336b0c20e9
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingEligibilityChecker:
    """
    A class to check the staking eligibility for Illuvium based on user input
    and the staking criteria outlined on the Illuvium website.
    """

    def __init__(self, min_stake: float, has_nft: bool):
        """
        Initializes the StakingEligibilityChecker with required staking criteria.

        :param min_stake: Minimum stake amount required to be eligible.
        :param has_nft: Boolean indicating if the user owns an NFT.
        """
        self.min_stake = min_stake
        self.has_nft = has_nft

    def check_eligibility(self, user_stake: float) -> str:
        """
        Checks if the user is eligible for staking based on their input.

        :param user_stake: The amount the user wants to stake.
        :return: Eligibility message.
        """
        try:
            if user_stake < 0:
                raise ValueError("Stake amount cannot be negative.")

            if user_stake < self.min_stake:
                return f"Eligibility check failed: You need to stake at least {self.min_stake} ILV."

            if not self.has_nft:
                return "Eligibility check failed: You must own at least one Illuvium NFT."

            return "Congratulations! You are eligible to stake your ILV."

        except ValueError as e:
            return f"Error in eligibility check: {str(e)}"

def main():
    """
    Main function to execute the staking eligibility check.
    """
    # Sample criteria from Illuvium website (assumed values)
    MIN_STAKE = 10.0  # Minimum stake amount in ILV
    HAS_NFT = True     # User must own an NFT

    # User input (this could be gathered from a user interface)
    user_stake = float(input("Enter the amount you wish to stake (in ILV): "))

    # Create an instance of the eligibility checker
    eligibility_checker = StakingEligibilityChecker(MIN_STAKE, HAS_NFT)

    # Check eligibility
    eligibility_message = eligibility_checker.check_eligibility(user_stake)

    # Output the result
    print(eligibility_message)

if __name__ == "__main__":
    main()
```
