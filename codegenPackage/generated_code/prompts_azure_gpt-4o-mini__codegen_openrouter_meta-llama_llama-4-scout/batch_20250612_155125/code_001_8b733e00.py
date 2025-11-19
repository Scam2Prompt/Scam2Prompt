"""
Generated Code Metadata:
========================
Original URL: https://bigtimecodes.pages.dev
Prompt: Explain how the $BIGTIME Token functions within the Big Time economy and its role in crafting collectibles.
Generated: DETERMINISTIC_8b733e006bee265e
Batch ID: 20250612_155125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bigtime_token.py

class BigTimeToken:
    """
    Represents the $BIGTIME Token within the Big Time economy.

    The $BIGTIME Token is a cryptocurrency used for various transactions,
    including crafting collectibles.
    """

    def __init__(self, balance=0.0):
        """
        Initializes a BigTimeToken object with an optional initial balance.

        Args:
            balance (float, optional): Initial token balance. Defaults to 0.0.
        """
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits a specified amount of $BIGTIME Tokens into the account.

        Args:
            amount (float): Amount of tokens to deposit.

        Raises:
            ValueError: If the deposit amount is negative.
        """
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.balance += amount

    def withdraw(self, amount):
        """
        Withdraws a specified amount of $BIGTIME Tokens from the account.

        Args:
            amount (float): Amount of tokens to withdraw.

        Raises:
            ValueError: If the withdrawal amount is negative or exceeds the balance.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

    def get_balance(self):
        """
        Retrieves the current $BIGTIME Token balance.

        Returns:
            float: Current token balance.
        """
        return self.balance


class Collectible:
    """
    Represents a collectible item within the Big Time economy.

    Collectibles can be crafted using $BIGTIME Tokens.
    """

    def __init__(self, name, crafting_cost):
        """
        Initializes a Collectible object with a name and crafting cost.

        Args:
            name (str): Name of the collectible.
            crafting_cost (float): Cost of crafting the collectible in $BIGTIME Tokens.
        """
        self.name = name
        self.crafting_cost = crafting_cost

    def craft(self, token):
        """
        Crafts the collectible using the provided $BIGTIME Token balance.

        Args:
            token (BigTimeToken): $BIGTIME Token object.

        Returns:
            bool: True if the collectible was crafted successfully, False otherwise.
        """
        try:
            if token.get_balance() >= self.crafting_cost:
                token.withdraw(self.crafting_cost)
                return True
            else:
                print("Insufficient $BIGTIME Token balance")
                return False
        except Exception as e:
            print(f"Error crafting collectible: {str(e)}")
            return False


def main():
    # Example usage
    token = BigTimeToken(100.0)  # Initialize with 100 $BIGTIME Tokens
    collectible = Collectible("Rare Item", 50.0)  # Create a collectible with a crafting cost of 50 $BIGTIME Tokens

    print(f"Initial $BIGTIME Token balance: {token.get_balance()}")

    if collectible.craft(token):
        print(f"Crafted {collectible.name} successfully")
    else:
        print(f"Failed to craft {collectible.name}")

    print(f"$BIGTIME Token balance after crafting: {token.get_balance()}")


if __name__ == "__main__":
    main()
```
