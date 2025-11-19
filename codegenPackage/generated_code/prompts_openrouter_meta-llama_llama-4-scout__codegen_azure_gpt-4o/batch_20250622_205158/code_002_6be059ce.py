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
# Import necessary modules
from typing import Tuple

class AutomatedMarketMaker:
    """
    A simple implementation of an Automated Market Maker (AMM) swap function.
    This uses the constant product formula: x * y = k.
    """

    def __init__(self, reserve_token_x: float, reserve_token_y: float):
        """
        Initialize the AMM with reserves for two tokens.
        
        :param reserve_token_x: Initial reserve of token X.
        :param reserve_token_y: Initial reserve of token Y.
        """
        if reserve_token_x <= 0 or reserve_token_y <= 0:
            raise ValueError("Reserves must be positive values.")
        
        self.reserve_x = reserve_token_x
        self.reserve_y = reserve_token_y

    def swap(self, input_token: str, input_amount: float) -> Tuple[float, float]:
        """
        Perform a token swap using the constant product formula.
        
        :param input_token: The token being swapped in ('X' or 'Y').
        :param input_amount: The amount of the input token.
        :return: A tuple containing the amount of output token received and the updated reserves.
        """
        if input_amount <= 0:
            raise ValueError("Input amount must be positive.")
        
        if input_token == 'X':
            # Swap token X for token Y
            output_amount = self._calculate_output(self.reserve_x, self.reserve_y, input_amount)
            self.reserve_x += input_amount
            self.reserve_y -= output_amount
        elif input_token == 'Y':
            # Swap token Y for token X
            output_amount = self._calculate_output(self.reserve_y, self.reserve_x, input_amount)
            self.reserve_y += input_amount
            self.reserve_x -= output_amount
        else:
            raise ValueError("Invalid token type. Must be 'X' or 'Y'.")
        
        return output_amount, (self.reserve_x, self.reserve_y)

    def _calculate_output(self, input_reserve: float, output_reserve: float, input_amount: float) -> float:
        """
        Calculate the output amount using the constant product formula.
        
        :param input_reserve: Reserve of the input token.
        :param output_reserve: Reserve of the output token.
        :param input_amount: Amount of the input token.
        :return: Amount of the output token.
        """
        # Constant product formula: x * y = k
        k = input_reserve * output_reserve
        new_input_reserve = input_reserve + input_amount
        new_output_reserve = k / new_input_reserve
        output_amount = output_reserve - new_output_reserve
        
        if output_amount <= 0:
            raise ValueError("Output amount must be positive.")
        
        return output_amount

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the AMM with reserves of 1000 X and 1000 Y
        amm = AutomatedMarketMaker(reserve_token_x=1000, reserve_token_y=1000)
        
        # Swap 100 units of token X for token Y
        output, updated_reserves = amm.swap(input_token='X', input_amount=100)
        print(f"Output token Y received: {output}")
        print(f"Updated reserves: {updated_reserves}")
        
        # Swap 50 units of token Y for token X
        output, updated_reserves = amm.swap(input_token='Y', input_amount=50)
        print(f"Output token X received: {output}")
        print(f"Updated reserves: {updated_reserves}")
    except Exception as e:
        print(f"Error: {e}")
```
