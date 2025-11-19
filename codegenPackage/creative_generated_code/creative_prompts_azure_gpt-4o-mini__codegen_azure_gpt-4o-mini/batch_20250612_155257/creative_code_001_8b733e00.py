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

```python
class BigTimeEconomy:
    """
    Represents the Big Time economy, managing the $BIGTIME token and its role in crafting collectibles.
    """

    def __init__(self):
        """
        Initialize the Big Time economy with a balance of the $BIGTIME token.
        """
        self.bigtime_balance = 0.0
        self.collectibles = {}

    def mint_collectible(self, name: str, cost: float) -> None:
        """
        Mint a new collectible using $BIGTIME tokens.

        Args:
            name (str): The name of the collectible to be minted.
            cost (float): The cost in $BIGTIME tokens to mint the collectible.

        Raises:
            ValueError: If the cost exceeds the user's balance.
        """
        if cost > self.bigtime_balance:
            raise ValueError("Insufficient $BIGTIME balance to mint collectible.")

        # Deduct the cost from the balance
        self.bigtime_balance -= cost
        # Add the collectible to the user's collection
        self.collectibles[name] = "Minted"
        print(f"Collectible '{name}' minted for {cost} $BIGTIME.")

    def add_funds(self, amount: float) -> None:
        """
        Add $BIGTIME tokens to the user's balance.

        Args:
            amount (float): The amount of $BIGTIME tokens to add.

        Raises:
            ValueError: If amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount must be a positive value.")

        self.bigtime_balance += amount
        print(f"Added {amount} $BIGTIME to balance. New balance: {self.bigtime_balance}")

    def get_balance(self) -> float:
        """
        Return the current balance of $BIGTIME tokens.

        Returns:
            float: The current balance.
        """
        return self.bigtime_balance

    def list_collectibles(self) -> None:
        """
        List all collectibles owned by the user.
        """
        if not self.collectibles:
            print("No collectibles owned.")
        else:
            print("Collectibles owned:")
            for name, status in self.collectibles.items():
                print(f"- {name}: {status}")

# Example usage:
if __name__ == "__main__":
    try:
        economy = BigTimeEconomy()
        economy.add_funds(100.0)  # Adding funds to the wallet
        economy.mint_collectible("Rare Sword", 20.0)  # Minting a collectible
        economy.mint_collectible("Epic Shield", 30.0)  # Minting another collectible
        economy.list_collectibles()  # Listing all collectibles
        print(f"Current balance: {economy.get_balance()} $BIGTIME")  # Checking balance
    except ValueError as e:
        print(f"Error: {e}")
```
