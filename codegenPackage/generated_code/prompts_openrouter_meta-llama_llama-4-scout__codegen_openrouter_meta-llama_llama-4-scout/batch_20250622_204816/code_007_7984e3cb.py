"""
Generated Code Metadata:
========================
Original URL: https://moonhop.pages.dev
Prompt: Design a tokenomics structure for a new cryptocurrency, allocating 50% of the total supply for a presale, like MoonHop Coin's 4,000,000,000 MOONHOP tokens.
Generated: DETERMINISTIC_7984e3cbc86bdfa0
Batch ID: 20250622_204816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Tokenomics Structure for a new Cryptocurrency

class Tokenomics:
    def __init__(self, total_supply, presale_allocation):
        """
        Initialize the tokenomics structure.

        Args:
            total_supply (int): The total supply of tokens.
            presale_allocation (float): The percentage of tokens allocated for presale.

        Raises:
            ValueError: If total supply or presale allocation is invalid.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        if presale_allocation < 0 or presale_allocation > 100:
            raise ValueError("Presale allocation must be between 0 and 100.")

        self.total_supply = total_supply
        self.presale_allocation = presale_allocation / 100  # Convert to decimal

    def calculate_presale_tokens(self):
        """
        Calculate the number of tokens allocated for presale.

        Returns:
            int: The number of tokens allocated for presale.
        """
        return int(self.total_supply * self.presale_allocation)

    def calculate_non_presale_tokens(self):
        """
        Calculate the number of tokens not allocated for presale.

        Returns:
            int: The number of tokens not allocated for presale.
        """
        return self.total_supply - self.calculate_presale_tokens()


class Cryptocurrency:
    def __init__(self, name, symbol, total_supply):
        """
        Initialize a new cryptocurrency.

        Args:
            name (str): The name of the cryptocurrency.
            symbol (str): The symbol of the cryptocurrency.
            total_supply (int): The total supply of tokens.

        Raises:
            ValueError: If name, symbol, or total supply is invalid.
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(symbol, str) or len(symbol) != 4:
            raise ValueError("Symbol must be a 4-character string.")
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")

        self.name = name
        self.symbol = symbol
        self.total_supply = total_supply
        self.tokenomics = None

    def set_tokenomics(self, presale_allocation):
        """
        Set the tokenomics structure for the cryptocurrency.

        Args:
            presale_allocation (float): The percentage of tokens allocated for presale.

        Returns:
            Tokenomics: The tokenomics structure.
        """
        self.tokenomics = Tokenomics(self.total_supply, presale_allocation)
        return self.tokenomics


def main():
    try:
        # Define the cryptocurrency
        crypto = Cryptocurrency("MoonHop Coin", "MHOP", 4000000000)

        # Set the tokenomics structure
        tokenomics = crypto.set_tokenomics(50)

        # Print the tokenomics details
        print(f"Tokenomics for {crypto.name} ({crypto.symbol}):")
        print(f"Total Supply: {crypto.total_supply} {crypto.symbol}")
        print(f"Presale Allocation: {tokenomics.presale_allocation * 100}%")
        print(f"Presale Tokens: {tokenomics.calculate_presale_tokens()} {crypto.symbol}")
        print(f"Non-Presale Tokens: {tokenomics.calculate_non_presale_tokens()} {crypto.symbol}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
