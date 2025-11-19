"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wieneraidog.pages.dev
Prompt: How can I implement daily staking rewards for an AI project similar to WienerAI?
Generated: DETERMINISTIC_929aa5388f9f3ec0
Batch ID: 20250612_162632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# daily_staking_rewards.py

from datetime import datetime, timedelta
from decimal import Decimal, getcontext
import json

# Set the precision for decimal operations
getcontext().prec = 6  # Adjust precision as needed

class StakingAccount:
    """Class representing a staking account for daily rewards."""

    def __init__(self, account_id, stake_amount, reward_rate):
        """
        Initialize a StakingAccount instance.

        :param account_id: Unique identifier for the staking account
        :param stake_amount: Amount staked by the user
        :param reward_rate: Daily reward rate as a decimal
        """
        self.account_id = account_id
        self.stake_amount = Decimal(stake_amount)
        self.reward_rate = Decimal(reward_rate)
        self.last_reward_claimed = datetime.now() - timedelta(days=1)  # Initialize to yesterday

    def calculate_rewards(self):
        """Calculate the total rewards earned since the last claim."""
        days_since_last_claim = (datetime.now() - self.last_reward_claimed).days
        rewards = self.stake_amount * self.reward_rate * days_since_last_claim
        
        return rewards

    def claim_rewards(self):
        """Claim the rewards and reset the last claim date."""
        rewards = self.calculate_rewards()
        if rewards > 0:
            self.last_reward_claimed = datetime.now()
            return rewards
        else:
            raise ValueError("No rewards available to claim.")


def load_accounts(filename):
    """Load staking accounts from a JSON file.

    :param filename: Path to the JSON file containing account data
    :return: List of StakingAccount instances
    """
    try:
        with open(filename, 'r') as file:
            accounts_data = json.load(file)
            accounts = [
                StakingAccount(account['account_id'], account['stake_amount'], account['reward_rate'])
                for account in accounts_data
            ]
            return accounts
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading accounts: {e}")
        return []


def save_accounts(accounts, filename):
    """Save staking accounts to a JSON file.

    :param accounts: List of StakingAccount instances to save
    :param filename: Path to the JSON file to save the account data
    """
    accounts_data = [{
        'account_id': account.account_id,
        'stake_amount': str(account.stake_amount),  # Convert Decimal to string for JSON serialization
        'reward_rate': str(account.reward_rate)
    } for account in accounts]

    with open(filename, 'w') as file:
        json.dump(accounts_data, file, indent=4)


def main():
    # Load accounts from a specified JSON file
    accounts = load_accounts('accounts.json')

    # Iterate through accounts and process rewards
    for account in accounts:
        try:
            rewards = account.claim_rewards()
            print(f"Account {account.account_id} has claimed {rewards} in rewards.")
        except ValueError as e:
            print(f"Account {account.account_id}: {e}")

    # Save updated accounts back to the JSON file
    save_accounts(accounts, 'accounts.json')


if __name__ == '__main__':
    main()
```

This code provides a simple staking reward system, supporting loading from and saving to a JSON file while ensuring proper error handling and documentation. Adjust the `accounts.json` file structure accordingly for the code to run correctly.
