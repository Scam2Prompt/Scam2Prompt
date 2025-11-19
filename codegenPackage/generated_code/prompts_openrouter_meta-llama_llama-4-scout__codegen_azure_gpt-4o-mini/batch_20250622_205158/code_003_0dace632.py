"""
Generated Code Metadata:
========================
Original URL: https://meversedex.gitbook.io
Prompt: How does MEVerse DEX plan to secure long-term value with liquidity, and what role does the DAO fund play in this process?
Generated: DETERMINISTIC_0dace6329d931658
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MEVerseDEX:
    """
    A class to represent the MEVerse Decentralized Exchange (DEX) and its liquidity management.
    """

    def __init__(self):
        """
        Initializes the MEVerse DEX with an empty liquidity pool and a DAO fund.
        """
        self.liquidity_pool = {}
        self.dao_fund = 0.0

    def add_liquidity(self, token: str, amount: float) -> None:
        """
        Adds liquidity to the DEX.

        Parameters:
        token (str): The token to add liquidity for.
        amount (float): The amount of liquidity to add.

        Raises:
        ValueError: If the amount is non-positive.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        if token in self.liquidity_pool:
            self.liquidity_pool[token] += amount
        else:
            self.liquidity_pool[token] = amount

        print(f"Added {amount} of {token} to liquidity pool.")

    def remove_liquidity(self, token: str, amount: float) -> None:
        """
        Removes liquidity from the DEX.

        Parameters:
        token (str): The token to remove liquidity for.
        amount (float): The amount of liquidity to remove.

        Raises:
        ValueError: If the amount is non-positive or exceeds available liquidity.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if token not in self.liquidity_pool or self.liquidity_pool[token] < amount:
            raise ValueError("Insufficient liquidity to remove.")

        self.liquidity_pool[token] -= amount
        print(f"Removed {amount} of {token} from liquidity pool.")

    def allocate_dao_fund(self, amount: float) -> None:
        """
        Allocates funds to the DAO fund.

        Parameters:
        amount (float): The amount to allocate to the DAO fund.

        Raises:
        ValueError: If the amount is non-positive.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        self.dao_fund += amount
        print(f"Allocated {amount} to DAO fund.")

    def get_liquidity(self, token: str) -> float:
        """
        Retrieves the current liquidity for a specific token.

        Parameters:
        token (str): The token to check liquidity for.

        Returns:
        float: The amount of liquidity available for the specified token.
        """
        return self.liquidity_pool.get(token, 0.0)

    def get_dao_fund(self) -> float:
        """
        Retrieves the current amount in the DAO fund.

        Returns:
        float: The amount currently in the DAO fund.
        """
        return self.dao_fund


# Example usage
if __name__ == "__main__":
    dex = MEVerseDEX()

    try:
        dex.add_liquidity("ETH", 10.0)
        dex.add_liquidity("BTC", 5.0)
        dex.remove_liquidity("ETH", 2.0)
        dex.allocate_dao_fund(100.0)

        print(f"Current ETH liquidity: {dex.get_liquidity('ETH')}")
        print(f"Current DAO fund: {dex.get_dao_fund()}")
    except ValueError as e:
        print(f"Error: {e}")
```
