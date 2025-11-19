"""
Generated Code Metadata:
========================
Original URL: https://meversedex.gitbook.io
Prompt: Write a Python code snippet to implement a simple Automated Market Maker (AMM) swap function, similar to the one offered by MEVerse DEX.
Generated: DETERMINISTIC_6be059ceaa77edea
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Tuple

class AutomatedMarketMaker:
    """
    A simple Automated Market Maker (AMM) implementation for token swaps.
    Implements a constant product formula similar to Uniswap's x*y=k.
    """
    
    def __init__(self, token_a_reserve: float, token_b_reserve: float):
        """
        Initialize the AMM with initial token reserves.
        
        Args:
            token_a_reserve: Initial reserve of token A
            token_b_reserve: Initial reserve of token B
        """
        self.token_a_reserve = token_a_reserve
        self.token_b_reserve = token_b_reserve
        self._validate_reserves()
    
    def _validate_reserves(self) -> None:
        """Validate that reserves are positive numbers."""
        if self.token_a_reserve <= 0 or self.token_b_reserve <= 0:
            raise ValueError("Token reserves must be positive numbers")
    
    def get_price(self, token_in: str) -> float:
        """
        Get the current price of one token in terms of the other.
        
        Args:
            token_in: The token to get price for ('A' or 'B')
            
        Returns:
            Price of token_in in terms of the other token
            
        Raises:
            ValueError: If token_in is not 'A' or 'B'
        """
        if token_in == 'A':
            return self.token_b_reserve / self.token_a_reserve
        elif token_in == 'B':
            return self.token_a_reserve / self.token_b_reserve
        else:
            raise ValueError("token_in must be either 'A' or 'B'")
    
    def swap(self, token_in: str, amount_in: float) -> Tuple[float, float]:
        """
        Perform a token swap using the constant product formula.
        
        Args:
            token_in: The token to swap in ('A' or 'B')
            amount_in: Amount of token_in to swap
            
        Returns:
            Tuple of (amount_out, new_reserve_a, new_reserve_b)
            
        Raises:
            ValueError: If token_in is invalid or amount_in is non-positive
        """
        if amount_in <= 0:
            raise ValueError("Amount to swap must be positive")
        
        if token_in == 'A':
            amount_out = self._calculate_output_amount(amount_in, self.token_a_reserve, self.token_b_reserve)
            self.token_a_reserve += amount_in
            self.token_b_reserve -= amount_out
        elif token_in == 'B':
            amount_out = self._calculate_output_amount(amount_in, self.token_b_reserve, self.token_a_reserve)
            self.token_b_reserve += amount_in
            self.token_a_reserve -= amount_out
        else:
            raise ValueError("token_in must be either 'A' or 'B'")
        
        return amount_out, self.token_a_reserve, self.token_b_reserve
    
    def _calculate_output_amount(self, amount_in: float, input_reserve: float, output_reserve: float) -> float:
        """
        Calculate the output amount using the constant product formula.
        
        Args:
            amount_in: Amount of input token
            input_reserve: Reserve of input token
            output_reserve: Reserve of output token
            
        Returns:
            Amount of output token to return
        """
        k = input_reserve * output_reserve
        new_input_reserve = input_reserve + amount_in
        new_output_reserve = k / new_input_reserve
        return output_reserve - new_output_reserve
    
    def add_liquidity(self, amount_a: float, amount_b: float) -> None:
        """
        Add liquidity to the pool while maintaining the current price ratio.
        
        Args:
            amount_a: Amount of token A to add
            amount_b: Amount of token B to add
            
        Raises:
            ValueError: If amounts don't match current price ratio
        """
        expected_amount_b = amount_a * self.get_price('A')
        if not math.isclose(amount_b, expected_amount_b, rel_tol=1e-9):
            raise ValueError("Amounts must match current price ratio")
        
        self.token_a_reserve += amount_a
        self.token_b_reserve += amount_b
    
    def remove_liquidity(self, share: float) -> Tuple[float, float]:
        """
        Remove liquidity from the pool proportionally.
        
        Args:
            share: Fraction of liquidity to remove (0 < share <= 1)
            
        Returns:
            Tuple of (amount_a, amount_b) removed
            
        Raises:
            ValueError: If share is invalid
        """
        if share <= 0 or share > 1:
            raise ValueError("Share must be between 0 and 1")
        
        amount_a = self.token_a_reserve * share
        amount_b = self.token_b_reserve * share
        
        self.token_a_reserve -= amount_a
        self.token_b_reserve -= amount_b
        
        return amount_a, amount_b
```
