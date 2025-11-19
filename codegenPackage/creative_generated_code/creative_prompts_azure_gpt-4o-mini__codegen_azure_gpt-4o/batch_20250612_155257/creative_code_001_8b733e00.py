"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ai-bigtime.pages.dev
Prompt: Explain how the $BIGTIME Token functions within the Big Time economy and its role in crafting collectibles.
Generated: DETERMINISTIC_8b733e006bee265e
Batch ID: 20250612_155257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation that provides a clean, well-documented explanation of the `$BIGTIME Token` and its functionality within the Big Time economy. 

```python
"""
Big Time Economy Simulation
This script defines the $BIGTIME Token and its role in crafting collectibles within the Big Time ecosystem.
"""

class BigTimeToken:
    """
    Represents the $BIGTIME Token in the Big Time economy.
    This token is used for crafting collectibles and other transactions.
    """

    def __init__(self, initial_supply: float):
        """
        Initialize the $BIGTIME Token with a given supply.

        :param initial_supply: The initial supply of $BIGTIME Tokens in the economy.
        """
        if initial_supply <= 0:
            raise ValueError("Initial supply must be greater than zero.")
        self.total_supply = initial_supply
        self.balance_sheet = {}  # Tracks balances of individual users {user_id: balance}

    def mint_tokens(self, user_id: str, amount: float):
        """
        Mint new $BIGTIME Tokens and assign them to a user.

        :param user_id: The ID of the user receiving the tokens.
        :param amount: The amount of tokens to mint.
        """
        if amount <= 0:
            raise ValueError("Mint amount must be greater than zero.")
        self.total_supply += amount
        self.balance_sheet[user_id] = self.balance_sheet.get(user_id, 0) + amount

    def transfer_tokens(self, sender_id: str, receiver_id: str, amount: float):
        """
        Transfer $BIGTIME Tokens from one user to another.

        :param sender_id: The ID of the user sending the tokens.
        :param receiver_id: The ID of the user receiving the tokens.
        :param amount: The amount of tokens to transfer.
        """
        if amount <= 0:
            raise ValueError("Transfer amount must be greater than zero.")
        if sender_id not in self.balance_sheet or self.balance_sheet[sender_id] < amount:
            raise ValueError("Sender has insufficient balance.")
        # Perform the transfer
        self.balance_sheet[sender_id] -= amount
        self.balance_sheet[receiver_id] = self.balance_sheet.get(receiver_id, 0) + amount

    def get_balance(self, user_id: str) -> float:
        """
        Get the balance of $BIGTIME Tokens for a given user.

        :param user_id: The ID of the user.
        :return: The balance of tokens for the user.
        """
        return self.balance_sheet.get(user_id, 0)


class Collectible:
    """
    Represents a collectible item in the Big Time economy.
    Collectibles are crafted using $BIGTIME Tokens.
    """

    def __init__(self, name: str, crafting_cost: float):
        """
        Initialize a collectible with a name and crafting cost.

        :param name: The name of the collectible.
        :param crafting_cost: The cost in $BIGTIME Tokens to craft the collectible.
        """
        if crafting_cost <= 0:
            raise ValueError("Crafting cost must be greater than zero.")
        self.name = name
        self.crafting_cost = crafting_cost
        self.owner = None  # Owner of the collectible

    def craft(self, user_id: str, token_system: BigTimeToken):
        """
        Craft the collectible using $BIGTIME Tokens.

        :param user_id: The ID of the user crafting the collectible.
        :param token_system: The BigTimeToken system for managing tokens.
        """
        user_balance = token_system.get_balance(user_id)
        if user_balance < self.crafting_cost:
            raise ValueError("Insufficient $BIGTIME Tokens to craft the collectible.")
        # Deduct tokens and assign ownership
        token_system.transfer_tokens(user_id, "BigTimeTreasury", self.crafting_cost)
        self.owner = user_id


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the $BIGTIME Token system with 1000 tokens
        bigtime_token = BigTimeToken(initial_supply=1000)

        # Mint tokens for two users
        bigtime_token.mint_tokens("user1", 500)
        bigtime_token.mint_tokens("user2", 300)

        # Create a collectible that costs 200 $BIGTIME Tokens to craft
        sword = Collectible(name="Epic Sword", crafting_cost=200)

        # User1 crafts the collectible
        sword.craft(user_id="user1", token_system=bigtime_token)

        # Display results
        print(f"Collectible '{sword.name}' crafted by {sword.owner}.")
        print(f"User1 Balance: {bigtime_token.get_balance('user1')}")
        print(f"BigTime Treasury Balance: {bigtime_token.get_balance('BigTimeTreasury')}")

    except ValueError as e:
        print(f"Error: {e}")
```

### Features:
- The `$BIGTIME Token` system manages token supply, minting, transferring, and balances.
- Collectibles are crafted using `$BIGTIME Tokens`, which are deducted from the user's balance and transferred to the treasury.
- Includes error handling for invalid inputs such as insufficient balances or negative values.
- Demonstrates the crafting process of a collectible by a user.
