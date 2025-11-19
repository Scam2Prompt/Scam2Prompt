"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappallthingslemon-explorer.pages.dev
Prompt: Write a script to check eligibility for claiming airdrops in the Lemon ecosystem.
Generated: DETERMINISTIC_8fd42b173828aa9e
Batch ID: 20250612_155903
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class AirdropEligibilityChecker:
    """
    AirdropEligibilityChecker verifies user eligibility for claiming airdrops
    in the Lemon ecosystem based on predefined criteria.
    """

    def __init__(self, user_data):
        """
        Initialize the checker with user data.

        :param user_data: Dictionary containing user information.
                          Expected keys: 'wallet_balance', 'last_transaction_date',
                          'is_verified', 'wallet_creation_date'
        """
        self.user_data = user_data

    def check_eligibility(self):
        """
        Check eligibility for airdrop based on predefined rules.

        :return: Boolean indicating eligibility (True if eligible, False otherwise).
        """
        try:
            # Rule 1: Minimum wallet balance
            if self.user_data['wallet_balance'] < 10:
                return False

            # Rule 2: Wallet must be verified
            if not self.user_data['is_verified']:
                return False

            # Rule 3: Wallet must be at least 30 days old
            wallet_age = (datetime.datetime.now() - self.user_data['wallet_creation_date']).days
            if wallet_age < 30:
                return False

            # Rule 4: User must have had a transaction in the last 60 days
            last_transaction_age = (datetime.datetime.now() - self.user_data['last_transaction_date']).days
            if last_transaction_age > 60:
                return False

            # All rules passed; user is eligible
            return True

        except KeyError as e:
            # Handle missing data gracefully
            print(f"Error: Missing required user data '{e.args[0]}'")
            return False
        except Exception as e:
            # Handle any other unexpected errors
            print(f"An unexpected error occurred: {str(e)}")
            return False


# Example Usage
if __name__ == "__main__":
    # Example user data
    user_data = {
        "wallet_balance": 15,  # User's wallet balance
        "last_transaction_date": datetime.datetime(2023, 9, 1),  # Last transaction date
        "is_verified": True,  # Whether the wallet is verified
        "wallet_creation_date": datetime.datetime(2023, 7, 15)  # Wallet creation date
    }

    # Create an instance of the eligibility checker
    eligibility_checker = AirdropEligibilityChecker(user_data)

    # Check eligibility
    if eligibility_checker.check_eligibility():
        print("User is eligible for the airdrop!")
    else:
        print("User is not eligible for the airdrop.")
```
