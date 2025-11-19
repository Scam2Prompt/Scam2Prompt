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
# Automated Market Maker (AMM) Swap Function

class Token:
    """Represents a token in the AMM."""
    def __init__(self, name, address, decimals):
        """
        Initializes a Token object.

        Args:
            name (str): The name of the token.
            address (str): The address of the token.
            decimals (int): The number of decimals for the token.
        """
        self.name = name
        self.address = address
        self.decimals = decimals


class AMM:
    """Represents an Automated Market Maker (AMM) for swapping tokens."""
    def __init__(self, token1, token2, reserve1, reserve2, fee=0.003):
        """
        Initializes an AMM object.

        Args:
            token1 (Token): The first token in the AMM.
            token2 (Token): The second token in the AMM.
            reserve1 (float): The initial reserve of token1.
            reserve2 (float): The initial reserve of token2.
            fee (float, optional): The swap fee. Defaults to 0.003 (0.3%).
        """
        self.token1 = token1
        self.token2 = token2
        self.reserve1 = reserve1
        self.reserve2 = reserve2
        self.fee = fee

    def _calculate_swap_amount(self, amount_in, reserve_in, reserve_out):
        """
        Calculates the amount out for a given amount in.

        Args:
            amount_in (float): The amount of token to swap in.
            reserve_in (float): The current reserve of the token being swapped in.
            reserve_out (float): The current reserve of the token being swapped out.

        Returns:
            float: The amount of token to swap out.
        """
        amount_in_with_fee = amount_in * (1 - self.fee)
        amount_out = (amount_in_with_fee * reserve_out) / (reserve_in + amount_in_with_fee)
        return amount_out

    def swap(self, amount_in, token_in):
        """
        Swaps a given amount of token_in for token_out.

        Args:
            amount_in (float): The amount of token_in to swap.
            token_in (Token): The token to swap in.

        Returns:
            float: The amount of token_out received.

        Raises:
            ValueError: If token_in is not one of the tokens in the AMM.
        """
        if token_in == self.token1:
            if self.reserve1 < amount_in:
                raise ValueError("Insufficient reserve for token1")
            amount_out = self._calculate_swap_amount(amount_in, self.reserve1, self.reserve2)
            self.reserve1 += amount_in
            self.reserve2 -= amount_out
            return amount_out
        elif token_in == self.token2:
            if self.reserve2 < amount_in:
                raise ValueError("Insufficient reserve for token2")
            amount_out = self._calculate_swap_amount(amount_in, self.reserve2, self.reserve1)
            self.reserve2 += amount_in
            self.reserve1 -= amount_out
            return amount_out
        else:
            raise ValueError("Invalid token for swap")


def main():
    # Example usage
    token1 = Token("Token A", "0x123", 18)
    token2 = Token("Token B", "0x456", 18)

    amm = AMM(token1, token2, 1000, 500)

    try:
        amount_in = 10
        token_in = token1
        amount_out = amm.swap(amount_in, token_in)
        print(f"Swapped {amount_in} {token_in.name} for {amount_out} {token2.name}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
