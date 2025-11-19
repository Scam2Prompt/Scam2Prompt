"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fffrfh.pages.dev
Prompt: Describe the utility of the MOR token within the Morpheus ecosystem and how it can be used for accessing network resources.
Generated: DETERMINISTIC_7ea2704d3efc2ad2
Batch ID: 20250612_163742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MorpheusToken:
    """
    A class to represent the MOR token within the Morpheus ecosystem.

    Attributes:
        total_supply (int): The total supply of MOR tokens.
        circulating_supply (int): The currently circulating MOR tokens.
        holders (dict): A dictionary tracking the balances of token holders.
    """

    def __init__(self, total_supply):
        """
        Initializes the MOR token with total supply.

        Args:
            total_supply (int): The total supply of MOR tokens.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        self.total_supply = total_supply
        self.circulating_supply = total_supply
        self.holders = {}

    def transfer(self, to_address, amount):
        """
        Transfers MOR tokens to a specified address.

        Args:
            to_address (str): The address to transfer tokens to.
            amount (int): The number of tokens to transfer.

        Raises:
            ValueError: If the amount is invalid or exceeds the balance.
        """
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        if self.holders.get(self.address, 0) < amount:
            raise ValueError("Insufficient balance for transfer.")

        self.holders[self.address] -= amount
        self.holders[to_address] = self.holders.get(to_address, 0) + amount

    def mint(self, amount):
        """
        Mints new MOR tokens, increasing the total and circulating supply.

        Args:
            amount (int): The number of tokens to mint.

        Raises:
            ValueError: If the amount is invalid.
        """
        if amount <= 0:
            raise ValueError("Minting amount must be positive.")
        self.circulating_supply += amount
        self.total_supply += amount

    def burn(self, amount):
        """
        Burns a specified amount of MOR tokens, reducing the circulating supply.

        Args:
            amount (int): The number of tokens to burn.

        Raises:
            ValueError: If the amount is invalid or exceeds the circulating supply.
        """
        if amount <= 0:
            raise ValueError("Burn amount must be positive.")
        if self.circulating_supply < amount:
            raise ValueError("Burn amount exceeds circulating supply.")
        
        self.circulating_supply -= amount

    def register_holder(self, address, amount):
        """
        Registers a new holder of MOR tokens and assigns an initial balance.

        Args:
            address (str): The address of the new holder.
            amount (int): The initial amount of tokens to assign.

        Raises:
            ValueError: If the amount is invalid or exceeds circulating supply.
        """
        if address in self.holders:
            raise ValueError("Address already holds tokens.")
        if amount <= 0 or amount > self.circulating_supply:
            raise ValueError("Invalid amount for initial balance.")

        self.holders[address] = amount
        self.circulating_supply -= amount

    def get_balance(self, address):
        """
        Retrieves the balance of MOR tokens for a specified address.

        Args:
            address (str): The address to check the balance for.

        Returns:
            int: The balance of MOR tokens for the specified address.
        """
        return self.holders.get(address, 0)


# Example usage
if __name__ == "__main__":
    try:
        mor_token = MorpheusToken(total_supply=1000000)
        mor_token.register_holder("user1", 100)
        mor_token.transfer("user2", 50)
        print(f"User1 Balance: {mor_token.get_balance('user1')}")
        print(f"User2 Balance: {mor_token.get_balance('user2')}")
    except ValueError as e:
        print(f"Error: {e}")
```
