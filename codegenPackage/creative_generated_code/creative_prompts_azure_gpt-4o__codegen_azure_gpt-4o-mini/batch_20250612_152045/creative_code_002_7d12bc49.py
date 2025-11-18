"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quickwasp.godaddysites.com
Prompt: Provide an example of how to calculate the invariant (k) in a liquidity pool using the constant product formula for two ERC-20 tokens, and demonstrate how it changes after a token swap.
Generated: DETERMINISTIC_7d12bc4942553fe7
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from web3 import Web3

class LiquidityPool:
    def __init__(self, token_a, token_b, reserve_a, reserve_b):
        """
        Initialize the liquidity pool with two tokens and their reserves.
        
        :param token_a: Address of the first ERC-20 token
        :param token_b: Address of the second ERC-20 token
        :param reserve_a: Initial reserve of the first token
        :param reserve_b: Initial reserve of the second token
        """
        self.token_a = token_a
        self.token_b = token_b
        self.reserve_a = reserve_a
        self.reserve_b = reserve_b
        self.k = self.calculate invariant()  # Calculate the invariant (k)

    def calculate_invariant(self):
        """
        Calculate the invariant (k) using the constant product formula.
        
        :return: The invariant value (k)
        """
        return self.reserve_a * self.reserve_b

    def swap(self, amount_in, from_token):
        """
        Perform a token swap and update the reserves according to the constant product formula.
        
        :param amount_in: The amount of the token being swapped in
        :param from_token: The token being swapped ('a' or 'b')
        
        :raises ValueError: If the from_token is not valid or if reserves are insufficient
        """
        if from_token not in ['a', 'b']:
            raise ValueError("Invalid token specified for swap. Use 'a' or 'b'.")

        if from_token == 'a':
            amount_out = self.calculate_amount_out(amount_in, self.reserve_a, self.reserve_b)
            self.reserve_a += amount_in
            self.reserve_b -= amount_out
        else:
            amount_out = self.calculate_amount_out(amount_in, self.reserve_b, self.reserve_a)
            self.reserve_b += amount_in
            self.reserve_a -= amount_out
        
        # Update the invariant after the swap
        self.k = self.calculate_invariant()

    def calculate_amount_out(self, amount_in, reserve_in, reserve_out):
        """
        Calculate the amount of output token received based on input amount.
        
        :param amount_in: Amount of the input token
        :param reserve_in: Current reserve of the input token
        :param reserve_out: Current reserve of the output token
        :return: Amount of the output token
        """
        if reserve_out == 0:
            raise ValueError("Insufficient reserve for output token.")
        
        # Constant product formula for calculating output amount
        return (amount_in * reserve_out) // (reserve_in + amount_in)

# Example Usage
if __name__ == "__main__":
    # Addresses of ERC-20 tokens (mock addresses)
    token_a_address = "0xTokenAAddress"
    token_b_address = "0xTokenBAddress"

    # Initial reserves for the liquidity pool
    initial_reserve_a = 1000
    initial_reserve_b = 2000

    # Create liquidity pool instance
    pool = LiquidityPool(token_a_address, token_b_address, initial_reserve_a, initial_reserve_b)

    print(f"Initial Invariant (k): {pool.k}")

    # Perform a swap, for example swapping 100 of token A for token B
    swap_amount = 100
    pool.swap(swap_amount, 'a')

    print(f"Post-swap Invariant (k): {pool.k}")
    print(f"New Reserves - Token A: {pool.reserve_a}, Token B: {pool.reserve_b}")
```
