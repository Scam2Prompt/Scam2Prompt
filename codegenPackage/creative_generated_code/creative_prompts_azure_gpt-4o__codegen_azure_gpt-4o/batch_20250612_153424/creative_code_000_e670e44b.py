"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dymension-xyz.github.io
Prompt: Write a Python script using Dymension's AMM model to simulate ERC-20 token swaps based on liquidity pool dynamics. Include features like flash swaps and price oracles as described in Dymension V2.
Generated: DETERMINISTIC_e670e44baa904971
Batch ID: 20250612_153424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math
from typing import Dict, Tuple


class LiquidityPool:
    """
    Represents a simple Automated Market Maker (AMM) liquidity pool
    for ERC-20 token swaps based on constant product formula.
    """

    def __init__(self, token_a: str, token_b: str, reserve_a: float, reserve_b: float):
        """
        Initializes the liquidity pool with two tokens and their reserves.

        :param token_a: The symbol of the first token (e.g., "ETH").
        :param token_b: The symbol of the second token (e.g., "USDC").
        :param reserve_a: Initial reserve of the first token.
        :param reserve_b: Initial reserve of the second token.
        """
        self.token_a = token_a
        self.token_b = token_b
        self.reserve_a = reserve_a
        self.reserve_b = reserve_b

    def get_price(self) -> Tuple[float, float]:
        """
        Calculates the price of each token relative to the other.

        :return: Tuple of (price of token_a in terms of token_b, price of token_b in terms of token_a)
        """
        price_a = self.reserve_b / self.reserve_a  # Price of token_a in terms of token_b
        price_b = self.reserve_a / self.reserve_b  # Price of token_b in terms of token_a
        return price_a, price_b

    def swap(self, input_token: str, input_amount: float) -> Tuple[str, float]:
        """
        Executes a token swap based on constant product formula.

        :param input_token: The token being swapped in (either token_a or token_b).
        :param input_amount: The amount of the input token.
        :return: A tuple containing the output token and the amount received.
        :raises ValueError: If input token is invalid or input amount is zero/negative.
        """
        if input_amount <= 0:
            raise ValueError("Input amount must be greater than zero.")
        if input_token not in [self.token_a, self.token_b]:
            raise ValueError("Invalid input token.")

        if input_token == self.token_a:
            # Swap token_a for token_b
            output_amount = self._calculate_output(self.reserve_a, self.reserve_b, input_amount)
            self.reserve_a += input_amount
            self.reserve_b -= output_amount
            return self.token_b, output_amount
        else:
            # Swap token_b for token_a
            output_amount = self._calculate_output(self.reserve_b, self.reserve_a, input_amount)
            self.reserve_b += input_amount
            self.reserve_a -= output_amount
            return self.token_a, output_amount

    def flash_swap(self, borrow_token: str, borrow_amount: float) -> Tuple[str, float]:
        """
        Executes a flash swap, allowing borrowing of tokens and immediate repayment.

        :param borrow_token: The token to borrow (either token_a or token_b).
        :param borrow_amount: The amount of the token to borrow.
        :return: A tuple containing the borrowed token and amount.
        :raises ValueError: If borrow token is invalid or borrow amount is zero/negative.
        """
        if borrow_amount <= 0:
            raise ValueError("Borrow amount must be greater than zero.")
        if borrow_token not in [self.token_a, self.token_b]:
            raise ValueError("Invalid borrow token.")

        # Borrow without reserves being updated
        if borrow_token == self.token_a:
            price_b = self.reserve_b / self.reserve_a
            repay_amount = borrow_amount * price_b
            return self.token_a, repay_amount
        else:
            price_a = self.reserve_a / self.reserve_b
            repay_amount = borrow_amount * price_a
            return self.token_b, repay_amount

    def _calculate_output(self, input_reserve: float, output_reserve: float, input_amount: float) -> float:
        """
        Calculates the output amount based on constant product formula.

        :param input_reserve: Reserve of input token.
        :param output_reserve: Reserve of output token.
        :param input_amount: Amount of input token.
        :return: Amount of output token.
        """
        invariant = input_reserve * output_reserve  # Constant product invariant
        new_input_reserve = input_reserve + input_amount
        new_output_reserve = invariant / new_input_reserve
        output_amount = output_reserve - new_output_reserve
        return output_amount


# Example Usage:
if __name__ == "__main__":
    # Create a liquidity pool with initial reserves
    pool = LiquidityPool("ETH", "USDC", reserve_a=100, reserve_b=2000)

    # Display initial prices
    price_eth, price_usdc = pool.get_price()
    print(f"Initial ETH price in USDC: {price_eth}")
    print(f"Initial USDC price in ETH: {price_usdc}")

    # Perform a token swap
    try:
        output_token, output_amount = pool.swap(input_token="ETH", input_amount=10)
        print(f"Swapped 10 ETH for {output_amount} {output_token}")
    except ValueError as e:
        print(f"Error during swap: {e}")

    # Perform a flash swap
    try:
        borrow_token, repay_amount = pool.flash_swap(borrow_token="USDC", borrow_amount=100)
        print(f"Borrowed 100 {borrow_token}, repay amount: {repay_amount}")
    except ValueError as e:
        print(f"Error during flash swap: {e}")
```
