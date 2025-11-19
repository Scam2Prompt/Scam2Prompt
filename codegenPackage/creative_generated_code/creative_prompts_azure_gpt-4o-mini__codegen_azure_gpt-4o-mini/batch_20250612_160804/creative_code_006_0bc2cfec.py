"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-io.web.app
Prompt: What are the best practices for managing tokenomics in a project like DOGE20 with a fixed supply?
Generated: DETERMINISTIC_0bc2cfecbf62455e
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Tokenomics:
    def __init__(self, total_supply: int):
        """
        Initializes the Tokenomics with a fixed total supply.

        :param total_supply: Total supply of tokens (must be a positive integer).
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        self.total_supply = total_supply
        self.circulating_supply = 0
        self.holders = {}

    def mint_tokens(self, address: str, amount: int):
        """
        Mints tokens to a specific address.

        :param address: The address to receive the tokens.
        :param amount: The amount of tokens to mint (must be positive).
        :raises ValueError: If amount is less than or equal to zero or if minting exceeds total supply.
        """
        if amount <= 0:
            raise ValueError("Amount must be a positive integer.")
        if self.circulating_supply + amount > self.total_supply:
            raise ValueError("Minting exceeds total supply.")

        self.circulating_supply += amount
        self.holders[address] = self.holders.get(address, 0) + amount

    def burn_tokens(self, address: str, amount: int):
        """
        Burns tokens from a specific address.

        :param address: The address from which to burn tokens.
        :param amount: The amount of tokens to burn (must be positive).
        :raises ValueError: If amount is less than or equal to zero or if the address has insufficient balance.
        """
        if amount <= 0:
            raise ValueError("Amount must be a positive integer.")
        if address not in self.holders or self.holders[address] < amount:
            raise ValueError("Insufficient balance to burn.")

        self.holders[address] -= amount
        self.circulating_supply -= amount

    def get_balance(self, address: str) -> int:
        """
        Retrieves the balance of tokens for a specific address.

        :param address: The address to check the balance of.
        :return: The balance of tokens for the specified address.
        """
        return self.holders.get(address, 0)

    def get_total_supply(self) -> int:
        """
        Retrieves the total supply of tokens.

        :return: The total supply of tokens.
        """
        return self.total_supply

    def get_circulating_supply(self) -> int:
        """
        Retrieves the circulating supply of tokens.

        :return: The circulating supply of tokens.
        """
        return self.circulating_supply

# Example usage
if __name__ == "__main__":
    try:
        tokenomics = Tokenomics(total_supply=1000000)
        tokenomics.mint_tokens("address1", 50000)
        tokenomics.burn_tokens("address1", 10000)
        print(f"Address1 balance: {tokenomics.get_balance('address1')}")
        print(f"Total supply: {tokenomics.get_total_supply()}")
        print(f"Circulating supply: {tokenomics.get_circulating_supply()}")
    except ValueError as e:
        print(f"Error: {e}")
```
