"""
Generated Code Metadata:
========================
Original URL: https://doge2014-io.pages.dev
Prompt: Develop a simple staking strategy for Doge2014 tokens, taking into account the 60% presale allocation, 25% staking allocation, and 10% liquidity allocation outlined in the tokenomics.
Generated: DETERMINISTIC_1abf1a2c5a589d14
Batch ID: 20250622_204712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Doge2014Tokenomics:
    def __init__(self, total_supply):
        """
        Initialize the Doge2014 tokenomics with the total supply of tokens.
        
        :param total_supply: Total number of Doge2014 tokens
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        
        self.total_supply = total_supply
        self.presale_allocation = self.calculate_presale_allocation()
        self.staking_allocation = self.calculate_staking_allocation()
        self.liquidity_allocation = self.calculate_liquidity_allocation()

    def calculate_presale_allocation(self):
        """
        Calculate the presale allocation (60% of total supply).
        
        :return: Presale allocation amount
        """
        return self.total_supply * 0.60

    def calculate_staking_allocation(self):
        """
        Calculate the staking allocation (25% of total supply).
        
        :return: Staking allocation amount
        """
        return self.total_supply * 0.25

    def calculate_liquidity_allocation(self):
        """
        Calculate the liquidity allocation (10% of total supply).
        
        :return: Liquidity allocation amount
        """
        return self.total_supply * 0.10

    def display_allocations(self):
        """
        Display the allocations for presale, staking, and liquidity.
        """
        print(f"Total Supply: {self.total_supply}")
        print(f"Presale Allocation (60%): {self.presale_allocation}")
        print(f"Staking Allocation (25%): {self.staking_allocation}")
        print(f"Liquidity Allocation (10%): {self.liquidity_allocation}")


if __name__ == "__main__":
    try:
        # Example total supply of Doge2014 tokens
        total_supply = 1000000  # 1 million tokens
        doge2014 = Doge2014Tokenomics(total_supply)
        doge2014.display_allocations()
    except ValueError as e:
        print(f"Error: {e}")
```
