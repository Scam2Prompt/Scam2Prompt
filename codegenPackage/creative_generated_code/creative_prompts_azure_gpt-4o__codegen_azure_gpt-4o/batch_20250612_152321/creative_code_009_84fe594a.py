"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://p-phantom.pages.dev
Prompt: Write code to verify user eligibility for token rewards based on wallet connection and predefined criteria, as seen in Phantom Galaxies' $ASTRAFER distribution system.
Generated: DETERMINISTIC_84fe594adf00ceb9
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class Wallet:
    def __init__(self, address, balance):
        """
        Represents a wallet object.

        :param address: The wallet's address (string).
        :param balance: The wallet's token balance (float).
        """
        self.address = address
        self.balance = balance


class TokenRewardEligibilityChecker:
    def __init__(self, minimum_balance, staking_duration_days):
        """
        Initializes the eligibility checker with predefined criteria.

        :param minimum_balance: Minimum token balance required (float).
        :param staking_duration_days: Minimum staking duration required in days (int).
        """
        self.minimum_balance = minimum_balance
        self.staking_duration_days = staking_duration_days

    def verify_eligibility(self, wallet, staking_start_timestamp):
        """
        Verifies whether a wallet is eligible for token rewards.

        :param wallet: Wallet object to verify.
        :param staking_start_timestamp: Unix timestamp representing staking start time.
        :return: Tuple (bool, str). True if eligible, False otherwise. Second value is a message.
        """
        try:
            # Ensure wallet has sufficient balance
            if wallet.balance < self.minimum_balance:
                return False, f"Wallet {wallet.address} does not meet the minimum balance criteria."

            # Ensure wallet has staked for the required duration
            current_timestamp = time.time()
            staking_duration = (current_timestamp - staking_start_timestamp) / (60 * 60 * 24)  # Convert to days
            if staking_duration < self.staking_duration_days:
                return False, f"Wallet {wallet.address} has not been staked for the required duration."

            # If both criteria are met, wallet is eligible
            return True, f"Wallet {wallet.address} is eligible for token rewards."

        except Exception as e:
            # Handle unexpected errors gracefully
            return False, f"Error verifying eligibility: {str(e)}"


# Example Usage
if __name__ == "__main__":
    # Inputs
    wallet_address = "0x123456789ABCDEF"
    wallet_balance = 500.0
    staking_start_time = time.time() - (60 * 60 * 24 * 30)  # Staked 30 days ago

    # Criteria for eligibility
    required_minimum_balance = 100.0
    required_staking_duration_days = 14

    # Instantiate wallet and eligibility checker
    user_wallet = Wallet(wallet_address, wallet_balance)
    eligibility_checker = TokenRewardEligibilityChecker(required_minimum_balance, required_staking_duration_days)

    # Verify eligibility
    is_eligible, message = eligibility_checker.verify_eligibility(user_wallet, staking_start_time)
    print(message)
```
