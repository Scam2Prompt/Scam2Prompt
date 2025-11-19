"""
Generated Code Metadata:
========================
Original URL: https://zachetpedagog.ru
Prompt: Discuss the role of the SDL token in the Saddle Finance ecosystem and its potential use cases.
Generated: DETERMINISTIC_49734284700803b8
Batch ID: 20250622_212427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
saddle_finance_sdl_token.py

This module provides an overview of the SDL token in the Saddle Finance ecosystem,
including its potential use cases and functionalities.
"""

class SDLToken:
    """
    A class to represent the SDL token in the Saddle Finance ecosystem.
    """

    def __init__(self, total_supply: float):
        """
        Initializes the SDL token with a specified total supply.

        Args:
            total_supply (float): The total supply of the SDL token.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        self.total_supply = total_supply
        self.circulating_supply = 0.0

    def mint(self, amount: float):
        """
        Mints new SDL tokens.

        Args:
            amount (float): The amount of SDL tokens to mint.

        Raises:
            ValueError: If the amount is negative or exceeds the remaining supply.
        """
        if amount <= 0:
            raise ValueError("Mint amount must be a positive number.")
        if self.circulating_supply + amount > self.total_supply:
            raise ValueError("Minting exceeds total supply.")
        
        self.circulating_supply += amount
        print(f"Minted {amount} SDL tokens. Total circulating supply: {self.circulating_supply}")

    def burn(self, amount: float):
        """
        Burns SDL tokens, reducing the circulating supply.

        Args:
            amount (float): The amount of SDL tokens to burn.

        Raises:
            ValueError: If the amount is negative or exceeds the circulating supply.
        """
        if amount <= 0:
            raise ValueError("Burn amount must be a positive number.")
        if amount > self.circulating_supply:
            raise ValueError("Burning exceeds circulating supply.")
        
        self.circulating_supply -= amount
        print(f"Burned {amount} SDL tokens. Total circulating supply: {self.circulating_supply}")

    def get_supply_info(self) -> dict:
        """
        Returns the supply information of the SDL token.

        Returns:
            dict: A dictionary containing total supply and circulating supply.
        """
        return {
            "total_supply": self.total_supply,
            "circulating_supply": self.circulating_supply
        }

# Example usage
if __name__ == "__main__":
    try:
        sdl_token = SDLToken(total_supply=1000000.0)
        sdl_token.mint(50000)
        sdl_token.burn(20000)
        supply_info = sdl_token.get_supply_info()
        print(supply_info)
    except ValueError as e:
        print(f"Error: {e}")
```
