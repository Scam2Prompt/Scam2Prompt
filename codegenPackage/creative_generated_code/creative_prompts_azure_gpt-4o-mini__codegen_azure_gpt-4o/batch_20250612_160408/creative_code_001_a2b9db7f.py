"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assets-telcoin.org
Prompt: Write a code snippet to implement $TEL rewards voting functionality in a Telcoin Wallet application.
Generated: DETERMINISTIC_a2b9db7f354dd079
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List

class TelcoinWallet:
    """
    TelcoinWallet class to manage TEL rewards voting functionality.
    """
    def __init__(self, user_id: str, balance: float):
        """
        Initialize the wallet with user ID and balance.

        :param user_id: Unique identifier for the user.
        :param balance: TEL balance in the wallet.
        """
        self.user_id = user_id
        self.balance = balance
        self.votes = {}

    def cast_vote(self, reward_id: str, vote_amount: float):
        """
        Allows the user to cast a vote for a reward.

        :param reward_id: Unique identifier for the reward being voted for.
        :param vote_amount: Amount of TEL used to cast the vote.
        :raises ValueError: If vote_amount is invalid or exceeds balance.
        """
        if vote_amount <= 0:
            raise ValueError("Vote amount must be greater than zero.")
        if vote_amount > self.balance:
            raise ValueError("Insufficient TEL balance to cast the vote.")

        # Deduct the vote amount from the user's balance
        self.balance -= vote_amount

        # Add the vote to the votes dictionary
        if reward_id in self.votes:
            self.votes[reward_id] += vote_amount
        else:
            self.votes[reward_id] = vote_amount

    def get_votes(self) -> dict:
        """
        Returns the current votes cast by the user.

        :return: Dictionary containing reward IDs and their respective vote amounts.
        """
        return self.votes

    def get_balance(self) -> float:
        """
        Returns the current TEL balance in the wallet.

        :return: TEL balance as a float.
        """
        return self.balance


def display_rewards(rewards: List[dict]):
    """
    Displays the available rewards for voting.

    :param rewards: List of rewards, each represented as a dictionary
                    with 'id' and 'description' keys.
    """
    print("Available Rewards:")
    for reward in rewards:
        print(f"ID: {reward['id']}, Description: {reward['description']}")


def main():
    """
    Main function to simulate TEL rewards voting functionality.
    """
    # Sample rewards data
    rewards_data = [
        {"id": "reward1", "description": "Reward 1 - Cashback Bonus"},
        {"id": "reward2", "description": "Reward 2 - Lower Transaction Fees"},
        {"id": "reward3", "description": "Reward 3 - Special Promotions"}
    ]

    # Display available rewards
    display_rewards(rewards_data)

    # Initialize wallet for a user
    user_wallet = TelcoinWallet(user_id="user123", balance=100.0)

    try:
        # Simulate user voting
        user_wallet.cast_vote(reward_id="reward1", vote_amount=20.0)
        user_wallet.cast_vote(reward_id="reward2", vote_amount=50.0)

        # Display user votes and remaining balance
        print("\nVotes Cast:")
        print(json.dumps(user_wallet.get_votes(), indent=2))
        print(f"Remaining Balance: {user_wallet.get_balance()} TEL")
    except ValueError as e:
        # Handle errors during voting
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
