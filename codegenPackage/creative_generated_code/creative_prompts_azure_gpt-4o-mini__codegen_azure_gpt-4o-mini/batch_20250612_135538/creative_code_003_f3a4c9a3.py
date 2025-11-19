"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana-nft-minter-delta.vercel.app
Prompt: Explain how the Buildoors ecosystem works, focusing on minting and earning $BLD.
Generated: DETERMINISTIC_f3a4c9a3a74e9438
Batch ID: 20250612_135538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Buildoors Ecosystem Simulation

class BuildoorsEcosystem:
    def __init__(self):
        """Initialize the Buildoors ecosystem with an empty minting pool and user balances."""
        self.minting_pool = 0
        self.users = {}  # Structure: {user_id: {'balance': float, 'minted': int}}

    def mint_tokens(self, user_id, amount):
        """
        Allows a user to mint $BLD tokens.

        Args:
            user_id (str): The unique identifier for the user.
            amount (int): The number of tokens to mint.

        Raises:
            ValueError: If the amount is less than or equal to zero.
            KeyError: If the user does not exist in the ecosystem.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        if user_id not in self.users:
            raise KeyError(f"User {user_id} not found in the ecosystem.")

        # Mint the tokens
        self.minting_pool += amount
        self.users[user_id]['minted'] += amount
        print(f"{amount} $BLD minted for user {user_id}. Current minting pool: {self.minting_pool}")

    def create_user(self, user_id):
        """
        Creates a new user in the ecosystem.

        Args:
            user_id (str): The unique identifier for the user.

        Raises:
            ValueError: If the user already exists.
        """
        if user_id in self.users:
            raise ValueError(f"User {user_id} already exists.")

        # Add the user to the ecosystem
        self.users[user_id] = {'balance': 0.0, 'minted': 0}
        print(f"User {user_id} created successfully.")

    def earn_rewards(self, user_id, reward_amount):
        """
        Allows a user to earn $BLD tokens based on their minted amount.

        Args:
            user_id (str): The unique identifier for the user.
            reward_amount (float): The amount of rewards to be added.

        Raises:
            KeyError: If the user does not exist in the ecosystem.
        """
        if user_id not in self.users:
            raise KeyError(f"User {user_id} not found in the ecosystem.")

        # Update user's balance with earned rewards
        self.users[user_id]['balance'] += reward_amount
        print(f"{reward_amount} $BLD rewards added for user {user_id}. New balance: {self.users[user_id]['balance']}")

    def get_user_info(self, user_id):
        """
        Retrieve information about a user.

        Args:
            user_id (str): The unique identifier for the user.

        Returns:
            dict: User information including balance and minted tokens.

        Raises:
            KeyError: If the user does not exist in the ecosystem.
        """
        if user_id not in self.users:
            raise KeyError(f"User {user_id} not found in the ecosystem.")

        return self.users[user_id]

# Example usage
if __name__ == "__main__":
    ecosystem = BuildoorsEcosystem()
    
    # Creating users
    ecosystem.create_user("user1")
    ecosystem.create_user("user2")

    # Minting tokens
    ecosystem.mint_tokens("user1", 100)
    ecosystem.mint_tokens("user2", 150)

    # Earning rewards
    ecosystem.earn_rewards("user1", 10.0)
    ecosystem.earn_rewards("user2", 15.0)

    # Retrieving user info
    print(ecosystem.get_user_info("user1"))
    print(ecosystem.get_user_info("user2"))
```
