"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-clone-theta.vercel.app
Prompt: Create a function to calculate token prices and slippage for swaps in a Uniswap-like pool.
Generated: DETERMINISTIC_38a0c6eb0df62c1b
Batch ID: 20250612_154908
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Tuple

class UniswapPool:
    def __init__(self, reserve_a: float, reserve_b: float):
        """
        Initializes the Uniswap-like pool with given reserves.

        :param reserve_a: The reserve amount of token A.
        :param reserve_b: The reserve amount of token B.
        """
        self.reserve_a = reserve_a
        self.reserve_b = reserve_b
    
    def calculate_price(self, amount_in: float, token: str) -> Tuple[float, float]:
        """
        Calculates the token price and slippage for a given amount of input tokens.

        :param amount_in: The amount of input tokens to swap.
        :param token: The type of token being swapped ('A' or 'B').
        :return: A tuple containing the output token amount and slippage percentage.
        """
        if token not in ['A', 'B']:
            raise ValueError("Invalid token type. Use 'A' or 'B'.")
        
        # Calculate output amount based on the constant product formula
        if token == 'A':
            output_amount = (self.reserve_b * amount_in) / (self.reserve_a + amount_in)
            slippage = self.calculate_slippage(amount_in, output_amount, self.reserve_a, self.reserve_b)
            return output_amount, slippage
        else:  # token == 'B'
            output_amount = (self.reserve_a * amount_in) / (self.reserve_b + amount_in)
            slippage = self.calculate_slippage(amount_in, output_amount, self.reserve_b, self.reserve_a)
            return output_amount, slippage

    @staticmethod
    def calculate_slippage(amount_in: float, output_amount: float, reserve_in: float, reserve_out: float) -> float:
        """
        Calculates the slippage percentage for a given swap.

        :param amount_in: The amount of input tokens.
        :param output_amount: The calculated output amount after the swap.
        :param reserve_in: The reserve amount of input token.
        :param reserve_out: The reserve amount of output token.
        :return: The slippage percentage.
        """
        # Calculate expected output amount without slippage
        expected_output = (reserve_out * amount_in) / (reserve_in + amount_in)
        # Slippage calculation
        slippage_percentage = ((expected_output - output_amount) / expected_output) * 100
        return slippage_percentage

# Example Usage
if __name__ == "__main__":
    try:
        # Create a Uniswap-like pool with initial reserves
        pool = UniswapPool(reserve_a=1000.0, reserve_b=2000.0)
        
        # Calculate token price and slippage for a swap
        amount_to_swap = 100.0  # Amount of token A to swap
        output_amount, slippage = pool.calculate_price(amount_to_swap, 'A')
        
        print(f"Output Amount: {output_amount:.4f} B")
        print(f"Slippage: {slippage:.2f}%")
    except Exception as e:
        print(f"Error: {e}")
```
