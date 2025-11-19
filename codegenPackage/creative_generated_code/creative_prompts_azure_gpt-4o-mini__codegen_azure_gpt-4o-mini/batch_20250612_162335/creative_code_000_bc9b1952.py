"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shdw.so
Prompt: How can I implement concentrated liquidity in a DeFi application using the principles outlined in Shadow Exchange's Sonic-native concentrated liquidity model?
Generated: DETERMINISTIC_bc9b19526d642190
Batch ID: 20250612_162335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Optional, Dict, Any

class ConcentratedLiquidityPool:
    """
    A class representing a concentrated liquidity pool for a decentralized finance (DeFi) application.
    """

    def __init__(self, token_a: str, token_b: str, initial_liquidity: float) -> None:
        """
        Initializes the liquidity pool with two tokens and an initial amount of liquidity.
        
        Args:
            token_a (str): The symbol of the first token.
            token_b (str): The symbol of the second token.
            initial_liquidity (float): The initial liquidity amount for the pool.
        """
        self.token_a = token_a
        self.token_b = token_b
        self.liquidity = initial_liquidity
        self.reserves: Dict[str, float] = {token_a: initial_liquidity, token_b: initial_liquidity}

    def add_liquidity(self, amount_a: float, amount_b: float) -> None:
        """
        Adds liquidity to the pool.
        
        Args:
            amount_a (float): The amount of token A to add.
            amount_b (float): The amount of token B to add.
        
        Raises:
            ValueError: If the amounts are non-positive.
        """
        if amount_a <= 0 or amount_b <= 0:
            raise ValueError("Liquidity amounts must be positive")

        self.reserves[self.token_a] += amount_a
        self.reserves[self.token_b] += amount_b
        self.liquidity += min(amount_a, amount_b)  # Simple model: min of both added amounts

    def remove_liquidity(self, amount: float) -> None:
        """
        Removes liquidity from the pool.
        
        Args:
            amount (float): The amount of liquidity to remove.
        
        Raises:
            ValueError: If the amount is non-positive or exceeds available liquidity.
        """
        if amount <= 0:
            raise ValueError("Removal amount must be positive")
        if amount > self.liquidity:
            raise ValueError("Insufficient liquidity in the pool")

        proportion_a = self.reserves[self.token_a] / self.liquidity
        proportion_b = self.reserves[self.token_b] / self.liquidity

        self.reserves[self.token_a] -= proportion_a * amount
        self.reserves[self.token_b] -= proportion_b * amount
        self.liquidity -= amount

    def get_reserves(self) -> Dict[str, float]:
        """
        Returns the current reserves of the pool.
        
        Returns:
            Dict[str, float]: A dictionary containing the reserves of token A and token B.
        """
        return self.reserves

    def get_liquidity(self) -> float:
        """
        Returns the current liquidity of the pool.
        
        Returns:
            float: The current liquidity amount.
        """
        return self.liquidity

def main():
    """
    Main function to demonstrate the functionality of the ConcentratedLiquidityPool.
    """
    try:
        pool = ConcentratedLiquidityPool('ETH', 'USDC', 1000.0)
        
        # Adding liquidity
        pool.add_liquidity(500.0, 500.0)
        print(f"Reserves after adding liquidity: {json.dumps(pool.get_reserves(), indent=2)}")
        
        # Removing liquidity
        pool.remove_liquidity(300.0)
        print(f"Reserves after removing liquidity: {json.dumps(pool.get_reserves(), indent=2)}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
